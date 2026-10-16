---
key: 视频生成/图生视频/LTX-2.3换装术｜先AI换装再让猫咪开口唱歌：换装+对口型一键搞定_2032438880057692162.json
name: LTX-2.3换装术｜先AI换装再让猫咪开口唱歌：换装+对口型一键搞定_2032438880057692162.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2032438880057692162.json
hash: 49e5eb28e7221667
coverage: 0.858974
learned_at: 2026-10-15 22:35:36
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LoraLoaderModelOnly, ResizeImagesByLongerEdge, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVPreprocess, KSamplerSelect, ComfyMathExpression, Reroute, ComfyMathExpression, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVAudioVAEDecode, ComfyMathExpression, PrimitiveInt, PrimitiveBoolean, CLIPTextEncode, LTXVConditioning, LTXVEmptyLatentAudio, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LatentUpscaleModelLoader, CLIPTextEncode, CFGGuider, VAEDecodeTiled, CheckpointLoaderSimple, LTXVConcatAVLatent, PrimitiveInt, LTXVAudioVAELoader, LTXAVTextEncoderLoader, PrimitiveStringMultiline, CLIPLoader, UNETLoader, TextEncodeQwenImageEditPlus, VAELoader, FluxKontextImageScale, VAEEncode, FluxKontextImageScale, MarkdownNote, PrimitiveInt, PrimitiveInt, LoraLoaderModelOnly, ModelSamplingAuraFlow, CFGNorm, PrimitiveInt, PrimitiveFloat, CreateVideo, AudioInfoNode, SolidMask, MelBandRoFormerModelLoader, MelBandRoFormerSampler, LTXVAudioVAEEncode, MathExpression|pysssss, Bjornulf_ShowInt, SetLatentNoiseMask, PreviewAudio, LoadAudio, SaveVideo, ImageResizeKJv2, KSampler, MarkdownNote, TextEncodeQwenImageEditPlus, LoadImage, LoadImage, VAEDecode, easy cleanGpuUsed, PreviewImage, Label (rgthree), Label (rgthree)]
patterns: [image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 4, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "denoise": 1, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 400485009205500, "steps": 40, "width": 97}
---

# 视频生成/图生视频/LTX-2.3换装术｜先AI换装再让猫咪开口唱歌：换装+对口型一键搞定_2032438880057692162.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2032438880057692162.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（78 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LoraLoaderModelOnly` ★核心
- `ResizeImagesByLongerEdge`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `KSamplerSelect` ★核心
- `ComfyMathExpression`
- `Reroute`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `LTXVAudioVAEDecode` ★核心
- `ComfyMathExpression`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVEmptyLatentAudio` ★核心
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `VAEDecodeTiled` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVConcatAVLatent`
- `PrimitiveInt`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `UNETLoader` ★核心
- `TextEncodeQwenImageEditPlus`
- `VAELoader`
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `FluxKontextImageScale`
- `MarkdownNote`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `PrimitiveInt`
- `PrimitiveFloat`
- `CreateVideo`
- `AudioInfoNode`
- `SolidMask`
- `MelBandRoFormerModelLoader`
- `MelBandRoFormerSampler` ★核心
- `LTXVAudioVAEEncode` ★核心
- `MathExpression|pysssss`
- `Bjornulf_ShowInt`
- `SetLatentNoiseMask`
- `PreviewAudio`
- `LoadAudio`
- `SaveVideo`
- `ImageResizeKJv2`
- `KSampler` ★核心
- `MarkdownNote`
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `LoadImage`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `PreviewImage`
- `Label (rgthree)`
- `Label (rgthree)`

**识别到的模式**：image_to_image

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `seed` = `400485009205500`
- `steps` = `40`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（67/78）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LoraLoaderModelOnly`、`ResizeImagesByLongerEdge`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVPreprocess`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`PrimitiveBoolean`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`VAEDecodeTiled`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`CLIPLoader`、`UNETLoader`、`TextEncodeQwenImageEditPlus`、`VAELoader`、`FluxKontextImageScale`、`VAEEncode`、`ModelSamplingAuraFlow`、`CFGNorm`、`CreateVideo`、`AudioInfoNode`、`SolidMask`、`MelBandRoFormerModelLoader`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`MathExpression|pysssss`、`Bjornulf_ShowInt`、`SetLatentNoiseMask`、`PreviewAudio`、`LoadAudio`、`SaveVideo`、`ImageResizeKJv2`、`KSampler`、`LoadImage`、`VAEDecode`、`easy cleanGpuUsed`、`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader
