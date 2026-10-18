---
key: 视频生成/图生视频/ltx2.3 image Upscaler图片高清修复_2074690010191843330.json
name: ltx2.3 image Upscaler图片高清修复_2074690010191843330.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/ltx2.3 image Upscaler图片高清修复_2074690010191843330.json
hash: 68852c2365fb80bc
coverage: 0.764706
learned_at: 2026-10-15 22:41:17
nodes: [GetImageSize, ImagePadKJ, ImageScaleToTotalPixels, Reroute, ImagePadKJ, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, ImageScaleToTotalPixels, LazySwitchKJ, LazySwitchKJ, EmptyImage, LazySwitchKJ, Int, PrimitiveNode, Int, Int, Int, Note, Note, Display Any (rgthree), Note, Float, SimpleMath+, SimpleMath+, SimpleMath+, ImageResizeKJv2, Display Any (rgthree), SimpleMath+, SimpleMath+, PreviewImage, ImageCrop+, GetImageSize, ImageResizeKJv2, Bool, LazySwitchKJ, LazySwitchKJ, Note, Blur, ImageScaleToTotalPixels, Image Rembg (Remove Background), SimpleMath+, Bool, Bool, PrimitiveInt, PrimitiveInt, RandomNoise, RandomNoise, LTXVAudioVAELoader, Reroute, ComfyMathExpression, LTXVConditioning, LatentUpscaleModelLoader, LTXVConcatAVLatent, ComfyMathExpression, PrimitiveInt, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, CLIPTextEncode, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, Reroute, Reroute, GetImageSize, KSamplerSelect, LTXVLatentUpsampler, SamplerCustomAdvanced, Reroute, Reroute, Reroute, LTXAVTextEncoderLoader, TextGenerateLTX2Prompt, CFGGuider, LTXVAudioVAEDecode, Reroute, ImageFromBatch, ImageFromBatch, ImageCrop+, LTXVSeparateAVLatent, LTXVCropGuides, LTXVImgToVideoInplace, CFGGuider, LTX2_NAG, CheckpointLoaderSimple, LoraLoader, LoraLoader, LTXVSeparateAVLatent, LTXVConcatAVLatent, SamplerCustomAdvanced, KSamplerSelect, LTXVChunkFeedForward, Note, ManualSigmas, ManualSigmas, ImageCrop+, LTXVImgToVideoInplace, Reroute, ResizeImagesByLongerEdge, ImageFromBatch, ImageFromBatch, Audio Cut (mtb), ComfyMathExpression, PrimitiveInt, Reroute, PrimitiveInt, PrimitiveInt, ComfyMathExpression, PreviewAny, LoraLoader, PrimitiveString, PrimitiveStringMultiline, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Reroute, Reroute, Power Lora Loader (rgthree), VAEDecodeTiled, ImageStitch, ImageStitch, LTXVPreprocess, Blur, SaveImage, LazySwitchKJ, PreviewImage, VHS_VideoCombine, ImageResizeKJv2, ImageResizeKJv2, MarkdownNote, Reroute, PreviewImage, LoadImage]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "lora_name": "ltx23_upscalify_4psc4l1fy.safetensors", "strength_clip": 1, "strength_model": 0, "width": 97}
---

