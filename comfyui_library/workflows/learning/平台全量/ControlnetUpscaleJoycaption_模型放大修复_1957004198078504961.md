---
key: 平台全量/ControlnetUpscaleJoycaption_模型放大修复_1957004198078504961.json
name: ControlnetUpscaleJoycaption_模型放大修复_1957004198078504961
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/ControlnetUpscaleJoycaption_模型放大修复_1957004198078504961.json
hash: 823f4bf95920c731
coverage: 0.956522
learned_at: 2026-11-14 00:22:57
nodes: [VAELoader, UNETLoader, SamplerCustomAdvanced, KSamplerSelect, BasicGuider, RandomNoise, FluxGuidance, ModelSamplingFlux, DualCLIPLoader, BasicScheduler, ControlNetApplyAdvanced, VAEEncode, ImageScaleBy, Get resolution [Crystools], CLIPTextEncode, CLIPTextEncode, JoyCaption2, VAEDecode, Image Comparer (rgthree), SaveImage, LoadImage, ControlNetLoader, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"controlnet_strength": 0.8}
---

# 平台全量/ControlnetUpscaleJoycaption_模型放大修复_1957004198078504961.json

> 来源文件 `comfyui_library/workflows/平台全量/ControlnetUpscaleJoycaption_模型放大修复_1957004198078504961.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `VAELoader`
- `UNETLoader` ★核心
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `RandomNoise`
- `FluxGuidance`
- `ModelSamplingFlux`
- `DualCLIPLoader`
- `BasicScheduler`
- `ControlNetApplyAdvanced` ★核心
- `VAEEncode` ★核心
- `ImageScaleBy`
- `Get resolution [Crystools]`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `JoyCaption2`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `LoadImage`
- `ControlNetLoader`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `controlnet_strength` = `0.8`

## 知识

覆盖率 **96%**（22/23）

**有卡**：`VAELoader`、`UNETLoader`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicGuider`、`RandomNoise`、`FluxGuidance`、`ModelSamplingFlux`、`DualCLIPLoader`、`BasicScheduler`、`ControlNetApplyAdvanced`、`VAEEncode`、`ImageScaleBy`、`Get resolution [Crystools]`、`CLIPTextEncode`、`JoyCaption2`、`VAEDecode`、`SaveImage`、`LoadImage`、`ControlNetLoader`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced、ControlNetLoader
