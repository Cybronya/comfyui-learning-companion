---
key: 视频生成/图生视频/Scail2长视频动作迁移(长视频低显存版) Motion Transfer (Long‑Video_2101561671167860738.json
name: Scail2长视频动作迁移(长视频低显存版) Motion Transfer (Long‑Video_2101561671167860738
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Scail2长视频动作迁移(长视频低显存版) Motion Transfer (Long‑Video_2101561671167860738.json
hash: 680cfefb6545834d
coverage: 0.456376
learned_at: 2026-10-17 02:14:35
nodes: [SAM3_VideoTrack, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SAM3_TrackToMask, EmptyImage, Reroute, GetNode, GetNode, GetImageRangeFromBatch, SAM3_VideoTrack, GetImageRangeFromBatch, SetNode, ResizeImageMaskNode, Reroute, GetNode, GetImageRangeFromBatch, GetNode, CLIPVisionLoader, VAELoader, SetNode, SetNode, SetNode, CLIPTextEncode, CLIPTextEncode, SetNode, SetNode, SetNode, ModelSamplingSD3, SetNode, BasicScheduler, SetNode, KSamplerSelect, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Reroute, Reroute, WanSCAILToVideo, PreviewAny, GetNode, GetNode, GetImageRangeFromBatch, GetNode, Reroute, GetNode, ImageConcatMulti, ImageConcatMulti, CLIPTextEncode, GetNode, SCAIL2ColoredMask, SetNode, SetNode, ImageCompositeMasked, SetNode, GetNode, Reroute, GetNode, GetNode, GetNode, ComfyMathExpression, PreviewAny, TensorLoopOpen, SamplerCustom, VAEDecode, GetNode, GetImageRangeFromBatch, ColorTransfer, BatchImagesNode, GetImageSize, GetNode, GetImageSize, ComfyMathExpression, TensorLoopClose, Reroute, GetNode, GetImageSize, ImageConcatMulti, GetNode, CheckpointLoaderSimple, WanSCAILToVideo, PreviewImage, PrimitiveInt, GetNode, ImageConcatMulti, SetNode, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, WanSCAILToVideo, CLIPLoader, VAEDecode, PrimitiveInt, llama_cpp_parameters, PrimitiveInt, llama_cpp_instruct_adv, VAEDecode, ColorTransfer, BatchImagesNode, SamplerCustom, SamplerCustom, VideoInfoLoaded, JWInteger, SetNode, ImageResizeKJv2, ImageResizeKJv2, CLIPVisionEncode, PrimitiveInt, SetNode, CR Text, UNETLoader, VHS_VideoCombine, VHS_VideoCombine, GetImageRangeFromBatch, Label (rgthree), Label (rgthree), VHS_VideoCombine, VHS_VideoCombine, LoadImage, VHS_VideoCombine, LoraLoaderModelOnly, VHS_LoadVideo]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1-multiplex-fp16.safetensors"}
---

# 视频生成/图生视频/Scail2长视频动作迁移(长视频低显存版) Motion Transfer (Long‑Video_2101561671167860738.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Scail2长视频动作迁移(长视频低显存版) Motion Transfer (Long‑Video_2101561671167860738.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（149 个）：
- `SAM3_VideoTrack`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SAM3_TrackToMask`
- `EmptyImage`
- `Reroute`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `SAM3_VideoTrack`
- `GetImageRangeFromBatch`
- `SetNode`
- `ResizeImageMaskNode`
- `Reroute`
- `GetNode`
- `GetImageRangeFromBatch`
- `GetNode`
- `CLIPVisionLoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `ModelSamplingSD3`
- `SetNode`
- `BasicScheduler`
- `SetNode`
- `KSamplerSelect` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `Reroute`
- `WanSCAILToVideo`
- `PreviewAny`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `GetNode`
- `Reroute`
- `GetNode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SCAIL2ColoredMask`
- `SetNode`
- `SetNode`
- `ImageCompositeMasked`
- `SetNode`
- `GetNode`
- `Reroute`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `PreviewAny`
- `TensorLoopOpen`
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `GetImageRangeFromBatch`
- `ColorTransfer`
- `BatchImagesNode`
- `GetImageSize`
- `GetNode`
- `GetImageSize`
- `ComfyMathExpression`
- `TensorLoopClose`
- `Reroute`
- `GetNode`
- `GetImageSize`
- `ImageConcatMulti`
- `GetNode`
- `CheckpointLoaderSimple` ★核心
- `WanSCAILToVideo`
- `PreviewImage`
- `PrimitiveInt`
- `GetNode`
- `ImageConcatMulti`
- `SetNode`
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `WanSCAILToVideo`
- `CLIPLoader`
- `VAEDecode` ★核心
- `PrimitiveInt`
- `llama_cpp_parameters`
- `PrimitiveInt`
- `llama_cpp_instruct_adv`
- `VAEDecode` ★核心
- `ColorTransfer`
- `BatchImagesNode`
- `SamplerCustom` ★核心
- `SamplerCustom` ★核心
- `VideoInfoLoaded`
- `JWInteger`
- `SetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `CLIPVisionEncode`
- `PrimitiveInt`
- `SetNode`
- `CR Text`
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `GetImageRangeFromBatch`
- `Label (rgthree)`
- `Label (rgthree)`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `VHS_LoadVideo`

## 关键参数

- `checkpoint` = `sam3.1-multiplex-fp16.safetensors`

## 知识

覆盖率 **46%**（68/149）

**有卡**：`SAM3_VideoTrack`、`SAM3_TrackToMask`、`EmptyImage`、`GetImageRangeFromBatch`、`ResizeImageMaskNode`、`CLIPVisionLoader`、`VAELoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`BasicScheduler`、`KSamplerSelect`、`WanSCAILToVideo`、`ImageConcatMulti`、`SCAIL2ColoredMask`、`ImageCompositeMasked`、`ComfyMathExpression`、`TensorLoopOpen`、`SamplerCustom`、`VAEDecode`、`ColorTransfer`、`BatchImagesNode`、`GetImageSize`、`TensorLoopClose`、`CheckpointLoaderSimple`、`GIMMVFI_interpolate`、`DownloadAndLoadGIMMVFIModel`、`CLIPLoader`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`VideoInfoLoaded`、`JWInteger`、`ImageResizeKJv2`、`CLIPVisionEncode`、`CR Text`、`UNETLoader`、`VHS_VideoCombine`、`Label (rgthree)`、`LoadImage`、`LoraLoaderModelOnly`、`VHS_LoadVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage
