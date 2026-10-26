---
key: 数字人/数字人/wanvideo_2_1_I2V_FantasyPortrait_表情迁移_1957329197184249857.json
name: wanvideo_2_1_I2V_FantasyPortrait_表情迁移_1957329197184249857
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/wanvideo_2_1_I2V_FantasyPortrait_表情迁移_1957329197184249857.json
hash: 73e0c2ab888677fb
coverage: 0.58
learned_at: 2026-10-26 01:59:30
nodes: [GetNode, INTConstant, INTConstant, SetNode, SetNode, SetNode, SetNode, WanVideoSetBlockSwap, FantasyPortraitModelLoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSetLoRAs, SetNode, WanVideoVAELoader, SetNode, GetNode, GetNode, ImageResizeKJv2, GetNode, FantasyPortraitFaceDetector, ImageResizeKJv2, WanVideoClipVisionEncode, GetNode, GetNode, VHS_LoadVideo, CLIPVisionLoader, GetNode, GetNode, GetNode, WanVideoImageToVideoEncode, SetNode, GetNode, SetNode, SetNode, GetNode, WanVideoTextEncodeCached, GetNode, WanVideoContextOptions, WanVideoSampler, WanVideoDecode, ImageConcatMulti, ImageConcatMulti, INTConstant, WanVideoAddFantasyPortrait, VHS_VideoCombine, VHS_VideoCombine, LoadImage]
patterns: []
missing: []
---

# 数字人/数字人/wanvideo_2_1_I2V_FantasyPortrait_表情迁移_1957329197184249857.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/wanvideo_2_1_I2V_FantasyPortrait_表情迁移_1957329197184249857.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（50 个）：
- `GetNode`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoSetBlockSwap`
- `FantasyPortraitModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `FantasyPortraitFaceDetector`
- `ImageResizeKJv2`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `GetNode`
- `WanVideoContextOptions`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `INTConstant`
- `WanVideoAddFantasyPortrait`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`

## 知识

覆盖率 **58%**（29/50）

**有卡**：`INTConstant`、`WanVideoSetBlockSwap`、`FantasyPortraitModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`ImageResizeKJv2`、`FantasyPortraitFaceDetector`、`WanVideoClipVisionEncode`、`VHS_LoadVideo`、`CLIPVisionLoader`、`WanVideoImageToVideoEncode`、`WanVideoTextEncodeCached`、`WanVideoContextOptions`、`WanVideoSampler`、`WanVideoDecode`、`ImageConcatMulti`、`WanVideoAddFantasyPortrait`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoLoraSelect
