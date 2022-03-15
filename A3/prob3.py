#!/usr/bin/python3

# Filename: prob1.py
# Author:   Eric Dunlop
# Course:   ITSC203
# Details:  investigating pefiles
# references:https://bufferoverflows.net/exploring-pe-files-with-python/
# 			https://docs.microsoft.com/en-us/windows/win32/debug/pe-format#machine-types



from datetime import datetime
import os, time
from pefile import PE
from struct import pack
from prettytable import PrettyTable
#================================================================
# used to parse the stings from microsoft into usable dictionaries
def mk_dict():
	
	startstring = '''paste from the website here'''
	string_list = startstring.split("\n")

	for i in range(1,len(string_list),3):		
		sys_dict[string_list[i]] = string_list[i-1]
		
	print(sys_dict)

#mk_dict()
#===================================================================


def mk_row(filename, mype22):

	row_list = []
	row_list.append(filename)

	# dos header
	row_list.append(mype22.DOS_HEADER.e_lfanew)

	# NT headers
	# pack the second arg bin info as a short from little endian
	row_list.append(pack('<H', mype22.NT_HEADERS.Signature))

	# file header
	row_list.append(machine_type_dict[hex(mype22.FILE_HEADER.Machine)])
	characteristics = hex(mype22.FILE_HEADER.Characteristics)

	# timestamp
	timestamp = mype22.FILE_HEADER.TimeDateStamp
	timestamp = datetime.strptime(time.ctime(timestamp), "%a %b %d %H:%M:%S %Y")
	row_list.append(timestamp.strftime("%m/%d/%Y %H:%M:%S"))

	# optional header
	binstr = str(bin(int(characteristics, 16)))[2:].zfill(16)
	tempstring = ""
	for i in range(15,0,-1):
		if int(binstr[i]):
			tempstring = tempstring + characteristics_dict[15-i] + "\n"
	row_list.append(tempstring)

	optMagic = hex(mype22.OPTIONAL_HEADER.Magic)
	for key in opt_magic_dict:
		if key == optMagic:
			row_list.append(opt_magic_dict[key])

	row_list.append(hex(mype22.OPTIONAL_HEADER.ImageBase))
	row_list.append(hex(mype22.OPTIONAL_HEADER.AddressOfEntryPoint))

	Subsystem = str(mype22.OPTIONAL_HEADER.Subsystem)
	for key in sys_dict:
		if key == Subsystem:
			row_list.append(sys_dict[key])

	if mype22.is_exe():
		row_list.append(".exe")
	elif mype22.is_dll():
		row_list.append(".dll")

	return row_list

#====================================================================

