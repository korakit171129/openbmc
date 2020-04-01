#!/usr/bin/env python3
#
# Copyright 2020-present Facebook. All Rights Reserved.
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

GPIOS = {
    "BMC_FCM_1_SEL": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "BMC_FCM_2_SEL": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "BMC_FPGA_JTAG_EN": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "BMC_GPIO53": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "BMC_GPIO55": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "BMC_GPIO57": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "BMC_GPIO61": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "BMC_GPIO63": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "BMC_I2C_SEL": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "BMC_JTAG_MUX_IN": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "1",
    },
    "BMC_PWRGD": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "BMC_SCM_CPLD_JTAG_EN_N": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "BMC_TPM_SPI_CS_N": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "BMC_TPM_SPI_PIRQ_N": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "1",
    },
    "BMC_UART1_NCTS": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "BMC_UART1_NDSR": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "BMC_UART1_NDTR": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "BMC_UART1_NRTS": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "BMC_UART_SEL_0": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "BMC_UART_SEL_1": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "BMC_UART_SEL_2": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "BMC_UART_SEL_3": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "CPU_RST#": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "FCM_1_CARD_PRESENT": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "1",
    },
    "FCM_1_CPLD_JTAG_EN_N": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "FCM_2_CARD_PRESENT": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "FCM_2_CPLD_JTAG_EN_N": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "FPGA_BMC_CONFIG_DONE": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "1",
    },
    "FPGA_CONFIG_SEL": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "FPGA_DEV_CLR_N": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "FPGA_DEV_OE": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "FPGA_NSTATUS": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "1",
    },
    "FWSPI_IO2_GPIO41": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "FWSPI_IO3_GPIO43": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "GPIO0_SGPMLD": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "GPIO109_PASSTHRU2_IN": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "1",
    },
    "GPIO120_SPI1_IO3": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "1",
    },
    "GPIO1_SGPMI": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "GPIO21_PASSTHRU2_OUT": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "GPIO35_FWSPIWP#": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "1",
    },
    "GPIO37_INDICATOR#": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "GPIO3_SGPMO": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "GPIO45_PASSTHRU1_OUT": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "1",
    },
    "GPIO5_SGPMCK": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "GPIO85_PASSTHRU1_IN": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "GPO1": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "GPO5_SPI1_IO2": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "I2C_TPM_INT_N": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "1",
    },
    "I2C_TPM_PP": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "PWRMONITOR_BMC": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "RESERVED_GPIO67": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "SPI1CK_GPIO122": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "SPI1CS1#_GPIO124": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "1",
    },
    "SPI1MISO_IO1_GPO4": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "SPI1MOSI_IO0_GPO3": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "1",
    },
    "SPI2CK_GPIO78": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "1",
    },
    "SPI2CS1#_GPIO86": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "1",
    },
    "SPI2CS2#_GPIO84": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "1",
    },
    "SPI2MISO_GPIO80": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "SPI2MOSI_GPIO82": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "SYS_CPLD_JTAG_EN_N": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "TEMP_SENSOR_ALERT": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "1",
    },
    "UCD90160A_1_GPI1": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "UCD90160A_2_GPI1": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "UCD90160A_CNTRL": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "1",
    },
    "VGAHS_GPIO2": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "VGAVS_GPIO4": {
        "active_low": "0",
        "direction": "in",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "WDTRST1_GPIO59": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
    "WDTRST2_GPIO51": {
        "active_low": "0",
        "direction": "out",
        "uevent": "",
        "edge": "none",
        "value": "0",
    },
}
