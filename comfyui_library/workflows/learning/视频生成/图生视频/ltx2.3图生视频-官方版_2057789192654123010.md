---
key: 视频生成/图生视频/ltx2.3图生视频-官方版_2057789192654123010.json
name: ltx2.3图生视频-官方版_2057789192654123010.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2057789192654123010.json
hash: fe571ae56a12fce5
coverage: 0.814815
learned_at: 2026-10-15 22:38:16
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, LTXVAudioVAELoader, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, ResizeImagesByLongerEdge, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVPreprocess, ResizeImageMaskNode, KSamplerSelect, ComfyMathExpression, Reroute, ComfyMathExpression, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, ComfyMathExpression, CLIPTextEncode, LTXVConditioning, LTXVEmptyLatentAudio, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LatentUpscaleModelLoader, CFGGuider, CheckpointLoaderSimple, LTXVConcatAVLatent, LoraLoader, TextGenerateLTX2Prompt, PreviewAny, CLIPTextEncode, ComfyMathExpression, ComfySwitchNode, PrimitiveStringMultiline, PrimitiveBoolean, PrimitiveInt, PrimitiveInt, PrimitiveInt, LTXVAudioVAEDecode, VAEDecodeTiled, CreateVideo, LoadImage, PrimitiveInt, SaveVideo, PrimitiveBoolean, LTXAVTextEncoderLoader, SetNode, GetNode, LoraLoaderModelOnly]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "lora_name": "gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors", "strength_clip": 1, "strength_model": 1, "width": 97}
---

# 视频生成/图生视频/ltx2.3图生视频-官方版_2057789192654123010.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2057789192654123010.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `LTXVAudioVAELoader`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `ResizeImagesByLongerEdge`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `ResizeImageMaskNode`
- `KSamplerSelect` ★核心
- `ComfyMathExpression`
- `Reroute`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `ComfyMathExpression`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVEmptyLatentAudio` ★核心
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `CFGGuider`
- `CheckpointLoaderSimple` ★核心
- `LTXVConcatAVLatent`
- `LoraLoader` ★核心
- `TextGenerateLTX2Prompt`
- `PreviewAny`
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `ComfySwitchNode`
- `PrimitiveStringMultiline`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `CreateVideo`
- `LoadImage`
- `PrimitiveInt`
- `SaveVideo`
- `PrimitiveBoolean`
- `LTXAVTextEncoderLoader`
- `SetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：lora

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `lora_name` = `gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **81%**（44/54）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`LTXVAudioVAELoader`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`ResizeImagesByLongerEdge`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVPreprocess`、`ResizeImageMaskNode`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`CheckpointLoaderSimple`、`LoraLoader`、`TextGenerateLTX2Prompt`、`PrimitiveBoolean`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`CreateVideo`、`LoadImage`、`SaveVideo`、`LTXAVTextEncoderLoader`、`LoraLoaderModelOnly`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
