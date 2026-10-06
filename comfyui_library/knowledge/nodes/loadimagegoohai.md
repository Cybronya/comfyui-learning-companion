# LoadImageGoohai

## 节点类型

`LoadImageGoohai`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 13 个 workflow 中。

## 输入

- `image:COMBO`（13 次）
- `upload:IMAGEUPLOAD`（13 次）
- `保留透明通道:BOOLEAN`（13 次）

## 输出

- `图像:IMAGE`（13 次）
- `遮罩:MASK`（13 次）
- `文件名:STRING`（13 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[null, "clipspace/70e9a7d48146d5cadbda96a2335f807ef92ebcba6a6114d54358983e9a44188c.png [input]", null, false]`（2 次）
- `["clipspace/177eb1686c1e6604b4471253369157d06bb6fa2d67616ad53483c5a14b0bffb2.jpg [input]", "clipspace/177eb1686c1e6604b4`（2 次）
- `["16d923c0e04f94c1925c7460ddf535988bba7443d918ec4480ad5e589fc7c290.jpg [input]", "16d923c0e04f94c1925c7460ddf535988bba74`（2 次）
- `[null, "3744648c3cfe9adf8a8be352c34a21925d049e39efbaf4dde2f713c8a1901935.png [input]", null, true]`（2 次）
- `["648fd228395f6a7c52c2e28a88d220ead3445c2ee067008fe1eaf85f6ca0f289.jpg [input]", "648fd228395f6a7c52c2e28a88d220ead3445c`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
