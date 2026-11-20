---
key: 平台全量/More accurate style transfer_1887407857405722625.json
name: More accurate style transfer_1887407857405722625
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/More accurate style transfer_1887407857405722625.json
hash: 56d289199c1a3bc2
coverage: 0.916667
learned_at: 2026-11-14 00:46:30
nodes: [ControlNetApplyAdvanced, CannyEdgePreprocessor, ControlNetApplyAdvanced, CheckpointLoaderSimple, PreviewImage, DepthAnythingPreprocessor, VAEEncode, VAEDecode, ImageSharpen, ControlNetLoader, LoadImage, SaveImage, PreviewImage, CR Simple Image Compare, KSampler, DifferentialDiffusion, PrepImageForClipVision, ImageScale, IPAdapterUnifiedLoader, IPAdapterClipVisionEnhancer, LoadImage, CLIPTextEncode, SDXLPromptStylerAll, CLIPTextEncode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 2, "checkpoint": "RealitiesEdgeXLLIGHTNING_TURBOV7.safetensors", "controlnet_strength": 0.5, "denoise": 0.85, "sampler_name": "dpmpp_sde", "scheduler": "karras", "seed": 350641373439805, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/More accurate style transfer_1887407857405722625.json

> 来源文件 `comfyui_library/workflows/平台全量/More accurate style transfer_1887407857405722625.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `ControlNetApplyAdvanced` ★核心
- `CannyEdgePreprocessor`
- `ControlNetApplyAdvanced` ★核心
- `CheckpointLoaderSimple` ★核心
- `PreviewImage`
- `DepthAnythingPreprocessor`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `ImageSharpen`
- `ControlNetLoader`
- `LoadImage`
- `SaveImage`
- `PreviewImage`
- `CR Simple Image Compare`
- `KSampler` ★核心
- `DifferentialDiffusion`
- `PrepImageForClipVision`
- `ImageScale`
- `IPAdapterUnifiedLoader`
- `IPAdapterClipVisionEnhancer`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `SDXLPromptStylerAll`
- `CLIPTextEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `controlnet_strength` = `0.5`
- `checkpoint` = `RealitiesEdgeXLLIGHTNING_TURBOV7.safetensors`
- `seed` = `350641373439805`
- `steps` = `8`
- `cfg` = `2`
- `sampler_name` = `dpmpp_sde`
- `scheduler` = `karras`
- `denoise` = `0.85`

## 知识

覆盖率 **92%**（22/24）

**有卡**：`ControlNetApplyAdvanced`、`CannyEdgePreprocessor`、`CheckpointLoaderSimple`、`DepthAnythingPreprocessor`、`VAEEncode`、`VAEDecode`、`ImageSharpen`、`ControlNetLoader`、`LoadImage`、`SaveImage`、`CR Simple Image Compare`、`KSampler`、`DifferentialDiffusion`、`PrepImageForClipVision`、`ImageScale`、`IPAdapterUnifiedLoader`、`IPAdapterClipVisionEnhancer`、`CLIPTextEncode`、`SDXLPromptStylerAll`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CannyEdgePreprocessor、ControlNetApplyAdvanced、ControlNetLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
