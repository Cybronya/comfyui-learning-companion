---
key: 视频生成/图生视频/多图参考-LTX2.3图生视频_2042794910578905089.json
name: 多图参考-LTX2.3图生视频_2042794910578905089.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/多图参考-LTX2.3图生视频_2042794910578905089.json
hash: b5dd731296c8236e
coverage: 0.836364
learned_at: 2026-10-15 22:36:29
nodes: [RandomNoise, LTXVConcatAVLatent, KSamplerSelect, CFGGuider, SamplerCustomAdvanced, LTXVSeparateAVLatent, ManualSigmas, ManualSigmas, LTXVSeparateAVLatent, RandomNoise, CFGGuider, LTXVAudioVAEDecode, VAEDecodeTiled, CLIPTextEncode, PrimitiveInt, PrimitiveInt, PrimitiveInt, LoraLoader, ImageResizeKJv2, LoadImage, LoadImage, LoadImage, LTXVPreprocess, ResizeImagesByLongerEdge, LTXVPreprocess, ResizeImagesByLongerEdge, LTXVPreprocess, ImageResizeKJv2, ResizeImagesByLongerEdge, ImageResizeKJv2, CheckpointLoaderSimple, LoraLoaderModelOnly, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, Fast Groups Bypasser (rgthree), Reroute, VHS_VideoCombine, TextGenerateLTX2Prompt, PreviewAny, Fast Groups Bypasser (rgthree), KSamplerSelect, SamplerCustomAdvanced, LTXVCropGuides, LTXVConditioning, LTX2_NAG, LTXVLatentUpsampler, LTXVConcatAVLatent, PrimitiveInt, Int, Int, LTXVImgToVideoInplace, RHHiddenNodes, CLIPTextEncode, PrimitiveStringMultiline]
patterns: [lora]
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "lora_name": "gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 视频生成/图生视频/多图参考-LTX2.3图生视频_2042794910578905089.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2042794910578905089.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（55 个）：
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `CFGGuider`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoraLoader` ★核心
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LTXVPreprocess`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ImageResizeKJv2`
- `ResizeImagesByLongerEdge`
- `ImageResizeKJv2`
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `Fast Groups Bypasser (rgthree)`
- `Reroute`
- `VHS_VideoCombine`
- `TextGenerateLTX2Prompt`
- `PreviewAny`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LTXVConditioning`
- `LTX2_NAG`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `PrimitiveInt`
- `Int`
- `Int`
- `LTXVImgToVideoInplace`
- `RHHiddenNodes`
- `CLIPTextEncode` ★核心
- `PrimitiveStringMultiline`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **84%**（46/55）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`ManualSigmas`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`CLIPTextEncode`、`LoraLoader`、`ImageResizeKJv2`、`LoadImage`、`LTXVPreprocess`、`ResizeImagesByLongerEdge`、`CheckpointLoaderSimple`、`LoraLoaderModelOnly`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`VHS_VideoCombine`、`TextGenerateLTX2Prompt`、`LTXVCropGuides`、`LTXVConditioning`、`LTX2_NAG`、`LTXVLatentUpsampler`、`Int`、`LTXVImgToVideoInplace`、`RHHiddenNodes`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
