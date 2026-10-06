# LayerUtility: ImageMaskScaleAs

## 节点类型

`LayerUtility: ImageMaskScaleAs`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `scale_as:*`（2 次）
- `image:IMAGE`（2 次）
- `mask:MASK`（2 次）
- `fit:COMBO`（2 次）
- `method:COMBO`（2 次）

## 输出

- `image:IMAGE`（2 次）
- `mask:MASK`（2 次）
- `original_size:BOX`（2 次）
- `widht:INT`（2 次）
- `height:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["letterbox", "lanczos"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
