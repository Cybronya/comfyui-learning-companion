---
key: 平台全量/Comfyui节点系列70-SAM3.1图像_视频语义分离节点组_2068957311976169474.json
name: Comfyui节点系列70-SAM3.1图像_视频语义分离节点组_2068957311976169474
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Comfyui节点系列70-SAM3.1图像_视频语义分离节点组_2068957311976169474.json
hash: d55730b79cb6a3f2
coverage: 0.873134
learned_at: 2026-11-14 00:22:43
nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, ReferenceLatent, ReferenceLatent, UNETLoader, VAEDecode, SaveImage, VHS_VideoCombine, CheckpointLoaderSimple, Note, CLIPTextEncode, Note, SAM3_TrackToMask, VHS_VideoCombine, VHS_VideoCombine, ImageAndMaskPreview, ImageAndMaskPreview, VHS_LoadVideo, Image Comparer (rgthree), KSampler, VAEEncode, CheckpointLoaderSimple, DownloadAndLoadSAM2Model, VHS_LoadVideo, Sam2Segmentation, Bjornulf_ShowFloat, Label (rgthree), PrimitiveStringMultiline, VAELoader, Seed (rgthree), ImageAndMaskPreview, Label (rgthree), SAM3_Detect, SAM3_Detect, MaskToImage, PreviewImage, ImageAndMaskPreview, MaskToImage, PreviewImage, ImageAndMaskPreview, SAM3_Detect, MaskToImage, PreviewImage, ImageAndMaskPreview, SAM3_Detect, CheckpointLoaderSimple, LoadImage, Note, CheckpointLoaderSimple, Note, VHS_VideoInfo, Note, SAM3_Detect, easy showAnything, ImageAndMaskPreview, SAM3_TrackPreview, VHS_VideoCombine, Note, Note, VHS_VideoCombine, VHS_LoadVideo, VHS_VideoInfo, ImageAndMaskPreview, VHS_VideoInfo, easy showAnything, ImageAndMaskPreview, VHS_VideoCombine, SAM3_TrackToMask, CLIPTextEncode, CheckpointLoaderSimple, LoadImage, CheckpointLoaderSimple, MaskPreview, SAM3_Detect, ImageAndMaskPreview, LoadImage, CLIPTextEncode, CLIPTextEncode, ImageAndMaskPreview, SAM3_Detect, CLIPTextEncode, SAM3_TrackPreview, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, SAM3_Detect, ImageAndMaskPreview, INPAINT_ExpandMask, InpaintModelConditioning, LoadImage, CLIPTextEncode, SAM3_TrackPreview, SAM3_VideoTrack, SAM3_TrackToMask, VHS_VideoInfo, MaskToImage, MaskToImage, ImageAndMaskPreview, VHS_VideoCombine, CLIPTextEncode, SAM3_VideoTrack, VHS_LoadVideo, CheckpointLoaderSimple, Note, CLIPTextEncode, MaskToImage, SAM3_TrackToMask, ImageAndMaskPreview, SAM3_TrackPreview, SAM3_VideoTrack, PointsEditor, VHS_VideoCombine, SAM3_VideoTrack, SAM3_TrackToMask, ImageAndMaskPreview, VHS_VideoCombine, SAM3_TrackToMask, SAM3_TrackToMask, SAM3_TrackToMask, Note, SAM3_VideoTrack, SAM3_VideoTrack, SAM3_TrackPreview, VHS_VideoCombine, VHS_VideoCombine, SCAIL2ColoredMask, Label (rgthree), Label (rgthree), MaskToImage, PreviewImage, SaveImage, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "sam3.1_multiplex_fp16.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 583731479550009, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Comfyui节点系列70-SAM3.1图像_视频语义分离节点组_2068957311976169474.json

