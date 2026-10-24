# workflow/232323

## 节点类型

`workflow/232323`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `clip:CLIP`（1 次）
- `image:IMAGE`（1 次）
- `ImageScale image:IMAGE`（1 次）
- `clip_vision:CLIP_VISION`（1 次）
- `ApplyPulidFlux model:MODEL`（1 次）
- `pulid_flux:PULIDFLUX`（1 次）
- `eva_clip:EVA_CLIP`（1 次）
- `face_analysis:FACEANALYSIS`（1 次）
- `attn_mask:MASK`（1 次）
- `CLIPTextEncode clip:CLIP`（1 次）

## 输出

- `SIGMAS:SIGMAS`（1 次）
- `negative:CONDITIONING`（1 次）
- `GUIDER:GUIDER`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["unsloth/Meta-Llama-3.1-8B-bnb-4bit", "", "nearest-exact", 768, 1280, "center", "nearest-exact", 768, 1280, "center", "`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
