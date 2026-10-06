# Sa2VANodeTpl

## 节点类型

`Sa2VANodeTpl`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `model_name:COMBO`（2 次）
- `mask_threshold:FLOAT`（2 次）
- `use_8bit_quantization:BOOLEAN`（2 次）
- `use_flash_attn:BOOLEAN`（2 次）
- `segmentation_prompt:STRING`（2 次）

## 输出

- `text_outputs:LIST`（2 次）
- `masks:MASK`（2 次）
- `mask_images:IMAGE`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["ByteDance/Sa2VA-Qwen3-VL-4B", 1, false, true, "pillow"]`（1 次）
- `["ByteDance/Sa2VA-Qwen3-VL-4B", 1, false, true, "person"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
