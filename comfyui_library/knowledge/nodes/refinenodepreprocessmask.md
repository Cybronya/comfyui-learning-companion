# RefineNodePreprocessMask

## 节点类型

`RefineNodePreprocessMask`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `mask:MASK`（2 次）
- `focus_crop:BOOLEAN`（2 次）
- `focus_crop_margin:INT`（2 次）
- `spatial_prompt_source:COMBO`（2 次）

## 输出

- `image:IMAGE`（2 次）
- `spatial_mask_image:IMAGE`（2 次）
- `mask:MASK`（2 次）
- `info:REFINENODE_INFO`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, 32, "mask"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
