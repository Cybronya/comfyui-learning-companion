---
key: 视频生成/文生视频/LTX 2.3 IC-LoRA 视频上色工作流_2035010437032448002.json
name: LTX 2.3 IC-LoRA 视频上色工作流_2035010437032448002
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX 2.3 IC-LoRA 视频上色工作流_2035010437032448002.json
hash: 9e6d998c853f5f9e
coverage: 0.938272
learned_at: 2026-10-15 22:44:31
nodes: [LTXVAudioVAEDecode, VAEDecodeTiled, KSamplerSelect, LTXVConditioning, LTXAddVideoICLoRAGuide, LTXVConcatAVLatent, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, EmptyLTXVLatentVideo, SamplerCustomAdvanced, LTXVCropGuides, LTXVSeparateAVLatent, DWPreprocessor, LTXVAudioVAELoader, CheckpointLoaderSimple, GemmaAPITextEncode, PrimitiveString, CLIPTextEncode, LTXVPreprocess, CFGGuider, ResizeImageMaskNode, GetImageSize, ManualSigmas, GemmaAPITextEncode, RandomNoise, CannyEdgePreprocessor, DepthCrafter, DownloadAndLoadDepthCrafterModel, LoraLoaderModelOnly, LTXAVTextEncoderLoader, CLIPTextEncode, SaveVideo, CreateVideo, CM_FloatToInt, LTXICLoRALoaderModelOnly, SimpleMath+, ResizeImageMaskNode, image_scale_pixel_v2, VHS_VideoInfoLoaded, CLIPLoader, ModelSamplingAuraFlow, CFGNorm, MarkdownNote, VAELoader, VAEDecode, GetImageSize+, KSampler, EmptySD3LatentImage, ImageScaleToTotalPixels, ImageScaleToTotalPixels, UNETLoader, TextEncodeQwenImageEditPlus, ReferenceLatent, VAEEncode, ReferenceLatent, LoadImage, LoadImage, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, SaveImage, VHS_LoadVideo, LoadImage, Image Comparer (rgthree), Image_Resize_longsize, LoadImage, ImageScaleToTotalPixels, JWImageExtractFromBatch, TextEncodeQwenImageEditPlus, PrimitiveBoolean, PreviewImage, DisTorchPurgeVRAMV2, VAEDecodeTiled, WD14Tagger|pysssss, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo, VHS_LoadVideo, VHS_VideoCombine, VHS_LoadVideo, VHS_VideoCombine]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 1, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 794792336549169, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/LTX 2.3 IC-LoRA 视频上色工作流_2035010437032448002.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX 2.3 IC-LoRA 视频上色工作流_2035010437032448002.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（81 个）：
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `KSamplerSelect` ★核心
- `LTXVConditioning`
- `LTXAddVideoICLoRAGuide`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVImgToVideoConditionOnly`
- `EmptyLTXVLatentVideo`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `DWPreprocessor`
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `GemmaAPITextEncode`
- `PrimitiveString`
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `CFGGuider`
- `ResizeImageMaskNode`
- `GetImageSize`
- `ManualSigmas`
- `GemmaAPITextEncode`
- `RandomNoise`
- `CannyEdgePreprocessor`
- `DepthCrafter`
- `DownloadAndLoadDepthCrafterModel`
- `LoraLoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `CLIPTextEncode` ★核心
- `SaveVideo`
- `CreateVideo`
- `CM_FloatToInt`
- `LTXICLoRALoaderModelOnly` ★核心
- `SimpleMath+`
- `ResizeImageMaskNode`
- `image_scale_pixel_v2`
- `VHS_VideoInfoLoaded`
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `MarkdownNote`
- `VAELoader`
- `VAEDecode` ★核心
- `GetImageSize+`
- `KSampler` ★核心
- `EmptySD3LatentImage`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `UNETLoader` ★核心
- `TextEncodeQwenImageEditPlus`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `LoadImage`
- `LoadImage`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `VHS_LoadVideo`
- `LoadImage`
- `Image Comparer (rgthree)`
- `Image_Resize_longsize`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `JWImageExtractFromBatch`
- `TextEncodeQwenImageEditPlus`
- `PrimitiveBoolean`
- `PreviewImage`
- `DisTorchPurgeVRAMV2`
- `VAEDecodeTiled` ★核心
- `WD14Tagger|pysssss`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**识别到的模式**：image_to_image

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `794792336549169`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（76/81）

**有卡**：`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`KSamplerSelect`、`LTXVConditioning`、`LTXAddVideoICLoRAGuide`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`LTXVImgToVideoConditionOnly`、`EmptyLTXVLatentVideo`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`DWPreprocessor`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`GemmaAPITextEncode`、`CLIPTextEncode`、`LTXVPreprocess`、`CFGGuider`、`ResizeImageMaskNode`、`GetImageSize`、`ManualSigmas`、`RandomNoise`、`CannyEdgePreprocessor`、`DepthCrafter`、`DownloadAndLoadDepthCrafterModel`、`LoraLoaderModelOnly`、`LTXAVTextEncoderLoader`、`SaveVideo`、`CreateVideo`、`CM_FloatToInt`、`LTXICLoRALoaderModelOnly`、`SimpleMath+`、`image_scale_pixel_v2`、`VHS_VideoInfoLoaded`、`CLIPLoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`VAELoader`、`VAEDecode`、`GetImageSize+`、`KSampler`、`EmptySD3LatentImage`、`ImageScaleToTotalPixels`、`UNETLoader`、`TextEncodeQwenImageEditPlus`、`ReferenceLatent`、`VAEEncode`、`LoadImage`、`SaveImage`、`VHS_LoadVideo`、`Image_Resize_longsize`、`JWImageExtractFromBatch`、`PrimitiveBoolean`、`DisTorchPurgeVRAMV2`、`WD14Tagger|pysssss`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
