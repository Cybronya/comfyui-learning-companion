---
key: 数字人/数字人/Wan Animate 2.2-角色替换-动作迁移-图生视频-许老师专用_1981594203375443969.json
name: Wan Animate 2.2-角色替换-动作迁移-图生视频-许老师专用_1981594203375443969
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan Animate 2.2-角色替换-动作迁移-图生视频-许老师专用_1981594203375443969.json
hash: f9074c3455ecb399
coverage: 0.4
learned_at: 2026-10-26 01:57:41
nodes: [PixelPerfectResolution, GetNode, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, GetNode, GetNode, SetNode, SetNode, DWPreprocessor, CLIPVisionLoader, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, WanVideoDecode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoVAELoader, SetNode, FaceMaskFromPoseKeypoints, SetNode, ImageCropByMaskAndResize, SetNode, GetImageSizeAndCount, ImageConcatMulti, SetNode, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, WanVideoSampler, VHS_VideoCombine, VHS_VideoCombine, SetNode, SetNode, WanVideoTextEncodeCached, ImageConcatMulti, SetNode, GetNode, GetNode, GetNode, SetNode, WanVideoAnimateEmbeds, Int, Int, VHS_LoadVideo, LoadImage, WanVideoModelLoader, WanVideoLoraSelectMulti]
patterns: []
missing: []
---

# 数字人/数字人/Wan Animate 2.2-角色替换-动作迁移-图生视频-许老师专用_1981594203375443969.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan Animate 2.2-角色替换-动作迁移-图生视频-许老师专用_1981594203375443969.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（65 个）：
- `PixelPerfectResolution`
- `GetNode`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `DWPreprocessor`
- `CLIPVisionLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoVAELoader`
- `SetNode`
- `FaceMaskFromPoseKeypoints`
- `SetNode`
- `ImageCropByMaskAndResize`
- `SetNode`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `WanVideoTextEncodeCached`
- `ImageConcatMulti`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoAnimateEmbeds`
- `Int`
- `Int`
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`

## 知识

覆盖率 **40%**（26/65）

**有卡**：`PixelPerfectResolution`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`DWPreprocessor`、`CLIPVisionLoader`、`WanVideoDecode`、`ImageResizeKJv2`、`WanVideoVAELoader`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`GetImageSizeAndCount`、`ImageConcatMulti`、`WanVideoClipVisionEncode`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`WanVideoAnimateEmbeds`、`Int`、`VHS_LoadVideo`、`LoadImage`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
