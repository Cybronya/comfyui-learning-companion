---
key: 图片生成/图生图/Z-image-controlne Union2.0局部重绘_2002990674276433922.json
name: Z-image-controlne Union2.0局部重绘_2002990674276433922
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-image-controlne Union2.0局部重绘_2002990674276433922.json
hash: 5f5e9f03a3e072a1
coverage: 0.9375
learned_at: 2026-10-23 11:30:59
nodes: [UNETLoader, CLIPLoader, ModelSamplingAuraFlow, ZImageFunControlnet, ModelPatchLoader, VAEDecode, KSampler, Image Comparer (rgthree), CLIPTextEncode, VAEEncode, CLIPTextEncode, LoadImage, 图像缩放V2_孤海, VAELoader, SaveImage, CR Text]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1.5, "denoise": 1, "sampler_name": "euler", "scheduler": "beta57", "seed": 1046975201775628, "steps": 10}
---

# 图片生成/图生图/Z-image-controlne Union2.0局部重绘_2002990674276433922.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-image-controlne Union2.0局部重绘_2002990674276433922.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Output → Other

**节点**（16 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `ZImageFunControlnet`
- `ModelPatchLoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `图像缩放V2_孤海`
- `VAELoader`
- `SaveImage`
- `CR Text`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1046975201775628`
- `steps` = `10`
- `cfg` = `1.5`
- `sampler_name` = `euler`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`UNETLoader`、`CLIPLoader`、`ModelSamplingAuraFlow`、`ZImageFunControlnet`、`ModelPatchLoader`、`VAEDecode`、`KSampler`、`CLIPTextEncode`、`VAEEncode`、`LoadImage`、`图像缩放V2_孤海`、`VAELoader`、`SaveImage`、`CR Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、ZImageFunControlnet
