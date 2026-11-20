---
key: 平台全量/电商最强视频换人物 wan2.2 secC_1983712131239616514.json
name: 电商最强视频换人物 wan2.2 secC_1983712131239616514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/电商最强视频换人物 wan2.2 secC_1983712131239616514.json
hash: 22ed2d129bcf8ed2
coverage: 0.525773
learned_at: 2026-11-14 02:24:22
nodes: [Anything Everywhere3, WanVideoVAELoader, GetNode, Seed Everywhere, SetNode, WanVideoClipVisionEncode, CLIPVisionLoader, WanVideoDecode, WanVideoLoraSelectMulti, GetNode, GetNode, PixelPerfectResolution, ImageCropByMaskAndResize, DWPreprocessor, ImageResize+, WanVideoAnimateEmbeds, WanVideoSampler, FaceMaskFromPoseKeypoints, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, LayerUtility: PurgeVRAM V2, WanVideoModelLoader, GetNode, GetNode, SetNode, SetNode, GetNode, VHS_VideoInfo, SetNode, SeCModelLoader, GetNode, CoordinatePlotter, PreviewImage, PreviewImage, CoordinatePlotter, GetNode, PrimitiveInt, SetNode, easy imageRemBg, SetNode, GetNode, SetNode, SetNode, LayerUtility: PurgeVRAM V2, SetNode, ImageFromBatch, PreviewImage, PreviewImage, PreviewImage, Reroute, PreviewImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, MathExpression|pysssss, WanVideoTextEncodeCached, easy showAnything, DrawMaskOnImage, SetNode, SeCVideoSegmentation, GrowMaskWithBlur, BlockifyMask, WanVideoTorchCompileSettings, WanVideoBlockSwap, MathExpression|pysssss, ImageResizeKJv2, Int, Int, VHS_VideoCombine, VHS_VideoCombine, easy cleanGpuUsed, PrimitiveInt, LoadImage, Text Multiline, VHS_LoadVideo, PointsEditor, Note, Note, Note]
patterns: []
missing: []
---

# 平台全量/电商最强视频换人物 wan2.2 secC_1983712131239616514.json

> 来源文件 `comfyui_library/workflows/平台全量/电商最强视频换人物 wan2.2 secC_1983712131239616514.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（97 个）：
- `Anything Everywhere3`
- `WanVideoVAELoader`
- `GetNode`
- `Seed Everywhere`
- `SetNode`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `GetNode`
- `PixelPerfectResolution`
- `ImageCropByMaskAndResize`
- `DWPreprocessor`
- `ImageResize+`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `FaceMaskFromPoseKeypoints`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoModelLoader`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoInfo`
- `SetNode`
- `SeCModelLoader`
- `GetNode`
- `CoordinatePlotter`
- `PreviewImage`
- `PreviewImage`
- `CoordinatePlotter`
- `GetNode`
- `PrimitiveInt`
- `SetNode`
- `easy imageRemBg`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `LayerUtility: PurgeVRAM V2`
- `SetNode`
- `ImageFromBatch`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `Reroute`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `MathExpression|pysssss`
- `WanVideoTextEncodeCached`
- `easy showAnything`
- `DrawMaskOnImage`
- `SetNode`
- `SeCVideoSegmentation`
- `GrowMaskWithBlur`
- `BlockifyMask`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `MathExpression|pysssss`
- `ImageResizeKJv2`
- `Int`
- `Int`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `PrimitiveInt`
- `LoadImage`
- `Text Multiline`
- `VHS_LoadVideo`
- `PointsEditor`
- `Note`
- `Note`
- `Note`

## 知识

覆盖率 **53%**（51/97）

**有卡**：`WanVideoVAELoader`、`Seed Everywhere`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoDecode`、`WanVideoLoraSelectMulti`、`PixelPerfectResolution`、`ImageCropByMaskAndResize`、`DWPreprocessor`、`ImageResize+`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`FaceMaskFromPoseKeypoints`、`LayerUtility: PurgeVRAM V2`、`WanVideoModelLoader`、`VHS_VideoInfo`、`SeCModelLoader`、`CoordinatePlotter`、`easy imageRemBg`、`ImageFromBatch`、`MathExpression|pysssss`、`WanVideoTextEncodeCached`、`DrawMaskOnImage`、`SeCVideoSegmentation`、`GrowMaskWithBlur`、`BlockifyMask`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`ImageResizeKJv2`、`Int`、`VHS_VideoCombine`、`easy cleanGpuUsed`、`LoadImage`、`Text Multiline`、`VHS_LoadVideo`、`PointsEditor`

**用到的条目**：LoadImage、Seed Everywhere、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti
