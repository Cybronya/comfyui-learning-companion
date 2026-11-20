---
key: 平台全量/人物抠图去背景PNG输出image2.1_2118265013197697025.json
name: 人物抠图去背景PNG输出image2.1_2118265013197697025
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/人物抠图去背景PNG输出image2.1_2118265013197697025.json
hash: c43ac582b46a59a0
coverage: 0.565217
learned_at: 2026-11-14 01:37:17
nodes: [SaveImage, Image Comparer (rgthree), VAELoader, VAEDecode, UNETLoader, PrimitiveStringMultiline, CLIPLoader, TextEncodeQwenImage21, EmptyLatentImage, QwenImage21Cache, KSampler, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, GetImageSize, Note, Note, Note, Note, Note, Note, Note, Note]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1076987742068974, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/人物抠图去背景PNG输出image2.1_2118265013197697025.json

> 来源文件 `comfyui_library/workflows/平台全量/人物抠图去背景PNG输出image2.1_2118265013197697025.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `SaveImage`
- `Image Comparer (rgthree)`
- `VAELoader`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `QwenImage21Cache`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `GetImageSize`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1076987742068974`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **57%**（13/23）

**有卡**：`SaveImage`、`VAELoader`、`VAEDecode`、`UNETLoader`、`CLIPLoader`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`QwenImage21Cache`、`KSampler`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`GetImageSize`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
