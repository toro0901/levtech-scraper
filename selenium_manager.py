# Seleniumでブラウザを操作するためのモジュール
from selenium import webdriver
from selenium.webdriver.common.by import By                 # 要素を探す方法（ID, CSS, XPATHなど）
from selenium.webdriver.chrome.options import Options       # Chrome起動オプション
from selenium.webdriver.remote.webdriver import WebDriver   # 型ヒント用（ブラウザ操作オブジェクト）
from selenium.webdriver.remote.webelement import WebElement # 型ヒント用（ボタンや入力欄などの要素）
from selenium.common.exceptions import NoSuchElementException        # エラー処理用 : 要素が見つからない場合
from selenium.common.exceptions import ElementClickInterceptedException # エラー処理用 : クリックできない場合
from selenium.common.exceptions import ElementNotInteractableException   # エラー処理用 : 要素が操作できない場合

# ログや待機に使う標準モジュール
import logging    # ログ出力用
import time       # 待機用（sleepなど）


class GetElement:
    """
    Webページ上の「ボタン」や「入力欄」などの要素を探すクラス
    """

    def __init__(self, chrome: WebDriver, logger: logging.Logger):
        # 既存のChromeブラウザとloggerを保持
        self.chrome: WebDriver = chrome
        self.logger: logging.Logger = logger

    def get_by_id(self, value: str) -> WebElement:
        """ID属性で要素を取得"""
        self.logger.debug(f"要素取得開始 :\n {value}")
        try:
            element = self.chrome.find_element(By.ID, value)
            self.logger.debug(f"要素取得完了 :\n {value}")
            return element
        except Exception as e:
            self.logger.error(f"要素取得失敗 :\n {e}")
            raise

    def get_by_name(self, value: str) -> WebElement:
        """name属性で要素を取得"""
        self.logger.debug(f"要素取得開始 :\n {value}")
        try:
            element = self.chrome.find_element(By.NAME, value)
            self.logger.debug(f"要素取得完了 :\n {value}")
            return element
        except Exception as e:
            self.logger.error(f"要素取得失敗 :\n {e}")
            raise

    def get_by_css(self, value: str) -> WebElement:
        """CSSセレクタで要素を取得"""
        self.logger.debug(f"要素取得開始 :\n {value}")
        try:
            element = self.chrome.find_element(By.CSS_SELECTOR, value)
            self.logger.debug(f"要素取得完了 :\n {value}")
            return element
        except Exception as e:
            self.logger.error(f"要素取得失敗 :\n {e}")
            raise

    def get_by_xpath(self, value: str) -> WebElement:
        """XPathで要素を取得"""
        self.logger.debug(f"要素取得開始 :\n {value}")
        try:
            element = self.chrome.find_element(By.XPATH, value)
            self.logger.debug(f"要素取得完了 :\n {value}")
            return element
        except Exception as e:
            self.logger.error(f"要素取得失敗 :\n {e}")
            raise

    def get_by_class_name(self, value: str) -> WebElement:
        """class名で要素を取得"""
        self.logger.debug(f"要素取得開始 :\n {value}")
        try:
            element = self.chrome.find_element(By.CLASS_NAME, value)
            self.logger.debug(f"要素取得完了 :\n {value}")
            return element
        except Exception as e:
            self.logger.error(f"要素取得失敗 :\n {e}")
            raise

    def get_by_tag_name(self, value: str) -> WebElement:
        """タグ名で要素を取得"""
        self.logger.debug(f"要素取得開始 :\n {value}")
        try:
            element = self.chrome.find_element(By.TAG_NAME, value)
            self.logger.debug(f"要素取得完了 :\n {value}")
            return element
        except Exception as e:
            self.logger.error(f"要素取得失敗 :\n {e}")
            raise

    def get_by_link_text(self, value: str) -> WebElement:
        """リンクテキストで要素を取得"""
        self.logger.debug(f"要素取得開始 :\n {value}")
        try:
            element = self.chrome.find_element(By.LINK_TEXT, value)
            self.logger.debug(f"要素取得完了 :\n {value}")
            return element
        except Exception as e:
            self.logger.error(f"要素取得失敗 :\n {e}")
            raise

    def get_by_partial_link_text(self, value: str) -> WebElement:
        """部分リンクテキストで要素を取得"""
        self.logger.debug(f"要素取得開始 :\n {value}")
        try:
            element = self.chrome.find_element(By.PARTIAL_LINK_TEXT, value)
            self.logger.debug(f"要素取得完了 :\n {value}")
            return element
        except Exception as e:
            self.logger.error(f"要素取得失敗 :\n {e}")
            raise



class ActionElement:
    """
    見つけた要素に対して操作するクラス
    例：文字を入力したり、クリックしたり
    """

    def __init__(self, logger: logging.Logger):
        self.logger = logger

    def send_keys(self, element: WebElement, text: str) -> None:
        """指定要素に文字を入力"""
        try:
            self.logger.debug("入力開始")
            element.send_keys(text)
            self.logger.debug(f"入力完了: {text}")
        except Exception as e:
            self.logger.error(f"操作失敗: {e}")
            raise

    def click(self, element: WebElement) -> None:
        """クリック操作"""
        try:
            self.logger.debug("クリック開始")
            element.click()
            self.logger.debug("クリック完了")
        except Exception as e:
            self.logger.error(f"操作失敗: {e}")
            raise

    def clear_and_send_keys(self, element: WebElement, text: str) -> None:
        """クリアして再入力"""
        try:
            self.logger.debug("入力クリア＆開始")
            element.clear()
            element.send_keys(text)
            self.logger.debug(f"入力完了: {text}")
        except Exception as e:
            self.logger.error(f"操作失敗: {e}")
            raise

    def safe_click(self, element: WebElement, chrome: WebDriver) -> None:
        """クリック操作（失敗時はJavaScriptクリックにフォールバック）"""
        self.logger.debug("クリック開始")
        try:
            element.click()
            self.logger.debug("クリック完了")
        except (ElementClickInterceptedException, ElementNotInteractableException) as e:
            self.logger.debug("通常クリック失敗、JavaScriptでフォールバック")
            try:
                chrome.execute_script("arguments[0].click();", element)
                self.logger.debug("JavaScriptクリック完了")
            except Exception as js_e:
                self.logger.error(f"操作失敗: {js_e}")
                raise
        except Exception as e:
            self.logger.error(f"操作失敗: {e}")
            raise



if __name__ == "__main__":
    """
    動作確認用
    - Chromeでログインページを開く
    - メールを入力
    - ログインボタンをクリック
    - ログを見れば操作が成功したか分かる
    """

    # ロガー設定
    logger = logging.getLogger("SeleniumTest")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Chrome起動
    chrome = webdriver.Chrome()
    try:
        # リベシティログイン画面表示
        chrome.get("https://libecity.com/signin")
        time.sleep(2)  # ページ読み込み待機

        # クラスインスタンス化
        get_element = GetElement(chrome, logger)
        action_element = ActionElement(logger)

        # メール入力欄を取得して入力
        email_input = get_element.get_by_css('input[placeholder="メールアドレス"]')
        action_element.send_keys(email_input, "user_name_test@gmail.com")

        # ログインボタンを取得してクリック
        login_button = get_element.get_by_css('button[type="submit"]')
        action_element.safe_click(login_button, chrome)

        time.sleep(3)  # 結果確認のため待機
        logger.info("画面を閉じました")
    finally:
        chrome.quit()
