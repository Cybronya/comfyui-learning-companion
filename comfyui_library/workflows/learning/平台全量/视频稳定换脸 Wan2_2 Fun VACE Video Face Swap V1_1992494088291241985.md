---
key: 平台全量/视频稳定换脸 Wan2_2 Fun VACE Video Face Swap V1_1992494088291241985.json
name: 视频稳定换脸 Wan2_2 Fun VACE Video Face Swap V1_1992494088291241985
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频稳定换脸 Wan2_2 Fun VACE Video Face Swap V1_1992494088291241985.json
hash: 401e354fac4f7019
coverage: 0.652174
learned_at: 2026-11-14 02:40:23
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, SetNode, SetNode, WanVideoVACEModelSelect, SetNode, GetNode, WanVideoDecode, GetNode, WanVideoVACEModelSelect, WanVideoModelLoader, WanVideoModelLoader, SetNode, ImageConcanate, GetNode, GetNode, GetNode, ImageConcanate, GetNode, GetNode, WanVideoSetLoRAs, PrimitiveInt, WanVideoSampler, WanVideoVAELoader, SetNode, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, GetNode, SetNode, UpscaleModelLoader, WanVideoVACEEncode, LoadWanVideoT5TextEncoder, Reroute, WanVideoSampler, WanVideoTextEncode, WanVideoBlockSwap, VHS_VideoCombine, SeedVR2BlockSwap, SeedVR2, SimpleMath+, ImpactInt, InpaintPreprocessor, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoInfo, GrowMaskWithBlur, PrimitiveNode, PrimitiveNode, Text Concatenate, LoadImage, LayerMask: HumanPartsUltra, SimpleMath+, SimpleMath+, PrimitiveInt, easy showAnything, ImageScaleToMegapixels, PreviewImage, Note, CR Text, Note, AutoCropFaces, Int, Int, VHS_LoadVideo, Int, VHS_VideoCombine, VHS_VideoCombine, LayerUtility: GeminiV2]
patterns: []
missing: []
---

# 平台全量/视频稳定换脸 Wan2_2 Fun VACE Video Face Swap V1_1992494088291241985.json

> 来源文件 `comfyui_library/workflows/平台全量/视频稳定换脸 Wan2_2 Fun VACE Video Face Swap V1_1992494088291241985.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（69 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoVACEModelSelect`
- `SetNode`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `WanVideoVACEModelSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `SetNode`
- `ImageConcanate`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcanate`
- `GetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `PrimitiveInt`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `SetNode`
- `UpscaleModelLoader`
- `WanVideoVACEEncode`
- `LoadWanVideoT5TextEncoder`
- `Reroute`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `SeedVR2BlockSwap`
- `SeedVR2`
- `SimpleMath+`
- `ImpactInt`
- `InpaintPreprocessor`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoInfo`
- `GrowMaskWithBlur`
- `PrimitiveNode`
- `PrimitiveNode`
- `Text Concatenate`
- `LoadImage`
- `LayerMask: HumanPartsUltra`
- `SimpleMath+`
- `SimpleMath+`
- `PrimitiveInt`
- `easy showAnything`
- `ImageScaleToMegapixels`
- `PreviewImage`
- `Note`
- `CR Text`
- `Note`
- `AutoCropFaces`
- `Int`
- `Int`
- `VHS_LoadVideo`
- `Int`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LayerUtility: GeminiV2`

## 知识

覆盖率 **65%**（45/69）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVACEModelSelect`、`WanVideoDecode`、`WanVideoModelLoader`、`ImageConcanate`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`UpscaleModelLoader`、`WanVideoVACEEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`SeedVR2BlockSwap`、`SeedVR2`、`SimpleMath+`、`ImpactInt`、`InpaintPreprocessor`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_VideoInfo`、`GrowMaskWithBlur`、`Text Concatenate`、`LoadImage`、`LayerMask: HumanPartsUltra`、`ImageScaleToMegapixels`、`CR Text`、`AutoCropFaces`、`Int`、`VHS_LoadVideo`、`LayerUtility: GeminiV2`

**用到的条目**：LoadImage、SeedVR2、SeedVR2BlockSwap、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode
