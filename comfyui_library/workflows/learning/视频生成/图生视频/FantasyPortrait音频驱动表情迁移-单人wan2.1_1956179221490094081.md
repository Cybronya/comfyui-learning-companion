---
key: 视频生成/图生视频/FantasyPortrait音频驱动表情迁移-单人wan2.1_1956179221490094081.json
name: FantasyPortrait音频驱动表情迁移-单人wan2.1_1956179221490094081.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1956179221490094081.json
hash: 3ce8039f4dbffbef
coverage: 0.833333
learned_at: 2026-10-15 22:31:12
nodes: [WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoBlockSwap, FantasyPortraitModelLoader, CLIPVisionLoader, WanVideoVAELoader, WanVideoDecode, ImageConcanate, ImageConcanate, WanVideoLoraSelect, WanVideoSampler, WanVideoSetLoRAs, WanVideoTextEncodeCached, PrimitiveInt, PrimitiveInt, LoadImage, WanVideoImageToVideoEncode, ImageResizeKJv2, Reroute, WanVideoClipVisionEncode, WanVideoAddFantasyPortrait, FantasyPortraitFaceDetector, Reroute, VHS_VideoCombine, VHS_VideoCombine, WanVideoSetBlockSwap, ImageResizeKJv2, VHS_LoadVideo, VHS_VideoInfoLoaded, Reroute]
patterns: []
missing: []
---

# 视频生成/图生视频/FantasyPortrait音频驱动表情迁移-单人wan2.1_1956179221490094081.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956179221490094081.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（30 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `FantasyPortraitModelLoader`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `ImageConcanate`
- `ImageConcanate`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `WanVideoImageToVideoEncode`
- `ImageResizeKJv2`
- `Reroute`
- `WanVideoClipVisionEncode`
- `WanVideoAddFantasyPortrait`
- `FantasyPortraitFaceDetector`
- `Reroute`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoSetBlockSwap`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `VHS_VideoInfoLoaded`
- `Reroute`

## 知识

覆盖率 **83%**（25/30）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`FantasyPortraitModelLoader`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoDecode`、`ImageConcanate`、`WanVideoLoraSelect`、`WanVideoSampler`、`WanVideoSetLoRAs`、`WanVideoTextEncodeCached`、`LoadImage`、`WanVideoImageToVideoEncode`、`ImageResizeKJv2`、`WanVideoClipVisionEncode`、`WanVideoAddFantasyPortrait`、`FantasyPortraitFaceDetector`、`VHS_VideoCombine`、`WanVideoSetBlockSwap`、`VHS_LoadVideo`、`VHS_VideoInfoLoaded`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoLoraSelect
