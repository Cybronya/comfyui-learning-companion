---
key: 视频生成/图生视频/【尺素】LTX2.3影视全案控制工作流（低配流畅运行）_2044462074100715521.json
name: 【尺素】LTX2.3影视全案控制工作流（低配流畅运行）_2044462074100715521.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2044462074100715521.json
hash: a15b4f1692440961
coverage: 0.659389
learned_at: 2026-10-15 22:36:38
nodes: [LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, GetImageSize, LTXVSeparateAVLatent, SolidMask, VAEDecodeTiled, MelBandRoFormerSampler, ResizeImagesByLongerEdge, LTXVPreprocess, ImageScaleBy, PreviewAny, Reroute, LTX2SamplingPreviewOverride, Reroute, Reroute, LTXVSeparateAVLatent, FloatConstant, RandomNoise, SamplerCustomAdvanced, MelBandRoFormerModelLoader, PrimitiveFloat, PreviewAudio, ResizeImagesByLongerEdge, LTXVPreprocess, KSamplerSelect, ManualSigmas, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, LTXAVTextEncoderLoader, Reroute, Audio Duration (mtb), MelBandRoFormerSampler, SolidMask, VAEDecodeTiled, LTXVAudioVAEDecode, PreviewAny, MathExpression|pysssss, Reroute, Reroute, PrimitiveInt, ResizeImageMaskNode, PrimitiveInt, Reroute, ResizeImageMaskNode, ResizeImagesByLongerEdge, SetLatentNoiseMask, SimpleMath+, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, Reroute, Reroute, Reroute, Reroute, Reroute, LTXVConcatAVLatent, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVPreprocess, Reroute, Reroute, SamplerCustomAdvanced, Reroute, LTXVSeparateAVLatent, Reroute, Reroute, LTXVConcatAVLatent, LTXVImgToVideoInplaceKJ, Reroute, Reroute, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoraLoaderModelOnly, CLIPTextEncode, easy imageSize, TextEncodeQwenImageEditPlus, KSampler, QwenMultiangleCameraNode, Reroute, Reroute, Reroute, EmptyLatentImage, PreviewAudio, Reroute, GetNode, SomethingToString, easy cleanGpuUsed, GetNode, llama_cpp_model_loader, llama_cpp_parameters, NormalizeAudioLoudness, Qwen3ASRTranscribe, Reroute, LoadImage, LoadImage, CreateVideo, ManualSigmas, CLIPLoader, CheckpointLoaderSimple, LTXVAudioVAEEncode, LTXVConditioning, CLIPTextEncode, Reroute, CFGGuider, LTXVConditioning, Reroute, PathchSageAttentionKJ, LTXVChunkFeedForward, CLIPTextEncode, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, RandomNoise, MathExpression|pysssss, Reroute, SetLatentNoiseMask, KSamplerSelect, LTXVImgToVideoInplace, LTX2_NAG, LTXVEmptyLatentAudio, ModelPatchTorchSettings, Reroute, Reroute, Reroute, Reroute, LoadAudio, AudioCrop, CheckpointLoaderSimple, LTXVAudioVAELoader, LoraLoaderModelOnly, LatentUpscaleModelLoader, LTXVCropGuides, Reroute, Reroute, LTXVSeparateAVLatent, LTXVLatentUpsampler, CFGGuider, KSamplerSelect, LTXVConcatAVLatent, ManualSigmas, LTXVAudioVAEDecode, PrimitiveStringMultiline, llama_cpp_instruct_adv, TextInput_, LoadImage, LTXVConditioning, CLIPTextEncode, CLIPTextEncode, PreviewAudio, SamplerCustomAdvanced, SamplerCustomAdvanced, AudioCrop, CR Prompt Text, PreviewImage, SaveVideo, VAEDecode, LoadImage, SaveImage, MarkdownNote, VHS_VideoCombine, CFGGuider, VAEDecodeTiled, LTXVAudioVAEDecode, VHS_VideoCombine, LTXVAudioVAEEncode, Audio Duration (mtb), Reroute, Reroute, Reroute, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, SimpleMath+, Fast Groups Bypasser (rgthree), ImageResizeKJv2, PrimitiveBoolean, LTXVSeparateAVLatent, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Qwen3ASRLoader, LongCatVoiceCloneTTS, AudioCrop, TextGenerateLTX2Prompt, MarkdownNote, SaveAudioMP3, LoadAudio, easy showAnything, TextGenerateLTX2Prompt, PreviewAny, ComfySwitchNode, LTXVConcatAVLatent, ComfySwitchNode, RandomNoise, SimpleMath+, PrimitiveFloat, easy seed, PrimitiveInt, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), LoadImage, PrimitiveStringMultiline, CheckpointLoaderSimple, LoraLoaderModelOnly, VAELoader, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LoraLoader, PreviewAny, INTConstant, INTConstant, LoadAudio, LoraLoaderModelOnly, LoraLoaderModelOnly, LatentUpscaleModelLoader, MelBandRoFormerModelLoader, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote]
patterns: [text_to_image, lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx2310eros_beta.safetensors", "denoise": 1, "height": 25, "lora_name": "gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors", "sampler_name": "euler_ancestral", "scheduler": "beta57", "seed": 1006560159285636, "steps": 8, "strength_clip": 1, "strength_model": 1, "width": 121}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/【尺素】LTX2.3影视全案控制工作流（低配流畅运行）_2044462074100715521.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2044462074100715521.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（229 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `GetImageSize`
- `LTXVSeparateAVLatent`
- `SolidMask`
- `VAEDecodeTiled` ★核心
- `MelBandRoFormerSampler` ★核心
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ImageScaleBy`
- `PreviewAny`
- `Reroute`
- `LTX2SamplingPreviewOverride`
- `Reroute`
- `Reroute`
- `LTXVSeparateAVLatent`
- `FloatConstant`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `MelBandRoFormerModelLoader`
- `PrimitiveFloat`
- `PreviewAudio`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXAVTextEncoderLoader`
- `Reroute`
- `Audio Duration (mtb)`
- `MelBandRoFormerSampler` ★核心
- `SolidMask`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `PreviewAny`
- `MathExpression|pysssss`
- `Reroute`
- `Reroute`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `PrimitiveInt`
- `Reroute`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `SetLatentNoiseMask`
- `SimpleMath+`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `Reroute`
- `Reroute`
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `LTXVSeparateAVLatent`
- `Reroute`
- `Reroute`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplaceKJ`
- `Reroute`
- `Reroute`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `easy imageSize`
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `QwenMultiangleCameraNode`
- `Reroute`
- `Reroute`
- `Reroute`
- `EmptyLatentImage` ★核心
- `PreviewAudio`
- `Reroute`
- `GetNode`
- `SomethingToString`
- `easy cleanGpuUsed`
- `GetNode`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `NormalizeAudioLoudness`
- `Qwen3ASRTranscribe`
- `Reroute`
- `LoadImage`
- `LoadImage`
- `CreateVideo`
- `ManualSigmas`
- `CLIPLoader`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAEEncode` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `Reroute`
- `CFGGuider`
- `LTXVConditioning`
- `Reroute`
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `CLIPTextEncode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `RandomNoise`
- `MathExpression|pysssss`
- `Reroute`
- `SetLatentNoiseMask`
- `KSamplerSelect` ★核心
- `LTXVImgToVideoInplace`
- `LTX2_NAG`
- `LTXVEmptyLatentAudio` ★核心
- `ModelPatchTorchSettings`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LoadAudio`
- `AudioCrop`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `LTXVCropGuides`
- `Reroute`
- `Reroute`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `LTXVAudioVAEDecode` ★核心
- `PrimitiveStringMultiline`
- `llama_cpp_instruct_adv`
- `TextInput_`
- `LoadImage`
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewAudio`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `AudioCrop`
- `CR Prompt Text`
- `PreviewImage`
- `SaveVideo`
- `VAEDecode` ★核心
- `LoadImage`
- `SaveImage`
- `MarkdownNote`
- `VHS_VideoCombine`
- `CFGGuider`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `VHS_VideoCombine`
- `LTXVAudioVAEEncode` ★核心
- `Audio Duration (mtb)`
- `Reroute`
- `Reroute`
- `Reroute`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `SimpleMath+`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`
- `PrimitiveBoolean`
- `LTXVSeparateAVLatent`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Qwen3ASRLoader`
- `LongCatVoiceCloneTTS`
- `AudioCrop`
- `TextGenerateLTX2Prompt`
- `MarkdownNote`
- `SaveAudioMP3`
- `LoadAudio`
- `easy showAnything`
- `TextGenerateLTX2Prompt`
- `PreviewAny`
- `ComfySwitchNode`
- `LTXVConcatAVLatent`
- `ComfySwitchNode`
- `RandomNoise`
- `SimpleMath+`
- `PrimitiveFloat`
- `easy seed`
- `PrimitiveInt`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `PrimitiveStringMultiline`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LoraLoader` ★核心
- `PreviewAny`
- `INTConstant`
- `INTConstant`
- `LoadAudio`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `MelBandRoFormerModelLoader`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`

**识别到的模式**：text_to_image、lora

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`
- `seed` = `1006560159285636`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta57`
- `denoise` = `1`
- `checkpoint` = `ltx2310eros_beta.safetensors`
- `lora_name` = `gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **66%**（151/229）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSize`、`LTXVSeparateAVLatent`、`SolidMask`、`VAEDecodeTiled`、`MelBandRoFormerSampler`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`ImageScaleBy`、`LTX2SamplingPreviewOverride`、`FloatConstant`、`RandomNoise`、`SamplerCustomAdvanced`、`MelBandRoFormerModelLoader`、`PreviewAudio`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`LTXAVTextEncoderLoader`、`Audio Duration (mtb)`、`LTXVAudioVAEDecode`、`MathExpression|pysssss`、`ResizeImageMaskNode`、`SetLatentNoiseMask`、`SimpleMath+`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVImgToVideoInplaceKJ`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`easy imageSize`、`TextEncodeQwenImageEditPlus`、`KSampler`、`QwenMultiangleCameraNode`、`EmptyLatentImage`、`SomethingToString`、`easy cleanGpuUsed`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`NormalizeAudioLoudness`、`Qwen3ASRTranscribe`、`LoadImage`、`CreateVideo`、`CLIPLoader`、`CheckpointLoaderSimple`、`LTXVAudioVAEEncode`、`LTXVConditioning`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`LTX2_NAG`、`ModelPatchTorchSettings`、`LoadAudio`、`AudioCrop`、`LTXVAudioVAELoader`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`llama_cpp_instruct_adv`、`TextInput_`、`CR Prompt Text`、`SaveVideo`、`VAEDecode`、`SaveImage`、`VHS_VideoCombine`、`ImageResizeKJv2`、`PrimitiveBoolean`、`Qwen3ASRLoader`、`LongCatVoiceCloneTTS`、`TextGenerateLTX2Prompt`、`SaveAudioMP3`、`easy seed`、`VAELoader`、`LoraLoader`、`INTConstant`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
