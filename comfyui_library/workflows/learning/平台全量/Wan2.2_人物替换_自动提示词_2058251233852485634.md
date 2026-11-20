---
key: 平台全量/Wan2.2_人物替换_自动提示词_2058251233852485634.json
name: Wan2.2_人物替换_自动提示词_2058251233852485634
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2_人物替换_自动提示词_2058251233852485634.json
hash: b6bbd6311f3ab5ad
coverage: 0.833333
learned_at: 2026-11-14 01:06:16
nodes: [OnnxDetectionModelLoader, WanVideoVAELoader, CLIPVisionLoader, GrowMask, BlockifyMask, SeCModelLoader, SeCVideoSegmentation, ImageBlend, WanVideoAnimateEmbeds, Evaluate Integers, GetImageSizeAndCount, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, WanVideoTorchCompileSettings, WanVideoLoraSelectMulti, DrawViTPose, ImageConcatMulti, ImageConcatMulti, PoseAndFaceDetection, PreviewImage, easy int, VHS_VideoCombine, Note, Note, Note, Evaluate Integers, easy showAnything, easy int, ImageFromBatch, LayerUtility: ImageMaskScaleAsV2, VHS_VideoCombine, ImageBatch, PrimitiveStringMultiline, VHS_VideoInfoLoaded, Note, ClothesSegment, WanVideoTextEncodeCached, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSampler, WanVideoClipVisionEncode, easy int, llama_cpp_parameters, Label (rgthree), VHS_VideoCombine, easy float, easy int, Note, VHS_LoadVideo, LoadImage, WanVideoDecode, DrawMaskOnImage, llama_cpp_model_loader, WanVideoContextOptions, WanVideoBlockSwap, WanVideoModelLoader, llama_cpp_instruct_adv, easy int, easy int, Note]
patterns: []
missing: []
---

# 平台全量/Wan2.2_人物替换_自动提示词_2058251233852485634.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2_人物替换_自动提示词_2058251233852485634.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（60 个）：
- `OnnxDetectionModelLoader`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `GrowMask`
- `BlockifyMask`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `ImageBlend`
- `WanVideoAnimateEmbeds`
- `Evaluate Integers`
- `GetImageSizeAndCount`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelectMulti`
- `DrawViTPose`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `PoseAndFaceDetection`
- `PreviewImage`
- `easy int`
- `VHS_VideoCombine`
- `Note`
- `Note`
- `Note`
- `Evaluate Integers`
- `easy showAnything`
- `easy int`
- `ImageFromBatch`
- `LayerUtility: ImageMaskScaleAsV2`
- `VHS_VideoCombine`
- `ImageBatch`
- `PrimitiveStringMultiline`
- `VHS_VideoInfoLoaded`
- `Note`
- `ClothesSegment`
- `WanVideoTextEncodeCached`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `WanVideoClipVisionEncode`
- `easy int`
- `llama_cpp_parameters`
- `Label (rgthree)`
- `VHS_VideoCombine`
- `easy float`
- `easy int`
- `Note`
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoDecode`
- `DrawMaskOnImage`
- `llama_cpp_model_loader`
- `WanVideoContextOptions`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `llama_cpp_instruct_adv`
- `easy int`
- `easy int`
- `Note`

## 知识

覆盖率 **83%**（50/60）

**有卡**：`OnnxDetectionModelLoader`、`WanVideoVAELoader`、`CLIPVisionLoader`、`GrowMask`、`BlockifyMask`、`SeCModelLoader`、`SeCVideoSegmentation`、`ImageBlend`、`WanVideoAnimateEmbeds`、`Evaluate Integers`、`GetImageSizeAndCount`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoTorchCompileSettings`、`WanVideoLoraSelectMulti`、`DrawViTPose`、`ImageConcatMulti`、`PoseAndFaceDetection`、`easy int`、`VHS_VideoCombine`、`ImageFromBatch`、`LayerUtility: ImageMaskScaleAsV2`、`ImageBatch`、`VHS_VideoInfoLoaded`、`ClothesSegment`、`WanVideoTextEncodeCached`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSampler`、`WanVideoClipVisionEncode`、`llama_cpp_parameters`、`Label (rgthree)`、`easy float`、`VHS_LoadVideo`、`LoadImage`、`WanVideoDecode`、`DrawMaskOnImage`、`llama_cpp_model_loader`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`llama_cpp_instruct_adv`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
