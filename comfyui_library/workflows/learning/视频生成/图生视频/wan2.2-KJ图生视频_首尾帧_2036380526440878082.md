---
key: 视频生成/图生视频/wan2.2-KJ图生视频_首尾帧_2036380526440878082.json
name: wan2.2-KJ图生视频_首尾帧_2036380526440878082.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2036380526440878082.json
hash: 892a6903b4364358
coverage: 0.769231
learned_at: 2026-10-15 22:35:52
nodes: [WanVideoBlockSwap, WanVideoDecode, WanVideoSampler, WanVideoVAELoader, VHS_VideoCombine, Note, WanVideoSampler, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, LoadImage, ImageResize+, WanVideoModelLoader, LoadWanVideoT5TextEncoder, Note, Note, Note, CreateCFGScheduleFloatList, LayerUtility: ImageScaleByAspectRatio V2, WanVideoImageToVideoEncode, LoadImage, Note, WanVideoTorchCompileSettings, Note, Int, WanVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2-KJ图生视频_首尾帧_2036380526440878082.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2036380526440878082.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（26 个）：
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `Note`
- `WanVideoSampler` ★核心
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `LoadImage`
- `ImageResize+`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `Note`
- `Note`
- `Note`
- `CreateCFGScheduleFloatList`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoImageToVideoEncode`
- `LoadImage`
- `Note`
- `WanVideoTorchCompileSettings`
- `Note`
- `Int`
- `WanVideoTextEncode`

## 知识

覆盖率 **77%**（20/26）

**有卡**：`WanVideoBlockSwap`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoVAELoader`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`LoadImage`、`ImageResize+`、`LoadWanVideoT5TextEncoder`、`CreateCFGScheduleFloatList`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoImageToVideoEncode`、`WanVideoTorchCompileSettings`、`Int`、`WanVideoTextEncode`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
