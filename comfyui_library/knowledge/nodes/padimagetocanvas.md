# PadImageToCanvas

## 节点类型

`PadImageToCanvas`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `image:IMAGE`（17 次）
- `width:INT`（17 次）
- `height:INT`（17 次）
- `fill_color:STRING`（17 次）
- `center:BOOLEAN`（17 次）
- `left_padding:INT`（17 次）
- `top_padding:INT`（17 次）

## 输出

- `IMAGE:IMAGE`（17 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[1024, 1024, "#FFFFFF", false, 100, 100]`（4 次）
- `[1024, 1024, "#FFFFFF", true, 100, 100]`（4 次）
- `[1024, 1024, "#FFFFFF", false, 200, 100]`（4 次）
- `[1024, 1024, "#FFFFFF", false, 200, 90]`（4 次）
- `[512, 512, "#FFFFFF", true, 0, 0]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
