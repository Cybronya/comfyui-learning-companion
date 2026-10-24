---
key: 图片生成/图生图/蒜-FLUX.1 Dev真人转复古动漫_1996908064022401025.json
name: 蒜-FLUX.1 Dev真人转复古动漫_1996908064022401025
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/蒜-FLUX.1 Dev真人转复古动漫_1996908064022401025.json
hash: 793441eaf705f46e
coverage: 0.84
learned_at: 2026-10-23 13:24:57
nodes: [CLIPTextEncode, ConditioningConcat, SamplerCustomAdvanced, VAEDecode, VAEEncode, VAELoader, RandomNoise, KSamplerSelect, BasicScheduler, BasicGuider, FluxGuidance, Miaoshouai_Tagger, PreviewImage, CLIPTextEncode, easy showAnything, UNETLoader, Lora Loader Stack (rgthree), ImageScale, CLIPAttentionMultiply, DualCLIPLoader, LoadImage, SaveImage, SDXLEmptyLatentSizePicker+, Image Comparer (rgthree), Note]
patterns: []
missing: []
parameters: {"batch_size": 0, "height": 1, "width": "768x1280 (0.6)"}
---

# 图片生成/图生图/蒜-FLUX.1 Dev真人转复古动漫_1996908064022401025.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/蒜-FLUX.1 Dev真人转复古动漫_1996908064022401025.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `CLIPTextEncode` ★核心
- `ConditioningConcat`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `VAELoader`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `BasicGuider`
- `FluxGuidance`
- `Miaoshouai_Tagger`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `UNETLoader` ★核心
- `Lora Loader Stack (rgthree)`
- `ImageScale`
- `CLIPAttentionMultiply`
- `DualCLIPLoader`
- `LoadImage`
- `SaveImage`
- `SDXLEmptyLatentSizePicker+` ★核心
- `Image Comparer (rgthree)`
- `Note`

## 关键参数

- `width` = `768x1280 (0.6)`
- `height` = `1`
- `batch_size` = `0`

## 知识

覆盖率 **84%**（21/25）

**有卡**：`CLIPTextEncode`、`ConditioningConcat`、`SamplerCustomAdvanced`、`VAEDecode`、`VAEEncode`、`VAELoader`、`RandomNoise`、`KSamplerSelect`、`BasicScheduler`、`BasicGuider`、`FluxGuidance`、`Miaoshouai_Tagger`、`UNETLoader`、`Lora Loader Stack (rgthree)`、`ImageScale`、`CLIPAttentionMultiply`、`DualCLIPLoader`、`LoadImage`、`SaveImage`、`SDXLEmptyLatentSizePicker+`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
