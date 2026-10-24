---
key: 图片生成/图生图/模特生成_Flux_2.0_1954114817915273218.json
name: 模特生成_Flux_2.0_1954114817915273218
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/模特生成_Flux_2.0_1954114817915273218.json
hash: ef41f74be574282d
coverage: 0.919643
learned_at: 2026-10-23 13:10:36
nodes: [DualCLIPLoader, VAELoader, Anything Everywhere3, ModelSamplingFlux, UNETLoader, CLIPTextEncode, CLIPTextEncode, UNETLoader, CLIPLoader, LoraLoaderModelOnly, VAEEncode, TTP_Tile_image_size, VAELoader, easy imageBatchToImageList, ImageScale, easy imageSize, InpaintModelConditioning, ReduxAdvanced, CLIPVisionLoader, StyleModelLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, ConditioningZeroOut, FluxGuidance, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, KSamplerSelect, BasicGuider, SamplerCustomAdvanced, VAEDecode, RH_Translator, JanusModelLoader, JanusImageUnderstanding, JanusModelLoader, Text Concatenate, SDXLPromptStyler, CR Text, JanusImageUnderstanding, easy imageSize, LayerUtility: ColorImage, LayerUtility: ColorPicker, ImageComposite+, LoadImage, RandomNoise, Anything Everywhere, KSampler, easy cleanGpuUsed, VAEDecode, FluxGuidance, BasicScheduler, easy cleanGpuUsed, LoraLoaderModelOnly, InpaintResize, InpaintCrop, easy makeImageForICLora, CLIPTextEncode, PreviewImage, CLIPTextEncode, Mask Fill Holes, LayerUtility: ImageScaleByAspectRatio V2, UpscaleModelLoader, KSampler, TTP_Image_Tile_Batch, VAEDecode, ImageListToImageBatch, TTP_Image_Assy, SaveImage, SaveImage, SaveImage, SaveImage, Int, Image Comparer (rgthree), Image Comparer (rgthree), LoadImage, Image Comparer (rgthree), LoadImage, CheckpointLoaderSimple, LoraLoaderModelOnly, ControlNetLoader, UltralyticsDetectorProvider, UltralyticsDetectorProvider, ControlNetApply, SAMLoader, FaceDetailer, SaveImage, CheckpointLoaderSimple, CLIPTextEncode, ControlNetLoader, ControlNetApply, MaskToSEGS, ResizeLongestToNode, ResizeLongestToNode, GrowMaskWithBlur, easy imageInsetCrop, InpaintStitch, Fast Groups Bypasser (rgthree), ChinesePrompt_Mix, PreviewImage, DetailerForEachDebug, easy cleanGpuUsed, CLIPTextEncode, easy cleanGpuUsed, ImageCompositeMasked, PreviewImage, LayerMask: MaskGrow, ImageScaleToTotalPixels, ImageUpscaleWithModel, ModelSamplingSD3, easy cleanGpuUsed, ResizeLongestToNode]
patterns: [text_to_image, image_to_image, controlnet]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "realDream_15SD15.safetensors", "controlnet_strength": 0.5300000000000001, "denoise": 0.10000000000000002, "height": 1024, "sampler_name": "heun", "scheduler": "beta", "seed": 177932711479417, "steps": 10, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/模特生成_Flux_2.0_1954114817915273218.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/模特生成_Flux_2.0_1954114817915273218.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（112 个）：
- `DualCLIPLoader`
- `VAELoader`
- `Anything Everywhere3`
- `ModelSamplingFlux`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `VAEEncode` ★核心
- `TTP_Tile_image_size`
- `VAELoader`
- `easy imageBatchToImageList`
- `ImageScale`
- `easy imageSize`
- `InpaintModelConditioning`
- `ReduxAdvanced`
- `CLIPVisionLoader`
- `StyleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `RH_Translator`
- `JanusModelLoader`
- `JanusImageUnderstanding`
- `JanusModelLoader`
- `Text Concatenate`
- `SDXLPromptStyler`
- `CR Text`
- `JanusImageUnderstanding`
- `easy imageSize`
- `LayerUtility: ColorImage`
- `LayerUtility: ColorPicker`
- `ImageComposite+`
- `LoadImage`
- `RandomNoise`
- `Anything Everywhere`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `FluxGuidance`
- `BasicScheduler`
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly` ★核心
- `InpaintResize`
- `InpaintCrop`
- `easy makeImageForICLora`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `Mask Fill Holes`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UpscaleModelLoader`
- `KSampler` ★核心
- `TTP_Image_Tile_Batch`
- `VAEDecode` ★核心
- `ImageListToImageBatch`
- `TTP_Image_Assy`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `Int`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `LoadImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `ControlNetLoader`
- `UltralyticsDetectorProvider`
- `UltralyticsDetectorProvider`
- `ControlNetApply` ★核心
- `SAMLoader`
- `FaceDetailer`
- `SaveImage`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `ControlNetLoader`
- `ControlNetApply` ★核心
- `MaskToSEGS`
- `ResizeLongestToNode`
- `ResizeLongestToNode`
- `GrowMaskWithBlur`
- `easy imageInsetCrop`
- `InpaintStitch`
- `Fast Groups Bypasser (rgthree)`
- `ChinesePrompt_Mix`
- `PreviewImage`
- `DetailerForEachDebug`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `ImageCompositeMasked`
- `PreviewImage`
- `LayerMask: MaskGrow`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `ModelSamplingSD3`
- `easy cleanGpuUsed`
- `ResizeLongestToNode`

