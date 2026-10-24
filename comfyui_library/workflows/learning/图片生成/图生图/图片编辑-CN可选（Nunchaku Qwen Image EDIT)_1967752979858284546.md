---
key: 图片生成/图生图/图片编辑-CN可选（Nunchaku Qwen Image EDIT)_1967752979858284546.json
name: 图片编辑-CN可选（Nunchaku Qwen Image EDIT)_1967752979858284546
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图片编辑-CN可选（Nunchaku Qwen Image EDIT)_1967752979858284546.json
hash: 5546e1c2165b2a71
coverage: 0.888889
learned_at: 2026-10-23 12:41:25
nodes: [ImageConcanate, SaveImage, ModelSamplingAuraFlow, CFGNorm, PreviewImage, SetUnionControlNetType, PreviewImage, SetUnionControlNetType, AIO_Preprocessor, AIO_Preprocessor, NunchakuQwenImageDiTLoader, KSampler, VAEDecode, SaveImage, VAEEncode, ImageScaleToMegapixels, CLIPLoader, LoadImage, LoadImage, ImpactSwitch, TextEncodeQwenImageEdit, VAELoader, ControlNetLoader, ControlNetApplySD3, ControlNetApplySD3, LoadImage, TextEncodeQwenImageEdit]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "controlnet_strength": 0.6000000000000001, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 809456897589742, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/图片编辑-CN可选（Nunchaku Qwen Image EDIT)_1967752979858284546.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图片编辑-CN可选（Nunchaku Qwen Image EDIT)_1967752979858284546.json`

## 结构

**生成流程**：Model → Encode → Control → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `ImageConcanate`
- `SaveImage`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `PreviewImage`
- `SetUnionControlNetType`
- `PreviewImage`
- `SetUnionControlNetType`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `NunchakuQwenImageDiTLoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `VAEEncode` ★核心
- `ImageScaleToMegapixels`
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `ImpactSwitch`
- `TextEncodeQwenImageEdit`
- `VAELoader`
- `ControlNetLoader`
- `ControlNetApplySD3` ★核心
- `ControlNetApplySD3` ★核心
- `LoadImage`
- `TextEncodeQwenImageEdit`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `809456897589742`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `controlnet_strength` = `0.6000000000000001`

## 知识

覆盖率 **89%**（24/27）

**有卡**：`ImageConcanate`、`SaveImage`、`ModelSamplingAuraFlow`、`CFGNorm`、`SetUnionControlNetType`、`AIO_Preprocessor`、`NunchakuQwenImageDiTLoader`、`KSampler`、`VAEDecode`、`VAEEncode`、`ImageScaleToMegapixels`、`CLIPLoader`、`LoadImage`、`TextEncodeQwenImageEdit`、`VAELoader`、`ControlNetLoader`、`ControlNetApplySD3`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、LoadImage、ControlNetLoader、SetUnionControlNetType、ControlNetApplySD3

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
