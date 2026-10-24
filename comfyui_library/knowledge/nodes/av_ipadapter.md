# AV_IPAdapter

## 节点类型

`AV_IPAdapter`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `model:MODEL`（5 次）
- `image:IMAGE`（5 次）
- `ip_adapter_opt:IPADAPTER`（5 次）
- `clip_vision_opt:CLIP_VISION`（5 次）
- `attn_mask:MASK`（5 次）
- `ip_adapter_name:COMBO`（4 次）
- `clip_name:COMBO`（4 次）
- `weight:FLOAT`（4 次）
- `start_at:FLOAT`（4 次）
- `end_at:FLOAT`（4 次）

## 输出

- `model:MODEL`（5 次）
- `pipeline:IPADAPTER`（5 次）
- `clip_vision:CLIP_VISION`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["ip-adapter_sdxl.safetensors", "CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors", 0.6900000000000002, 0, 1, "standard", tru`（2 次）
- `["ip-adapter_sdxl_vit-h.safetensors", "CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors", 0.65, 0, 0, "standard", "style tran`（1 次）
- `["ip-adapter-plus_sdxl_vit-h.safetensors", "CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors", 0.9, 0, 0, "style transfer", "`（1 次）
- `["ip-adapter-plus_sdxl_vit-h.safetensors", "CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors", 0.99, 0, 0, 1, "standard"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
