---
key: 视频生成/图生视频/Wan2.2-14B+Lightx2v图生视频加速版放大补帧生成2K高清视频_1950107460180860930.json
name: Wan2.2-14B+Lightx2v图生视频加速版放大补帧生成2K高清视频_1950107460180860930.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-14B+Lightx2v图生视频加速版放大补帧生成2K高清视频_1950107460180860930.json
hash: 638086044200f236
coverage: 0.972973
learned_at: 2026-10-15 22:30:53
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoModelLoader, JWInteger, LoadImage, WanVideoTorchCompileSettings, WanVideoLoraSelect, WanVideoLoraSelect, ImageResizeKJv2, Text Multiline, LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoImageToVideoEncode, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoVAELoader, WanVideoSampler, SimpleMath+, JWInteger, JWInteger, PrimitiveNode, Primitive integer [Crystools], Primitive integer [Crystools], UpscaleModelLoader, ImageUpscaleWithModel, VHS_VideoCombine, Primitive integer [Crystools], RIFE VFI, VHS_VideoCombine, WanVideoDecode, easy cleanGpuUsed, JWInteger, JWInteger]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-14B+Lightx2v图生视频加速版放大补帧生成2K高清视频_1950107460180860930.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950107460180860930.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（37 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `JWInteger`
- `LoadImage`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `ImageResizeKJv2`
- `Text Multiline`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoImageToVideoEncode`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoSampler` ★核心
- `SimpleMath+`
- `JWInteger`
- `JWInteger`
- `PrimitiveNode`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `VHS_VideoCombine`
- `Primitive integer [Crystools]`
- `RIFE VFI`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `JWInteger`
- `JWInteger`

## 知识

覆盖率 **97%**（36/37）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`JWInteger`、`LoadImage`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelect`、`ImageResizeKJv2`、`Text Multiline`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoImageToVideoEncode`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`WanVideoVAELoader`、`SimpleMath+`、`Primitive integer [Crystools]`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`VHS_VideoCombine`、`RIFE VFI`、`WanVideoDecode`、`easy cleanGpuUsed`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
