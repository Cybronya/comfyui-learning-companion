---
key: 图片生成/图生图/Qwen Image2.1换脸局部重绘｜超高一致性脸部编辑_2108063537095593986.json
name: Qwen Image2.1换脸局部重绘｜超高一致性脸部编辑_2108063537095593986
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image2.1换脸局部重绘｜超高一致性脸部编辑_2108063537095593986.json
hash: 67520ba79df0ea7d
coverage: 0.695853
learned_at: 2026-10-21 00:42:52
nodes: [Reroute, Reroute, AILab_ImagePreview, GetImageSizeAndCount, ComfyMathExpression, AutoCropFaces, ImagePadForOutpaint, ImageScaleToTotalPixels, InvertMask, AutoCropFaces, Image Paste Crop, ImageToMask, AILab_Preview, ImagePadForOutpaint, Reroute, Reroute, AILab_ImagePreview, GetImageSizeAndCount, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, AutoCropFaces, ComfyMathExpression, ImageScaleToTotalPixels, ModelAttentionBackend, AILab_Preview, QwenImage21Cache, KSamplerSelect, RandomNoise, CFGGuider, BasicScheduler, InpaintModelConditioning, SamplerCustomAdvanced, easy cleanGpuUsed, VAEDecode, easy cleanGpuUsed, Image Comparer (rgthree), Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Image Paste Crop, ImageCropByMask, FaceAnalysisModels, FaceEmbedDistance, PreviewImage, Image Comparer (rgthree), TextEncodeQwenImage21, Reroute, Reroute, Reroute, ModelAttentionBackend, AILab_Preview, InpaintModelConditioning, INTConstant, QwenImage21Cache, KSamplerSelect, RandomNoise, CFGGuider, BasicScheduler, FaceAnalysisModels, FaceEmbedDistance, SamplerCustomAdvanced, easy cleanGpuUsed, PreviewImage, VAEDecode, Image Comparer (rgthree), easy cleanGpuUsed, Reroute, Reroute, Reroute, Reroute, FaceAnalysisModels, FaceEmbedDistance, PreviewImage, TextEncodeQwenImage21, Reroute, SAM3_Detect, MaskToImage, AILab_ImagePreview, AILab_ImagePreview, AILab_ImagePreview, AILab_ImagePreview, AILab_ImagePreview, Image Comparer (rgthree), AILab_ImagePreview, AILab_ImagePreview, AILab_ImagePreview, Image Paste Crop, ImageCropByMask, FaceAnalysisModels, FaceEmbedDistance, PreviewImage, AILab_ImagePreview, Image Comparer (rgthree), Reroute, AIO_Preprocessor, GetImageSizeAndCount, AILab_ImagePreview, Reroute, Reroute, BatchImagesNode, Reroute, SaveImage, ImageStitch, ImageStitch, Reroute, Reroute, Reroute, ImageScaleToMaxDimension, VOSR2ModelLoader, VOSR2Upscale, Images to RGB, Reroute, easy cleanGpuUsed, easy cleanGpuUsed, FaceAnalysisModels, PreviewImage, AILab_ImagePreview, FaceEmbedDistance, Image Comparer (rgthree), Reroute, AILab_ImagePreview, FaceAnalysisModels, FaceAlign, AutoCropFaces, LoadImage, Reroute, Reroute, SeedVR2LoadVAEModel, PreviewImage, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, Reroute, easy cleanGpuUsed, Reroute, Reroute, Reroute, Reroute, PreviewImage, Image Comparer (rgthree), UNETLoader, CLIPLoader, VAELoader, UNETLoader, CLIPLoader, VAELoader, Reroute, Reroute, LoadImage, Seed (rgthree), MaskToImage, SAM3_Detect, CheckpointLoaderSimple, CLIPTextEncode, GetImageSizeAndCount, ImageBlend, ColorMatchV2, ImageBlend, OpenposePreprocessor, SetNode, PrimitiveFloat, GetNode, PreviewImage, ImageBlend, INTConstant, Seed (rgthree), Reroute, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "sam3.1_multiplex_fp16.safetensors", "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image2.1换脸局部重绘｜超高一致性脸部编辑_2108063537095593986.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image2.1换脸局部重绘｜超高一致性脸部编辑_2108063537095593986.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（217 个）：
- `Reroute`
- `Reroute`
- `AILab_ImagePreview`
- `GetImageSizeAndCount`
- `ComfyMathExpression`
- `AutoCropFaces`
- `ImagePadForOutpaint`
- `ImageScaleToTotalPixels`
- `InvertMask`
- `AutoCropFaces`
- `Image Paste Crop`
- `ImageToMask`
- `AILab_Preview`
- `ImagePadForOutpaint`
- `Reroute`
- `Reroute`
- `AILab_ImagePreview`
- `GetImageSizeAndCount`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `AutoCropFaces`
- `ComfyMathExpression`
- `ImageScaleToTotalPixels`
- `ModelAttentionBackend`
- `AILab_Preview`
- `QwenImage21Cache`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `BasicScheduler`
- `InpaintModelConditioning`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `Image Comparer (rgthree)`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Image Paste Crop`
- `ImageCropByMask`
- `FaceAnalysisModels`
- `FaceEmbedDistance`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `TextEncodeQwenImage21`
- `Reroute`
- `Reroute`
- `Reroute`
- `ModelAttentionBackend`
- `AILab_Preview`
- `InpaintModelConditioning`
- `INTConstant`
- `QwenImage21Cache`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `BasicScheduler`
- `FaceAnalysisModels`
- `FaceEmbedDistance`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `PreviewImage`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `FaceAnalysisModels`
- `FaceEmbedDistance`
- `PreviewImage`
- `TextEncodeQwenImage21`
- `Reroute`
- `SAM3_Detect`
- `MaskToImage`
- `AILab_ImagePreview`
- `AILab_ImagePreview`
- `AILab_ImagePreview`
- `AILab_ImagePreview`
- `AILab_ImagePreview`
- `Image Comparer (rgthree)`
- `AILab_ImagePreview`
- `AILab_ImagePreview`
- `AILab_ImagePreview`
- `Image Paste Crop`
- `ImageCropByMask`
- `FaceAnalysisModels`
- `FaceEmbedDistance`
- `PreviewImage`
- `AILab_ImagePreview`
- `Image Comparer (rgthree)`
- `Reroute`
- `AIO_Preprocessor`
- `GetImageSizeAndCount`
- `AILab_ImagePreview`
- `Reroute`
- `Reroute`
- `BatchImagesNode`
- `Reroute`
- `SaveImage`
- `ImageStitch`
- `ImageStitch`
- `Reroute`
- `Reroute`
- `Reroute`
- `ImageScaleToMaxDimension`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `Images to RGB`
- `Reroute`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `FaceAnalysisModels`
- `PreviewImage`
- `AILab_ImagePreview`
- `FaceEmbedDistance`
- `Image Comparer (rgthree)`
- `Reroute`
- `AILab_ImagePreview`
- `FaceAnalysisModels`
- `FaceAlign`
- `AutoCropFaces`
- `LoadImage`
- `Reroute`
- `Reroute`
- `SeedVR2LoadVAEModel`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `Reroute`
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Reroute`
- `Reroute`
- `LoadImage`
- `Seed (rgthree)`
- `MaskToImage`
- `SAM3_Detect`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `GetImageSizeAndCount`
- `ImageBlend`
- `ColorMatchV2`
- `ImageBlend`
- `OpenposePreprocessor`
- `SetNode`
- `PrimitiveFloat`
- `GetNode`
- `PreviewImage`
- `ImageBlend`
- `INTConstant`
- `Seed (rgthree)`
- `Reroute`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **70%**（151/217）

**有卡**：`AILab_ImagePreview`、`GetImageSizeAndCount`、`ComfyMathExpression`、`AutoCropFaces`、`ImagePadForOutpaint`、`ImageScaleToTotalPixels`、`InvertMask`、`Image Paste Crop`、`ImageToMask`、`AILab_Preview`、`ModelAttentionBackend`、`QwenImage21Cache`、`KSamplerSelect`、`RandomNoise`、`CFGGuider`、`BasicScheduler`、`InpaintModelConditioning`、`SamplerCustomAdvanced`、`easy cleanGpuUsed`、`VAEDecode`、`ImageCropByMask`、`FaceAnalysisModels`、`FaceEmbedDistance`、`TextEncodeQwenImage21`、`INTConstant`、`SAM3_Detect`、`MaskToImage`、`AIO_Preprocessor`、`BatchImagesNode`、`SaveImage`、`ImageStitch`、`ImageScaleToMaxDimension`、`VOSR2ModelLoader`、`VOSR2Upscale`、`Images to RGB`、`FaceAlign`、`LoadImage`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`Seed (rgthree)`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`ImageBlend`、`ColorMatchV2`、`OpenposePreprocessor`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
