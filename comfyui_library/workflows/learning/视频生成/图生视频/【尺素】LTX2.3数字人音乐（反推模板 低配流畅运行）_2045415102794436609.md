---
key: 视频生成/图生视频/【尺素】LTX2.3数字人音乐（反推模板 低配流畅运行）_2045415102794436609.json
name: 【尺素】LTX2.3数字人音乐（反推模板 低配流畅运行）_2045415102794436609.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【尺素】LTX2.3数字人音乐（反推模板 低配流畅运行）_2045415102794436609.json
hash: 95d6fc9cf31edc3b
coverage: 0.627273
learned_at: 2026-10-15 22:36:47
nodes: [SetNode, SetNode, LTXVPreprocess, PreviewAny, Reroute, LTX2SamplingPreviewOverride, Reroute, Reroute, Reroute, Reroute, GetNode, SomethingToString, easy cleanGpuUsed, GetNode, llama_cpp_parameters, ManualSigmas, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, RandomNoise, MathExpression|pysssss, Reroute, SetLatentNoiseMask, KSamplerSelect, LTXVEmptyLatentAudio, Reroute, Reroute, Reroute, Reroute, Reroute, LTXVAudioVAEDecode, LTXVConditioning, CLIPTextEncode, CLIPTextEncode, PreviewAudio, CFGGuider, VAEDecodeTiled, LTXVAudioVAEEncode, Audio Duration (mtb), Reroute, Reroute, LTXVImgToVideoInplace, Fast Groups Bypasser (rgthree), PrimitiveBoolean, Reroute, Reroute, Reroute, LoraLoader, LTXVConcatAVLatent, RandomNoise, SimpleMath+, easy seed, PrimitiveInt, SimpleMath+, Reroute, MarkdownNote, LTXVAudioVAELoader, LTXAVTextEncoderLoader, MelBandRoFormerModelLoader, ComfySwitchNode, LoraLoaderModelOnly, LatentUpscaleModelLoader, LTXVSeparateAVLatent, LTXVLatentUpsampler, CFGGuider, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecodeTiled, VHS_VideoCombine, TextGenerateLTX2Prompt, PreviewAny, Reroute, ImageScaleBy, EmptyLTXVLatentVideo, ImageResize+, VHS_VideoCombine, SamplerCustomAdvanced, AudioCrop, SolidMask, GetImageSize, Reroute, llama_cpp_instruct_adv, LTX2_NAG, LoraLoaderModelOnly, LTXVImgToVideoInplace, ManualSigmas, MarkdownNote, MelBandRoFormerSampler, VAELoader, PrimitiveFloat, Fast Groups Bypasser (rgthree), LayerUtility: ImageScaleByAspectRatio V2, ResizeImagesByLongerEdge, LayerUtility: ImageScaleByAspectRatio V2, easy showAnything, CheckpointLoaderSimple, LoraLoaderModelOnly, llama_cpp_model_loader, TextInput_, LoadImage, PrimitiveStringMultiline, LoadAudio, LTXVSeparateAVLatent, SamplerCustomAdvanced, Reroute]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-distilled-1.1.safetensors", "height": 25, "lora_name": "gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors", "strength_clip": 1, "strength_model": 1, "width": 121}
---

# 视频生成/图生视频/【尺素】LTX2.3数字人音乐（反推模板 低配流畅运行）_2045415102794436609.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2045415102794436609.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（110 个）：
- `SetNode`
- `SetNode`
- `LTXVPreprocess`
- `PreviewAny`
- `Reroute`
- `LTX2SamplingPreviewOverride`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `GetNode`
- `SomethingToString`
- `easy cleanGpuUsed`
- `GetNode`
- `llama_cpp_parameters`
- `ManualSigmas`
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
- `LTXVEmptyLatentAudio` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LTXVAudioVAEDecode` ★核心
- `LTXVConditioning`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewAudio`
- `CFGGuider`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEEncode` ★核心
- `Audio Duration (mtb)`
- `Reroute`
- `Reroute`
- `LTXVImgToVideoInplace`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveBoolean`
- `Reroute`
- `Reroute`
- `Reroute`
- `LoraLoader` ★核心
- `LTXVConcatAVLatent`
- `RandomNoise`
- `SimpleMath+`
- `easy seed`
- `PrimitiveInt`
- `SimpleMath+`
- `Reroute`
- `MarkdownNote`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `MelBandRoFormerModelLoader`
- `ComfySwitchNode`
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleModelLoader`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `TextGenerateLTX2Prompt`
- `PreviewAny`
- `Reroute`
- `ImageScaleBy`
- `EmptyLTXVLatentVideo`
- `ImageResize+`
- `VHS_VideoCombine`
- `SamplerCustomAdvanced` ★核心
- `AudioCrop`
- `SolidMask`
- `GetImageSize`
- `Reroute`
- `llama_cpp_instruct_adv`
- `LTX2_NAG`
- `LoraLoaderModelOnly` ★核心
- `LTXVImgToVideoInplace`
- `ManualSigmas`
- `MarkdownNote`
- `MelBandRoFormerSampler` ★核心
- `VAELoader`
- `PrimitiveFloat`
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ResizeImagesByLongerEdge`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy showAnything`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `llama_cpp_model_loader`
- `TextInput_`
- `LoadImage`
- `PrimitiveStringMultiline`
- `LoadAudio`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `Reroute`

**识别到的模式**：lora

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`
- `lora_name` = `gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-1.1.safetensors`

## 知识

覆盖率 **63%**（69/110）

**有卡**：`LTXVPreprocess`、`LTX2SamplingPreviewOverride`、`SomethingToString`、`easy cleanGpuUsed`、`llama_cpp_parameters`、`ManualSigmas`、`RandomNoise`、`MathExpression|pysssss`、`SetLatentNoiseMask`、`KSamplerSelect`、`LTXVEmptyLatentAudio`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`CLIPTextEncode`、`PreviewAudio`、`CFGGuider`、`VAEDecodeTiled`、`LTXVAudioVAEEncode`、`Audio Duration (mtb)`、`LTXVImgToVideoInplace`、`PrimitiveBoolean`、`LoraLoader`、`LTXVConcatAVLatent`、`SimpleMath+`、`easy seed`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`MelBandRoFormerModelLoader`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`VHS_VideoCombine`、`TextGenerateLTX2Prompt`、`ImageScaleBy`、`EmptyLTXVLatentVideo`、`ImageResize+`、`SamplerCustomAdvanced`、`AudioCrop`、`SolidMask`、`GetImageSize`、`llama_cpp_instruct_adv`、`LTX2_NAG`、`MelBandRoFormerSampler`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ResizeImagesByLongerEdge`、`CheckpointLoaderSimple`、`llama_cpp_model_loader`、`TextInput_`、`LoadImage`、`LoadAudio`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect
