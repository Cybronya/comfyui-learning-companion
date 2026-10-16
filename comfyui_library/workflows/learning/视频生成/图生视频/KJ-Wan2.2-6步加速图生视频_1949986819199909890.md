---
key: 视频生成/图生视频/KJ-Wan2.2-6步加速图生视频_1949986819199909890.json
name: KJ-Wan2.2-6步加速图生视频_1949986819199909890.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1949986819199909890.json
hash: b84ade4237da9fdf
coverage: 0.852941
learned_at: 2026-10-15 22:30:50
nodes: [LoadWanVideoT5TextEncoder, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSampler, WanVideoSampler, WanVideoSetBlockSwap, GetImageSizeAndCount, VHS_VideoCombine, WanVideoSetLoRAs, CreateCFGScheduleFloatList, WanVideoLoraSelect, WanVideoTorchCompileSettings, WanVideoBlockSwap, Note, MathExpression|pysssss, Note, Note, LoadImage, Note, Note, WanVideoVAELoader, ImageResizeKJv2, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoModelLoader, Text Multiline, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], WanVideoDecode, WanVideoLoraSelect, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/KJ-Wan2.2-6步加速图生视频_1949986819199909890.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1949986819199909890.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（34 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSetBlockSwap`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `WanVideoLoraSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `Note`
- `MathExpression|pysssss`
- `Note`
- `Note`
- `LoadImage`
- `Note`
- `Note`
- `WanVideoVAELoader`
- `ImageResizeKJv2`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `Text Multiline`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`

## 知识

覆盖率 **85%**（29/34）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSampler`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`CreateCFGScheduleFloatList`、`WanVideoLoraSelect`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`MathExpression|pysssss`、`LoadImage`、`WanVideoVAELoader`、`ImageResizeKJv2`、`WanVideoImageToVideoEncode`、`WanVideoModelLoader`、`Text Multiline`、`Primitive integer [Crystools]`、`WanVideoDecode`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
