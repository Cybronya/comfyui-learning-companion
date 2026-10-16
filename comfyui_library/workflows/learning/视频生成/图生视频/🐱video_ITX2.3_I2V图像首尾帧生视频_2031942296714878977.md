---
key: 视频生成/图生视频/🐱video_ITX2.3_I2V图像首尾帧生视频_2031942296714878977.json
name: 🐱video_ITX2.3_I2V图像首尾帧生视频_2031942296714878977.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2031942296714878977.json
hash: 288070b435a17162
coverage: 0.888889
learned_at: 2026-10-15 22:35:34
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, KSamplerSelect, Reroute, LTXVConditioning, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, CFGGuider, TextGenerateLTX2Prompt, LoraLoader, LoraLoaderModelOnly, VAEDecodeTiled, LTXVAudioVAEDecode, LTXAVTextEncoderLoader, PrimitiveBoolean, CLIPTextEncode, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, ResizeImagesByLongerEdge, LTXVPreprocess, ResizeImagesByLongerEdge, LTXVPreprocess, LTXVAudioVAELoader, CheckpointLoaderSimple, CLIPTextEncode, LoadImage, LTXVImgToVideoInplaceKJ, LTXVConcatAVLatent, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveInt, PrimitiveInt, LayerUtility: ImageScaleByAspectRatio V2, PrimitiveFloat, PreviewAny, LatentUpscaleModelLoader, RH_LLMAPI_Pro_Node, SaveVideo, CreateVideo]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "lora_name": "gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors", "strength_clip": 1, "strength_model": 1, "width": 97}
---

# 视频生成/图生视频/🐱video_ITX2.3_I2V图像首尾帧生视频_2031942296714878977.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2031942296714878977.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
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
- `TextGenerateLTX2Prompt`
- `LoraLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `LTXAVTextEncoderLoader`
- `PrimitiveBoolean`
- `CLIPTextEncode` ★核心
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LTXVImgToVideoInplaceKJ`
- `LTXVConcatAVLatent`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveInt`
- `PrimitiveInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PrimitiveFloat`
- `PreviewAny`
- `LatentUpscaleModelLoader`
- `RH_LLMAPI_Pro_Node`
- `SaveVideo`
- `CreateVideo`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **89%**（48/54）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`TextGenerateLTX2Prompt`、`LoraLoader`、`LoraLoaderModelOnly`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`LTXAVTextEncoderLoader`、`PrimitiveBoolean`、`CLIPTextEncode`、`ComfyMathExpression`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`LoadImage`、`LTXVImgToVideoInplaceKJ`、`LayerUtility: ImageScaleByAspectRatio V2`、`LatentUpscaleModelLoader`、`RH_LLMAPI_Pro_Node`、`SaveVideo`、`CreateVideo`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
