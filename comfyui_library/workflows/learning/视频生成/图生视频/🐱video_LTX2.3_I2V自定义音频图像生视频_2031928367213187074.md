---
key: 视频生成/图生视频/🐱video_LTX2.3_I2V自定义音频图像生视频_2031928367213187074.json
name: 🐱video_LTX2.3_I2V自定义音频图像生视频_2031928367213187074.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2031928367213187074.json
hash: 69036d938f698bd2
coverage: 0.877193
learned_at: 2026-10-15 22:35:33
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, KSamplerSelect, Reroute, LTXVConditioning, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, CFGGuider, LTXVImgToVideoInplace, SolidMask, LTXVConcatAVLatent, SetLatentNoiseMask, LatentUpscaleModelLoader, LoraLoader, LoraLoaderModelOnly, VAEDecodeTiled, LTXVAudioVAEDecode, CreateVideo, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, LayerUtility: ImageScaleByAspectRatio V2, ResizeImagesByLongerEdge, LTXVPreprocess, CLIPTextEncode, SaveVideo, ComfyMathExpression, EmptyLTXVLatentVideo, ComfyMathExpression, LTXVAudioVAEEncode, Qwen3ASRLoader_DFT, PreviewAny, CLIPTextEncode, Qwen3ASRTranscribe_DFT, TrimAudioDuration, PreviewAny, LoadImage, PrimitiveFloat, PrimitiveInt, PrimitiveInt, LoadAudio, PrimitiveBoolean, TextGenerateLTX2Prompt, RH_LLMAPI_Pro_Node]
patterns: [lora]
missing: []
parameters: {"checkpoint": "ltx-2.3-22b-dev.safetensors", "lora_name": "gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors", "strength_clip": 1, "strength_model": 1}
---

# 视频生成/图生视频/🐱video_LTX2.3_I2V自定义音频图像生视频_2031928367213187074.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2031928367213187074.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
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
- `LTXVConditioning`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `LTXVImgToVideoInplace`
- `SolidMask`
- `LTXVConcatAVLatent`
- `SetLatentNoiseMask`
- `LatentUpscaleModelLoader`
- `LoraLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `CLIPTextEncode` ★核心
- `SaveVideo`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `LTXVAudioVAEEncode` ★核心
- `Qwen3ASRLoader_DFT`
- `PreviewAny`
- `CLIPTextEncode` ★核心
- `Qwen3ASRTranscribe_DFT`
- `TrimAudioDuration`
- `PreviewAny`
- `LoadImage`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadAudio`
- `PrimitiveBoolean`
- `TextGenerateLTX2Prompt`
- `RH_LLMAPI_Pro_Node`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **88%**（50/57）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`SolidMask`、`SetLatentNoiseMask`、`LatentUpscaleModelLoader`、`LoraLoader`、`LoraLoaderModelOnly`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`CreateVideo`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`ComfyMathExpression`、`LayerUtility: ImageScaleByAspectRatio V2`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`CLIPTextEncode`、`SaveVideo`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEEncode`、`Qwen3ASRLoader_DFT`、`Qwen3ASRTranscribe_DFT`、`TrimAudioDuration`、`LoadImage`、`LoadAudio`、`PrimitiveBoolean`、`TextGenerateLTX2Prompt`、`RH_LLMAPI_Pro_Node`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
