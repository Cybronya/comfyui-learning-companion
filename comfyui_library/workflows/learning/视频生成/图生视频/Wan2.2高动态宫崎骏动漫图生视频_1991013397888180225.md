---
key: 视频生成/图生视频/Wan2.2高动态宫崎骏动漫图生视频_1991013397888180225.json
name: Wan2.2高动态宫崎骏动漫图生视频_1991013397888180225.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2高动态宫崎骏动漫图生视频_1991013397888180225.json
hash: fc71675e49f0d614
coverage: 0.956522
learned_at: 2026-10-15 22:33:12
nodes: [WanVideoLoraSelect, WanVideoModelLoader, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoScheduler, WanVideoImageToVideoEncode, WanVideoVAELoader, WanVideoScheduler, WanVideoLoraSelect, WanVideoModelLoader, LoadImage, WanVideoTextEncode, GetImageSizeAndCount, WanVideoDecode, WanVideoSampler, WanVideoSampler, CreateCFGScheduleFloatList, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveNode, WanVideoSigmaToStep, Float, LoadWanVideoT5TextEncoder, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2高动态宫崎骏动漫图生视频_1991013397888180225.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1991013397888180225.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（23 个）：
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoScheduler`
- `WanVideoImageToVideoEncode`
- `WanVideoVAELoader`
- `WanVideoScheduler`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `LoadImage`
- `WanVideoTextEncode`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `CreateCFGScheduleFloatList`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveNode`
- `WanVideoSigmaToStep`
- `Float`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`

## 知识

覆盖率 **96%**（22/23）

**有卡**：`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoScheduler`、`WanVideoImageToVideoEncode`、`WanVideoVAELoader`、`LoadImage`、`WanVideoTextEncode`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSigmaToStep`、`Float`、`LoadWanVideoT5TextEncoder`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
