---
key: 图片生成/图生图/FLUX.2-KLEIN-自动抠图-一键电商换场景换背景_2020005854803664897.json
name: FLUX.2-KLEIN-自动抠图-一键电商换场景换背景_2020005854803664897
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.2-KLEIN-自动抠图-一键电商换场景换背景_2020005854803664897.json
hash: 84d533f268f5b67c
coverage: 0.758621
learned_at: 2026-10-23 10:54:12
nodes: [Image Comparer (rgthree), Image Comparer (rgthree), Image Comparer (rgthree), Image Comparer (rgthree), Image Comparer (rgthree), CR Text Concatenate, easy imageRemBg, easy imageRemBg, LayerUtility: ImageScaleByAspectRatio V2, LayerMask: MaskGrow, VAELoader, AILab_QwenVL, CR Text, ShowText, CLIPLoader, LoraLoaderModelOnly, PainterFluxImageEdit, UNETLoader, KSampler, VAEDecode, Image Comparer (rgthree), LoadImage, LoadImage, Label (rgthree), MaskPreview, easy imageDetailTransfer, CustomAddLabel, Image Comparer (rgthree), SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 555, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FLUX.2-KLEIN-自动抠图-一键电商换场景换背景_2020005854803664897.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.2-KLEIN-自动抠图-一键电商换场景换背景_2020005854803664897.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `CR Text Concatenate`
- `easy imageRemBg`
- `easy imageRemBg`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerMask: MaskGrow`
- `VAELoader`
- `AILab_QwenVL`
- `CR Text`
- `ShowText`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `PainterFluxImageEdit`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoadImage`
- `Label (rgthree)`
- `MaskPreview`
- `easy imageDetailTransfer`
- `CustomAddLabel`
- `Image Comparer (rgthree)`
- `SaveImage`

## 关键参数

- `seed` = `555`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **76%**（22/29）

**有卡**：`CR Text Concatenate`、`easy imageRemBg`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerMask: MaskGrow`、`VAELoader`、`AILab_QwenVL`、`CR Text`、`ShowText`、`CLIPLoader`、`LoraLoaderModelOnly`、`PainterFluxImageEdit`、`UNETLoader`、`KSampler`、`VAEDecode`、`LoadImage`、`Label (rgthree)`、`MaskPreview`、`easy imageDetailTransfer`、`CustomAddLabel`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、PainterFluxImageEdit

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
