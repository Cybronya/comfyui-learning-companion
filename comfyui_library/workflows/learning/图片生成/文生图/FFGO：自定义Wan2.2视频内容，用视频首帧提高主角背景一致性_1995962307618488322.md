---
key: 图片生成/文生图/FFGO：自定义Wan2.2视频内容，用视频首帧提高主角背景一致性_1995962307618488322.json
name: FFGO：自定义Wan2.2视频内容，用视频首帧提高主角背景一致性_1995962307618488322
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/FFGO：自定义Wan2.2视频内容，用视频首帧提高主角背景一致性_1995962307618488322.json
hash: 2adcc85a6aa3721f
coverage: 0.938776
learned_at: 2026-10-19 21:32:27
nodes: [LoadWanVideoT5TextEncoder, WanVideoVAELoader, ImageResizeKJv2, WanVideoImageToVideoEncode, INTConstant, INTConstant, WanVideoDecode, WanVideoSampler, WanVideoSampler, GetImageSizeAndCount, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoTorchCompileSettings, Reroute, CreateCFGScheduleFloatList, LoadImage, LoadImage, ImageResizeKJv2, RMBG, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImageStitch, ImageResizeKJv2, PreviewImage, PreviewImage, ImageFromBatch+, SaveImage, VHS_VideoCombine, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, LoadImage, RMBG, RMBG, RMBG, AILab_ImageStitch, LoadImage, LoadImage, LoadImage, LoadImage, RH_Nano_Banana2_Image2Image, WanVideoTextEncode]
patterns: []
missing: []
---

# 图片生成/文生图/FFGO：自定义Wan2.2视频内容，用视频首帧提高主角背景一致性_1995962307618488322.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/FFGO：自定义Wan2.2视频内容，用视频首帧提高主角背景一致性_1995962307618488322.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（49 个）：
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

## 知识

覆盖率 **94%**（46/49）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`ImageResizeKJv2`、`WanVideoImageToVideoEncode`、`INTConstant`、`WanVideoDecode`、`WanVideoSampler`、`GetImageSizeAndCount`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`CreateCFGScheduleFloatList`、`LoadImage`、`RMBG`、`ImageStitch`、`ImageFromBatch+`、`SaveImage`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`AILab_ImageStitch`、`RH_Nano_Banana2_Image2Image`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
