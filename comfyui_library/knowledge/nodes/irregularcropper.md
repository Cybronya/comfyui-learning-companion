# IrregularCropper

## 节点类型

`IrregularCropper`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `crop_mode:COMBO`（2 次）
- `background_fill:COMBO`（2 次）
- `edge_smooth:INT`（2 次）
- `auto_crop:BOOLEAN`（2 次）
- `crop_padding:INT`（2 次）

## 输出

- `裁剪图像:IMAGE`（2 次）
- `选择区域:MASK`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["polygon", "transparent", 0, true, 10, "多边形模式：点击添加顶点，双击闭合路径\n自由绘制模式：按住鼠标拖拽绘制选择区域", 1015350357451675, "randomize", null]`（1 次）
- `["polygon", "transparent", 0, true, 10, "多边形模式：点击添加顶点，双击闭合路径\n自由绘制模式：按住鼠标拖拽绘制选择区域", 802483167736461, "randomize", null]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
