---
key: 视频生成/图生视频/（自用）KJ版Wan2.2图生视频超级加速版V3（大幅度提高速度）_1952588298072068097.json
name: （自用）KJ版Wan2.2图生视频超级加速版V3（大幅度提高速度）_1952588298072068097.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/（自用）KJ版Wan2.2图生视频超级加速版V3（大幅度提高速度）_1952588298072068097.json
hash: 5924ac20ca853393
coverage: 0.85
learned_at: 2026-10-15 22:31:02
nodes: [WanVideoTorchCompileSettings, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, CreateCFGScheduleFloatList, INTConstant, INTConstant, JWInteger, Note, Note, CR Prompt Text, Note, WanVideoModelLoader, WanVideoModelLoader, Note, JWInteger, WanVideoImageToVideoEncode, WanVideoVAELoader, PrimitiveNode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader, LoadLatent, VHS_VideoCombine, WanVideoDecode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, Note, SaveLatent, LoadImage, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, WanVideoSampler]
patterns: []
missing: []
---

# 视频生成/图生视频/（自用）KJ版Wan2.2图生视频超级加速版V3（大幅度提高速度）_1952588298072068097.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952588298072068097.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（40 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `INTConstant`
- `JWInteger`
- `Note`
- `Note`
- `CR Prompt Text`
- `Note`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `Note`
- `JWInteger`
- `WanVideoImageToVideoEncode`
- `WanVideoVAELoader`
- `PrimitiveNode`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `LoadLatent`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `Note`
- `SaveLatent`
- `LoadImage`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoSampler` ★核心

## 知识

覆盖率 **85%**（34/40）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`CreateCFGScheduleFloatList`、`INTConstant`、`JWInteger`、`CR Prompt Text`、`WanVideoModelLoader`、`WanVideoImageToVideoEncode`、`WanVideoVAELoader`、`LayerUtility: PurgeVRAM`、`WanVideoSampler`、`WanVideoTextEncode`、`LoadLatent`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoLoraSelect`、`SaveLatent`、`LoadImage`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、SaveLatent、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
