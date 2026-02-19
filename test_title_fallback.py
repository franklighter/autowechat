"""
測試標題容錯機制
此腳本用於測試 find_window_with_title_fallback 函數是否正常工作
"""

from pywechat.WechatTools import find_window_with_title_fallback, Desktop, Independent_window

def test_title_fallback():
    """測試標題容錯功能"""
    print("開始測試標題容錯機制...")

    # 初始化
    desktop = Desktop(**Independent_window().Desktop)

    # 測試視窗列表
    test_windows = [
        ('ChannelWindow', Independent_window().ChannelWindow),
        ('ContactProfileWindow', Independent_window().ContactProfileWindow),
        ('OldIncomingCallWindow', Independent_window().OldIncomingCallWindow),
        ('NewIncomingCallWindow', Independent_window().NewIncomingCallWindow),
        ('OldVoiceCallWindow', Independent_window().OldVoiceCallWindow),
        ('NewVoiceCallWindow', Independent_window().NewVoiceCallWindow),
        ('OldVideoCallWindow', Independent_window().OldVideoCallWindow),
        ('NewVideoCallWindow', Independent_window().NewVideoCallWindow),
    ]

    print("\n測試的視窗規格:")
    for name, spec in test_windows:
        if 'title' in spec and spec['title'] == '微信':
            print(f"  - {name}: {spec}")

    print("\n容錯機制說明:")
    print("  1. 首先嘗試使用 'title': '微信'")
    print("  2. 如果失敗,嘗試使用 'title': 'WeChat'")
    print("  3. 如果仍失敗,嘗試使用 'title': 'Weixin'")
    print("\n這樣可以支援不同語言版本的微信!")

if __name__ == "__main__":
    test_title_fallback()
