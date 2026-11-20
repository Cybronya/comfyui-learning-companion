---
key: 平台全量/hgjuwhghweighwighweikghwekhweghwewwegw_2000403006531174402.json
name: hgjuwhghweighwighweikghwekhweghwewwegw_2000403006531174402
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/hgjuwhghweighwighweikghwekhweghwewwegw_2000403006531174402.json
hash: b17b3aaecb1b94ea
coverage: 0.942857
learned_at: 2026-11-14 01:12:27
nodes: [GetImageSizeAndCount, OnnxDetectionModelLoader, ImageFromBatch, CLIPVisionLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, easy int, SeCVideoSegmentation, DrawMaskOnImage, BlockifyMask, ImageResizeKJv2, PrimitiveInt, WanVideoAnimateEmbeds, INTConstant, DrawViTPose, RIFE VFI, ImageUpscaleWithModelBatched, UpscaleModelLoader, RIFE VFI, UpscaleModelLoader, ImageUpscaleWithModelBatched, VHS_VideoCombine, RIFE VFI, ImageUpscaleWithModelBatched, UpscaleModelLoader, RIFE VFI, UpscaleModelLoader, RIFE VFI, ImageUpscaleWithModelBatched, UpscaleModelLoader, RIFE VFI, UpscaleModelLoader, VHS_VideoCombine, RIFE VFI, ImageUpscaleWithModelBatched, UpscaleModelLoader, RIFE VFI, UpscaleModelLoader, VHS_VideoCombine, ImageUpscaleWithModelBatched, ImageUpscaleWithModelBatched, ImageUpscaleWithModelBatched, PointsEditor, VHS_VideoCombine, VHS_VideoCombine, PreviewImage, WanVideoSampler, WanVideoModelLoader, WanVideoVAELoader, WanVideoBlockSwap, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, PoseAndFaceDetection, INTConstant, PreviewImage, VHS_VideoCombine, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, easy showAnything, WanVideoClipVisionEncode, GrowMaskWithBlur, VHS_VideoCombine, SeCModelLoader, VHS_VideoCombine, VHS_LoadVideo, VHS_VideoCombine, WanVideoLoraSelectMulti, LoadImage]
patterns: []
missing: []
---

# 平台全量/hgjuwhghweighwighweikghwekhweghwewwegw_2000403006531174402.json

> 来源文件 `comfyui_library/workflows/平台全量/hgjuwhghweighwighweikghwekhweghwewwegw_2000403006531174402.json`

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
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PreviewImage`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
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
- `SeCModelLoader`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoLoraSelectMulti`
- `LoadImage`

## 知识

覆盖率 **94%**（66/70）

**有卡**：`GetImageSizeAndCount`、`OnnxDetectionModelLoader`、`ImageFromBatch`、`CLIPVisionLoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`easy int`、`SeCVideoSegmentation`、`DrawMaskOnImage`、`BlockifyMask`、`ImageResizeKJv2`、`WanVideoAnimateEmbeds`、`INTConstant`、`DrawViTPose`、`RIFE VFI`、`ImageUpscaleWithModelBatched`、`UpscaleModelLoader`、`VHS_VideoCombine`、`PointsEditor`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoTextEncodeCached`、`WanVideoTorchCompileSettings`、`PoseAndFaceDetection`、`WanVideoDecode`、`WanVideoClipVisionEncode`、`GrowMaskWithBlur`、`SeCModelLoader`、`VHS_LoadVideo`、`WanVideoLoraSelectMulti`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
