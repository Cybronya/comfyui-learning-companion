---
key: 视频生成/图生视频/LTX2.3 i2v 优化版_2030584551327670273.json
name: LTX2.3 i2v 优化版_2030584551327670273.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 i2v 优化版_2030584551327670273.json
hash: e8b19d4fb5b6df09
coverage: 0.846154
learned_at: 2026-10-15 22:35:27
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LTXVLatentUpsampler, KSamplerSelect, Reroute, EmptyLTXVLatentVideo, LTXVAudioVAEDecode, PrimitiveInt, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, MarkdownNote, CreateVideo, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, LTXVConcatAVLatent, ResizeImageMaskNode, LTXVPreprocess, LTXVImgToVideoInplace, PrimitiveInt, ResizeImagesByLongerEdge, CheckpointLoaderSimple, CFGGuider, CLIPTextEncode, LTXVConditioning, LTXVImgToVideoInplace, SaveVideo, PrimitiveInt, PrimitiveInt, LoraLoaderModelOnly, ManualSigmas, llama_cpp_parameters, llama_cpp_model_loader, llama_cpp_instruct_adv, Fast Groups Bypasser (rgthree), ImageResizeKJv2, LoadImage, PrimitiveStringMultiline, CLIPTextEncode, LTX2_NAG]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3 i2v 优化版_2030584551327670273.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2030584551327670273.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（52 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `KSamplerSelect` ★核心
- `Reroute`
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
- `CreateVideo`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `LTXVImgToVideoInplace`
- `PrimitiveInt`
- `ResizeImagesByLongerEdge`
- `CheckpointLoaderSimple` ★核心
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `SaveVideo`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoraLoaderModelOnly` ★核心
- `ManualSigmas`
- `llama_cpp_parameters`
- `llama_cpp_model_loader`
- `llama_cpp_instruct_adv`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`
- `LoadImage`
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `LTX2_NAG`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **85%**（44/52）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`CreateVideo`、`ComfyMathExpression`、`ResizeImageMaskNode`、`LTXVPreprocess`、`LTXVImgToVideoInplace`、`ResizeImagesByLongerEdge`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`LTXVConditioning`、`SaveVideo`、`LoraLoaderModelOnly`、`llama_cpp_parameters`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`ImageResizeKJv2`、`LoadImage`、`LTX2_NAG`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
