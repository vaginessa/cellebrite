import Mits.Configuration.Config as MitsConfig
from Mits.Utils.upy import upy
# This function is not needed on the UFED, as it is used only with legacy

def gen_response(challange):
    key = [0x04, 0x30, 0xA0, 0xE3, 0x00, 0x20, 0x8D, 0xE2, 0x00, 0x10, 0xA0, 0xE3, 0x04, 0x0, 0xA0, 0xE1]


validFilenameChars = "-_.()[] %s%s" % (string.ascii_letters, string.digits)
def removeDisallowedFilenameChars(filename):

def hex_to_bin(path):
    the function returns the load address of the binary code as extracted from the hex
    data = file(path,"rb").read()
    load_address = eval ("0x"+ lines[0][9:-2])
    lines = lines[2:]
    return load_address
TIME_NAME = 1
def timed_xrange(start,stop=None,step=None, bytes_per_iteration = 1):
    #do loop
    i = start

        current_time = time()
        i += step

#pack and unpack functions:
def pack64L(data):
def pack64B(data):
def pack32L(data):
def pack32B(data):
def pack24L(data):
def pack24B(data):
def pack16L(data):
def pack16B(data):
def pack8B(data):
def unpack8B(data):
def unpack16B(data):
def unpack16L(data):
def unpack16l(data):
def unpack24L(data):
def unpack24l(data):
def unpack24B(data):
def unpack32L(data):
def unpack32B(data):
def unpack32l(data):
def pack32l(data):

def unpack64L(data):
def unpack64B(data):
def unpack64l(data):
def pack64l(data):

def pack64l(data):
def pack642b(data):

def get_log_path(prefix, middle):

def get_dump_file_name(prefix, middle, start=None, end=None, baseAddr=None):

def get_dump_path(prefix, middle, start=None, end=None, baseAddr=None):




def xor_strings(s1, s2):
def get_stdout(command, redirect_err_to_out = False):
    p = subprocess.Popen(my_split(command), stdout = subprocess.PIPE, stderr = subprocess.PIPE)
def blockify(s, block_size):



def rev_byte(b):
rev_array = [rev_byte(b) for b in range(0x100)]
def rev8(in_str):