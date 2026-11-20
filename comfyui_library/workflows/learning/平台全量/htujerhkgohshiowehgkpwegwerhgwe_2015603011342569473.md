---
key: 平台全量/htujerhkgohshiowehgkpwegwerhgwe_2015603011342569473.json
name: htujerhkgohshiowehgkpwegwerhgwe_2015603011342569473
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/htujerhkgohshiowehgkpwegwerhgwe_2015603011342569473.json
hash: 047e7e97d0b148fc
coverage: 0.942857
learned_at: 2026-11-14 01:12:29
nodes: [GetImageSizeAndCount, OnnxDetectionModelLoader, ImageFromBatch, CLIPVisionLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, easy int, SeCVideoSegmentation, DrawMaskOnImage, BlockifyMask, ImageResizeKJv2, PrimitiveInt, WanVideoAnimateEmbeds, INTConstant, DrawViTPose, RIFE VFI, ImageUpscaleWithModelBatched, UpscaleModelLoader, RIFE VFI, UpscaleModelLoader, ImageUpscaleWithModelBatched, VHS_VideoCombine, RIFE VFI, ImageUpscaleWithModelBatched, UpscaleModelLoader, RIFE VFI, UpscaleModelLoader, RIFE VFI, ImageUpscaleWithModelBatched, UpscaleModelLoader, RIFE VFI, UpscaleModelLoader, VHS_VideoCombine, RIFE VFI, ImageUpscaleWithModelBatched, UpscaleModelLoader, RIFE VFI, UpscaleModelLoader, VHS_VideoCombine, ImageUpscaleWithModelBatched, ImageUpscaleWithModelBatched, ImageUpscaleWithModelBatched, PointsEditor, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, PreviewImage, WanVideoSampler, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoVAELoader, WanVideoBlockSwap, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, PoseAndFaceDetection, INTConstant, PreviewImage, VHS_VideoCombine, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, easy showAnything, WanVideoClipVisionEncode, GrowMaskWithBlur, VHS_VideoCombine, VHS_VideoCombine, SeCModelLoader, LoadImage]
patterns: []
missing: []
---

# 平台全量/htujerhkgohshiowehgkpwegwerhgwe_2015603011342569473.json

> 来源文件 `comfyui_library/workflows/平台全量/htujerhkgohshiowehgkpwegwerhgwe_2015603011342569473.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（70 个）：
- `GetImageSizeAndCount`
- `OnnxDetectionModelLoader`
- `ImageFromBatch`
- `CLIPVisionLoader`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `easy int`
- `SeCVideoSegmentation`
- `DrawMaskOnImage`
- `BlockifyMask`
- `ImageResizeKJv2`
- `PrimitiveInt`
- `WanVideoAnimateEmbeds`
- `INTConstant`
- `DrawViTPose`
- `RIFE VFI`
- `ImageUpscaleWithModelBatched`
- `UpscaleModelLoader`
- `RIFE VFI`
- `UpscaleModelLoader`
- `ImageUpscaleWithModelBatched`
- `VHS_VideoCombine`
- `RIFE VFI`
- `ImageUpscaleWithModelBatched`
- `UpscaleModelLoader`
- `RIFE VFI`
- `UpscaleModelLoader`
- `RIFE VFI`
- `ImageUpscaleWithModelBatched`
- `UpscaleModelLoader`
- `RIFE VFI`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `RIFE VFI`
- `ImageUpscaleWithModelBatched`
- `UpscaleModelLoader`
- `RIFE VFI`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `ImageUpscaleWithModelBatched`
- `ImageUpscaleWithModelBatched`
- `ImageUpscaleWithModelBatched`
- `PointsEditor`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PreviewImage`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `PoseAndFaceDetection`
- `INTConstant`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `easy showAnything`
- `WanVideoClipVisionEncode`
- `GrowMaskWithBlur`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SeCModelLoader`
- `LoadImage`

## 知识

覆盖率 **94%**（66/70）

**有卡**：`GetImageSizeAndCount`、`OnnxDetectionModelLoader`、`ImageFromBatch`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`easy int`、`SeCVideoSegmentation`、`DrawMaskOnImage`、`BlockifyMask`、`ImageResizeKJv2`、`WanVideoAnimateEmbeds`、`INTConstant`、`DrawViTPose`、`RIFE VFI`、`ImageUpscaleWithModelBatched`、`UpscaleModelLoader`、`VHS_VideoCombine`、`PointsEditor`、`VHS_LoadVideo`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`WanVideoTorchCompileSettings`、`PoseAndFaceDetection`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`GrowMaskWithBlur`、`SeCModelLoader`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
