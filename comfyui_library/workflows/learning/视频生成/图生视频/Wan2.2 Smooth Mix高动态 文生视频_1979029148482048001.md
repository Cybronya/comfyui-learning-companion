---
key: 视频生成/图生视频/Wan2.2 Smooth Mix高动态 文生视频_1979029148482048001.json
name: Wan2.2 Smooth Mix高动态 文生视频_1979029148482048001.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Smooth Mix高动态 文生视频_1979029148482048001.json
hash: 7c4df9c6f1ee9e20
coverage: 0.916667
learned_at: 2026-10-15 22:32:21
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoDecode, GetImageSizeAndCount, WanVideoLoraSelect, WanVideoEmptyEmbeds, Primitive integer [Crystools], LoadWanVideoT5TextEncoder, WanVideoTextEncode, Primitive integer [Crystools], WanVideoSampler, WanVideoSampler, WanVideoTorchCompileSettings, Primitive integer [Crystools], PrimitiveFloat, CreateCFGScheduleFloatList, Primitive integer [Crystools], WanVideoModelLoader, Primitive integer [Crystools], WanVideoLoraSelect, VHS_VideoCombine, SimpleMath+, Primitive integer [Crystools], WanVideoBlockSwap, SimpleMath+, WanVideoModelLoader, WanVideoVAELoader, LoadImage, JjkText, JjkText, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Smooth Mix高动态 文生视频_1979029148482048001.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1979029148482048001.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `WanVideoLoraSelect`
- `WanVideoEmptyEmbeds`
- `Primitive integer [Crystools]`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `Primitive integer [Crystools]`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `Primitive integer [Crystools]`
- `PrimitiveFloat`
- `CreateCFGScheduleFloatList`
- `Primitive integer [Crystools]`
- `WanVideoModelLoader`
- `Primitive integer [Crystools]`
- `WanVideoLoraSelect`
- `VHS_VideoCombine`
- `SimpleMath+`
- `Primitive integer [Crystools]`
- `WanVideoBlockSwap`
- `SimpleMath+`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `LoadImage`
- `JjkText`
- `JjkText`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`

## 知识

覆盖率 **92%**（33/36）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoLoraSelect`、`WanVideoEmptyEmbeds`、`Primitive integer [Crystools]`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoTorchCompileSettings`、`CreateCFGScheduleFloatList`、`WanVideoModelLoader`、`VHS_VideoCombine`、`SimpleMath+`、`WanVideoVAELoader`、`LoadImage`、`easy cleanGpuUsed`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect
