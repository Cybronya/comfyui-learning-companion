---
key: 视频生成/图生视频/LTX2.3& qwen3.6提示词图生视频_2089610911387574273.json
name: LTX2.3& qwen3.6提示词图生视频_2089610911387574273
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3& qwen3.6提示词图生视频_2089610911387574273.json
hash: bef522394cdab41f
coverage: 0.918367
learned_at: 2026-10-16 22:01:58
nodes: [KSamplerSelect, LTXVScheduler, SamplerCustomAdvanced, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LTXVImgToVideoInplace, LTXVConcatAVLatent, EmptyLTXVLatentVideo, VAEDecode, LTXVSeparateAVLatent, LTXVAudioVAEDecode, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVConcatAVLatent, LTXVCropGuides, CreateVideo, RandomNoise, LTXVAudioVAELoader, KSampler, PreviewAny, easy saveText, llama_cpp_parameters, MarkdownNote, MarkdownNote, LoraLoaderModelOnly, CLIPTextEncode, LoraLoaderModelOnly, CFGGuider, SaveVideo, llama_cpp_model_loader, CLIPTextEncode, Int, Int, PrimitiveInt, EmptyImage, ImageScaleBy, GetImageSize, GetImageSize, LTXVEmptyLatentAudio, ResizeImagesByLongerEdge, LTXVPreprocess, LTXVConditioning, CheckpointLoaderSimple, LTXAVTextEncoderLoader, Text, LoadImage, Text, ResizeImageMaskNode, llama_cpp_instruct_adv]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.35, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 193667285183299, "steps": 4, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.3& qwen3.6提示词图生视频_2089610911387574273.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3& qwen3.6提示词图生视频_2089610911387574273.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `EmptyLTXVLatentVideo`
- `VAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `CreateVideo`
- `RandomNoise`
- `LTXVAudioVAELoader`
- `KSampler` ★核心
- `PreviewAny`
- `easy saveText`
- `llama_cpp_parameters`
- `MarkdownNote`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CFGGuider`
- `SaveVideo`
- `llama_cpp_model_loader`
- `CLIPTextEncode` ★核心
- `Int`
- `Int`
- `PrimitiveInt`
- `EmptyImage`
- `ImageScaleBy`
- `GetImageSize`
- `GetImageSize`
- `LTXVEmptyLatentAudio` ★核心
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LTXVConditioning`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `Text`
- `LoadImage`
- `Text`
- `ResizeImageMaskNode`
- `llama_cpp_instruct_adv`

## 关键参数

- `seed` = `193667285183299`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.35`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **92%**（45/49）

**有卡**：`KSamplerSelect`、`LTXVScheduler`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`LTXVImgToVideoInplace`、`LTXVConcatAVLatent`、`EmptyLTXVLatentVideo`、`VAEDecode`、`LTXVAudioVAEDecode`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`CreateVideo`、`RandomNoise`、`LTXVAudioVAELoader`、`KSampler`、`easy saveText`、`llama_cpp_parameters`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`CFGGuider`、`SaveVideo`、`llama_cpp_model_loader`、`Int`、`EmptyImage`、`ImageScaleBy`、`GetImageSize`、`LTXVEmptyLatentAudio`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LTXVConditioning`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`Text`、`LoadImage`、`ResizeImageMaskNode`、`llama_cpp_instruct_adv`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
