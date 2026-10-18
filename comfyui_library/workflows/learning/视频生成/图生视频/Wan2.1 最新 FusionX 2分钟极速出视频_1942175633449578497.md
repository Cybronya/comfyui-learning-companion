---
key: 视频生成/图生视频/Wan2.1 最新 FusionX 2分钟极速出视频_1942175633449578497.json
name: Wan2.1 最新 FusionX 2分钟极速出视频_1942175633449578497.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1 最新 FusionX 2分钟极速出视频_1942175633449578497.json
hash: 8b28514f2adc94eb
coverage: 0.916667
learned_at: 2026-10-15 22:30:36
nodes: [ImageUpscaleWithModel, GetImageRangeFromBatch, PreviewImage, ImageResizeKJ, UpscaleModelLoader, ImpactFloat, RIFE VFI, VHS_VideoCombine, PreviewImage, WanVideoImageToVideoEncode, ImageResizeKJ, WanVideoTextEncode, LoadImage, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoVAELoader, VHS_VideoCombine, WanVideoDecode, WanVideoModelLoader, WanVideoBlockSwap, easy int, WanVideoSampler, CR Text, WanVideoTorchCompileSettings]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1 最新 FusionX 2分钟极速出视频_1942175633449578497.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1942175633449578497.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（24 个）：
- `ImageUpscaleWithModel`
- `GetImageRangeFromBatch`
- `PreviewImage`
- `ImageResizeKJ`
- `UpscaleModelLoader`
- `ImpactFloat`
- `RIFE VFI`
- `VHS_VideoCombine`
- `PreviewImage`
- `WanVideoImageToVideoEncode`
- `ImageResizeKJ`
- `WanVideoTextEncode`
- `LoadImage`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `easy int`
- `WanVideoSampler` ★核心
- `CR Text`
- `WanVideoTorchCompileSettings`

## 知识

覆盖率 **92%**（22/24）

**有卡**：`ImageUpscaleWithModel`、`GetImageRangeFromBatch`、`ImageResizeKJ`、`UpscaleModelLoader`、`ImpactFloat`、`RIFE VFI`、`VHS_VideoCombine`、`WanVideoImageToVideoEncode`、`WanVideoTextEncode`、`LoadImage`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoDecode`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`easy int`、`WanVideoSampler`、`CR Text`、`WanVideoTorchCompileSettings`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoLoraSelect
