---
key: 视频生成/图生视频/KJ版Wan2.2 图生视频超级加速+镜头切换V2版_1950822532939186177.json
name: KJ版Wan2.2 图生视频超级加速+镜头切换V2版_1950822532939186177.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950822532939186177.json
hash: 25415bab5f7d6800
coverage: 0.962963
learned_at: 2026-10-15 22:30:56
nodes: [WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, CreateCFGScheduleFloatList, PrimitiveNode, WanVideoImageToVideoEncode, WanVideoSampler, LayerUtility: PurgeVRAM, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoVAELoader, WanVideoBlockSwap, LoadWanVideoT5TextEncoder, LayerUtility: ImageScaleByAspectRatio V2, GetImageSizeAndCount, ImageFromBatch+, WanVideoSampler, WanVideoTextEncode, LoadImage, LayerUtility: PurgeVRAM, WanVideoTorchCompileSettings, WanVideoDecode, CR Prompt Text, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/KJ版Wan2.2 图生视频超级加速+镜头切换V2版_1950822532939186177.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950822532939186177.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（27 个）：
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `CreateCFGScheduleFloatList`
- `PrimitiveNode`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `LayerUtility: PurgeVRAM`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `LoadWanVideoT5TextEncoder`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSizeAndCount`
- `ImageFromBatch+`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `LoadImage`
- `LayerUtility: PurgeVRAM`
- `WanVideoTorchCompileSettings`
- `WanVideoDecode`
- `CR Prompt Text`
- `VHS_VideoCombine`

## 知识

覆盖率 **96%**（26/27）

**有卡**：`WanVideoLoraSelect`、`WanVideoModelLoader`、`CreateCFGScheduleFloatList`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`LayerUtility: PurgeVRAM`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSizeAndCount`、`ImageFromBatch+`、`WanVideoTextEncode`、`LoadImage`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`CR Prompt Text`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
