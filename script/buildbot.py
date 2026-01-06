import asyncio
import os
import sys
from telethon import TelegramClient

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHATID")
MESSAGE_THREAD_ID = os.environ.get("MESSAGE_THREAD_ID")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

# Build information from environment
KERNEL_VERSION = os.environ.get("KERNEL_VERSION", "")
FULL_VERSION = os.environ.get("FULL_VERSION", "")
KSU_BRANCH = os.environ.get("KSU_BRANCH", "")
KSUVER = os.environ.get("KSUVER", "")
HOOK_METHOD = os.environ.get("HOOK_METHOD", "")
KPM_ENABLE = os.environ.get("KPM_ENABLE", "")
LZ4KD_ENABLE = os.environ.get("LZ4KD_ENABLE", "")
LZ4_ZSTD_ENABLE = os.environ.get("LZ4_ZSTD_ENABLE", "")
BBR_ENABLE = os.environ.get("BBR_ENABLE", "")
BETTER_NET = os.environ.get("BETTER_NET", "")
ADIOS_ENABLE = os.environ.get("ADIOS_ENABLE", "")
REKERNEL_ENABLE = os.environ.get("REKERNEL_ENABLE", "")
BASEBAND_GUARD = os.environ.get("BASEBAND_GUARD", "")
TIME_FORM = os.environ.get("TIME_FORM", "")

MSG_TEMPLATE = """
**New Build Published!**
#SM8750 #OKI

```Kernel Info
Version: {full_version}
Kernel: {kernel_version}
KSU Branch: {ksu_branch}
KSU Version: {ksuver}
Build Time: {time_form}

Features:
- Hook Method: {hook_method}
- KPM: {kpm_enable}
- LZ4KD: {lz4kd_enable}
- LZ4 & ZSTD: {lz4_zstd_enable}
- BBR: {bbr_enable}
- Better Network: {better_net}
- ADIOS: {adios_enable}
- Re-Kernel: {rekernel_enable}
- Baseband Guard: {baseband_guard}
```

**#OPPO #OPlus #Realme #Android15**
""".strip()


def get_caption():
    msg = MSG_TEMPLATE.format(
        full_version=FULL_VERSION,
        kernel_version=KERNEL_VERSION,
        ksu_branch=KSU_BRANCH,
        ksuver=KSUVER,
        time_form=TIME_FORM,
        hook_method=HOOK_METHOD,
        kpm_enable=KPM_ENABLE,
        lz4kd_enable=LZ4KD_ENABLE,
        lz4_zstd_enable=LZ4_ZSTD_ENABLE,
        bbr_enable=BBR_ENABLE,
        better_net=BETTER_NET,
        adios_enable=ADIOS_ENABLE,
        rekernel_enable=REKERNEL_ENABLE,
        baseband_guard=BASEBAND_GUARD,
    )
    if len(msg) > 1024:
        return f"SM8750 Kernel {FULL_VERSION}"
    return msg


def check_environ():
    global CHAT_ID, MESSAGE_THREAD_ID, API_ID, API_HASH
    if BOT_TOKEN is None:
        print("[-] Invalid BOT_TOKEN")
        exit(1)
    if CHAT_ID is None:
        print("[-] Invalid CHAT_ID")
        exit(1)
    else:
        try:
            CHAT_ID = int(CHAT_ID)
        except:
            pass
    if MESSAGE_THREAD_ID is not None and MESSAGE_THREAD_ID != "":
        try:
            MESSAGE_THREAD_ID = int(MESSAGE_THREAD_ID)
        except:
            print("[-] Invalid MESSAGE_THREAD_ID")
            exit(1)
    else:
        MESSAGE_THREAD_ID = None
    
    if API_ID is None:
        print("[-] Invalid API_ID")
        exit(1)
    else:
        try:
            API_ID = int(API_ID)
        except:
            print("[-] Invalid API_ID format")
            exit(1)
    
    if API_HASH is None:
        print("[-] Invalid API_HASH")
        exit(1)


async def main():
    print("[+] Uploading to telegram")
    check_environ()
    files = sys.argv[1:]
    print("[+] Files:", files)
    if len(files) <= 0:
        print("[-] No files to upload")
        exit(1)
    print("[+] Logging in Telegram with bot")
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    session_dir = os.path.join(script_dir, "ksubot")
    async with await TelegramClient(session=session_dir, api_id=API_ID, api_hash=API_HASH).start(bot_token=BOT_TOKEN) as bot:
        caption = [""] * len(files)
        caption[-1] = get_caption()
        print("[+] Caption: ")
        print("---")
        print(caption)
        print("---")
        print("[+] Sending")
        await bot.send_file(entity=CHAT_ID, file=files, caption=caption, reply_to=MESSAGE_THREAD_ID, parse_mode="markdown")
        print("[+] Done!")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"[-] An error occurred: {e}")
