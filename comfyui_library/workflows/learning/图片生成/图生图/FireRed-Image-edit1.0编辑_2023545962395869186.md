---
key: 图片生成/图生图/FireRed-Image-edit1.0编辑_2023545962395869186.json
name: FireRed-Image-edit1.0编辑_2023545962395869186
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-edit1.0编辑_2023545962395869186.json
hash: 380cfcf115c7770d
coverage: 0.730769
learned_at: 2026-10-23 10:55:49
nodes: [UNETLoader, SetNode, CLIPLoader, SetNode, SetNode, VAELoader, GetNode, GetNode, GetNode, LoraLoaderModelOnly, Reroute, FluxKontextImageScale, FluxKontextImageScale, VAEDecode, GetNode, GetNode, LoraLoaderModelOnly, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, Reroute, Reroute, GetImageSize, EmptyLatentImage, FluxKontextImageScale, GetNode, easy anythingIndexSwitch, easy anythingInversedSwitch, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, GetImageSize, EmptyLatentImage, KSampler, YCImageAccumulator, KSampler, SaveImage, LayerUtility: TextBox, Int, YCImageAccumulator, LoadImage, LoadImage, easy anythingIndexSwitch, YCImageAccumulator, LoadImage, LayerUtility: TextBox, LayerUtility: TextBox, LayerUtility: TextBox, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), VAEDecode, SaveImage, Note]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 93990668462618, "steps": 8, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-edit1.0编辑_2023545962395869186.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-edit1.0编辑_2023545962395869186.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `UNETLoader` ★核心
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `VAELoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `FluxKontextImageScale`
- `FluxKontextImageScale`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `Reroute`
- `Reroute`
- `GetImageSize`
- `EmptyLatentImage` ★核心
- `FluxKontextImageScale`
- `GetNode`
- `easy anythingIndexSwitch`
- `easy anythingInversedSwitch`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `GetImageSize`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `YCImageAccumulator`
- `KSampler` ★核心
- `SaveImage`
- `LayerUtility: TextBox`
- `Int`
- `YCImageAccumulator`
- `LoadImage`
- `LoadImage`
- `easy anythingIndexSwitch`
- `YCImageAccumulator`
- `LoadImage`
- `LayerUtility: TextBox`
- `LayerUtility: TextBox`
- `LayerUtility: TextBox`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `VAEDecode` ★核心
- `SaveImage`
- `Note`

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `93990668462618`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **73%**（38/52）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`FluxKontextImageScale`、`VAEDecode`、`TextEncodeQwenImageEditPlus`、`GetImageSize`、`EmptyLatentImage`、`easy anythingIndexSwitch`、`easy anythingInversedSwitch`、`KSampler`、`YCImageAccumulator`、`SaveImage`、`LayerUtility: TextBox`、`Int`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