**识别到的模式**：text_to_image、image_to_image、controlnet

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `177932711479417`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `heun`
- `scheduler` = `beta`
- `denoise` = `0.10000000000000002`
- `checkpoint` = `realDream_15SD15.safetensors`
- `controlnet_strength` = `0.5300000000000001`

## 知识

覆盖率 **92%**（103/112）

**有卡**：`DualCLIPLoader`、`VAELoader`、`ModelSamplingFlux`、`UNETLoader`、`CLIPTextEncode`、`CLIPLoader`、`LoraLoaderModelOnly`、`VAEEncode`、`TTP_Tile_image_size`、`easy imageBatchToImageList`、`ImageScale`、`easy imageSize`、`InpaintModelConditioning`、`ReduxAdvanced`、`CLIPVisionLoader`、`StyleModelLoader`、`ConditioningZeroOut`、`FluxGuidance`、`EmptyLatentImage`、`KSamplerSelect`、`BasicGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`RH_Translator`、`JanusModelLoader`、`JanusImageUnderstanding`、`Text Concatenate`、`SDXLPromptStyler`、`CR Text`、`LayerUtility: ColorImage`、`LayerUtility: ColorPicker`、`ImageComposite+`、`LoadImage`、`RandomNoise`、`KSampler`、`easy cleanGpuUsed`、`BasicScheduler`、`InpaintResize`、`InpaintCrop`、`easy makeImageForICLora`、`Mask Fill Holes`、`LayerUtility: ImageScaleByAspectRatio V2`、`UpscaleModelLoader`、`TTP_Image_Tile_Batch`、`ImageListToImageBatch`、`TTP_Image_Assy`、`SaveImage`、`Int`、`CheckpointLoaderSimple`、`ControlNetLoader`、`UltralyticsDetectorProvider`、`ControlNetApply`、`SAMLoader`、`FaceDetailer`、`MaskToSEGS`、`ResizeLongestToNode`、`GrowMaskWithBlur`、`easy imageInsetCrop`、`InpaintStitch`、`ChinesePrompt_Mix`、`DetailerForEachDebug`、`ImageCompositeMasked`、`LayerMask: MaskGrow`、`ImageScaleToTotalPixels`、`ImageUpscaleWithModel`、`ModelSamplingSD3`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
