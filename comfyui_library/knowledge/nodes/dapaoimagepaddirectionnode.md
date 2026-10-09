# DapaoImagePadDirectionNode

## 节点类型

`DapaoImagePadDirectionNode`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `📸 图像:IMAGE`（1 次）
- `😷 遮罩:MASK`（1 次）
- `📏 单位:COMBO`（1 次）
- `⬅️ 左:INT`（1 次）
- `➡️ 右:INT`（1 次）
- `⬆️ 上:INT`（1 次）
- `⬇️ 下:INT`（1 次）
- `🎨 填充颜色:COMBO`（1 次）
- `🌈 填充色HEX:STRING`（1 次）
- `🌫️ 羽化:INT`（1 次）

## 输出

- `🖼️ 图像:IMAGE`（1 次）
- `😷 遮罩:MASK`（1 次）
- `❓ 是否外补:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["百分比", 120, 120, 30, 60, "green", "#000000", 0, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
