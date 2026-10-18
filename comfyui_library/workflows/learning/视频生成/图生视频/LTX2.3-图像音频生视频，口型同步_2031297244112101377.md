---
key: 视频生成/图生视频/LTX2.3-图像音频生视频，口型同步_2031297244112101377.json
name: LTX2.3-图像音频生视频，口型同步_2031297244112101377.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-图像音频生视频，口型同步_2031297244112101377.json
hash: 238009e7e2fe254d
coverage: 0.875
learned_at: 2026-10-15 22:35:30
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVImgToVideoInplace, KSamplerSelect, Reroute, LTXVAudioVAEDecode, CLIPTextEncode, LTXVConditioning, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, CLIPTextEncode, CFGGuider, VAEDecodeTiled, LTXVImgToVideoInplace, SolidMask, LTXVAudioVAELoader, EmptyLTXVLatentVideo, LTXVAudioVAEEncode, LoraLoaderModelOnly, CheckpointLoaderSimple, PreviewAny, LatentUpscaleModelLoader, LTXVCropGuides, LTXVLatentUpsampler, LTXVConcatAVLatent, SetLatentNoiseMask, ResizeImagesByLongerEdge, LTXVPreprocess, SimpleMath+, SimpleMath+, ComfyMathExpression, SimpleMath+, ManualSigmas, PrimitiveStringMultiline, PrimitiveFloat, LTXAVTextEncoderLoader, TextGenerateLTX2Prompt, LoraLoader, LoadImage, LoadImage, LoadAudio, PrimitiveInt, PrimitiveBoolean, PrimitiveInt, PrimitiveInt, TrimAudioDuration, ImageResize+, LoadImage, CreateVideo, SaveVideo]
patterns: [lora]
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "lora_name": "gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 视频生成/图生视频/LTX2.3-图像音频生视频，口型同步_2031297244112101377.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2031297244112101377.json`

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
- `PrimitiveStringMultiline`
- `PrimitiveFloat`
- `LTXAVTextEncoderLoader`
- `TextGenerateLTX2Prompt`
- `LoraLoader` ★核心
- `LoadImage`
- `LoadImage`
- `LoadAudio`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveInt`
- `TrimAudioDuration`
- `ImageResize+`
- `LoadImage`
- `CreateVideo`
- `SaveVideo`

**识别到的模式**：lora

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `lora_name` = `gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **88%**（49/56）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVImgToVideoInplace`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`SolidMask`、`LTXVAudioVAELoader`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEEncode`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`SetLatentNoiseMask`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`SimpleMath+`、`ComfyMathExpression`、`LTXAVTextEncoderLoader`、`TextGenerateLTX2Prompt`、`LoraLoader`、`LoadImage`、`LoadAudio`、`PrimitiveBoolean`、`TrimAudioDuration`、`ImageResize+`、`CreateVideo`、`SaveVideo`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
