# DeepSeek 余额查询桌面小工具

一款基于 pywebview 的轻量级桌面应用，用于查询 DeepSeek API 账户余额。

## 功能特性

- 查询 DeepSeek API 账户总余额、赠送余额、充值余额
- 自动刷新（间隔可配置）
- 玻璃质感 UI 设计
- 窗口拖拽支持
- 错误状态显示
- 可打包为独立 EXE

## 截图

| 正常状态 | 异常状态 |
|---------|---------|
| ![正常](https://via.placeholder.com/300x400?text=Normal) | ![异常](https://via.placeholder.com/300x400?text=Error) |

## 快速开始

### 从源码运行

1. 安装依赖：

```bash
pip install pywebview requests
```

2. 配置 API Key：

编辑 `config.json`：

```json
{
  "api_key": "sk-your-api-key-here",
  "auto_refresh_seconds": 30
}
```

3. 运行：

```bash
python check_balance.pyw
```

### 下载 EXE

前往 [Releases](https://github.com/Asuka-Liu/DeepseekGetBalance/releases) 下载最新版本，解压后双击 `DeepSeekBalance.exe` 运行。

## 配置说明

`config.json` 参数：

| 参数 | 类型 | 说明 |
|------|------|------|
| `api_key` | string | DeepSeek API 密钥 |
| `auto_refresh_seconds` | int | 自动刷新间隔（秒），默认 30 |

## 自行打包

```bash
pip install pyinstaller
py -m PyInstaller --noconfirm --onefile --windowed --name "DeepSeekBalance" --add-data "index.html;." --icon "icon.ico" "check_balance.pyw"
```

生成的 EXE 在 `dist/` 目录下。

## 技术栈

- Python 3.12+
- pywebview - 桌面窗口
- requests - HTTP 请求
- PyInstaller - 打包

## 许可证

MIT License
