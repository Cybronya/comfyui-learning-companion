---
key: 视频生成/图生视频/【人物替换】Wan2.2+Animate+角色替换视频动作迁移+KJ加速版-StarAI_1982315306993500162.json
name: 【人物替换】Wan2.2+Animate+角色替换视频动作迁移+KJ加速版-StarAI_1982315306993500162.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1982315306993500162.json
hash: 8987cd55238b2b4e
coverage: 0.453125
learned_at: 2026-10-15 22:32:40
nodes: [SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, WanVideoTextEncodeCached, WanVideoDecode, SetNode, JWInteger, SetNode, JWInteger, Int, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoSampler, GetNode, VHS_VideoCombine, GetNode, SetNode, VHS_LoadVideo, ImageCropByMaskAndResize, FaceMaskFromPoseKeypoints, VHS_VideoCombine, SetNode, SetNode, DWPreprocessor, PixelPerfectResolution, GetNode, GetNode, GetNode, SetNode, SetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, WanVideoBlockSwap, WanVideoModelLoader, CLIPVisionLoader, WanVideoVAELoader, WanVideoLoraSelectMulti, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, ImageResizeKJv2, WanVideoAnimateEmbeds, GetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine, LoadImage, CR Text]
patterns: []
missing: []
---

# 视频生成/图生视频/【人物替换】Wan2.2+Animate+角色替换视频动作迁移+KJ加速版-StarAI_1982315306993500162.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1982315306993500162.json`

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
- `VHS_LoadVideo`
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
- `LoadImage`
- `CR Text`

## 知识

覆盖率 **45%**（29/64）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`JWInteger`、`Int`、`WanVideoSampler`、`VHS_VideoCombine`、`VHS_LoadVideo`、`ImageCropByMaskAndResize`、`FaceMaskFromPoseKeypoints`、`DWPreprocessor`、`PixelPerfectResolution`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`ImageResizeKJv2`、`WanVideoAnimateEmbeds`、`GetImageSizeAndCount`、`ImageConcatMulti`、`LoadImage`、`CR Text`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