machine_type_dict = {'0x0': 'IMAGE_FILE_MACHINE_UNKNOWN', '0x1d3': 'IMAGE_FILE_MACHINE_AM33', '0x8664': 'IMAGE_FILE_MACHINE_AMD64', '0x1c0': 'IMAGE_FILE_MACHINE_ARM', '0xaa64': 'IMAGE_FILE_MACHINE_ARM64', '0x1c4': 'IMAGE_FILE_MACHINE_ARMNT', '0xebc': 'IMAGE_FILE_MACHINE_EBC', '0x14c': 'IMAGE_FILE_MACHINE_I386', '0x200': 'IMAGE_FILE_MACHINE_IA64', '0x6232': 'IMAGE_FILE_MACHINE_LOONGARCH32', '0x6264': 'IMAGE_FILE_MACHINE_LOONGARCH64', '0x9041': 'IMAGE_FILE_MACHINE_M32R', '0x266': 'IMAGE_FILE_MACHINE_MIPS16', '0x366': 'IMAGE_FILE_MACHINE_MIPSFPU', '0x466': 'IMAGE_FILE_MACHINE_MIPSFPU16', '0x1f0': 'IMAGE_FILE_MACHINE_POWERPC', '0x1f1': 'IMAGE_FILE_MACHINE_POWERPCFP', '0x166': 'IMAGE_FILE_MACHINE_R4000', '0x5032': 'IMAGE_FILE_MACHINE_RISCV32', '0x5064': 'IMAGE_FILE_MACHINE_RISCV64', '0x5128': 'IMAGE_FILE_MACHINE_RISCV128', '0x1a2': 'IMAGE_FILE_MACHINE_SH3', '0x1a3': 'IMAGE_FILE_MACHINE_SH3DSP', '0x1a6': 'IMAGE_FILE_MACHINE_SH4', '0x1a8': 'IMAGE_FILE_MACHINE_SH5', '0x1c2': 'IMAGE_FILE_MACHINE_THUMB', '0x169': 'IMAGE_FILE_MACHINE_WCEMIPSV2'}
characteristics_dict = {0: 'IMAGE_FILE_RELOCS_STRIPPED', 1: 'IMAGE_FILE_EXECUTABLE_IMAGE', 2: 'IMAGE_FILE_LINE_NUMS_STRIPPED', 3: 'IMAGE_FILE_LOCAL_SYMS_STRIPPED', 4: 'IMAGE_FILE_AGGRESSIVE_WS_TRIM', 5: 'IMAGE_FILE_LARGE_ADDRESS_ AWARE', 6: 'UNUSED', 7: 'IMAGE_FILE_BYTES_REVERSED_LO', 8: 'IMAGE_FILE_32BIT_MACHINE', 9: 'IMAGE_FILE_DEBUG_STRIPPED', 10: 'IMAGE_FILE_REMOVABLE_RUN_ FROM_SWAP', 11: 'IMAGE_FILE_NET_RUN_FROM_SWAP', 12: 'IMAGE_FILE_SYSTEM', 13: 'IMAGE_FILE_DLL', 14: 'IMAGE_FILE_UP_SYSTEM_ONLY', 15: 'IMAGE_FILE_BYTES_REVERSED_HI'}
opt_magic_dict = {"0x10b": "PE32", "0x20b": "PE32+", "0x107": "ROM"}
sys_dict = {'0': 'IMAGE_SUBSYSTEM_UNKNOWN', '1': 'IMAGE_SUBSYSTEM_NATIVE', '2': 'IMAGE_SUBSYSTEM_WINDOWS_GUI', '3': 'IMAGE_SUBSYSTEM_WINDOWS_CUI', '5': 'IMAGE_SUBSYSTEM_OS2_CUI', '7': 'IMAGE_SUBSYSTEM_POSIX_CUI', '8': 'IMAGE_SUBSYSTEM_NATIVE_WINDOWS', '9': 'IMAGE_SUBSYSTEM_WINDOWS_CE_GUI', '10': 'IMAGE_SUBSYSTEM_EFI_APPLICATION', '11': 'IMAGE_SUBSYSTEM_EFI_BOOT_ SERVICE_DRIVER', '12': 'IMAGE_SUBSYSTEM_EFI_RUNTIME_ DRIVER', '13': 'IMAGE_SUBSYSTEM_EFI_ROM', '14': 'IMAGE_SUBSYSTEM_XBOX', '16': 'IMAGE_SUBSYSTEM_WINDOWS_BOOT_APPLICATION'}

efile_table = PrettyTable(hrules = True)
efile_table.field_names = ["Filename", "PEHdrOff", "PESig", "Machine", "Timestamp", "Characteristics", "OptMagic", "ImageBase", "Entry Point", "Subsystem", "dll/exe"]
reject_list = []

for root, dirs, files in os.walk("."):
	for file in files:
		try:
			mype22 = PE(file)
			dosmagic = hex(mype22.DOS_HEADER.e_magic)
			if dosmagic == "0x5a4d":
				efile_table.add_row(mk_row(file, mype22))
			else:
				reject_list.append(file)
		except: 
			reject_list.append(file)
# row_list = 


print(efile_table)
print("\nrejected files:\n")
for reject in reject_list:
	print(reject)