> 来源文件 `comfyui_library/workflows/平台全量/Comfyui节点系列70-SAM3.1图像_视频语义分离节点组_2068957311976169474.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（134 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `ReferenceLatent`
- `ReferenceLatent`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `VHS_VideoCombine`
- `CheckpointLoaderSimple` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `Note`
- `SAM3_TrackToMask`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageAndMaskPreview`
- `ImageAndMaskPreview`
- `VHS_LoadVideo`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `DownloadAndLoadSAM2Model`
- `VHS_LoadVideo`
- `Sam2Segmentation`
- `Bjornulf_ShowFloat`
- `Label (rgthree)`
- `PrimitiveStringMultiline`
- `VAELoader`
- `Seed (rgthree)`
- `ImageAndMaskPreview`
- `Label (rgthree)`
- `SAM3_Detect`
- `SAM3_Detect`
- `MaskToImage`
- `PreviewImage`
- `ImageAndMaskPreview`
- `MaskToImage`
- `PreviewImage`
- `ImageAndMaskPreview`
- `SAM3_Detect`
- `MaskToImage`
- `PreviewImage`
- `ImageAndMaskPreview`
- `SAM3_Detect`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `Note`
- `CheckpointLoaderSimple` ★核心
- `Note`
- `VHS_VideoInfo`
- `Note`
- `SAM3_Detect`
- `easy showAnything`
- `ImageAndMaskPreview`
- `SAM3_TrackPreview`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `VHS_VideoInfo`
- `ImageAndMaskPreview`
- `VHS_VideoInfo`
- `easy showAnything`
- `ImageAndMaskPreview`
- `VHS_VideoCombine`
- `SAM3_TrackToMask`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `MaskPreview`
- `SAM3_Detect`
- `ImageAndMaskPreview`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageAndMaskPreview`
- `SAM3_Detect`
- `CLIPTextEncode` ★核心
- `SAM3_TrackPreview`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SAM3_Detect`
- `ImageAndMaskPreview`
- `INPAINT_ExpandMask`
- `InpaintModelConditioning`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `SAM3_TrackPreview`
- `SAM3_VideoTrack`
- `SAM3_TrackToMask`
- `VHS_VideoInfo`
- `MaskToImage`
- `MaskToImage`
- `ImageAndMaskPreview`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `SAM3_VideoTrack`
- `VHS_LoadVideo`
- `CheckpointLoaderSimple` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `MaskToImage`
- `SAM3_TrackToMask`
- `ImageAndMaskPreview`
- `SAM3_TrackPreview`
- `SAM3_VideoTrack`
- `PointsEditor`
- `VHS_VideoCombine`
- `SAM3_VideoTrack`
- `SAM3_TrackToMask`
- `ImageAndMaskPreview`
- `VHS_VideoCombine`
- `SAM3_TrackToMask`
- `SAM3_TrackToMask`
- `SAM3_TrackToMask`
- `Note`
- `SAM3_VideoTrack`
- `SAM3_VideoTrack`
- `SAM3_TrackPreview`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SCAIL2ColoredMask`
- `Label (rgthree)`
- `Label (rgthree)`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`
- `seed` = `583731479550009`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（117/134）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`ConditioningZeroOut`、`ReferenceLatent`、`UNETLoader`、`VAEDecode`、`SaveImage`、`VHS_VideoCombine`、`CheckpointLoaderSimple`、`SAM3_TrackToMask`、`ImageAndMaskPreview`、`VHS_LoadVideo`、`KSampler`、`VAEEncode`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`Bjornulf_ShowFloat`、`Label (rgthree)`、`VAELoader`、`Seed (rgthree)`、`SAM3_Detect`、`MaskToImage`、`LoadImage`、`VHS_VideoInfo`、`SAM3_TrackPreview`、`MaskPreview`、`LayerUtility: ImageScaleByAspectRatio V2`、`INPAINT_ExpandMask`、`InpaintModelConditioning`、`SAM3_VideoTrack`、`PointsEditor`、`SCAIL2ColoredMask`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
