# TextOverlayImage

## 节点类型

`TextOverlayImage`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `图像:IMAGE`（6 次）
- `文字颜色:*`（6 次）
- `文本:STRING`（6 次）
- `字体:COMBO`（6 次）
- `字体大小:INT`（6 次）
- `字体颜色:COMBO`（6 次）
- `排版:COMBO`（6 次）
- `X位置:INT`（6 次）
- `Y位置:INT`（6 次）

## 输出

- `图像:IMAGE`（6 次）
- `文字遮罩:MASK`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "C", 128, "黑", "横向", 384, 512]`（6 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
