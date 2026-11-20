---
key: 平台全量/换装-FireRed 1.1_2039251921885728770.json
name: 换装-FireRed 1.1_2039251921885728770
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/换装-FireRed 1.1_2039251921885728770.json
hash: c8dfdc88f76aa693
coverage: 0.75
learned_at: 2026-11-14 02:09:11
nodes: [LoraLoaderModelOnly, ModelSamplingAuraFlow, CFGNorm, KSampler, VAEDecode, CLIPLoader, JjkText, JjkText, LayerUtility: ImageScaleByAspectRatio V2, SetNode, Light-Tool: SimpleTextConnect, ShowText, GetNode, GetNode, CLIPTextEncode, VAELoader, TextEncodeQwenImageEditPlus, GetNode, VAEEncode, SaveImage, Anything Everywhere3, LoadImage, LoadImage, Int, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, BiRefNet_Hugo, LayerMask: SegmentAnythingUltra V2, FillMaskWithColor, SetNode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 738254021440338, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/换装-FireRed 1.1_2039251921885728770.json

> 来源文件 `comfyui_library/workflows/平台全量/换装-FireRed 1.1_2039251921885728770.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `JjkText`
- `JjkText`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `Light-Tool: SimpleTextConnect`
- `ShowText`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `TextEncodeQwenImageEditPlus`
- `GetNode`
- `VAEEncode` ★核心
- `SaveImage`
- `Anything Everywhere3`
- `LoadImage`
- `LoadImage`
- `Int`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `BiRefNet_Hugo`
- `LayerMask: SegmentAnythingUltra V2`
- `FillMaskWithColor`
- `SetNode`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `738254021440338`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **75%**（24/32）

**有卡**：`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`CFGNorm`、`KSampler`、`VAEDecode`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`Light-Tool: SimpleTextConnect`、`ShowText`、`CLIPTextEncode`、`VAELoader`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`SaveImage`、`LoadImage`、`Int`、`UNETLoader`、`BiRefNet_Hugo`、`LayerMask: SegmentAnythingUltra V2`、`FillMaskWithColor`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
