---
key: 图片生成/图生图/F.2 Klein 9B电商产品换背景_2061791311056953345.json
name: F.2 Klein 9B电商产品换背景_2061791311056953345
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2 Klein 9B电商产品换背景_2061791311056953345.json
hash: b88d386e86922f45
coverage: 0.902439
learned_at: 2026-10-21 00:38:55
nodes: [AILab_LoadImage, CR Text, JoinStrings, Image Comparer (rgthree), AILab_ColorInput, VAELoader, KSampler, ShowText|pysssss, CR Text, RMBG, Image Comparer (rgthree), AILab_ColorInput, VAELoader, CLIPLoader, KSampler, CR Text, AILab_QwenVL, CR Text, GetImageSize+, PainterFluxImageEdit, UNETLoader, JoinStrings, CLIPLoader, LoraLoaderModelOnly, VAEDecode, SaveImage, VAEDecode, SaveImage, ImageLoader, DownloadAndLoadQwen2_5_VLModel, ImageLoader, PainterFluxImageEdit, Qwen2_5_VL_Run, GetImageSize+, ConstrainImage|pysssss, ImageLoader, ConstrainImage|pysssss, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, UNETLoader, RMBG]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 447426078833645, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/F.2 Klein 9B电商产品换背景_2061791311056953345.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2 Klein 9B电商产品换背景_2061791311056953345.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `AILab_LoadImage`
- `CR Text`
- `JoinStrings`
- `Image Comparer (rgthree)`
- `AILab_ColorInput`
- `VAELoader`
- `KSampler` ★核心
- `ShowText|pysssss`
- `CR Text`
- `RMBG`
- `Image Comparer (rgthree)`
- `AILab_ColorInput`
- `VAELoader`
- `CLIPLoader`
- `KSampler` ★核心
- `CR Text`
- `AILab_QwenVL`
- `CR Text`
- `GetImageSize+`
- `PainterFluxImageEdit`
- `UNETLoader` ★核心
- `JoinStrings`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `SaveImage`
- `ImageLoader`
- `DownloadAndLoadQwen2_5_VLModel`
- `ImageLoader`
- `PainterFluxImageEdit`
- `Qwen2_5_VL_Run`
- `GetImageSize+`
- `ConstrainImage|pysssss`
- `ImageLoader`
- `ConstrainImage|pysssss`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `RMBG`

## 关键参数

- `seed` = `447426078833645`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（37/41）

**有卡**：`AILab_LoadImage`、`CR Text`、`JoinStrings`、`AILab_ColorInput`、`VAELoader`、`KSampler`、`RMBG`、`CLIPLoader`、`AILab_QwenVL`、`GetImageSize+`、`PainterFluxImageEdit`、`UNETLoader`、`LoraLoaderModelOnly`、`VAEDecode`、`SaveImage`、`ImageLoader`、`DownloadAndLoadQwen2_5_VLModel`、`Qwen2_5_VL_Run`、`ConstrainImage|pysssss`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、PainterFluxImageEdit、GetImageSize+

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
