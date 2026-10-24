---
key: 图片生成/图生图/Flux.2-Klein图片处理-快速出图_2068580867752161281.json
name: Flux.2-Klein图片处理-快速出图_2068580867752161281
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux.2-Klein图片处理-快速出图_2068580867752161281.json
hash: 346a98b227c7a803
coverage: 0.882353
learned_at: 2026-10-23 10:58:50
nodes: [VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, KSampler, Image Comparer (rgthree), EmptyFlux2LatentImage, VAELoader, CLIPTextEncode, ReferenceLatent, CLIPLoader, UNETLoader, CLIPTextEncode, ReferenceLatent, LoadImage, PreviewImage, VAEDecode, SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 523048884273134, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Flux.2-Klein图片处理-快速出图_2068580867752161281.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux.2-Klein图片处理-快速出图_2068580867752161281.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `EmptyFlux2LatentImage`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `LoadImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `523048884273134`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM`、`KSampler`、`EmptyFlux2LatentImage`、`VAELoader`、`CLIPTextEncode`、`ReferenceLatent`、`CLIPLoader`、`UNETLoader`、`LoadImage`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage、EmptyFlux2LatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
