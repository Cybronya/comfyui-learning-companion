---
key: 视频生成/图生视频/minimax h3 fl2va首尾帧2K二采｜Qwen3.8 27B反推版V1_2092051378125500418.json
name: minimax h3 fl2va首尾帧2K二采｜Qwen3.8 27B反推版V1_2092051378125500418
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/minimax h3 fl2va首尾帧2K二采｜Qwen3.8 27B反推版V1_2092051378125500418.json
hash: 4bc030d2714df88b
coverage: 0.832432
learned_at: 2026-10-16 22:59:30
nodes: [easy forLoopEnd, GetImageSizeAndCount, SetNode, easy showAnything, MathExpression|pysssss, easy showAnything, CLIPTextEncode, SetNode, RandomNoise, KSamplerSelect, LTXVSeparateAVLatent, GetNode, SetNode, LatentUpscaleModelLoader, LTXVConcatAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, GetNode, GetNode, GetNode, LTXVEmptyLatentAudio, LTXAVTextEncoderLoader, LTXVConditioning, GetNode, LTXVCropGuides, SamplerCustomAdvanced, LTXVLatentUpsampler, CLIPTextEncode, easy cleanGpuUsed, easy showAnything, ManualSigmas, ManualSigmas, CheckpointLoaderSimple, VAEEncode, InjectLatentNoise+, ManualSigmas, LoraLoaderModelOnly, LTX2_NAG, LTXVPreprocess, LTXVPreprocess, SetNode, LoraLoaderModelOnly, LTXVAudioVAELoader, InjectLatentNoise+, ManualSigmas, LTXVAddGuideMulti, CFGGuider, VHS_VideoCombine, PreviewImage, LTX2MemoryEfficientSageAttentionPatch, Reroute, PrimitiveFloat, RandomNoise, Int, KSamplerSelect, BasicGuider, RandomNoise, SamplerCustomAdvanced, VAEDecodeAudio, easy cleanGpuUsed, Int, GetNode, VAEDecode, VHS_VideoCombine, LoraLoaderModelOnly, GetNode, SamplerCustomAdvanced, RandomNoise, BasicGuider, KSamplerSelect, VAEDecode, GetNode, VAEDecodeAudio, VHS_VideoCombine, BasicScheduler, MiniMaxH3LatentUpscaleCombined, KSamplerSelect, ImageScaleBy, PrimitiveStringMultiline, BasicScheduler, VHS_VideoCombine, Int, GetImageSize, RandomNoise, VAEDecodeAudio, VAEDecode, easy showAnything, KSamplerSelect, MiniMaxH3ReferenceToVideo, LoadImage, CLIPLoader, VHS_VideoCombine, ComfyMathExpression, LoraLoaderModelOnly, easy cleanGpuUsed, SamplerCustomAdvanced, VAEDecode, CLIPLoader, CR Text, ComfyMathExpression, BasicGuider, LoadImage, ComfyMathExpression, PreviewImage, easy forLoopStart, MiniMaxH3ImageToVideo, VAEDecodeAudio, SetNode, easy cleanGpuUsed, ImageScaleBy, ResolutionSelector, VHS_VideoCombine, VAELoader, MiniMaxH3ReferenceToVideo, VAELoader, VHS_VideoCombine, BasicScheduler, SetNode, easy cleanGpuUsed, SomethingToString, ProcessString, llama_cpp_parameters, llama_cpp_instruct_adv, JoinStrings, PreviewImage, PreviewAny, CR Prompt Text, TextInput_, ShowText|pysssss, TextInput_, llama_cpp_model_loader, ImageConcatMulti, ImageResize+, ImageResize+, GetNode, SamplerCustomAdvanced, LoraLoaderModelOnly, LTXVConcatAVLatent, LTXVSeparateAVLatent, Float, MinimaxH3LatentUpscaler3D, VAELoader, VAELoader, UNETLoader, BasicGuider, LoraLoaderModelOnly, SLASageAttention, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, SLASageAttention, MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, ModelAttentionBackend, LoraLoaderModelOnly, BasicScheduler, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/minimax h3 fl2va首尾帧2K二采｜Qwen3.8 27B反推版V1_2092051378125500418.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/minimax h3 fl2va首尾帧2K二采｜Qwen3.8 27B反推版V1_2092051378125500418.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（185 个）：
- `easy forLoopEnd`
- `GetImageSizeAndCount`
- `SetNode`
- `easy showAnything`
- `MathExpression|pysssss`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `SetNode`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `SetNode`
- `LatentUpscaleModelLoader`
- `LTXVConcatAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `LTXAVTextEncoderLoader`
- `LTXVConditioning`
- `GetNode`
- `LTXVCropGuides`
- `SamplerCustomAdvanced` ★核心
- `LTXVLatentUpsampler` ★核心
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `easy showAnything`
- `ManualSigmas`
- `ManualSigmas`
- `CheckpointLoaderSimple` ★核心
- `VAEEncode` ★核心
- `InjectLatentNoise+`
- `ManualSigmas`
- `LoraLoaderModelOnly` ★核心
- `LTX2_NAG`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `InjectLatentNoise+`
- `ManualSigmas`
- `LTXVAddGuideMulti`
- `CFGGuider`
- `VHS_VideoCombine`
- `PreviewImage`
- `LTX2MemoryEfficientSageAttentionPatch`
- `Reroute`
- `PrimitiveFloat`
- `RandomNoise`
- `Int`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeAudio` ★核心
- `easy cleanGpuUsed`
- `Int`
- `GetNode`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `VAEDecodeAudio` ★核心
- `VHS_VideoCombine`
- `BasicScheduler`
- `MiniMaxH3LatentUpscaleCombined`
- `KSamplerSelect` ★核心
- `ImageScaleBy`
- `PrimitiveStringMultiline`
- `BasicScheduler`
- `VHS_VideoCombine`
- `Int`
- `GetImageSize`
- `RandomNoise`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `easy showAnything`
- `KSamplerSelect` ★核心
- `MiniMaxH3ReferenceToVideo`
- `LoadImage`
- `CLIPLoader`
- `VHS_VideoCombine`
- `ComfyMathExpression`
- `LoraLoaderModelOnly` ★核心
- `easy cleanGpuUsed`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `CR Text`
- `ComfyMathExpression`
- `BasicGuider`
- `LoadImage`
- `ComfyMathExpression`
- `PreviewImage`
- `easy forLoopStart`
- `MiniMaxH3ImageToVideo`
- `VAEDecodeAudio` ★核心
- `SetNode`
- `easy cleanGpuUsed`
- `ImageScaleBy`
- `ResolutionSelector`
- `VHS_VideoCombine`
- `VAELoader`
- `MiniMaxH3ReferenceToVideo`
- `VAELoader`
- `VHS_VideoCombine`
- `BasicScheduler`
- `SetNode`
- `easy cleanGpuUsed`
- `SomethingToString`
- `ProcessString`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `JoinStrings`
- `PreviewImage`
- `PreviewAny`
- `CR Prompt Text`
- `TextInput_`
- `ShowText|pysssss`
- `TextInput_`
- `llama_cpp_model_loader`
- `ImageConcatMulti`
- `ImageResize+`
- `ImageResize+`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `Float`
- `MinimaxH3LatentUpscaler3D`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `BasicGuider`
- `LoraLoaderModelOnly` ★核心
- `SLASageAttention`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `SLASageAttention`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `UNETLoader` ★核心
- `ModelAttentionBackend`
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `孤海注释`
- `孤海注释`
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
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **83%**（154/185）

**有卡**：`easy forLoopEnd`、`GetImageSizeAndCount`、`MathExpression|pysssss`、`CLIPTextEncode`、`RandomNoise`、`KSamplerSelect`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`LTXVConcatAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXVEmptyLatentAudio`、`LTXAVTextEncoderLoader`、`LTXVConditioning`、`LTXVCropGuides`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`easy cleanGpuUsed`、`ManualSigmas`、`CheckpointLoaderSimple`、`VAEEncode`、`InjectLatentNoise+`、`LoraLoaderModelOnly`、`LTX2_NAG`、`LTXVPreprocess`、`LTXVAudioVAELoader`、`LTXVAddGuideMulti`、`CFGGuider`、`VHS_VideoCombine`、`LTX2MemoryEfficientSageAttentionPatch`、`Int`、`BasicGuider`、`VAEDecodeAudio`、`VAEDecode`、`BasicScheduler`、`MiniMaxH3LatentUpscaleCombined`、`ImageScaleBy`、`GetImageSize`、`MiniMaxH3ReferenceToVideo`、`LoadImage`、`CLIPLoader`、`ComfyMathExpression`、`CR Text`、`easy forLoopStart`、`MiniMaxH3ImageToVideo`、`ResolutionSelector`、`VAELoader`、`SomethingToString`、`ProcessString`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`JoinStrings`、`CR Prompt Text`、`TextInput_`、`llama_cpp_model_loader`、`ImageConcatMulti`、`ImageResize+`、`Float`、`MinimaxH3LatentUpscaler3D`、`UNETLoader`、`SLASageAttention`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ModelAttentionBackend`、`KSampler`、`solarL_SaveImagesToZip`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
