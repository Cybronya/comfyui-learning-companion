# PrepareImageAndMaskForInpaint

## 节点类型

`PrepareImageAndMaskForInpaint`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `image:IMAGE`（4 次）
- `mask:MASK`（4 次）

## 输出

- `inpaint_image:IMAGE`（4 次）
- `inpaint_mask:MASK`（4 次）
- `overlay_image:IMAGE`（4 次）
- `crop_region:CROP_REGION`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[0, true, 0]`（2 次）
- `[4, false, 32]`（1 次）
- `[4, true, 32]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
