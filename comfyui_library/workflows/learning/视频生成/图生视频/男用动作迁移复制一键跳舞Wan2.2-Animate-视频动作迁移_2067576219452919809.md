---
key: 视频生成/图生视频/男用动作迁移复制一键跳舞Wan2.2-Animate-视频动作迁移_2067576219452919809.json
name: 男用动作迁移复制一键跳舞Wan2.2-Animate-视频动作迁移_2067576219452919809.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2067576219452919809.json
hash: adf3fa6bb5715c88
coverage: 1
learned_at: 2026-10-15 22:40:07
nodes: [PixelPerfectResolution, DWPreprocessor, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoVAELoader, WanVideoClipVisionEncode, CLIPVisionLoader, WanVideoSetLoRAs, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, WanVideoSampler, GetImageSizeAndCount, RHHiddenNodes, WanVideoTextEncodeCached, WanVideoModelLoader, WanVideoLoraSelectMulti, ImageResizeKJv2, Text, JWInteger, JWInteger, LoadImage, ImageConcatMulti, VHS_VideoCombine, SaveImage, ImageConcatMulti, WanVideoDecode, VHS_LoadVideo, TT_img_enc, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/男用动作迁移复制一键跳舞Wan2.2-Animate-视频动作迁移_2067576219452919809.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2067576219452919809.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（29 个）：
- `PixelPerfectResolution`
- `DWPreprocessor`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `WanVideoSetLoRAs`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `WanVideoSampler` ★核心
- `GetImageSizeAndCount`
- `RHHiddenNodes`
- `WanVideoTextEncodeCached`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `ImageResizeKJv2`
- `Text`
- `JWInteger`
- `JWInteger`
- `LoadImage`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `SaveImage`
- `ImageConcatMulti`
- `WanVideoDecode`
- `VHS_LoadVideo`
- `TT_img_enc`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（29/29）

**有卡**：`PixelPerfectResolution`、`DWPreprocessor`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`FaceMaskFromPoseKeypoints`、`ImageCropByMaskAndResize`、`WanVideoSampler`、`GetImageSizeAndCount`、`RHHiddenNodes`、`WanVideoTextEncodeCached`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`ImageResizeKJv2`、`Text`、`JWInteger`、`LoadImage`、`ImageConcatMulti`、`VHS_VideoCombine`、`SaveImage`、`WanVideoDecode`、`VHS_LoadVideo`、`TT_img_enc`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
