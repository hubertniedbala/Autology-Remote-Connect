#!/usr/bin/env python3
import os
import sys
import warnings
import asyncio
import json
import traceback
import websockets
from threading import Thread
from Foundation import NSObject, NSStatusBar, NSMenu, NSMenuItem, NSApplication
from AppKit import NSImage, NSStatusItem, NSVariableStatusItemLength
import objc

# Filtruj ostrzeżenie o pkg_resources
warnings.filterwarnings("ignore", category=DeprecationWarning, module="pkg_resources")

class DroneProxy:
    def __init__(self):
        self.is_connected = False
        self.drone_ip = None

    def connect(self, ip):
        try:
            self.is_connected = True
            self.drone_ip = ip
            return {"status": "success", "message": "✅ Połączono z dronem (tryb symulacji)!"}
        except Exception as e:
            return {"status": "error", "message": f"❌ Błąd połączenia: {str(e)}"}

    def disconnect(self):
        if not self.is_connected:
            return {"status": "error", "message": "❌ Dron nie jest połączony!"}
        try:
            self.is_connected = False
            return {"status": "success", "message": "👋 Rozłączono z dronem!"}
        except Exception as e:
            return {"status": "error", "message": f"❌ Błąd rozłączania: {str(e)}"}

class MenuBarApp(NSObject):
    def init(self):
        self = objc.super(MenuBarApp, self).init()
        if self is None:
            return None
        
        self.statusitem = NSStatusBar.systemStatusBar().statusItemWithLength_(NSVariableStatusItemLength)
        
        # Użyj ścieżki względnej do zasobu w aplikacji
        icon_path = os.path.join(os.path.dirname(__file__), 'icons', 'menubar_icon.png')
        icon = NSImage.alloc().initWithContentsOfFile_(icon_path)
        if icon:
            icon.setTemplate_(True)  # To sprawia, że ikona automatycznie dostosowuje się do motywu
            icon.setSize_((18, 18))  # Ustaw stały rozmiar ikony
            self.statusitem.setImage_(icon)
            self.statusitem.setTitle_("")  # Wyczyść tytuł
        else:
            print(f"Nie można załadować ikony z: {icon_path}")
            self.statusitem.setTitle_("��")
        
        self.menu = NSMenu.alloc().init()
        self.statusitem.setMenu_(self.menu)
        
        menuitem = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(
            "Start Server", "startServer:", ""
        )
        self.menu.addItem_(menuitem)
        
        menuitem = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(
            "Status: Stopped", None, ""
        )
        self.menu.addItem_(menuitem)
        
        self.menu.addItem_(NSMenuItem.separatorItem())
        
        menuitem = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(
            "Quit", "terminate:", "q"
        )
        self.menu.addItem_(menuitem)
        
        self.server_running = False
        self.server_thread = None
        return self

    def startServer_(self, sender):
        if not self.server_running:
            self.server_running = True
            sender.setTitle_("Stop Server")
            self.menu.itemAtIndex_(1).setTitle_("Status: Running")
            # Nie zmieniamy ikony przy starcie/stopie serwera
            self.server_thread = Thread(target=self.run_server_in_thread)
            self.server_thread.start()
        else:
            self.server_running = False
            sender.setTitle_("Start Server")
            self.menu.itemAtIndex_(1).setTitle_("Status: Stopped")
            if self.server_thread:
                self.server_thread.join()

    def run_server_in_thread(self):
        asyncio.run(self.run_server())

    async def run_server(self):
        try:
            print("🚀 Uruchamianie lokalnego serwera proxy dla drona...")
            async with websockets.serve(self.handle_drone_commands, "localhost", 8765):
                print("✅ Serwer proxy jest gotowy na porcie 8765")
                print("ℹ️ Czekam na połączenia...")
                while self.server_running:
                    await asyncio.sleep(1)
        except Exception as e:
            print(f"Server error: {e}")
            self.server_running = False
            self.menu.itemAtIndex_(0).setTitle_("Start Server")
            self.menu.itemAtIndex_(1).setTitle_("Status: Error")

    async def handle_drone_commands(self, websocket):
        drone_proxy = DroneProxy()
        async for message in websocket:
            try:
                data = json.loads(message)
                command = data.get("command")
                params = data.get("data")

                if command == "connect":
                    response = drone_proxy.connect(params.get("ip"))
                elif command == "disconnect":
                    response = drone_proxy.disconnect()
                elif command == "takeoff":
                    response = drone_proxy.takeoff()
                elif command == "land":
                    response = drone_proxy.land()
                else:
                    response = {"status": "error", "message": "❌ Nieznana komenda"}

                await websocket.send(json.dumps(response))
            except Exception as e:
                await websocket.send(json.dumps({
                    "status": "error",
                    "message": f"❌ Błąd: {str(e)}"
                }))

if __name__ == "__main__":
    try:
        app = NSApplication.sharedApplication()
        delegate = MenuBarApp.alloc().init()
        app.setDelegate_(delegate)
        app.run()
    except Exception as e:
        print(f"Fatal error: {e}")
        traceback.print_exc()
        sys.exit(1) 