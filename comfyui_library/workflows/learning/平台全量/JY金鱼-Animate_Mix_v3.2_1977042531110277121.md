---
key: 平台全量/JY金鱼-Animate_Mix_v3.2_1977042531110277121.json
name: JY金鱼-Animate_Mix_v3.2_1977042531110277121
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/JY金鱼-Animate_Mix_v3.2_1977042531110277121.json
hash: d1677ef8841769f7
coverage: 0.484375
learned_at: 2026-11-14 00:33:05
nodes: [GetNode, SetNode, PreviewImage, GetNode, GetNode, SetNode, WanVideoClipVisionEncode, WanVideoSetBlockSwap, WanVideoTorchCompileSettings, SetNode, DownloadAndLoadGIMMVFIModel, VHS_VideoCombine, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, Note, easy showAnything, GetNode, GetNode, PrimitiveFloat, Note, VHS_VideoCombine, Note, WanVideoDecode, GetImageSizeAndCount, GetNode, GetNode, PlaySound|pysssss, Note, GetNode, GetNode, ImageResizeKJv2, GetNode, PoseAndFaceDetection, SetNode, SetNode, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, ImageConcatMulti, GetNode, SetNode, CLIPVisionLoader, MarkdownNote, VHS_VideoCombine, GetNode, ImageBlend, GrowMask, BlockifyMask, DrawMaskOnImage, SetNode, SetNode, Note, SAM2Segment, DrawViTPose, GetNode, GetNode, GetNode, EmptyImage, Note, GIMMVFI_interpolate, MarkdownNote, Note, SetNode, SetNode, SetNode, WanVideoAnimateEmbeds, WanVideoVAELoader, WanVideoTextEncodeCached, Note, Fast Groups Bypasser (rgthree), ImageFromBatch, PrimitiveInt, GetNode, GetNode, Note, SeCModelLoader, SetNode, SetNode, CoordinatePlotter, CoordinatePlotter, GetNode, GetNode, WanVideoBlockSwap, Fast Groups Bypasser (rgthree), PreviewImage, SeCVideoSegmentation, GrowMask, BlockifyMask, DrawMaskOnImage, ImageBlend, LayerUtility: PurgeVRAM V2, VHS_VideoCombine, WanVideoSampler, LoadImage, GetNode, GetNode, easy cleanGpuUsed, UpscaleModelLoader, RHBatchImages:, RHBatchImages:, UpscaleModelLoader, ImageUpscaleWithModel, ImageUpscaleWithModel, GetNode, RHBatchImages:, ImageUpscaleWithModel, UpscaleModelLoader, VHS_VideoCombine, ImageUpscaleWithModelBatched, ImageConcatMulti, INTConstant, INTConstant, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelectMulti, PreviewImage, PointsEditor, VHS_VideoCombine, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/JY金鱼-Animate_Mix_v3.2_1977042531110277121.json

> 来源文件 `comfyui_library/workflows/平台全量/JY金鱼-Animate_Mix_v3.2_1977042531110277121.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（128 个）：
- `GetNode`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoClipVisionEncode`
- `WanVideoSetBlockSwap`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `DownloadAndLoadGIMMVFIModel`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `Note`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `PrimitiveFloat`
- `Note`
- `VHS_VideoCombine`
- `Note`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `PlaySound|pysssss`
- `Note`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `PoseAndFaceDetection`
- `SetNode`
- `SetNode`
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `SetNode`
- `CLIPVisionLoader`
- `MarkdownNote`
- `VHS_VideoCombine`
- `GetNode`
- `ImageBlend`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `SetNode`
- `SetNode`
- `Note`
- `SAM2Segment`
- `DrawViTPose`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyImage`
- `Note`
- `GIMMVFI_interpolate`
- `MarkdownNote`
- `Note`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoAnimateEmbeds`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `ImageFromBatch`
- `PrimitiveInt`
- `GetNode`
- `GetNode`
- `Note`
- `SeCModelLoader`
- `SetNode`
- `SetNode`
- `CoordinatePlotter`
- `CoordinatePlotter`
- `GetNode`
- `GetNode`
- `WanVideoBlockSwap`
- `Fast Groups Bypasser (rgthree)`
- `PreviewImage`
- `SeCVideoSegmentation`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `ImageBlend`
- `LayerUtility: PurgeVRAM V2`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `LoadImage`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `UpscaleModelLoader`
- `RHBatchImages:`
- `RHBatchImages:`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `ImageUpscaleWithModel`
- `GetNode`
- `RHBatchImages:`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `ImageUpscaleWithModelBatched`
- `ImageConcatMulti`
- `INTConstant`
- `INTConstant`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelectMulti`
- `PreviewImage`
- `PointsEditor`
- `VHS_VideoCombine`
- `VHS_LoadVideo`

## 知识

覆盖率 **48%**（62/128）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`DownloadAndLoadGIMMVFIModel`、`VHS_VideoCombine`、`WanVideoDecode`、`GetImageSizeAndCount`、`PlaySound|pysssss`、`ImageResizeKJv2`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`ImageConcatMulti`、`CLIPVisionLoader`、`ImageBlend`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`SAM2Segment`、`DrawViTPose`、`EmptyImage`、`GIMMVFI_interpolate`、`WanVideoAnimateEmbeds`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`ImageFromBatch`、`SeCModelLoader`、`CoordinatePlotter`、`WanVideoBlockSwap`、`SeCVideoSegmentation`、`LayerUtility: PurgeVRAM V2`、`WanVideoSampler`、`LoadImage`、`easy cleanGpuUsed`、`UpscaleModelLoader`、`RHBatchImages:`、`ImageUpscaleWithModel`、`ImageUpscaleWithModelBatched`、`INTConstant`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoLoraSelectMulti`、`PointsEditor`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelect、WanVideoLoraSelectMulti
