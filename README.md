# 深潜器静水压力云图演示

一个简单的深潜器静水压力教学演示程序：在浏览器中展示三维深潜器模型，
输入（或自动增加）下潜深度后，实时显示壳体表面的静水压力分布云图。

- 压力模型：`P = ρgh`（海水密度 ρ = 1025 kg/m³），逐顶点着色
- 深度范围：0 ~ 12000 m，色标 0 ~ 120 MPa（Jet 色标）
- 附带效果：下潜气泡、背景随深度由浅蓝渐变至深黑、鼠标旋转/缩放视图

> 说明：壳体垂向压力梯度（10 m 艇高仅约 0.1 MPa）相对全量程过小，
> 显示时做了 ×600 的垂向放大以便观察；HUD 数值均为未放大的真实量。

## 文件清单

| 文件 | 说明 |
|---|---|
| `index.html` | 演示页面（全部逻辑都在其中，Three.js r147） |
| `sub.zip` | 深潜器三维模型（zip 压缩，解压出 `sub.glb` 放到本目录） |
| `three.min.js` / `OrbitControls.js` / `BufferGeometryUtils.js` / `GLTFLoader.js` | Three.js 及插件（本地化，无需联网） |
| `launcher.py` | 启动器：内置 HTTP 服务器并自动打开浏览器 |

## 准备

先把 `sub.zip` 解压，得到 `sub.glb` 并与 `index.html` 放在同一目录。

## 运行方式

由于浏览器禁止 `file://` 下加载模型，需通过本地 HTTP 打开：

**方式一（推荐）**：Python 启动器

```
python launcher.py
```

**方式二**：任意静态服务器

```
python -m http.server 8000
# 然后浏览器访问 http://127.0.0.1:8000/index.html
```

## 打包为 exe（可选）

```
pip install pyinstaller
python -m PyInstaller --onefile --name 深潜器压力云图演示 ^
  --add-data "index.html;." --add-data "sub.glb;." ^
  --add-data "three.min.js;." --add-data "OrbitControls.js;." ^
  --add-data "BufferGeometryUtils.js;." --add-data "GLTFLoader.js;." ^
  launcher.py
```

生成的单个 exe 即可脱离 Python 环境直接分发运行。

## 备注

模型原始大小约 139 MB，超过 GitHub 单文件 100 MB 限制，故仓库中以 zip
压缩形式（约 68 MB）提供，下载后请先解压。
