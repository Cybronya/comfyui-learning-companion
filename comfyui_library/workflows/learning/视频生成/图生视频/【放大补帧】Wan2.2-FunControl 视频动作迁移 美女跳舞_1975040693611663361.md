---
key: 视频生成/图生视频/【放大补帧】Wan2.2-FunControl 视频动作迁移 美女跳舞_1975040693611663361.json
name: 【放大补帧】Wan2.2-FunControl 视频动作迁移 美女跳舞_1975040693611663361.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1975040693611663361.json
hash: 16671a4e9ef44c04
coverage: 0.606061
learned_at: 2026-10-15 22:32:07
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoTorchCompileSettings, ImageResize+, ImageResize+, ControlNextGetPoses, WanVideoEncode, WanVideoControlEmbeds, WanVideoImageToVideoEncode, easy seed, INTConstant, INTConstant, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoSampler, easy positive, MathExpression|pysssss, ImpactInt, ImpactInt, VHS_VideoInfoSource, ImageUpscaleWithModel, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, VHS_VideoCombine, JWInteger, WanVideoModelLoader, WanVideoModelLoader, WanVideoVAELoader, RIFE VFI, VHS_LoadVideo, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, WanVideoLoraSelect, UpscaleModelLoader, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/【放大补帧】Wan2.2-FunControl 视频动作迁移 美女跳舞_1975040693611663361.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1975040693611663361.json`

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
- `VHS_VideoCombine`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `JWInteger`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `RIFE VFI`
- `VHS_LoadVideo`
- `LoadWanVideoT5TextEncoder`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `UpscaleModelLoader`
- `LoadImage`

## 知识

覆盖率 **61%**（40/66）

**有卡**：`WanVideoTorchCompileSettings`、`ImageResize+`、`ControlNextGetPoses`、`WanVideoEncode`、`WanVideoControlEmbeds`、`WanVideoImageToVideoEncode`、`easy seed`、`INTConstant`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`easy positive`、`MathExpression|pysssss`、`ImpactInt`、`VHS_VideoInfoSource`、`ImageUpscaleWithModel`、`WanVideoDecode`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`JWInteger`、`WanVideoModelLoader`、`WanVideoVAELoader`、`RIFE VFI`、`VHS_LoadVideo`、`LoadWanVideoT5TextEncoder`、`WanVideoLoraSelect`、`UpscaleModelLoader`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
