#!/usr/bin/env python3
#
# Copyright 2014-present Facebook. All Rights Reserved.
#
# This program file is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program in a file named COPYING; if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA
#
import rest_modbus
import rest_usb2i2c_reset
from aiohttp import web
from rest_utils import dumps_bytestr, get_endpoints


class boardApp_Handler:

    # Disable the endpoint in BMC until we root cause cp2112 issues.
    # Handler to reset usb-to-i2c
    # async def rest_usb2i2c_reset_hdl(self,request):
    # return rest_usb2i2c_reset.set_usb2i2c()

    # Handler for Modbus_registers resource endpoint
    async def helper_modbus_registers_hdl(self, request):
        return web.json_response(
            await rest_modbus.get_modbus_registers(), dumps=dumps_bytestr
        )
