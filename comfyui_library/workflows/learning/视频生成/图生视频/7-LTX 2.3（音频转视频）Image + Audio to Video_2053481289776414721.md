---
key: 视频生成/图生视频/7-LTX 2.3（音频转视频）Image + Audio to Video_2053481289776414721.json
name: 7-LTX 2.3（音频转视频）Image + Audio to Video_2053481289776414721.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/7-LTX 2.3（音频转视频）Image + Audio to Video_2053481289776414721.json
hash: 636900ba93cd73de
coverage: 0.859649
learned_at: 2026-10-15 22:37:39
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, KSamplerSelect, Reroute, LTXVAudioVAEDecode, LTXVConditioning, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, CLIPTextEncode, SolidMask, PrimitiveBoolean, ResizeImagesByLongerEdge, LTXVPreprocess, PrimitiveInt, EmptyLTXVLatentVideo, LTXVAudioVAEEncode, LTXVConcatAVLatent, SetLatentNoiseMask, LoraLoader, LTXVImgToVideoInplace, TrimAudioDuration, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, PreviewAny, CreateVideo, easy cleanGpuUsed, easy clearCacheAll, TextGenerateLTX2Prompt, CFGGuider, CFGGuider, CLIPTextEncode, SaveVideo, PrimitiveFloat, PrimitiveInt, PrimitiveInt, VAEDecode, PrimitiveStringMultiline, LoadImage, LoadAudio, CheckpointLoaderSimple, LTXVAudioVAELoader, LoraLoaderModelOnly, Note, LTXAVTextEncoderLoader, LatentUpscaleModelLoader, ResizeImageMaskNode]
patterns: [lora]
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev.safetensors", "lora_name": "gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 视频生成/图生视频/7-LTX 2.3（音频转视频）Image + Audio to Video_2053481289776414721.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2053481289776414721.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `KSamplerSelect` ★核心
- `Reroute`
- `LTXVAudioVAEDecode` ★核心
- `LTXVConditioning`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `SolidMask`
- `PrimitiveBoolean`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `PrimitiveInt`
- `EmptyLTXVLatentVideo`
- `LTXVAudioVAEEncode` ★核心
- `LTXVConcatAVLatent`
- `SetLatentNoiseMask`
- `LoraLoader` ★核心
- `LTXVImgToVideoInplace`
- `TrimAudioDuration`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PreviewAny`
- `CreateVideo`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `TextGenerateLTX2Prompt`
- `CFGGuider`
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `SaveVideo`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveInt`
- `VAEDecode` ★核心
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadAudio`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `LTXAVTextEncoderLoader`
- `LatentUpscaleModelLoader`
- `ResizeImageMaskNode`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **86%**（49/57）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`CLIPTextEncode`、`SolidMask`、`PrimitiveBoolean`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`LoraLoader`、`TrimAudioDuration`、`ComfyMathExpression`、`CreateVideo`、`easy cleanGpuUsed`、`easy clearCacheAll`、`TextGenerateLTX2Prompt`、`CFGGuider`、`SaveVideo`、`VAEDecode`、`LoadImage`、`LoadAudio`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LoraLoaderModelOnly`、`LTXAVTextEncoderLoader`、`LatentUpscaleModelLoader`、`ResizeImageMaskNode`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
