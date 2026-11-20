---
key: 平台全量/Wan2.1_I2V_FantasyPortrait_表情迁移_2011699230167011330.json
name: Wan2.1_I2V_FantasyPortrait_表情迁移_2011699230167011330
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1_I2V_FantasyPortrait_表情迁移_2011699230167011330.json
hash: cc117c84003ec31a
coverage: 0.833333
learned_at: 2026-11-14 01:04:42
nodes: [INTConstant, SetNode, SetNode, WanVideoSetBlockSwap, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoSetLoRAs, GetNode, INTConstant, WanVideoLoraSelect, WanVideoSampler, WanVideoClipVisionEncode, VHS_VideoCombine, WanVideoDecode, SetNode, WanVideoVAELoader, FantasyPortraitModelLoader, ImageResizeKJv2, LoadImage, VHS_VideoInfoLoaded, ImageResizeKJv2, FantasyPortraitFaceDetector, WanVideoAddFantasyPortrait, SetNode, WanVideoContextOptions, CLIPVisionLoader, WanVideoImageToVideoEncode, SetNode, WanVideoModelLoader, VHS_LoadVideo, WanVideoTextEncodeCached, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine, CR SDXL Aspect Ratio]
patterns: []
missing: []
---

# 平台全量/Wan2.1_I2V_FantasyPortrait_表情迁移_2011699230167011330.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1_I2V_FantasyPortrait_表情迁移_2011699230167011330.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（36 个）：
- `INTConstant`
- `SetNode`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `GetNode`
- `INTConstant`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `WanVideoClipVisionEncode`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `SetNode`
- `WanVideoVAELoader`
- `FantasyPortraitModelLoader`
- `ImageResizeKJv2`
- `LoadImage`
- `VHS_VideoInfoLoaded`
- `ImageResizeKJv2`
- `FantasyPortraitFaceDetector`
- `WanVideoAddFantasyPortrait`
- `SetNode`
- `WanVideoContextOptions`
- `CLIPVisionLoader`
- `WanVideoImageToVideoEncode`
- `SetNode`
- `WanVideoModelLoader`
- `VHS_LoadVideo`
- `WanVideoTextEncodeCached`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `CR SDXL Aspect Ratio`

## 知识

覆盖率 **83%**（30/36）

**有卡**：`INTConstant`、`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoSampler`、`WanVideoClipVisionEncode`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoVAELoader`、`FantasyPortraitModelLoader`、`ImageResizeKJv2`、`LoadImage`、`VHS_VideoInfoLoaded`、`FantasyPortraitFaceDetector`、`WanVideoAddFantasyPortrait`、`WanVideoContextOptions`、`CLIPVisionLoader`、`WanVideoImageToVideoEncode`、`WanVideoModelLoader`、`VHS_LoadVideo`、`WanVideoTextEncodeCached`、`ImageConcatMulti`、`CR SDXL Aspect Ratio`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelect
