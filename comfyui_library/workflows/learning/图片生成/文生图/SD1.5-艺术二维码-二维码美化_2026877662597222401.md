---
key: 图片生成/文生图/SD1.5-艺术二维码-二维码美化_2026877662597222401.json
name: SD1.5-艺术二维码-二维码美化_2026877662597222401
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/SD1.5-艺术二维码-二维码美化_2026877662597222401.json
hash: 062014820b653967
coverage: 0.777778
learned_at: 2026-10-19 22:29:52
nodes: [CLIPTextEncode, CLIPTextEncode, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, CLIPTextEncode, BasicScheduler, VAEEncodeTiled, SamplerEulerAncestral, BasicScheduler, SamplerEulerAncestral, easy cleanGpuUsed, SamplerCustom, easy showAnything, CLIPTextEncode, SeedVR2VideoUpscaler, Image Comparer (rgthree), VAEDecodeTiled, AILab_QwenVL, UNETLoader, LoraLoaderModelOnly, ModelSamplingSD3, CLIPLoader, Image Comparer (rgthree), ControlNetApplyAdvanced, ControlNetLoader, ControlNetApplyAdvanced, CLIPSetLastLayer, CheckpointLoaderSimple, ControlNetLoader, SamplerCustomAdvanced, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, PreviewAny, easy promptConcat, easy positive, LayerUtility: ImageBlend, easy positive, PrimitiveNode, LoadImage, Note, Note, CFGGuider, VAEEncode, PreviewImage, SaveImage, Note, RandomNoise, LayerUtility: ImageMaskScaleAs, Reroute, ImageBlur, PreviewImage, Image Comparer (rgthree), VAELoader, easy cleanGpuUsed]
patterns: []
missing: []
parameters: {"checkpoint": "SD1.5 dreamshaper_8.safetensors", "controlnet_strength": 1.0000000000000002}
---

# 图片生成/文生图/SD1.5-艺术二维码-二维码美化_2026877662597222401.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/SD1.5-艺术二维码-二维码美化_2026877662597222401.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `CLIPTextEncode` ★核心
- `BasicScheduler`
- `VAEEncodeTiled` ★核心
- `SamplerEulerAncestral` ★核心
- `BasicScheduler`
- `SamplerEulerAncestral` ★核心
- `easy cleanGpuUsed`
- `SamplerCustom` ★核心
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `SeedVR2VideoUpscaler`
- `Image Comparer (rgthree)`
- `VAEDecodeTiled` ★核心
- `AILab_QwenVL`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingSD3`
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `ControlNetApplyAdvanced` ★核心
- `ControlNetLoader`
- `ControlNetApplyAdvanced` ★核心
- `CLIPSetLastLayer`
- `CheckpointLoaderSimple` ★核心
- `ControlNetLoader`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewAny`
- `easy promptConcat`
- `easy positive`
- `LayerUtility: ImageBlend`
- `easy positive`
- `PrimitiveNode`
- `LoadImage`
- `Note`
- `Note`
- `CFGGuider`
- `VAEEncode` ★核心
- `PreviewImage`
- `SaveImage`
- `Note`
- `RandomNoise`
- `LayerUtility: ImageMaskScaleAs`
- `Reroute`
- `ImageBlur`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `VAELoader`
- `easy cleanGpuUsed`

## 关键参数

- `controlnet_strength` = `1.0000000000000002`
- `checkpoint` = `SD1.5 dreamshaper_8.safetensors`

## 知识

覆盖率 **78%**（42/54）

**有卡**：`CLIPTextEncode`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`BasicScheduler`、`VAEEncodeTiled`、`SamplerEulerAncestral`、`easy cleanGpuUsed`、`SamplerCustom`、`SeedVR2VideoUpscaler`、`VAEDecodeTiled`、`AILab_QwenVL`、`UNETLoader`、`LoraLoaderModelOnly`、`ModelSamplingSD3`、`CLIPLoader`、`ControlNetApplyAdvanced`、`ControlNetLoader`、`CLIPSetLastLayer`、`CheckpointLoaderSimple`、`SamplerCustomAdvanced`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy promptConcat`、`easy positive`、`LayerUtility: ImageBlend`、`LoadImage`、`CFGGuider`、`VAEEncode`、`SaveImage`、`RandomNoise`、`LayerUtility: ImageMaskScaleAs`、`ImageBlur`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage
