---
key: 图片生成/图生图/FLUX.2+Klein9B单图_2105504127831855106.json
name: FLUX.2+Klein9B单图_2105504127831855106
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2+Klein9B单图_2105504127831855106.json
hash: 98544a585af61364
coverage: 0.941176
learned_at: 2026-10-23 10:54:09
nodes: [CR Text, AILab_ColorInput, VAELoader, KSampler, GetImageSize+, CLIPLoader, VAEDecode, SaveImage, LoraLoaderModelOnly, UNETLoader, RMBG, CR Text, JoinStrings, Image Comparer (rgthree), ConstrainImage|pysssss, ImageLoader, PainterFluxImageEdit]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 73512777984360, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FLUX.2+Klein9B单图_2105504127831855106.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2+Klein9B单图_2105504127831855106.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `CR Text`
- `AILab_ColorInput`
- `VAELoader`
- `KSampler` ★核心
- `GetImageSize+`
- `CLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `RMBG`
- `CR Text`
- `JoinStrings`
- `Image Comparer (rgthree)`
- `ConstrainImage|pysssss`
- `ImageLoader`
- `PainterFluxImageEdit`

## 关键参数

- `seed` = `73512777984360`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`CR Text`、`AILab_ColorInput`、`VAELoader`、`KSampler`、`GetImageSize+`、`CLIPLoader`、`VAEDecode`、`SaveImage`、`LoraLoaderModelOnly`、`UNETLoader`、`RMBG`、`JoinStrings`、`ConstrainImage|pysssss`、`ImageLoader`、`PainterFluxImageEdit`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、PainterFluxImageEdit、GetImageSize+

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
