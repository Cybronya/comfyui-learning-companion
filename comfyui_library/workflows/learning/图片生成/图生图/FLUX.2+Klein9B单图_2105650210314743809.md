---
key: 图片生成/图生图/FLUX.2+Klein9B单图_2105650210314743809.json
name: FLUX.2+Klein9B单图_2105650210314743809
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2+Klein9B单图_2105650210314743809.json
hash: dd7a9f8cccc7b3b7
coverage: 0.941176
learned_at: 2026-10-23 10:54:10
nodes: [CR Text, JoinStrings, Image Comparer (rgthree), AILab_ColorInput, VAELoader, KSampler, GetImageSize+, PainterFluxImageEdit, CLIPLoader, VAEDecode, SaveImage, ConstrainImage|pysssss, LoraLoaderModelOnly, UNETLoader, RMBG, ImageLoader, CR Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1009392648554891, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FLUX.2+Klein9B单图_2105650210314743809.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2+Klein9B单图_2105650210314743809.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `CR Text`
- `JoinStrings`
- `Image Comparer (rgthree)`
- `AILab_ColorInput`
- `VAELoader`
- `KSampler` ★核心
- `GetImageSize+`
- `PainterFluxImageEdit`
- `CLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `ConstrainImage|pysssss`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `RMBG`
- `ImageLoader`
- `CR Text`

## 关键参数

- `seed` = `1009392648554891`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`CR Text`、`JoinStrings`、`AILab_ColorInput`、`VAELoader`、`KSampler`、`GetImageSize+`、`PainterFluxImageEdit`、`CLIPLoader`、`VAEDecode`、`SaveImage`、`ConstrainImage|pysssss`、`LoraLoaderModelOnly`、`UNETLoader`、`RMBG`、`ImageLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、PainterFluxImageEdit、GetImageSize+

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
