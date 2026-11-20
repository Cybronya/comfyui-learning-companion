---
key: 平台全量/Flux. Watercolor Storybook Style – Characters_Scen_1889576178997518338.json
name: Flux. Watercolor Storybook Style – Characters_Scen_1889576178997518338
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux. Watercolor Storybook Style – Characters_Scen_1889576178997518338.json
hash: f5c37270963974f0
coverage: 0.814815
learned_at: 2026-11-14 00:28:43
nodes: [DepthAnything_V2, PreviewImage, ModelSamplingFlux, FluxGuidance, EmptyLatentImage, ApplyFluxControlNet, CLIPTextEncode, XlabsSampler, VAELoader, VAEDecode, Image Comparer (rgthree), LoadImage, LoraLoader, UNETLoader, LoadFluxControlNet, DownloadAndLoadDepthAnythingV2Model, UpscaleModelLoader, ImageResize+, ImageUpscaleWithModel, PreviewImage, DualCLIPLoader, CLIPTextEncode, TextCombinerTwo, ShowText|pysssss, RH_Captioner, JjkText, SaveImage]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "height": 1024, "lora_name": "F1. 超好看的小清新水彩绘本画风格_V1.0.safetensors", "strength_clip": 1, "strength_model": 1, "width": 1024}
---

# 平台全量/Flux. Watercolor Storybook Style – Characters_Scen_1889576178997518338.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux. Watercolor Storybook Style – Characters_Scen_1889576178997518338.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `DepthAnything_V2`
- `PreviewImage`
- `ModelSamplingFlux`
- `FluxGuidance`
- `EmptyLatentImage` ★核心
- `ApplyFluxControlNet`
- `CLIPTextEncode` ★核心
- `XlabsSampler` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoraLoader` ★核心
- `UNETLoader` ★核心
- `LoadFluxControlNet`
- `DownloadAndLoadDepthAnythingV2Model`
- `UpscaleModelLoader`
- `ImageResize+`
- `ImageUpscaleWithModel`
- `PreviewImage`
- `DualCLIPLoader`
- `CLIPTextEncode` ★核心
- `TextCombinerTwo`
- `ShowText|pysssss`
- `RH_Captioner`
- `JjkText`
- `SaveImage`

**识别到的模式**：lora

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `lora_name` = `F1. 超好看的小清新水彩绘本画风格_V1.0.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **81%**（22/27）

**有卡**：`DepthAnything_V2`、`ModelSamplingFlux`、`FluxGuidance`、`EmptyLatentImage`、`ApplyFluxControlNet`、`CLIPTextEncode`、`XlabsSampler`、`VAELoader`、`VAEDecode`、`LoadImage`、`LoraLoader`、`UNETLoader`、`LoadFluxControlNet`、`DownloadAndLoadDepthAnythingV2Model`、`UpscaleModelLoader`、`ImageResize+`、`ImageUpscaleWithModel`、`DualCLIPLoader`、`TextCombinerTwo`、`RH_Captioner`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、ApplyFluxControlNet、DepthAnything_V2
