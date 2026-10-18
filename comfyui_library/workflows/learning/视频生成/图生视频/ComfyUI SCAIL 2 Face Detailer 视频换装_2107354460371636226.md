---
key: 视频生成/图生视频/ComfyUI SCAIL 2 Face Detailer 视频换装_2107354460371636226.json
name: ComfyUI SCAIL 2 Face Detailer 视频换装_2107354460371636226
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/ComfyUI SCAIL 2 Face Detailer 视频换装_2107354460371636226.json
hash: 242c79023b11d641
coverage: 0.516129
learned_at: 2026-10-17 22:17:18
nodes: [CLIPLoader, CLIPVisionLoader, SetNode, SetNode, SetNode, SetNode, DiffusionModelLoaderKJ, LoraLoaderModelOnly, VAELoader, Note, CheckpointLoaderSimple, SetNode, SetNode, VHS_VideoCombine, GetNode, GetNode, VHS_VideoCombine, GetNode, BasicScheduler, GetNode, GetNode, GetNode, GetNode, KSamplerSelect, GetNode, ModelSamplingSD3, VHS_VideoCombine, ImageConcatMulti, VHS_VideoCombine, CLIPTextEncode, SetNode, DownloadAndLoadGIMMVFIModel, SimpleMath+, GetNode, Note, SetNode, easy ifElse, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageConcatMulti, VHS_VideoCombine, easy ifElse, VHS_VideoCombine, GetNode, GetImageSize, PreviewImage, ImageResizeKJv2, SCAIL2FaceCompositeBack, BasicScheduler, GetNode, GetNode, GetNode, GetNode, KSamplerSelect, GetNode, ImageResizeKJv2, CLIPTextEncode, ImageResizeKJv2, GetNode, SCAIL2SegmentPlanBuilder, SetNode, ComfySwitchNode, SimpleMath+, GetNode, ModelSamplingSD3, GIMMVFI_interpolate, VHS_VideoCombine, GetNode, VHS_VideoCombine, SetNode, Note, PrimitiveStringMultiline, VHS_LoadVideo, Note, VHS_VideoInfo, SCAIL2ScheduledLongVideoWithSAM, PrimitiveBoolean, SCAIL2HeadTrackCrop, SCAIL2AlignReferenceFaceToCrop, SCAIL2ScheduledLongVideoWithSAM, PrimitiveInt, SCAIL2SegmentPlanBuilder, SimpleMath+, Fast Groups Bypasser (rgthree), CS-MultiImageLoader, ImageResizeKJv2, LoadImage, SaveImage, Label (rgthree)]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 视频生成/图生视频/ComfyUI SCAIL 2 Face Detailer 视频换装_2107354460371636226.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/ComfyUI SCAIL 2 Face Detailer 视频换装_2107354460371636226.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（93 个）：
- `CLIPLoader`
- `CLIPVisionLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `DiffusionModelLoaderKJ`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `Note`
- `CheckpointLoaderSimple` ★核心
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `BasicScheduler`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `SetNode`
- `DownloadAndLoadGIMMVFIModel`
- `SimpleMath+`
- `GetNode`
- `Note`
- `SetNode`
- `easy ifElse`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `easy ifElse`
- `VHS_VideoCombine`
- `GetNode`
- `GetImageSize`
- `PreviewImage`
- `ImageResizeKJv2`
- `SCAIL2FaceCompositeBack`
- `BasicScheduler`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `ImageResizeKJv2`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `GetNode`
- `SCAIL2SegmentPlanBuilder`
- `SetNode`
- `ComfySwitchNode`
- `SimpleMath+`
- `GetNode`
- `ModelSamplingSD3`
- `GIMMVFI_interpolate`
- `VHS_VideoCombine`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `Note`
- `PrimitiveStringMultiline`
- `VHS_LoadVideo`
- `Note`
- `VHS_VideoInfo`
- `SCAIL2ScheduledLongVideoWithSAM`
- `PrimitiveBoolean`
- `SCAIL2HeadTrackCrop`
- `SCAIL2AlignReferenceFaceToCrop`
- `SCAIL2ScheduledLongVideoWithSAM`
- `PrimitiveInt`
- `SCAIL2SegmentPlanBuilder`
- `SimpleMath+`
- `Fast Groups Bypasser (rgthree)`
- `CS-MultiImageLoader`
- `ImageResizeKJv2`
- `LoadImage`
- `SaveImage`
- `Label (rgthree)`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **52%**（48/93）

**有卡**：`CLIPLoader`、`CLIPVisionLoader`、`DiffusionModelLoaderKJ`、`LoraLoaderModelOnly`、`VAELoader`、`CheckpointLoaderSimple`、`VHS_VideoCombine`、`BasicScheduler`、`KSamplerSelect`、`ModelSamplingSD3`、`ImageConcatMulti`、`CLIPTextEncode`、`DownloadAndLoadGIMMVFIModel`、`SimpleMath+`、`GetImageSize`、`ImageResizeKJv2`、`SCAIL2FaceCompositeBack`、`SCAIL2SegmentPlanBuilder`、`GIMMVFI_interpolate`、`VHS_LoadVideo`、`VHS_VideoInfo`、`SCAIL2ScheduledLongVideoWithSAM`、`PrimitiveBoolean`、`SCAIL2HeadTrackCrop`、`SCAIL2AlignReferenceFaceToCrop`、`CS-MultiImageLoader`、`LoadImage`、`SaveImage`、`Label (rgthree)`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect、CLIPVisionLoader
