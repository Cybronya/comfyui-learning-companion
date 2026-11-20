---
key: 平台全量/扩图：Perfect Outpainting with Flux_1839710049769062401.json
name: 扩图：Perfect Outpainting with Flux_1839710049769062401
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/扩图：Perfect Outpainting with Flux_1839710049769062401.json
hash: 7016aebb65411572
coverage: 0.666667
learned_at: 2026-11-14 02:05:21
nodes: [CLIPTextEncode, SetLatentNoiseMask, Image Comparer (rgthree), CheckpointLoaderSimple, CLIPTextEncode, Image Blank, InvertMask, LayerUtility: ImageBlendAdvance V2, Anything Everywhere, SetNode, KSampler, VAEEncodeForInpaint, GetNode, ControlNetApplyAdvanced, SetUnionControlNetType, SetNode, CR Prompt Text, VAEDecode, SetNode, Anything Everywhere3, GrowMaskWithBlur, GetNode, GetNode, VAEEncode, CLIPTextEncode, FluxGuidance, CLIPTextEncode, GetNode, ControlNetLoader, CheckpointLoaderSimple, PreviewImage, KSampler, LoadImage, VAEDecode, SaveImage, PreviewImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "checkpoint": "realvisxlV50_v50LightningBakedvae.safetensors", "controlnet_strength": 1, "denoise": 0.9500000000000001, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 1002816647452751, "steps": 30}
---

# 平台全量/扩图：Perfect Outpainting with Flux_1839710049769062401.json

> 来源文件 `comfyui_library/workflows/平台全量/扩图：Perfect Outpainting with Flux_1839710049769062401.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `CLIPTextEncode` ★核心
- `SetLatentNoiseMask`
- `Image Comparer (rgthree)`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `Image Blank`
- `InvertMask`
- `LayerUtility: ImageBlendAdvance V2`
- `Anything Everywhere`
- `SetNode`
- `KSampler` ★核心
- `VAEEncodeForInpaint` ★核心
- `GetNode`
- `ControlNetApplyAdvanced` ★核心
- `SetUnionControlNetType`
- `SetNode`
- `CR Prompt Text`
- `VAEDecode` ★核心
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
- `ControlNetLoader`
- `CheckpointLoaderSimple` ★核心
- `PreviewImage`
- `KSampler` ★核心
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `checkpoint` = `realvisxlV50_v50LightningBakedvae.safetensors`
- `seed` = `1002816647452751`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `0.9500000000000001`
- `controlnet_strength` = `1`

## 知识

覆盖率 **67%**（24/36）

**有卡**：`CLIPTextEncode`、`SetLatentNoiseMask`、`CheckpointLoaderSimple`、`Image Blank`、`InvertMask`、`LayerUtility: ImageBlendAdvance V2`、`KSampler`、`VAEEncodeForInpaint`、`ControlNetApplyAdvanced`、`SetUnionControlNetType`、`CR Prompt Text`、`VAEDecode`、`GrowMaskWithBlur`、`VAEEncode`、`FluxGuidance`、`ControlNetLoader`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced、ControlNetLoader、SetUnionControlNetType
