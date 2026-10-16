---
key: 视频生成/图生视频/001-(KJ版)Wan2.2高质量图生视频-优调版_1958374851545350145.json
name: 001-(KJ版)Wan2.2高质量图生视频-优调版_1958374851545350145.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1958374851545350145.json
hash: ca1135b4b3759c11
coverage: 0.829268
learned_at: 2026-10-15 22:31:22
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, Note, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, WanVideoImageToVideoEncode, Note, JWInteger, JWInteger, Reroute, VHS_VideoCombine, WanVideoBlockSwap, WanVideoTextEncode, WanVideoSetLoRAs, ImageScaleBy, RIFE VFI, GetImageSizeAndCount, Note, WanVideoSampler, LayerUtility: PurgeVRAM V2, GetImageSizeAndCount, LayerUtility: PurgeVRAM V2, PrimitiveNode, VHS_VideoCombine, WanVideoDecode, WanVideoSetLoRAs, WanVideoLoraSelect, INTConstant, INTConstant, WanVideoSampler, CreateCFGScheduleFloatList, FloatToSigmas, StringToFloatList, CR Prompt Text, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/001-(KJ版)Wan2.2高质量图生视频-优调版_1958374851545350145.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1958374851545350145.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（41 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `Note`
- `Note`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoImageToVideoEncode`
- `Note`
- `JWInteger`
- `JWInteger`
- `Reroute`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoTextEncode`
- `WanVideoSetLoRAs`
- `ImageScaleBy`
- `RIFE VFI`
- `GetImageSizeAndCount`
- `Note`
- `WanVideoSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `GetImageSizeAndCount`
- `LayerUtility: PurgeVRAM V2`
- `PrimitiveNode`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `INTConstant`
- `INTConstant`
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `FloatToSigmas`
- `StringToFloatList`
- `CR Prompt Text`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `LoadImage`

## 知识

覆盖率 **83%**（34/41）

**有卡**：`WanVideoSetBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoImageToVideoEncode`、`JWInteger`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`WanVideoSetLoRAs`、`ImageScaleBy`、`RIFE VFI`、`GetImageSizeAndCount`、`WanVideoSampler`、`LayerUtility: PurgeVRAM V2`、`WanVideoDecode`、`WanVideoLoraSelect`、`INTConstant`、`CreateCFGScheduleFloatList`、`FloatToSigmas`、`StringToFloatList`、`CR Prompt Text`、`WanVideoModelLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
