---
key: 视频生成/图生视频/wan2.2首尾帧-转身_指定动作_运镜-真人_动画_2027958356681433090.json
name: wan2.2首尾帧-转身_指定动作_运镜-真人_动画_2027958356681433090.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2027958356681433090.json
hash: 7130d602157bce9a
coverage: 1
learned_at: 2026-10-15 22:35:18
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, ImpactInt, ImpactInt, LoadImage, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoDecode, WanVideoTextEncode, WanVideoModelLoader, ImageResizeKJv2, CM_IntToFloat, easy int, ImpactInt, LoadImage, VHS_VideoCombine, CR Text, GetImageSizeAndCount, INTConstant, INTConstant, CreateCFGScheduleFloatList, WanVideoModelLoader, ImageResizeKJv2, RHHiddenNodes]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2首尾帧-转身_指定动作_运镜-真人_动画_2027958356681433090.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2027958356681433090.json`

## 结构

**生成流程**：Model → Process → Other

**节点**（27 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `ImpactInt`
- `ImpactInt`
- `LoadImage`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoTextEncode`
- `WanVideoModelLoader`
- `ImageResizeKJv2`
- `CM_IntToFloat`
- `easy int`
- `ImpactInt`
- `LoadImage`
- `VHS_VideoCombine`
- `CR Text`
- `GetImageSizeAndCount`
- `INTConstant`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `WanVideoModelLoader`
- `ImageResizeKJv2`
- `RHHiddenNodes`

## 知识

覆盖率 **100%**（27/27）

**有卡**：`WanVideoSetBlockSwap`、`ImpactInt`、`LoadImage`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoDecode`、`WanVideoTextEncode`、`WanVideoModelLoader`、`ImageResizeKJv2`、`CM_IntToFloat`、`easy int`、`VHS_VideoCombine`、`CR Text`、`GetImageSizeAndCount`、`INTConstant`、`CreateCFGScheduleFloatList`、`RHHiddenNodes`

**用到的条目**：LoadImage、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect、GetImageSizeAndCount
