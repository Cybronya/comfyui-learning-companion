# LayerMask: SAM2VideoUltra

## 节点类型

`LayerMask: SAM2VideoUltra`

## 分类

Mask

## 作用

遮罩类节点：生成或处理遮罩（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `bboxes:BBOXES`（2 次）
- `first_frame_mask:MASK`（2 次）
- `pre_mask:MASK`（2 次）
- `sam2_model:COMBO`（2 次）
- `precision:COMBO`（2 次）
- `cache_model:BOOLEAN`（2 次）
- `individual_objects:BOOLEAN`（2 次）
- `mask_preview_color:STRING`（2 次）
- `detail_method:COMBO`（2 次）

## 输出

- `mask:MASK`（2 次）
- `preview:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["sam2_hiera_base_plus.safetensors", "fp16", false, false, "#FF0080", "VITMatte", 6, 4, 0.15000000000000002, 0.99, true,`（1 次）
- `["sam2.1_hiera_large.safetensors", "fp16", false, false, "#FF0080", "VITMatte", 6, 4, 0.15, 0.99, true, "cuda", 0.5]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
