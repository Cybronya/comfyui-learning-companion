---
key: 视频生成/图生视频/Wan2.1：Wanmove 图生视频，轨迹控制运动_1999283559233974273.json
name: Wan2.1：Wanmove 图生视频，轨迹控制运动_1999283559233974273.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1999283559233974273.json
hash: 3c2a85a6732275a1
coverage: 0.965517
learned_at: 2026-10-15 22:33:36
nodes: [INTConstant, INTConstant, LayerUtility: ImageScaleByAspectRatio V2, CLIPVisionLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, WanVideoTorchCompileSettings, RepeatImageBatch, WanVideoClipVisionEncode, VHS_VideoCombine, VHS_VideoCombine, WanVideoImageToVideoEncode, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoAddWanMoveTracks, ImageConcanate, WanVideoWanDrawWanMoveTracks, WanVideoSampler, WanVideoDecode, easy showAnything, SplineEditor, WanVideoTextEncode, LoadImage, Text Multiline, HAIGC_VideoLoader, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1：Wanmove 图生视频，轨迹控制运动_1999283559233974273.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1999283559233974273.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（29 个）：
- `INTConstant`
- `INTConstant`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `RepeatImageBatch`
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoImageToVideoEncode`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoAddWanMoveTracks`
- `ImageConcanate`
- `WanVideoWanDrawWanMoveTracks`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `easy showAnything`
- `SplineEditor`
- `WanVideoTextEncode`
- `LoadImage`
- `Text Multiline`
- `HAIGC_VideoLoader`
- `VHS_VideoCombine`

## 知识

覆盖率 **97%**（28/29）

**有卡**：`INTConstant`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPVisionLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`RepeatImageBatch`、`WanVideoClipVisionEncode`、`VHS_VideoCombine`、`WanVideoImageToVideoEncode`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`WanVideoAddWanMoveTracks`、`ImageConcanate`、`WanVideoWanDrawWanMoveTracks`、`WanVideoSampler`、`WanVideoDecode`、`SplineEditor`、`WanVideoTextEncode`、`LoadImage`、`Text Multiline`、`HAIGC_VideoLoader`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode
