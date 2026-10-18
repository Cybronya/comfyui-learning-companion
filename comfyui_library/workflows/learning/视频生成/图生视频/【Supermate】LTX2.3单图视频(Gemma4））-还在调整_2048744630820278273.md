---
key: 视频生成/图生视频/【Supermate】LTX2.3单图视频(Gemma4））-还在调整_2048744630820278273.json
name: 【Supermate】LTX2.3单图视频(Gemma4））-还在调整_2048744630820278273.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【Supermate】LTX2.3单图视频(Gemma4））-还在调整_2048744630820278273.json
hash: a0f653ca9d411cfc
coverage: 0.898305
learned_at: 2026-10-15 22:37:11
nodes: [LTXVConditioning, PreviewAny, easy saveText, llama_cpp_parameters, llama_cpp_model_loader, llama_cpp_instruct_adv, Text, Text, llama_cpp_instruct_adv, MarkdownNote, Label (rgthree), LoraLoaderModelOnly, LTXVScheduler, easy cleanGpuUsed, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LTXVImgToVideoInplace, Int, Int, LoadImage, CLIPTextEncode, easy showAnything, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, VAEDecode, LTXVSeparateAVLatent, LTXVAudioVAEDecode, easy cleanGpuUsed, KSampler, LTXVConcatAVLatent, MarkdownNote, LTXVLatentUpsampler, LTXVImgToVideoInplace, SaveVideo, ResizeImageMaskNode, EmptyLTXVLatentVideo, LTXVEmptyLatentAudio, GetImageSize, ImageScaleBy, EmptyImage, ResizeImagesByLongerEdge, LTXVPreprocess, LTXVConcatAVLatent, GetImageSize, LTXVCropGuides, LTXVSeparateAVLatent, easy cleanGpuUsed, LatentUpscaleModelLoader, CLIPTextEncode, Note, Text, CFGGuider, PrimitiveInt, CreateVideo, llama_cpp_parameters, llama_cpp_model_loader, Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.35, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 343810310006004, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/【Supermate】LTX2.3单图视频(Gemma4））-还在调整_2048744630820278273.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2048744630820278273.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
- `LTXVConditioning`
- `PreviewAny`
- `easy saveText`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `Text`
- `Text`
- `llama_cpp_instruct_adv`
- `MarkdownNote`
- `Label (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `LTXVScheduler`
- `easy cleanGpuUsed`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LTXVImgToVideoInplace`
- `Int`
- `Int`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `LTXVConcatAVLatent`
- `MarkdownNote`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `SaveVideo`
- `ResizeImageMaskNode`
- `EmptyLTXVLatentVideo`
- `LTXVEmptyLatentAudio` ★核心
- `GetImageSize`
- `ImageScaleBy`
- `EmptyImage`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LTXVConcatAVLatent`
- `GetImageSize`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `easy cleanGpuUsed`
- `LatentUpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `Note`
- `Text`
- `CFGGuider`
- `PrimitiveInt`
- `CreateVideo`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `Text`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `343810310006004`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.35`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **90%**（53/59）

**有卡**：`LTXVConditioning`、`easy saveText`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`Text`、`Label (rgthree)`、`LoraLoaderModelOnly`、`LTXVScheduler`、`easy cleanGpuUsed`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LTXVImgToVideoInplace`、`Int`、`LoadImage`、`CLIPTextEncode`、`KSamplerSelect`、`RandomNoise`、`SamplerCustomAdvanced`、`VAEDecode`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`KSampler`、`LTXVConcatAVLatent`、`LTXVLatentUpsampler`、`SaveVideo`、`ResizeImageMaskNode`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`GetImageSize`、`ImageScaleBy`、`EmptyImage`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LTXVCropGuides`、`LatentUpscaleModelLoader`、`CFGGuider`、`CreateVideo`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
