---
key: 视频生成/图生视频/LTX2.3-三段采样-- 视频质感飙升秒变大片_2041110942255161346.json
name: LTX2.3-三段采样-- 视频质感飙升秒变大片_2041110942255161346.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2041110942255161346.json
hash: f5558c68bde10088
coverage: 0.5
learned_at: 2026-10-15 22:36:18
nodes: [SetNode, SetNode, SetNode, GetNode, SetNode, GetNode, SetNode, SetNode, SetNode, LTXVPreprocess, SetNode, GetNode, GetNode, ComfyMathExpression, LTXVCropGuides, LTXVSeparateAVLatent, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, SamplerCustomAdvanced, CFGGuider, VAELoaderKJ, SamplerCustomAdvanced, CFGGuider, ManualSigmas, VAELoaderKJ, GetNode, GetNode, ComfyMathExpression, GetNode, GetNode, UNETLoader, KSamplerSelect, GetNode, ComfyMathExpression, LTXVSeparateAVLatent, RandomNoise, GetNode, GetNode, GetNode, ComfyMathExpression, SamplerCustomAdvanced, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, GetNode, GetNode, GetNode, LTXVImgToVideoInplace, GetNode, LTXVLatentUpsampler, VAEDecodeTiled, VHS_VideoCombine, DualCLIPLoader, SetNode, GetNode, GetNode, GetNode, GetNode, CLIPTextEncode, ComfyMathExpression, LTXVConditioning, SetNode, SetNode, LoraLoader, CLIPTextEncode, SetNode, GetNode, GetNode, SetNode, SetNode, LTXVConcatAVLatent, LTXVImgToVideoInplace, SetNode, GetNode, GetNode, GetNode, ResizeImagesByLongerEdge, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, ImageResizeKJv2, PrimitiveInt, PrimitiveInt, PrimitiveInt, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVSeparateAVLatent, LoadImage, LatentUpscaleModelLoader, LTXVAudioVAEDecode, PrimitiveInt, RandomNoise, PrimitiveStringMultiline]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "height": 25, "lora_name": "gemma-3-12b-it-abliterated_heretic_lora_rank64_bf16.safetensors", "strength_clip": 1, "strength_model": 1, "width": 97}
---

# 视频生成/图生视频/LTX2.3-三段采样-- 视频质感飙升秒变大片_2041110942255161346.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2041110942255161346.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（102 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXVPreprocess`
- `SetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `VAELoaderKJ`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `ManualSigmas`
- `VAELoaderKJ`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `KSamplerSelect` ★核心
- `GetNode`
- `ComfyMathExpression`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplace`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `DualCLIPLoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `LTXVConditioning`
- `SetNode`
- `SetNode`
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ResizeImagesByLongerEdge`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LatentUpscaleModelLoader`
- `LTXVAudioVAEDecode` ★核心
- `PrimitiveInt`
- `RandomNoise`
- `PrimitiveStringMultiline`

**识别到的模式**：lora

## 关键参数

- `lora_name` = `gemma-3-12b-it-abliterated_heretic_lora_rank64_bf16.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **50%**（51/102）

**有卡**：`LTXVPreprocess`、`ComfyMathExpression`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`KSamplerSelect`、`ManualSigmas`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`CFGGuider`、`VAELoaderKJ`、`UNETLoader`、`RandomNoise`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`VHS_VideoCombine`、`DualCLIPLoader`、`CLIPTextEncode`、`LTXVConditioning`、`LoraLoader`、`ResizeImagesByLongerEdge`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`ImageResizeKJv2`、`LoadImage`、`LatentUpscaleModelLoader`、`LTXVAudioVAEDecode`

**用到的条目**：CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
