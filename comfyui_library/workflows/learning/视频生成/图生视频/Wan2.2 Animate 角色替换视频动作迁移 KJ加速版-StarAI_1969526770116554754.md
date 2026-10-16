---
key: 视频生成/图生视频/Wan2.2 Animate 角色替换视频动作迁移 KJ加速版-StarAI_1969526770116554754.json
name: Wan2.2 Animate 角色替换视频动作迁移 KJ加速版-StarAI_1969526770116554754.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1969526770116554754.json
hash: c05d9fc1b9115cff
coverage: 0.446154
learned_at: 2026-10-15 22:31:49
nodes: [SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, WanVideoTextEncodeCached, WanVideoDecode, SetNode, JWInteger, SetNode, JWInteger, Int, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoSampler, GetNode, VHS_VideoCombine, MarkdownNote, GetNode, SetNode, CR Text, VHS_LoadVideo, ImageCropByMaskAndResize, FaceMaskFromPoseKeypoints, VHS_VideoCombine, SetNode, SetNode, DWPreprocessor, PixelPerfectResolution, GetNode, GetNode, GetNode, SetNode, SetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, WanVideoBlockSwap, WanVideoModelLoader, CLIPVisionLoader, WanVideoVAELoader, WanVideoLoraSelectMulti, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, LoadImage, ImageResizeKJv2, WanVideoAnimateEmbeds, GetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, ImageConcatMulti, ImageConcatMulti, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate 角色替换视频动作迁移 KJ加速版-StarAI_1969526770116554754.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1969526770116554754.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（65 个）：
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
- `MarkdownNote`
- `GetNode`
- `SetNode`
- `CR Text`
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
- `LoadImage`
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

## 知识

覆盖率 **45%**（29/65）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`JWInteger`、`Int`、`WanVideoSampler`、`VHS_VideoCombine`、`CR Text`、`VHS_LoadVideo`、`ImageCropByMaskAndResize`、`FaceMaskFromPoseKeypoints`、`DWPreprocessor`、`PixelPerfectResolution`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`LoadImage`、`ImageResizeKJv2`、`WanVideoAnimateEmbeds`、`GetImageSizeAndCount`、`ImageConcatMulti`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
