---
key: 视频生成/图生视频/Wan2.2 Animate ——飞翔荷兰人_1971146513277689858.json
name: Wan2.2 Animate ——飞翔荷兰人_1971146513277689858.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1971146513277689858.json
hash: 36207e9121dcca78
coverage: 0.461538
learned_at: 2026-10-15 22:31:55
nodes: [SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoDecode, SetNode, JWInteger, SetNode, JWInteger, Int, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoSampler, GetNode, GetNode, SetNode, ImageCropByMaskAndResize, FaceMaskFromPoseKeypoints, VHS_VideoCombine, SetNode, SetNode, DWPreprocessor, PixelPerfectResolution, GetNode, GetNode, GetNode, SetNode, SetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, SetNode, WanVideoBlockSwap, WanVideoModelLoader, CLIPVisionLoader, WanVideoVAELoader, WanVideoLoraSelectMulti, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, ImageResizeKJv2, WanVideoAnimateEmbeds, GetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, ImageConcatMulti, ImageConcatMulti, WanVideoTextEncodeCached, AILab_MiniCPM_4_V, CR Text, VHS_VideoCombine, VHS_VideoCombine, GetNode, WanVideoClipVisionEncode, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate ——飞翔荷兰人_1971146513277689858.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1971146513277689858.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（65 个）：
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
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
- `WanVideoSampler` ★核心
- `GetNode`
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
- `WanVideoTextEncodeCached`
- `AILab_MiniCPM_4_V`
- `CR Text`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetNode`
- `WanVideoClipVisionEncode`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **46%**（30/65）

**有卡**：`WanVideoDecode`、`JWInteger`、`Int`、`WanVideoSampler`、`ImageCropByMaskAndResize`、`FaceMaskFromPoseKeypoints`、`VHS_VideoCombine`、`DWPreprocessor`、`PixelPerfectResolution`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoLoraSelectMulti`、`ImageResizeKJv2`、`WanVideoAnimateEmbeds`、`GetImageSizeAndCount`、`ImageConcatMulti`、`WanVideoTextEncodeCached`、`AILab_MiniCPM_4_V`、`CR Text`、`WanVideoClipVisionEncode`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
