---
key: 视频生成/图生视频/最新wan2.2图生视频，可在线运行，效果非常OK_1953038544099020801.json
name: 最新wan2.2图生视频，可在线运行，效果非常OK_1953038544099020801.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/最新wan2.2图生视频，可在线运行，效果非常OK_1953038544099020801.json
hash: 9b6a37b4a61bfa0d
coverage: 1
learned_at: 2026-10-15 22:31:04
nodes: [WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoTorchCompileSettings, LayerUtility: ImageScaleByAspectRatio V2, WanVideoTextEncode, WanVideoSetBlockSwap, WanVideoSampler, WanVideoImageToVideoEncode, WanVideoSetBlockSwap, Primitive integer [Crystools], CreateCFGScheduleFloatList, WanVideoSetLoRAs, MathExpression|pysssss, Primitive integer [Crystools], WanVideoSetLoRAs, WanVideoModelLoader, WanVideoSampler, ImageListToImageBatch, easy imageBatchToImageList, WanVideoDecode, VHS_VideoCombine, WanVideoLoraSelect, WanVideoLoraSelect, LoadImage, Primitive integer [Crystools], ImpactInt, WanVideoModelLoader, Text Multiline]
patterns: []
missing: []
---

# 视频生成/图生视频/最新wan2.2图生视频，可在线运行，效果非常OK_1953038544099020801.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1953038544099020801.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（29 个）：
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoTextEncode`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`
- `WanVideoSetBlockSwap`
- `Primitive integer [Crystools]`
- `CreateCFGScheduleFloatList`
- `WanVideoSetLoRAs`
- `MathExpression|pysssss`
- `Primitive integer [Crystools]`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `ImageListToImageBatch`
- `easy imageBatchToImageList`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadImage`
- `Primitive integer [Crystools]`
- `ImpactInt`
- `WanVideoModelLoader`
- `Text Multiline`

## 知识

覆盖率 **100%**（29/29）

**有卡**：`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoTextEncode`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoImageToVideoEncode`、`Primitive integer [Crystools]`、`CreateCFGScheduleFloatList`、`WanVideoSetLoRAs`、`MathExpression|pysssss`、`WanVideoModelLoader`、`ImageListToImageBatch`、`easy imageBatchToImageList`、`WanVideoDecode`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`LoadImage`、`ImpactInt`、`Text Multiline`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
