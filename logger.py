import logging

# ====== ログレベルごとのカラーコード設定 ======
# ANSIエスケープシーケンスを使って、ログの文字色を変更します
LEVEL_COLORS = {
    logging.DEBUG: "\033[34m",    # DEBUG → 青
    logging.INFO: "\033[32m",     # INFO → 緑
    logging.WARNING: "\033[33m",  # WARNING → 黄
    logging.ERROR: "\033[31m",    # ERROR → 赤
    logging.CRITICAL: "\033[35m"  # CRITICAL → マゼンタ
}
RESET_COLOR = "\033[0m"  # 色を元に戻すコード


# ====== 色付きフォーマッタの定義 ======
class ColorFormatter(logging.Formatter):
    """
    ログメッセージに色を付けるフォーマッタクラス。
    ログレベルに応じて文字色を変更します。
    """
    def format(self, record):
        # ログレベルに対応する色を取得（なければ白）
        color = LEVEL_COLORS.get(record.levelno, "\033[37m")
        # 通常のフォーマット処理
        message = super().format(record)
        # 色付きメッセージを返す
        return f"{color}{message}{RESET_COLOR}"


# ====== ロガーを管理するクラス ======
class Logger:
    """
    色付きログを出力するLoggerクラス。
    初期化時にコンソール用のハンドラを設定します。
    """
    def __init__(self, name=__name__):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)  # すべてのレベルのログを出力

        # ハンドラがすでに設定されていない場合のみ追加（重複防止）
        if not self.logger.handlers:
            console_handler = logging.StreamHandler()  # 標準出力用ハンドラ
            formatter = ColorFormatter("%(levelname)s : %(message)s")  # 表示形式の設定
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

    def get_logger(self):
        """
        ロガーインスタンスを返す。
        他のモジュールでも使えるようにするためのメソッド。
        """
        return self.logger


# ====== 動作確認用コード ======
if __name__ == "__main__":
    # Loggerクラスからロガーを取得
    logger = Logger(__name__).get_logger()

    # 各ログレベルでメッセージを出力
    logger.debug("これはデバッグメッセージです")
    logger.info("これは情報メッセージです")
    logger.warning("これは警告メッセージです")
    logger.error("これはエラーメッセージです")
    logger.critical("これは重大なエラーメッセージです")
