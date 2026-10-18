---
key: 视频生成/图生视频/Wan2.2-FunControl美女跳舞_1971091047734484993.json
name: Wan2.2-FunControl美女跳舞_1971091047734484993.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-FunControl美女跳舞_1971091047734484993.json
hash: f78e286bd690da58
coverage: 0.606061
learned_at: 2026-10-15 22:31:55
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoTorchCompileSettings, ImageResize+, ImageResize+, ControlNextGetPoses, WanVideoEncode, WanVideoControlEmbeds, WanVideoImageToVideoEncode, easy seed, INTConstant, INTConstant, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoSampler, easy positive, MathExpression|pysssss, ImpactInt, ImpactInt, VHS_VideoInfoSource, ImageUpscaleWithModel, WanVideoDecode, GetImageSizeAndCount, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, JWInteger, WanVideoModelLoader, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, RIFE VFI, LoadImage, WanVideoLoraSelect, WanVideoLoraSelect, VHS_VideoCombine, VHS_LoadVideo, SetNode, VHS_VideoCombine, UpscaleModelLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-FunControl美女跳舞_1971091047734484993.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1971091047734484993.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（66 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `ImageResize+`
- `ImageResize+`
- `ControlNextGetPoses`
- `WanVideoEncode`
- `WanVideoControlEmbeds`
- `WanVideoImageToVideoEncode`
- `easy seed`
- `INTConstant`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `easy positive`
- `MathExpression|pysssss`
- `ImpactInt`
- `ImpactInt`
- `VHS_VideoInfoSource`
- `ImageUpscaleWithModel`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `JWInteger`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `RIFE VFI`
- `LoadImage`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `SetNode`
- `VHS_VideoCombine`
- `UpscaleModelLoader`

## 知识

覆盖率 **61%**（40/66）

**有卡**：`WanVideoTorchCompileSettings`、`ImageResize+`、`ControlNextGetPoses`、`WanVideoEncode`、`WanVideoControlEmbeds`、`WanVideoImageToVideoEncode`、`easy seed`、`INTConstant`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`easy positive`、`MathExpression|pysssss`、`ImpactInt`、`VHS_VideoInfoSource`、`ImageUpscaleWithModel`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`JWInteger`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`RIFE VFI`、`LoadImage`、`WanVideoLoraSelect`、`VHS_VideoCombine`、`VHS_LoadVideo`、`UpscaleModelLoader`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
