# [Comfy3D] CharacterGen MVDiffusion Model

## 节点类型

`[Comfy3D] CharacterGen MVDiffusion Model`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `character_mv_gen_pipe:CHARACTER_MV_GEN_PIPE`（1 次）
- `reference_image:IMAGE`（1 次）
- `reference_mask:MASK`（1 次）
- `target_image_width:INT`（1 次）
- `target_image_height:INT`（1 次）
- `seed:INT`（1 次）
- `guidance_scale:FLOAT`（1 次）
- `num_inference_steps:INT`（1 次）
- `prompt:STRING`（1 次）
- `prompt_neg:STRING`（1 次）

## 输出

- `multiviews:IMAGE`（1 次）
- `orbit_camposes:ORBIT_CAMPOSES`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[512, 768, 501621593187865, "randomize", 5, 40, "high quality, best quality", "", 1.5]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
