---
key: 视频生成/图生视频/Wan2.2+Animate+角色替换视频动作迁移+KJ加速版_1993551269581225986.json
name: Wan2.2+Animate+角色替换视频动作迁移+KJ加速版_1993551269581225986.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2+Animate+角色替换视频动作迁移+KJ加速版_1993551269581225986.json
hash: 96f78679f20c4067
coverage: 0.453125
learned_at: 2026-10-15 22:33:18
nodes: [SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, WanVideoTextEncodeCached, WanVideoDecode, SetNode, JWInteger, SetNode, JWInteger, Int, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoSampler, GetNode, VHS_VideoCombine, GetNode, SetNode, ImageCropByMaskAndResize, FaceMaskFromPoseKeypoints, VHS_VideoCombine, SetNode, SetNode, DWPreprocessor, PixelPerfectResolution, GetNode, GetNode, GetNode, SetNode, SetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, WanVideoBlockSwap, WanVideoModelLoader, CLIPVisionLoader, WanVideoVAELoader, WanVideoLoraSelectMulti, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, ImageResizeKJv2, WanVideoAnimateEmbeds, GetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine, CR Text, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2+Animate+角色替换视频动作迁移+KJ加速版_1993551269581225986.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1993551269581225986.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（64 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `WanVideoTextEncodeCached`
- `WanVideoDecode`
- `SetNode`
- `JWInteger`
- `SetNode`
- `JWInteger`
- `Int`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
- `ImageCropByMaskAndResize`
- `FaceMaskFromPoseKeypoints`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `DWPreprocessor`
- `PixelPerfectResolution`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `WanVideoLoraSelectMulti`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImageResizeKJv2`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `CR Text`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **45%**（29/64）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`JWInteger`、`Int`、`WanVideoSampler`、`VHS_VideoCombine`、`ImageCropByMaskAndResize`、`FaceMaskFromPoseKeypoints`、`DWPreprocessor`、`PixelPerfectResolution`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`ImageResizeKJv2`、`WanVideoAnimateEmbeds`、`GetImageSizeAndCount`、`ImageConcatMulti`、`CR Text`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
