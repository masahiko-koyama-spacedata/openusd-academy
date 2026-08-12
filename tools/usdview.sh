#!/bin/zsh
# ソースからビルドした OpenUSD の usdview を開く。
#
# usdview は pip install usd-core には含まれないので、
# ~/Developer/usd-install にビルドしたものを使う（AGENTS.md 参照）。
# PYTHONPATH を通さないと pxr が見つからず起動しない。
#
# 使い方: tools/usdview.sh <file.usda> [usdview のオプション...]

USD_INSTALL="${USD_INSTALL:-$HOME/Developer/usd-install}"

if [ ! -x "$USD_INSTALL/bin/usdview" ]; then
  echo "usdview が見つかりません: $USD_INSTALL/bin/usdview" >&2
  echo "AGENTS.md の「ローカルのビルド環境」を参照してください。" >&2
  exit 1
fi

if [ $# -eq 0 ]; then
  echo "使い方: tools/usdview.sh <file.usda> [options]" >&2
  exit 2
fi

export PYTHONPATH="$USD_INSTALL/lib/python3.9/site-packages:$PYTHONPATH"
export PATH="$USD_INSTALL/bin:$PATH"

# USDA の相対参照はファイル自身の場所から解決されるので、そこへ移る
target="$1"; shift
cd "$(dirname "$target")" || exit 1
exec "$USD_INSTALL/bin/usdview" "$(basename "$target")" "$@"
