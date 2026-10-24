---
key: 图片生成/图生图/WAN2.1洗图_1947171235845562370.json
name: WAN2.1洗图_1947171235845562370
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/WAN2.1洗图_1947171235845562370.json
hash: 4344ec638f41b005
coverage: 0.894737
learned_at: 2026-10-23 11:27:26
nodes: [CLIPLoader, VAELoader, RH_Captioner, VAEDecode, Image Comparer (rgthree), SaveImage, UNETLoader, easy showAnything, VAEEncode, LoraLoaderModelOnly, PathchSageAttentionKJ, LayerUtility: ImageScaleRestore V2, UpscaleModelLoader, CLIPTextEncode, ImageUpscaleWithModel, CLIPTextEncode, LoraLoaderModelOnly, KSampler, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.18000000000000005, "sampler_name": "uni_pc", "scheduler": "beta", "seed": 1093099436642798, "steps": 10}
---

# 图片生成/图生图/WAN2.1洗图_1947171235845562370.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/WAN2.1洗图_1947171235845562370.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `CLIPLoader`
- `VAELoader`
- `RH_Captioner`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `UNETLoader` ★核心
- `easy showAnything`
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `LayerUtility: ImageScaleRestore V2`
- `UpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `ImageUpscaleWithModel`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1093099436642798`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `beta`
- `denoise` = `0.18000000000000005`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`CLIPLoader`、`VAELoader`、`RH_Captioner`、`VAEDecode`、`SaveImage`、`UNETLoader`、`VAEEncode`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`LayerUtility: ImageScaleRestore V2`、`UpscaleModelLoader`、`CLIPTextEncode`、`ImageUpscaleWithModel`、`KSampler`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
