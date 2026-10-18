---
key: 视频生成/图生视频/wanvideo_2_1_I2V_FantasyPortrait_表情迁移_1957641914193473538.json
name: wanvideo_2_1_I2V_FantasyPortrait_表情迁移_1957641914193473538.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wanvideo_2_1_I2V_FantasyPortrait_表情迁移_1957641914193473538.json
hash: b22d7775d57039d7
coverage: 0.58
learned_at: 2026-10-15 22:31:17
nodes: [GetNode, INTConstant, SetNode, SetNode, SetNode, SetNode, WanVideoSetBlockSwap, FantasyPortraitModelLoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSetLoRAs, SetNode, WanVideoVAELoader, SetNode, GetNode, GetNode, ImageResizeKJv2, GetNode, FantasyPortraitFaceDetector, ImageResizeKJv2, WanVideoClipVisionEncode, GetNode, GetNode, CLIPVisionLoader, GetNode, GetNode, GetNode, WanVideoImageToVideoEncode, SetNode, GetNode, SetNode, SetNode, GetNode, WanVideoTextEncodeCached, GetNode, WanVideoContextOptions, WanVideoSampler, WanVideoDecode, ImageConcatMulti, ImageConcatMulti, WanVideoAddFantasyPortrait, VHS_VideoCombine, VHS_VideoCombine, INTConstant, INTConstant, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/wanvideo_2_1_I2V_FantasyPortrait_表情迁移_1957641914193473538.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1957641914193473538.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（50 个）：
- `GetNode`
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
- `WanVideoAddFantasyPortrait`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **58%**（29/50）

**有卡**：`INTConstant`、`WanVideoSetBlockSwap`、`FantasyPortraitModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`ImageResizeKJv2`、`FantasyPortraitFaceDetector`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoImageToVideoEncode`、`WanVideoTextEncodeCached`、`WanVideoContextOptions`、`WanVideoSampler`、`WanVideoDecode`、`ImageConcatMulti`、`WanVideoAddFantasyPortrait`、`VHS_VideoCombine`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoLoraSelect
