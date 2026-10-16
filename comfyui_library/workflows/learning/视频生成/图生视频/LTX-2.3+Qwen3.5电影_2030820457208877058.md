---
key: 视频生成/图生视频/LTX-2.3+Qwen3.5电影_2030820457208877058.json
name: LTX-2.3+Qwen3.5电影_2030820457208877058.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2030820457208877058.json
hash: 1c35c0ff420f613c
coverage: 0.918367
learned_at: 2026-10-15 22:35:27
nodes: [LTXVConcatAVLatent, LTXVAudioVAELoader, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, LTXVCropGuides, LoraLoaderModelOnly, LTXVLatentUpsampler, LTXVImgToVideoInplace, KSamplerSelect, Reroute, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, LTXVEmptyLatentAudio, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LatentUpscaleModelLoader, CLIPTextEncode, CFGGuider, VAEDecodeTiled, LTXVPreprocess, CreateVideo, ComfyMathExpression, LTXAVTextEncoderLoader, CheckpointLoaderSimple, RandomNoise, RandomNoise, CFGGuider, PrimitiveBoolean, SaveVideo, MarkdownNote, ResizeImagesByLongerEdge, QZ_ResolutionPreset, ResizeImageMaskNode, PrimitiveInt, PrimitiveInt, llama_cpp_model_loader, llama_cpp_parameters, llama_cpp_instruct_adv, ComfyMathExpression, ComfyMathExpression, LTXVImgToVideoInplace, LTXVConcatAVLatent, CLIPTextEncode, LTXVConditioning, LoadImage, CR Text]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX-2.3+Qwen3.5电影_2030820457208877058.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2030820457208877058.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `LTXVConcatAVLatent`
- `LTXVAudioVAELoader`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LoraLoaderModelOnly` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `KSamplerSelect` ★核心
- `Reroute`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEDecode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `VAEDecodeTiled` ★核心
- `LTXVPreprocess`
- `CreateVideo`
- `ComfyMathExpression`
- `LTXAVTextEncoderLoader`
- `CheckpointLoaderSimple` ★核心
- `RandomNoise`
- `RandomNoise`
- `CFGGuider`
- `PrimitiveBoolean`
- `SaveVideo`
- `MarkdownNote`
- `ResizeImagesByLongerEdge`
- `QZ_ResolutionPreset`
- `ResizeImageMaskNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`
- `llama_cpp_instruct_adv`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LoadImage`
- `CR Text`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **92%**（45/49）

**有卡**：`LTXVConcatAVLatent`、`LTXVAudioVAELoader`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LoraLoaderModelOnly`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`CLIPTextEncode`、`CFGGuider`、`VAEDecodeTiled`、`LTXVPreprocess`、`CreateVideo`、`ComfyMathExpression`、`LTXAVTextEncoderLoader`、`CheckpointLoaderSimple`、`RandomNoise`、`PrimitiveBoolean`、`SaveVideo`、`ResizeImagesByLongerEdge`、`QZ_ResolutionPreset`、`ResizeImageMaskNode`、`llama_cpp_model_loader`、`llama_cpp_parameters`、`llama_cpp_instruct_adv`、`LTXVConditioning`、`LoadImage`、`CR Text`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
