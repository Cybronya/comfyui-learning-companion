---
key: 图片生成/图生图/F.2Klein9B换脸换头二合一_2061626857174421505.json
name: F.2Klein9B换脸换头二合一_2061626857174421505
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.2Klein9B换脸换头二合一_2061626857174421505.json
hash: 4b3aa69e1d14e068
coverage: 0.888889
learned_at: 2026-10-23 10:52:41
nodes: [Mute / Bypass Repeater (rgthree), Fast Bypasser (rgthree), PainterFluxImageEdit, KSampler, SaveImage, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, easy ifElse, easy anythingIndexSwitch, SolidMask, easy isMaskEmpty, CR Text, easy imageRemBg, DapaoImageAspectRatioResizeNode, AutoCropFaces, Image Comparer (rgthree), DapaoImageAspectRatioResizeNode, VAEDecode, LoadImage, LoadImage, ImageConcanate, ImageConcanate, PreviewImage, CR Text, easy int]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1008744692647134, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/F.2Klein9B换脸换头二合一_2061626857174421505.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.2Klein9B换脸换头二合一_2061626857174421505.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `Mute / Bypass Repeater (rgthree)`
- `Fast Bypasser (rgthree)`
- `PainterFluxImageEdit`
- `KSampler` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `easy ifElse`
- `easy anythingIndexSwitch`
- `SolidMask`
- `easy isMaskEmpty`
- `CR Text`
- `easy imageRemBg`
- `DapaoImageAspectRatioResizeNode`
- `AutoCropFaces`
- `Image Comparer (rgthree)`
- `DapaoImageAspectRatioResizeNode`
- `VAEDecode` ★核心
- `LoadImage`
- `LoadImage`
- `ImageConcanate`
- `ImageConcanate`
- `PreviewImage`
- `CR Text`
- `easy int`

## 关键参数

- `seed` = `1008744692647134`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`Mute / Bypass Repeater (rgthree)`、`Fast Bypasser (rgthree)`、`PainterFluxImageEdit`、`KSampler`、`SaveImage`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`easy anythingIndexSwitch`、`SolidMask`、`easy isMaskEmpty`、`CR Text`、`easy imageRemBg`、`DapaoImageAspectRatioResizeNode`、`AutoCropFaces`、`VAEDecode`、`LoadImage`、`ImageConcanate`、`easy int`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、PainterFluxImageEdit

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
