---
key: 视频生成/文生视频/LTX2.3-文本音频生视频(口型同步)_2031312855026376705.json
name: LTX2.3-文本音频生视频(口型同步)_2031312855026376705
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3-文本音频生视频(口型同步)_2031312855026376705.json
hash: 25cd682eeccd8b68
coverage: 0.821429
learned_at: 2026-10-11 03:16:46
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVImgToVideoInplace, KSamplerSelect, Reroute, LTXVAudioVAEDecode, LTXVConditioning, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, CFGGuider, VAEDecodeTiled, LTXVImgToVideoInplace, SolidMask, LTXVAudioVAELoader, CreateVideo, EmptyLTXVLatentVideo, LTXVAudioVAEEncode, LoraLoaderModelOnly, CheckpointLoaderSimple, LatentUpscaleModelLoader, LTXVCropGuides, LTXVLatentUpsampler, LTXVConcatAVLatent, SetLatentNoiseMask, ResizeImagesByLongerEdge, LTXVPreprocess, SimpleMath+, SimpleMath+, ComfyMathExpression, SimpleMath+, ManualSigmas, ResizeImageMaskNode, LoadImage, LoadImage, PrimitiveInt, TrimAudioDuration, LoadImage, PrimitiveFloat, LTXAVTextEncoderLoader, PrimitiveBoolean, CLIPTextEncode, PreviewAny, PrimitiveInt, PrimitiveInt, SaveVideo, PrimitiveStringMultiline, LoraLoader, CLIPTextEncode, TextGenerateLTX2Prompt, LoadAudio]
patterns: [lora]
missing: [SimpleMath+, SimpleMath+, SimpleMath+]
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "lora_name": "gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors", "strength_clip": 1, "strength_model": 1}
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3-文本音频生视频(口型同步)_2031312855026376705.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3-文本音频生视频(口型同步)_2031312855026376705.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
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
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
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
- `ResizeImageMaskNode`
- `LoadImage`
- `LoadImage`
- `PrimitiveInt`
- `TrimAudioDuration`
- `LoadImage`
- `PrimitiveFloat`
- `LTXAVTextEncoderLoader`
- `PrimitiveBoolean`
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `PrimitiveInt`
- `PrimitiveInt`
- `SaveVideo`
- `PrimitiveStringMultiline`
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `TextGenerateLTX2Prompt`
- `LoadAudio`

**识别到的模式**：lora

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `lora_name` = `gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **82%**（46/56）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVImgToVideoInplace`、`LTXVAudioVAEDecode`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`SolidMask`、`LTXVAudioVAELoader`、`CreateVideo`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEEncode`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`SetLatentNoiseMask`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`ComfyMathExpression`、`ResizeImageMaskNode`、`LoadImage`、`TrimAudioDuration`、`LTXAVTextEncoderLoader`、`PrimitiveBoolean`、`CLIPTextEncode`、`SaveVideo`、`LoraLoader`、`TextGenerateLTX2Prompt`、`LoadAudio`

**缺卡**（3）：`SimpleMath+`、`SimpleMath+`、`SimpleMath+`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler

## 学习发现

- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
