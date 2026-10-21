---
key: 图片生成/图生图/图片精修_质感修复Texture_Restoration_Retouching_2099340238937219074.json
name: 图片精修_质感修复Texture_Restoration_Retouching_2099340238937219074
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图片精修_质感修复Texture_Restoration_Retouching_2099340238937219074.json
hash: b66045d926aa82ae
coverage: 0.842105
learned_at: 2026-10-21 00:51:20
nodes: [CLIPTextEncode, PathchSageAttentionKJ, ModelSamplingSD3, VAEEncode, CLIPLoader, UNETLoader, VAELoader, LoraLoader, LoraLoader, LoraLoader, VAEDecode, Image Comparer (rgthree), SaveImage, KSampler, easy imageScaleDownToSize, Note, Note, CLIPTextEncode, LoadImage]
patterns: [image_to_image, lora]
missing: []
parameters: {"cfg": 1, "denoise": 0.30000000000000004, "lora_name": "wan-1024-电商-30epl.safetensors", "sampler_name": "res_2m", "scheduler": "beta", "seed": 445223951976583, "steps": 10, "strength_clip": 0.4000000000000001, "strength_model": 0.4000000000000001}
---

# 图片生成/图生图/图片精修_质感修复Texture_Restoration_Retouching_2099340238937219074.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图片精修_质感修复Texture_Restoration_Retouching_2099340238937219074.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `VAEEncode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `KSampler` ★核心
- `easy imageScaleDownToSize`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `LoadImage`

**识别到的模式**：image_to_image、lora

## 关键参数

- `lora_name` = `wan-1024-电商-30epl.safetensors`
- `strength_model` = `0.4000000000000001`
- `strength_clip` = `0.4000000000000001`
- `seed` = `445223951976583`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_2m`
- `scheduler` = `beta`
- `denoise` = `0.30000000000000004`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`CLIPTextEncode`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`VAEEncode`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`LoraLoader`、`VAEDecode`、`SaveImage`、`KSampler`、`easy imageScaleDownToSize`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、VAEEncode
