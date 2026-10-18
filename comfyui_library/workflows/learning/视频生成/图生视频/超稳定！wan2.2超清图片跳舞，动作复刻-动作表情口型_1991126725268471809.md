---
key: 视频生成/图生视频/超稳定！wan2.2超清图片跳舞，动作复刻-动作表情口型_1991126725268471809.json
name: 超稳定！wan2.2超清图片跳舞，动作复刻-动作表情口型_1991126725268471809.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/超稳定！wan2.2超清图片跳舞，动作复刻-动作表情口型_1991126725268471809.json
hash: 10a9f946396649e2
coverage: 0.563636
learned_at: 2026-10-15 22:33:12
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, DWPreprocessor, VHS_VideoCombine, CLIPVisionLoader, WanVideoVAELoader, WanVideoTextEncodeCached, GetNode, GetNode, SetNode, SetNode, JWInteger, PixelPerfectResolution, SetNode, ImageCropByMaskAndResize, FaceMaskFromPoseKeypoints, SetNode, SetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, SetNode, Reroute, GetNode, SetNode, SetNode, VHS_VideoInfoLoaded, SetNode, GetNode, WanVideoLoraSelectMulti, WanVideoAnimateEmbeds, GetNode, WanVideoDecode, VHS_VideoCombine, VHS_LoadVideo, GetImageSizeAndCount, VHS_VideoCombine, GetNode, GetNode, GetNode, SetNode, JWInteger, LoadImage, ImageConcatMulti, GetNode, GetNode, WanVideoBlockSwap, WanVideoClipVisionEncode, LayerUtility: ImageScaleByAspectRatio V2, ImageConcatMulti, WanVideoSampler, WanVideoModelLoader, CR Prompt Text, easy seed]
patterns: []
missing: []
---

# 视频生成/图生视频/超稳定！wan2.2超清图片跳舞，动作复刻-动作表情口型_1991126725268471809.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1991126725268471809.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（55 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `DWPreprocessor`
- `VHS_VideoCombine`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `JWInteger`
- `PixelPerfectResolution`
- `SetNode`
- `ImageCropByMaskAndResize`
- `FaceMaskFromPoseKeypoints`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `Reroute`
- `GetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `GetNode`
- `WanVideoLoraSelectMulti`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `JWInteger`
- `LoadImage`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageConcatMulti`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `CR Prompt Text`
- `easy seed`

## 知识

覆盖率 **56%**（31/55）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`DWPreprocessor`、`VHS_VideoCombine`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`JWInteger`、`PixelPerfectResolution`、`ImageCropByMaskAndResize`、`FaceMaskFromPoseKeypoints`、`ImageResizeKJv2`、`VHS_VideoInfoLoaded`、`WanVideoLoraSelectMulti`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`VHS_LoadVideo`、`GetImageSizeAndCount`、`LoadImage`、`ImageConcatMulti`、`WanVideoBlockSwap`、`WanVideoClipVisionEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoSampler`、`WanVideoModelLoader`、`CR Prompt Text`、`easy seed`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、easy seed、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached
