# DapaoImageAspectRatioResizeNode

## 节点类型

`DapaoImageAspectRatioResizeNode`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `📸 图像:IMAGE`（1 次）
- `😷 遮罩:MASK`（1 次）
- `📐 宽高比:COMBO`（1 次）
- `📏 比例宽度:INT`（1 次）
- `📏 比例高度:INT`（1 次）
- `🎨 适应模式:COMBO`（1 次）
- `🔍 缩放算法:COMBO`（1 次）
- `🔢 尺寸倍数:INT`（1 次）
- `📏 锁定边长:COMBO`（1 次）
- `📏 锁定长度:INT`（1 次）

## 输出

- `🖼️ 图像:IMAGE`（1 次）
- `😷 遮罩:MASK`（1 次）
- `📏 原始尺寸:INT`（1 次）
- `📏 宽度:INT`（1 次）
- `📏 高度:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["原图", 1, 1, "包含", "lanczos", 8, "锁定最长边", 1024, "#000000"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
