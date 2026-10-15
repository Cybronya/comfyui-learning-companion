---
key: 图片生成/文生图/Flux_ControlNet-Union-Pro-2.0最新多合一CN控制_1914378926058340353.json
name: Flux_ControlNet-Union-Pro-2.0最新多合一CN控制_1914378926058340353
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux_ControlNet-Union-Pro-2.0最新多合一CN控制_1914378926058340353.json
hash: 92d0233540184726
coverage: 0.909091
learned_at: 2026-10-15 22:26:26
nodes: [UNETLoader, DualCLIPLoader, FluxGuidance, CLIPTextEncode, KSampler, VAEDecode, ImageScaleBy, VAEEncode, VAELoader, VAEDecode, SaveImage, ImageResizeKJ, UpscaleModelLoader, UltimateSDUpscale, HEDPreprocessor, MiDaS-DepthMapPreprocessor, CannyEdgePreprocessor, ControlNetLoader, ControlNetApplyAdvanced, CLIPTextEncode, Image Switch (JPS), PreviewImage, SaveImage, SaveImage, EmptySD3LatentImage, DWPreprocessor, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, KSampler, LayerUtility: TextBox, SetUnionControlNetType, Note, Note]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "controlnet_strength": 0.8000000000000002, "denoise": 0.4000000000000001, "sampler_name": "euler", "scheduler": "beta", "seed": 378813125626722, "steps": 20}
---

# 图片生成/文生图/Flux_ControlNet-Union-Pro-2.0最新多合一CN控制_1914378926058340353.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux_ControlNet-Union-Pro-2.0最新多合一CN控制_1914378926058340353.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImageScaleBy`
- `VAEEncode` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `ImageResizeKJ`
- `UpscaleModelLoader`
- `UltimateSDUpscale`
- `HEDPreprocessor`
- `MiDaS-DepthMapPreprocessor`
- `CannyEdgePreprocessor`
- `ControlNetLoader`
- `ControlNetApplyAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `Image Switch (JPS)`
- `PreviewImage`
- `SaveImage`
- `SaveImage`
- `EmptySD3LatentImage`
- `DWPreprocessor`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `KSampler` ★核心
- `LayerUtility: TextBox`
- `SetUnionControlNetType`
- `Note`
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `378813125626722`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `0.4000000000000001`
- `controlnet_strength` = `0.8000000000000002`

## 知识

覆盖率 **91%**（30/33）

**有卡**：`UNETLoader`、`DualCLIPLoader`、`FluxGuidance`、`CLIPTextEncode`、`KSampler`、`VAEDecode`、`ImageScaleBy`、`VAEEncode`、`VAELoader`、`SaveImage`、`ImageResizeKJ`、`UpscaleModelLoader`、`UltimateSDUpscale`、`HEDPreprocessor`、`MiDaS-DepthMapPreprocessor`、`CannyEdgePreprocessor`、`ControlNetLoader`、`ControlNetApplyAdvanced`、`Image Switch (JPS)`、`EmptySD3LatentImage`、`DWPreprocessor`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`LayerUtility: TextBox`、`SetUnionControlNetType`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、ControlNetApplyAdvanced
