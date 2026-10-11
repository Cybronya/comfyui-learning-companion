---
key: 视频生成/文生视频/LTX2.3官方工作流_2070310733811896321.json
name: LTX2.3官方工作流_2070310733811896321
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3官方工作流_2070310733811896321.json
hash: 0528c05b0629cd99
coverage: 0.830189
learned_at: 2026-10-11 20:21:27
nodes: [SaveVideo, MarkdownNote, RandomNoise, RandomNoise, LTXVConcatAVLatent, LTXVAudioVAELoader, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LoraLoaderModelOnly, ResizeImagesByLongerEdge, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVPreprocess, ResizeImageMaskNode, KSamplerSelect, ComfyMathExpression, Reroute, ComfyMathExpression, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVAudioVAEDecode, ComfyMathExpression, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveBoolean, CLIPTextEncode, LTXVConditioning, LTXVEmptyLatentAudio, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, CreateVideo, LatentUpscaleModelLoader, PrimitiveInt, CLIPTextEncode, CFGGuider, VAEDecodeTiled, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LTXVConcatAVLatent, ComfyMathExpression, EmptyImage, LoraLoader, TextGenerateLTX2Prompt, PreviewAny, ComfySwitchNode, PrimitiveBoolean, PrimitiveStringMultiline]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "lora_name": "gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors", "strength_clip": 1, "strength_model": 1, "width": 97}
---

# 视频生成/文生视频/LTX2.3官方工作流_2070310733811896321.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3官方工作流_2070310733811896321.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `SaveVideo`
- `MarkdownNote`
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `LTXVAudioVAELoader`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LoraLoaderModelOnly` ★核心
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
- `LTXVAudioVAEDecode` ★核心
- `ComfyMathExpression`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveBoolean`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVEmptyLatentAudio` ★核心
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `CreateVideo`
- `LatentUpscaleModelLoader`
- `PrimitiveInt`
- `CLIPTextEncode` ★核心
- `CFGGuider`
- `VAEDecodeTiled` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `LTXVConcatAVLatent`
- `ComfyMathExpression`
- `EmptyImage`
- `LoraLoader` ★核心
- `TextGenerateLTX2Prompt`
- `PreviewAny`
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`

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

覆盖率 **83%**（44/53）

**有卡**：`SaveVideo`、`RandomNoise`、`LTXVConcatAVLatent`、`LTXVAudioVAELoader`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LoraLoaderModelOnly`、`ResizeImagesByLongerEdge`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVPreprocess`、`ResizeImageMaskNode`、`ComfyMathExpression`、`EmptyLTXVLatentVideo`、`LTXVAudioVAEDecode`、`PrimitiveBoolean`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`CreateVideo`、`LatentUpscaleModelLoader`、`VAEDecodeTiled`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`EmptyImage`、`LoraLoader`、`TextGenerateLTX2Prompt`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
