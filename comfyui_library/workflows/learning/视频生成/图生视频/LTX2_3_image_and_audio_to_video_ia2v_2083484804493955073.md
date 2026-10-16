---
key: 视频生成/图生视频/LTX2_3_image_and_audio_to_video_ia2v_2083484804493955073.json
name: LTX2_3_image_and_audio_to_video_ia2v_2083484804493955073
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2_3_image_and_audio_to_video_ia2v_2083484804493955073.json
hash: 4d8df060e6afb024
coverage: 0.830508
learned_at: 2026-10-16 19:17:13
nodes: [RecordAudio, LoadImage, MarkdownNote, RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, KSamplerSelect, Reroute, LTXVAudioVAEDecode, CLIPTextEncode, LTXVConditioning, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, CLIPTextEncode, CFGGuider, VAEDecodeTiled, LTXVImgToVideoInplace, PrimitiveInt, SolidMask, LTXVAudioVAELoader, PrimitiveBoolean, ResizeImagesByLongerEdge, LTXVPreprocess, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, ComfyMathExpression, PrimitiveInt, TrimAudioDuration, LTXVAudioVAEEncode, LTXVConcatAVLatent, SetLatentNoiseMask, LatentUpscaleModelLoader, LoraLoaderModelOnly, CheckpointLoaderSimple, LTXAVTextEncoderLoader, ResizeImageMaskNode, LoraLoader, TextGenerateLTX2Prompt, ComfySwitchNode, PrimitiveBoolean, SaveVideo, PreviewAny, PrimitiveInt, PrimitiveFloat, MarkdownNote, LoadAudio, PrimitiveStringMultiline]
patterns: [lora]
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "lora_name": "gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 视频生成/图生视频/LTX2_3_image_and_audio_to_video_ia2v_2083484804493955073.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2_3_image_and_audio_to_video_ia2v_2083484804493955073.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
- `RecordAudio`
- `LoadImage`
- `MarkdownNote`
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `KSamplerSelect` ★核心
- `Reroute`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `VAEDecodeTiled` ★核心
- `LTXVImgToVideoInplace`
- `PrimitiveInt`
- `SolidMask`
- `LTXVAudioVAELoader`
- `PrimitiveBoolean`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `PrimitiveInt`
- `TrimAudioDuration`
- `LTXVAudioVAEEncode` ★核心
- `LTXVConcatAVLatent`
- `SetLatentNoiseMask`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `ResizeImageMaskNode`
- `LoraLoader` ★核心
- `TextGenerateLTX2Prompt`
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `SaveVideo`
- `PreviewAny`
- `PrimitiveInt`
- `PrimitiveFloat`
- `MarkdownNote`
- `LoadAudio`
- `PrimitiveStringMultiline`

**识别到的模式**：lora

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `lora_name` = `gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **83%**（49/59）

**有卡**：`RecordAudio`、`LoadImage`、`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`SolidMask`、`LTXVAudioVAELoader`、`PrimitiveBoolean`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`ComfyMathExpression`、`CreateVideo`、`EmptyLTXVLatentVideo`、`TrimAudioDuration`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`ResizeImageMaskNode`、`LoraLoader`、`TextGenerateLTX2Prompt`、`SaveVideo`、`LoadAudio`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