# 视频生成/图生视频/ltx2.3 image Upscaler图片高清修复_2074690010191843330.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2074690010191843330.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（136 个）：
- `GetImageSize`
- `ImagePadKJ`
- `ImageScaleToTotalPixels`
- `Reroute`
- `ImagePadKJ`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `ImageScaleToTotalPixels`
- `LazySwitchKJ`
- `LazySwitchKJ`
- `EmptyImage`
- `LazySwitchKJ`
- `Int`
- `PrimitiveNode`
- `Int`
- `Int`
- `Int`
- `Note`
- `Note`
- `Display Any (rgthree)`
- `Note`
- `Float`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `ImageResizeKJv2`
- `Display Any (rgthree)`
- `SimpleMath+`
- `SimpleMath+`
- `PreviewImage`
- `ImageCrop+`
- `GetImageSize`
- `ImageResizeKJv2`
- `Bool`
- `LazySwitchKJ`
- `LazySwitchKJ`
- `Note`
- `Blur`
- `ImageScaleToTotalPixels`
- `Image Rembg (Remove Background)`
- `SimpleMath+`
- `Bool`
- `Bool`
- `PrimitiveInt`
- `PrimitiveInt`
- `RandomNoise`
- `RandomNoise`
- `LTXVAudioVAELoader`
- `Reroute`
- `ComfyMathExpression`
- `LTXVConditioning`
- `LatentUpscaleModelLoader`
- `LTXVConcatAVLatent`
- `ComfyMathExpression`
- `PrimitiveInt`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `Reroute`
- `Reroute`
- `GetImageSize`
- `KSamplerSelect` ★核心
- `LTXVLatentUpsampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXAVTextEncoderLoader`
- `TextGenerateLTX2Prompt`
- `CFGGuider`
- `LTXVAudioVAEDecode` ★核心
- `Reroute`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageCrop+`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `CFGGuider`
- `LTX2_NAG`
- `CheckpointLoaderSimple` ★核心
- `LoraLoader` ★核心
- `LoraLoader` ★核心
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `LTXVChunkFeedForward`
- `Note`
- `ManualSigmas`
- `ManualSigmas`
- `ImageCrop+`
- `LTXVImgToVideoInplace`
- `Reroute`
- `ResizeImagesByLongerEdge`
- `ImageFromBatch`
- `ImageFromBatch`
- `Audio Cut (mtb)`
- `ComfyMathExpression`
- `PrimitiveInt`
- `Reroute`
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfyMathExpression`
- `PreviewAny`
- `LoraLoader` ★核心
- `PrimitiveString`
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Reroute`
- `Reroute`
- `Power Lora Loader (rgthree)`
- `VAEDecodeTiled` ★核心
- `ImageStitch`
- `ImageStitch`
- `LTXVPreprocess`
- `Blur`
- `SaveImage`
- `LazySwitchKJ`
- `PreviewImage`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `MarkdownNote`
- `Reroute`
- `PreviewImage`
- `LoadImage`

**识别到的模式**：lora

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `lora_name` = `ltx23_upscalify_4psc4l1fy.safetensors`
- `strength_model` = `0`
- `strength_clip` = `1`

## 知识

覆盖率 **76%**（104/136）

**有卡**：`GetImageSize`、`ImagePadKJ`、`ImageScaleToTotalPixels`、`SimpleMath+`、`LazySwitchKJ`、`EmptyImage`、`Int`、`Display Any (rgthree)`、`Float`、`ImageResizeKJv2`、`ImageCrop+`、`Bool`、`Blur`、`Image Rembg (Remove Background)`、`RandomNoise`、`LTXVAudioVAELoader`、`ComfyMathExpression`、`LTXVConditioning`、`LatentUpscaleModelLoader`、`LTXVConcatAVLatent`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`CLIPTextEncode`、`KSamplerSelect`、`LTXVLatentUpsampler`、`SamplerCustomAdvanced`、`LTXAVTextEncoderLoader`、`TextGenerateLTX2Prompt`、`CFGGuider`、`LTXVAudioVAEDecode`、`ImageFromBatch`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXVImgToVideoInplace`、`LTX2_NAG`、`CheckpointLoaderSimple`、`LoraLoader`、`LTXVChunkFeedForward`、`ManualSigmas`、`ResizeImagesByLongerEdge`、`Audio Cut (mtb)`、`LoraLoaderModelOnly`、`Power Lora Loader (rgthree)`、`VAEDecodeTiled`、`ImageStitch`、`LTXVPreprocess`、`SaveImage`、`VHS_VideoCombine`、`LoadImage`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
