# CreateBoundingBoxes

## 节点类型

`CreateBoundingBoxes`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `background:IMAGE`（5 次）
- `bboxes:BOUNDING_BOX,ARRAY,STRING`（5 次）

## 输出

- `preview:IMAGE`（5 次）
- `bboxes:BOUNDING_BOX`（5 次）
- `elements:ARRAY`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[896, 1152, [{"x": 192, "y": 384, "width": 288, "height": 352, "metadata": {"type": "obj", "text": "", "desc": "Change i`（1 次）
- `[1024, 1024, [{"x": 128, "y": 32, "width": 824, "height": 124, "metadata": {"type": "text", "text": "Ideogram P-Image", `（1 次）
- `[896, 1152, [{"x": 96, "y": 768, "width": 672, "height": 352, "metadata": {"type": "obj", "text": "", "desc": "Change th`（1 次）
- `[896, 1152, [{"x": 448, "y": 384, "width": 128, "height": 128, "metadata": {"type": "obj", "text": "", "desc": "Change t`（1 次）
- `[896, 1152, [{"x": 0, "y": 0, "width": 896, "height": 1152, "metadata": {"type": "obj", "text": "", "desc": "the whole p`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
