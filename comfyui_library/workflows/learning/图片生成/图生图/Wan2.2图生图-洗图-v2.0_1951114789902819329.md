---
key: 图片生成/图生图/Wan2.2图生图-洗图-v2.0_1951114789902819329.json
name: Wan2.2图生图-洗图-v2.0_1951114789902819329
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2图生图-洗图-v2.0_1951114789902819329.json
hash: 3a80d20748593696
coverage: 0.966667
learned_at: 2026-10-23 11:28:20
nodes: [LoraLoaderModelOnly, CLIPTextEncode, VAEEncode, PathchSageAttentionKJ, ModelSamplingSD3, UNETLoader, VAEDecode, CLIPLoader, VAELoader, PDIMAGE_LongerSize, VAEDecode, SaveImage, SaveImage, KSampler, Float, RH_Captioner, LoadImage, UNETLoader, CLIPTextEncode, PreviewImage, Seed_, LoadImage, KSampler, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, Float, PMRF]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 497163970725457, "steps": 10}
---

# 图片生成/图生图/Wan2.2图生图-洗图-v2.0_1951114789902819329.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2图生图-洗图-v2.0_1951114789902819329.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `PDIMAGE_LongerSize`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `KSampler` ★核心
- `Float`
- `RH_Captioner`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `Seed_`
- `LoadImage`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `Float`
- `PMRF`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `497163970725457`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **97%**（29/30）

**有卡**：`LoraLoaderModelOnly`、`CLIPTextEncode`、`VAEEncode`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`UNETLoader`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`PDIMAGE_LongerSize`、`SaveImage`、`KSampler`、`Float`、`RH_Captioner`、`LoadImage`、`Seed_`、`PMRF`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
