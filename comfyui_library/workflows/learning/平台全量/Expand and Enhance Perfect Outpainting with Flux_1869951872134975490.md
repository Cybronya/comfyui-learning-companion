---
key: 平台全量/Expand and Enhance Perfect Outpainting with Flux_1869951872134975490.json
name: Expand and Enhance Perfect Outpainting with Flux_1869951872134975490
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Expand and Enhance Perfect Outpainting with Flux_1869951872134975490.json
hash: 82598bd1fa51154e
coverage: 0.685714
learned_at: 2026-11-14 00:24:00
nodes: [CLIPTextEncode, SetLatentNoiseMask, Image Comparer (rgthree), CLIPTextEncode, KSampler, InvertMask, LayerUtility: ImageBlendAdvance V2, Anything Everywhere, SetNode, KSampler, VAEEncodeForInpaint, GetNode, ControlNetApplyAdvanced, SetNode, PreviewImage, SetNode, Anything Everywhere3, GrowMaskWithBlur, GetNode, GetNode, VAEEncode, CLIPTextEncode, FluxGuidance, CLIPTextEncode, GetNode, VAEDecode, Image Blank, LoadImage, ControlNetLoader, SetUnionControlNetType, CheckpointLoaderSimple, VAEDecode, SaveImage, CheckpointLoaderSimple, CR Prompt Text]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 3, "checkpoint": "flux1-dev-fp8-Comfy-Org.safetensors", "controlnet_strength": 1, "denoise": 1, "sampler_name": "dpmpp_3m_sde", "scheduler": "karras", "seed": 460103653384879, "steps": 30}
---

# 平台全量/Expand and Enhance Perfect Outpainting with Flux_1869951872134975490.json

> 来源文件 `comfyui_library/workflows/平台全量/Expand and Enhance Perfect Outpainting with Flux_1869951872134975490.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `CLIPTextEncode` ★核心
- `SetLatentNoiseMask`
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `InvertMask`
- `LayerUtility: ImageBlendAdvance V2`
- `Anything Everywhere`
- `SetNode`
- `KSampler` ★核心
- `VAEEncodeForInpaint` ★核心
- `GetNode`
- `ControlNetApplyAdvanced` ★核心
- `SetNode`
- `PreviewImage`
- `SetNode`
- `Anything Everywhere3`
- `GrowMaskWithBlur`
- `GetNode`
- `GetNode`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `Image Blank`
- `LoadImage`
- `ControlNetLoader`
- `SetUnionControlNetType`
- `CheckpointLoaderSimple` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CheckpointLoaderSimple` ★核心
- `CR Prompt Text`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `460103653384879`
- `steps` = `30`
- `cfg` = `3`
- `sampler_name` = `dpmpp_3m_sde`
- `scheduler` = `karras`
- `denoise` = `1`
- `controlnet_strength` = `1`
- `checkpoint` = `flux1-dev-fp8-Comfy-Org.safetensors`

## 知识

覆盖率 **69%**（24/35）

**有卡**：`CLIPTextEncode`、`SetLatentNoiseMask`、`KSampler`、`InvertMask`、`LayerUtility: ImageBlendAdvance V2`、`VAEEncodeForInpaint`、`ControlNetApplyAdvanced`、`GrowMaskWithBlur`、`VAEEncode`、`FluxGuidance`、`VAEDecode`、`Image Blank`、`LoadImage`、`ControlNetLoader`、`SetUnionControlNetType`、`CheckpointLoaderSimple`、`SaveImage`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced、ControlNetLoader、SetUnionControlNetType
