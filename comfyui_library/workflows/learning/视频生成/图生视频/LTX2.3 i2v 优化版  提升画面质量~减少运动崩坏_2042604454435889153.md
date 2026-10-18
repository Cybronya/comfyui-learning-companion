---
key: 视频生成/图生视频/LTX2.3 i2v 优化版  提升画面质量~减少运动崩坏_2042604454435889153.json
name: LTX2.3 i2v 优化版  提升画面质量~减少运动崩坏_2042604454435889153.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 i2v 优化版  提升画面质量~减少运动崩坏_2042604454435889153.json
hash: e680e7a76a65df36
coverage: 0.849057
learned_at: 2026-10-15 22:36:28
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, KSamplerSelect, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, PrimitiveInt, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, MarkdownNote, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, LTXVConcatAVLatent, LTXVImgToVideoInplace, PrimitiveInt, ResizeImagesByLongerEdge, CheckpointLoaderSimple, CFGGuider, CLIPTextEncode, LTXVConditioning, SaveVideo, PrimitiveInt, PrimitiveInt, LoraLoaderModelOnly, llama_cpp_parameters, llama_cpp_model_loader, llama_cpp_instruct_adv, Fast Groups Bypasser (rgthree), ImageResizeKJv2, CLIPTextEncode, LTX2_NAG, PrimitiveStringMultiline, LTXVPreprocess, LoadImage, ManualSigmas, Reroute, LatentUpscaleModelLoader, CreateVideo, LTXVLatentUpsampler, LTXVLatentUpsampler, LTXVImgToVideoInplace]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3 i2v 优化版  提升画面质量~减少运动崩坏_2042604454435889153.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2042604454435889153.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `KSamplerSelect` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEDecode` ★核心
- `PrimitiveInt`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `MarkdownNote`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `PrimitiveInt`
- `ResizeImagesByLongerEdge`
- `CheckpointLoaderSimple` ★核心
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `SaveVideo`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoraLoaderModelOnly` ★核心
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`
- `CLIPTextEncode` ★核心
- `LTX2_NAG`
- `PrimitiveStringMultiline`
- `LTXVPreprocess`
- `LoadImage`
- `ManualSigmas`
- `Reroute`
- `LatentUpscaleModelLoader`
- `CreateVideo`
- `LTXVLatentUpsampler` ★核心
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **85%**（45/53）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`ComfyMathExpression`、`LTXVImgToVideoInplace`、`ResizeImagesByLongerEdge`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`LTXVConditioning`、`SaveVideo`、`LoraLoaderModelOnly`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`ImageResizeKJv2`、`LTX2_NAG`、`LTXVPreprocess`、`LoadImage`、`CreateVideo`、`LTXVLatentUpsampler`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
