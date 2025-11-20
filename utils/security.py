import getpass
from utils.colors import Color

PIN_CODE = "21022005"   # PIN yang kamu minta


def require_pin():
    """
    Meminta PIN untuk command sensitif.
    """
    pin = getpass.getpass(Color.WARNING + "Masukkan PIN: " + Color.RESET)

    if pin != PIN_CODE:
        print(Color.ERROR + "PIN salah. Akses ditolak." + Color.RESET)
        exit(1)  # stop program

    print(Color.OK + "PIN benar, akses diberikan." + Color.RESET)
