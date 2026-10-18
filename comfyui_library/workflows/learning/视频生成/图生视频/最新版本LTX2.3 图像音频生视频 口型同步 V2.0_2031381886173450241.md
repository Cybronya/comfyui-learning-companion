---
key: 视频生成/图生视频/最新版本LTX2.3 图像音频生视频 口型同步 V2.0_2031381886173450241.json
name: 最新版本LTX2.3 图像音频生视频 口型同步 V2.0_2031381886173450241.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/最新版本LTX2.3 图像音频生视频 口型同步 V2.0_2031381886173450241.json
hash: c4204339a0a40884
coverage: 0.87037
learned_at: 2026-10-15 22:35:31
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVImgToVideoInplace, KSamplerSelect, Reroute, LTXVAudioVAEDecode, CLIPTextEncode, LTXVConditioning, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, CLIPTextEncode, CFGGuider, VAEDecodeTiled, LTXVImgToVideoInplace, SolidMask, LTXVAudioVAELoader, CreateVideo, EmptyLTXVLatentVideo, LTXVAudioVAEEncode, LoraLoaderModelOnly, CheckpointLoaderSimple, PreviewAny, LatentUpscaleModelLoader, LTXVCropGuides, LTXVLatentUpsampler, LTXVConcatAVLatent, SetLatentNoiseMask, ResizeImagesByLongerEdge, LTXVPreprocess, SimpleMath+, SimpleMath+, ComfyMathExpression, SimpleMath+, ManualSigmas, TrimAudioDuration, LTXAVTextEncoderLoader, PrimitiveInt, PrimitiveInt, SaveVideo, ResizeImageMaskNode, TextGenerateLTX2Prompt, LoraLoader, LoadImage, PrimitiveInt, PrimitiveBoolean, LoadAudio, PrimitiveFloat, PrimitiveStringMultiline]
patterns: [lora]
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "lora_name": "gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 视频生成/图生视频/最新版本LTX2.3 图像音频生视频 口型同步 V2.0_2031381886173450241.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2031381886173450241.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVImgToVideoInplace`
- `KSamplerSelect` ★核心
- `Reroute`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `VAEDecodeTiled` ★核心
- `LTXVImgToVideoInplace`
- `SolidMask`
- `LTXVAudioVAELoader`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `PreviewAny`
- `LatentUpscaleModelLoader`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `SetLatentNoiseMask`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `SimpleMath+`
- `SimpleMath+`
- `ComfyMathExpression`
- `SimpleMath+`
- `ManualSigmas`
- `TrimAudioDuration`
- `LTXAVTextEncoderLoader`
- `PrimitiveInt`
- `PrimitiveInt`
- `SaveVideo`
- `ResizeImageMaskNode`
- `TextGenerateLTX2Prompt`
- `LoraLoader` ★核心
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `LoadAudio`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`

**识别到的模式**：lora

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `lora_name` = `gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **87%**（47/54）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVImgToVideoInplace`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`SolidMask`、`LTXVAudioVAELoader`、`CreateVideo`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEEncode`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`SetLatentNoiseMask`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`SimpleMath+`、`ComfyMathExpression`、`TrimAudioDuration`、`LTXAVTextEncoderLoader`、`SaveVideo`、`ResizeImageMaskNode`、`TextGenerateLTX2Prompt`、`LoraLoader`、`LoadImage`、`PrimitiveBoolean`、`LoadAudio`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
