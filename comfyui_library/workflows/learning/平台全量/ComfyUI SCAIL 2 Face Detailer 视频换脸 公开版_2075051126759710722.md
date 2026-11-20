---
key: 平台全量/ComfyUI SCAIL 2 Face Detailer 视频换脸 公开版_2075051126759710722.json
name: ComfyUI SCAIL 2 Face Detailer 视频换脸 公开版_2075051126759710722
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/ComfyUI SCAIL 2 Face Detailer 视频换脸 公开版_2075051126759710722.json
hash: f6019e2fd413f1a6
coverage: 0.590909
learned_at: 2026-11-14 00:22:18
nodes: [CLIPLoader, CLIPVisionLoader, SetNode, SetNode, SetNode, Label (rgthree), Label (rgthree), Label (rgthree), SetNode, DiffusionModelLoaderKJ, LoraLoaderModelOnly, VAELoader, Note, CheckpointLoaderSimple, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, KSamplerSelect, BasicScheduler, GetNode, GetNode, ModelSamplingSD3, Note, Note, Label (rgthree), SetNode, ImageResizeKJv2, PreviewImage, ImageResizeKJv2, GetImageSize, GetNode, VHS_VideoCombine, GetNode, VHS_VideoCombine, DownloadAndLoadGIMMVFIModel, Note, GIMMVFI_interpolate, VHS_VideoInfo, easy ifElse, SetNode, GetNode, SimpleMath+, easy ifElse, SCAIL2FaceCompositeBack, VHS_VideoCombine, PrimitiveBoolean, SimpleMath+, ImageResizeKJv2, GetNode, SCAIL2ScheduledLongVideoWithSAM, PrimitiveInt, Label (rgthree), SCAIL2SegmentPlanBuilder, VHS_LoadVideo, ImageResizeKJv2, SCAIL2HeadTrackCrop, SCAIL2AlignReferenceFaceToCrop, LoadImage, SetNode, CLIPTextEncode, VHS_VideoCombine, LoadImage, SaveImage]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 平台全量/ComfyUI SCAIL 2 Face Detailer 视频换脸 公开版_2075051126759710722.json

> 来源文件 `comfyui_library/workflows/平台全量/ComfyUI SCAIL 2 Face Detailer 视频换脸 公开版_2075051126759710722.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（66 个）：
- `CLIPLoader`
- `CLIPVisionLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `SetNode`
- `DiffusionModelLoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `Note`
- `CheckpointLoaderSimple` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `GetNode`
- `GetNode`
- `ModelSamplingSD3`
- `Note`
- `Note`
- `Label (rgthree)`
- `SetNode`
- `ImageResizeKJv2`
- `PreviewImage`
- `ImageResizeKJv2`
- `GetImageSize`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `VHS_VideoCombine`
- `DownloadAndLoadGIMMVFIModel`
- `Note`
- `GIMMVFI_interpolate`
- `VHS_VideoInfo`
- `easy ifElse`
- `SetNode`
- `GetNode`
- `SimpleMath+`
- `easy ifElse`
- `SCAIL2FaceCompositeBack`
- `VHS_VideoCombine`
- `PrimitiveBoolean`
- `SimpleMath+`
- `ImageResizeKJv2`
- `GetNode`
- `SCAIL2ScheduledLongVideoWithSAM`
- `PrimitiveInt`
- `Label (rgthree)`
- `SCAIL2SegmentPlanBuilder`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `SCAIL2HeadTrackCrop`
- `SCAIL2AlignReferenceFaceToCrop`
- `LoadImage`
- `SetNode`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `SaveImage`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **59%**（39/66）

**有卡**：`CLIPLoader`、`CLIPVisionLoader`、`Label (rgthree)`、`DiffusionModelLoaderKJ`、`LoraLoaderModelOnly`、`VAELoader`、`CheckpointLoaderSimple`、`KSamplerSelect`、`BasicScheduler`、`ModelSamplingSD3`、`ImageResizeKJv2`、`GetImageSize`、`VHS_VideoCombine`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`VHS_VideoInfo`、`SimpleMath+`、`SCAIL2FaceCompositeBack`、`PrimitiveBoolean`、`SCAIL2ScheduledLongVideoWithSAM`、`SCAIL2SegmentPlanBuilder`、`VHS_LoadVideo`、`SCAIL2HeadTrackCrop`、`SCAIL2AlignReferenceFaceToCrop`、`LoadImage`、`CLIPTextEncode`、`SaveImage`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPLoader、CLIPTextEncode、LoadImage、KSamplerSelect、CLIPVisionLoader
