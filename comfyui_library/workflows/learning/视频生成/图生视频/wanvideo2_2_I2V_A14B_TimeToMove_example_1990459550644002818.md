---
key: 视频生成/图生视频/wanvideo2_2_I2V_A14B_TimeToMove_example_1990459550644002818.json
name: wanvideo2_2_I2V_A14B_TimeToMove_example_1990459550644002818.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1990459550644002818.json
hash: 98344e9f635e18cf
coverage: 0.695652
learned_at: 2026-10-15 22:33:10
nodes: [WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, WanVideoVAELoader, SetNode, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, SetNode, LoadImage, VHS_LoadVideo, GetNode, WanVideoImageToVideoEncode, WanVideoEncode, VHS_LoadVideo, ImageResizeKJv2, ImageToMask, WanVideoModelLoader, ImageResizeKJv2, SetNode, GetNode, WanVideoAddTTMLatents, SetNode, GetNode, GetNode, GetNode, INTConstant, INTConstant, CreateCFGScheduleFloatList, GetNode, WanVideoSampler, WanVideoSampler, AILab_QwenVL, PreviewAny, WanVideoTextEncodeCached, ImageResizeKJv2, SetNode, GetNode, GetImageSizeAndCount, WanVideoDecode, WanVideoDecode, VHS_VideoCombine, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/wanvideo2_2_I2V_A14B_TimeToMove_example_1990459550644002818.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1990459550644002818.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（46 个）：
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `SetNode`
- `LoadImage`
- `VHS_LoadVideo`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `WanVideoEncode`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `ImageToMask`
- `WanVideoModelLoader`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `WanVideoAddTTMLatents`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `AILab_QwenVL`
- `PreviewAny`
- `WanVideoTextEncodeCached`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **70%**（32/46）

**有卡**：`WanVideoBlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LoadImage`、`VHS_LoadVideo`、`WanVideoImageToVideoEncode`、`WanVideoEncode`、`ImageResizeKJv2`、`ImageToMask`、`WanVideoAddTTMLatents`、`INTConstant`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`AILab_QwenVL`、`WanVideoTextEncodeCached`、`GetImageSizeAndCount`、`WanVideoDecode`、`VHS_VideoCombine`、`ImageConcatMulti`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、WanVideoDecode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoEncode
