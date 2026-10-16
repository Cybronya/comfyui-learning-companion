---
key: 视频生成/图生视频/FFGO：自定义Wan2.2视频内容，用视频首帧提高主角背景一致性_1994305244540715009.json
name: FFGO：自定义Wan2.2视频内容，用视频首帧提高主角背景一致性_1994305244540715009.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1994305244540715009.json
hash: 16473c6221b3a777
coverage: 0.94
learned_at: 2026-10-15 22:33:20
nodes: [LoadWanVideoT5TextEncoder, WanVideoVAELoader, ImageResizeKJv2, WanVideoImageToVideoEncode, INTConstant, INTConstant, WanVideoDecode, WanVideoSampler, WanVideoSampler, GetImageSizeAndCount, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoTorchCompileSettings, Reroute, CreateCFGScheduleFloatList, LoadImage, LoadImage, ImageResizeKJv2, RMBG, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImageStitch, ImageResizeKJv2, PreviewImage, PreviewImage, ImageFromBatch+, SaveImage, VHS_VideoCombine, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, LoadImage, RMBG, RMBG, RMBG, AILab_ImageStitch, LoadImage, LoadImage, LoadImage, LoadImage, RH_Nano_Banana2_Image2Image, WanVideoTextEncode, Label (rgthree)]
patterns: []
missing: []
---

# 视频生成/图生视频/FFGO：自定义Wan2.2视频内容，用视频首帧提高主角背景一致性_1994305244540715009.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1994305244540715009.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（50 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `ImageResizeKJv2`
- `WanVideoImageToVideoEncode`
- `INTConstant`
- `INTConstant`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `GetImageSizeAndCount`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoTorchCompileSettings`
- `Reroute`
- `CreateCFGScheduleFloatList`
- `LoadImage`
- `LoadImage`
- `ImageResizeKJv2`
- `RMBG`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageStitch`
- `ImageResizeKJv2`
- `PreviewImage`
- `PreviewImage`
- `ImageFromBatch+`
- `SaveImage`
- `VHS_VideoCombine`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadImage`
- `RMBG`
- `RMBG`
- `RMBG`
- `AILab_ImageStitch`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `RH_Nano_Banana2_Image2Image`
- `WanVideoTextEncode`
- `Label (rgthree)`

## 知识

覆盖率 **94%**（47/50）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`ImageResizeKJv2`、`WanVideoImageToVideoEncode`、`INTConstant`、`WanVideoDecode`、`WanVideoSampler`、`GetImageSizeAndCount`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`CreateCFGScheduleFloatList`、`LoadImage`、`RMBG`、`ImageStitch`、`ImageFromBatch+`、`SaveImage`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`AILab_ImageStitch`、`RH_Nano_Banana2_Image2Image`、`WanVideoTextEncode`、`Label (rgthree)`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
