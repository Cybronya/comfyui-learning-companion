---
key: 图片生成/文生图/Flux_ControlNet-Union-Pro-2.0最新多合一CN控制_1914378926058340353.json
name: Flux_ControlNet-Union-Pro-2.0最新多合一CN控制_1914378926058340353
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux_ControlNet-Union-Pro-2.0最新多合一CN控制_1914378926058340353.json
hash: 92d0233540184726
coverage: 0.787879
learned_at: 2026-10-10 20:58:36
nodes: [UNETLoader, DualCLIPLoader, FluxGuidance, CLIPTextEncode, KSampler, VAEDecode, ImageScaleBy, VAEEncode, VAELoader, VAEDecode, SaveImage, ImageResizeKJ, UpscaleModelLoader, UltimateSDUpscale, HEDPreprocessor, MiDaS-DepthMapPreprocessor, CannyEdgePreprocessor, ControlNetLoader, ControlNetApplyAdvanced, CLIPTextEncode, Image Switch (JPS), PreviewImage, SaveImage, SaveImage, EmptySD3LatentImage, DWPreprocessor, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, KSampler, LayerUtility: TextBox, SetUnionControlNetType, Note, Note]
patterns: [image_to_image]
missing: [Image Switch (JPS), LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: TextBox, MiDaS-DepthMapPreprocessor]
parameters: {"cfg": 1, "controlnet_strength": 0.8000000000000002, "denoise": 0.4000000000000001, "sampler_name": "euler", "scheduler": "beta", "seed": 378813125626722, "steps": 20}
discoveries: [次要节点 `Image Switch (JPS)` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: TextBox` 知识库中没有该节点类型的任何知识, 次要节点 `MiDaS-DepthMapPreprocessor` 仅有 ControlNet 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Flux_ControlNet-Union-Pro-2.0最新多合一CN控制_1914378926058340353.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux_ControlNet-Union-Pro-2.0最新多合一CN控制_1914378926058340353.json`

## 结构

**节点**（33 个）：
- `UNETLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `CLIPTextEncode`
- `KSampler`
- `VAEDecode`
- `ImageScaleBy`
- `VAEEncode`
- `VAELoader`
- `VAEDecode`
- `SaveImage`
- `ImageResizeKJ`
- `UpscaleModelLoader`
- `UltimateSDUpscale`
- `HEDPreprocessor`
- `MiDaS-DepthMapPreprocessor`
- `CannyEdgePreprocessor`
- `ControlNetLoader`
- `ControlNetApplyAdvanced`
- `CLIPTextEncode`
- `Image Switch (JPS)`
- `PreviewImage`
- `SaveImage`
- `SaveImage`
- `EmptySD3LatentImage`
- `DWPreprocessor`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `KSampler`
- `LayerUtility: TextBox`
- `SetUnionControlNetType`
- `Note`
- `Note`

**识别到的模式**：image_to_image

## 关键参数

- `cfg` = `1`
- `controlnet_strength` = `0.8000000000000002`
- `denoise` = `0.4000000000000001`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `seed` = `378813125626722`
- `steps` = `20`

## 知识

覆盖率 **79%**（26/33）

**有卡**：`UNETLoader`、`DualCLIPLoader`、`FluxGuidance`、`CLIPTextEncode`、`KSampler`、`VAEDecode`、`ImageScaleBy`、`VAEEncode`、`VAELoader`、`SaveImage`、`ImageResizeKJ`、`UpscaleModelLoader`、`UltimateSDUpscale`、`HEDPreprocessor`、`MiDaS-DepthMapPreprocessor`、`CannyEdgePreprocessor`、`ControlNetLoader`、`ControlNetApplyAdvanced`、`Image Switch (JPS)`、`PreviewImage`、`EmptySD3LatentImage`、`DWPreprocessor`

**缺卡**（4）：`Image Switch (JPS)`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: TextBox`、`MiDaS-DepthMapPreprocessor`

## 学习发现

- 次要节点 `Image Switch (JPS)` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: TextBox` 知识库中没有该节点类型的任何知识
- 次要节点 `MiDaS-DepthMapPreprocessor` 仅有 ControlNet 的通用知识，没有该节点自己的说明
