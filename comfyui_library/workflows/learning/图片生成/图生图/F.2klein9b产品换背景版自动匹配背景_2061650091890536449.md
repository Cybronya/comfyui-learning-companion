---
key: 图片生成/图生图/F.2klein9b产品换背景版自动匹配背景_2061650091890536449.json
name: F.2klein9b产品换背景版自动匹配背景_2061650091890536449
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2klein9b产品换背景版自动匹配背景_2061650091890536449.json
hash: 0043b50aeb786894
coverage: 0.771429
learned_at: 2026-10-23 10:52:52
nodes: [CLIPLoader, GetNode, Image Comparer (rgthree), GetImageSize, GrowMaskWithBlur, VAELoader, VAEDecode, KSampler, 孤海-遮罩混合运算, CR Text, JoinStrings, PainterFluxImageEdit, PreviewImage, GetNode, MaskPreview+, CR Text, ShowText|pysssss, SaveImage, PainterFluxImageEdit, KSampler, VAEDecode, easy imageConcat, Image Comparer (rgthree), SetNode, SaveImage, LoraLoaderModelOnly, UNETLoader, CR Text, LoraLoaderModelOnly, LoadImage, AILab_MiniCPM_4_V, LayerUtility: ImageScaleByAspectRatio V2, Int, RMBG, SetNode]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 441856971938843, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/F.2klein9b产品换背景版自动匹配背景_2061650091890536449.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2klein9b产品换背景版自动匹配背景_2061650091890536449.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `CLIPLoader`
- `GetNode`
- `Image Comparer (rgthree)`
- `GetImageSize`
- `GrowMaskWithBlur`
- `VAELoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `孤海-遮罩混合运算`
- `CR Text`
- `JoinStrings`
- `PainterFluxImageEdit`
- `PreviewImage`
- `GetNode`
- `MaskPreview+`
- `CR Text`
- `ShowText|pysssss`
- `SaveImage`
- `PainterFluxImageEdit`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `easy imageConcat`
- `Image Comparer (rgthree)`
- `SetNode`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `AILab_MiniCPM_4_V`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `RMBG`
- `SetNode`

## 关键参数

- `seed` = `441856971938843`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（27/35）

**有卡**：`CLIPLoader`、`GetImageSize`、`GrowMaskWithBlur`、`VAELoader`、`VAEDecode`、`KSampler`、`孤海-遮罩混合运算`、`CR Text`、`JoinStrings`、`PainterFluxImageEdit`、`MaskPreview+`、`SaveImage`、`easy imageConcat`、`LoraLoaderModelOnly`、`UNETLoader`、`LoadImage`、`AILab_MiniCPM_4_V`、`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`RMBG`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、PainterFluxImageEdit

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
