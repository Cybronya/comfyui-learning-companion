---
key: 视频生成/文生视频/LTX2.3文生视频_2072147459652014081.json
name: LTX2.3文生视频_2072147459652014081
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频_2072147459652014081.json
hash: 4b4e980a6dbb7086
coverage: 0.830189
learned_at: 2026-10-11 20:21:27
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, LTXVAudioVAELoader, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LoraLoaderModelOnly, LTXVLatentUpsampler, LTXVImgToVideoInplace, KSamplerSelect, Reroute, ComfyMathExpression, LTXVAudioVAEDecode, ComfyMathExpression, CLIPTextEncode, LTXVConditioning, ManualSigmas, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, LatentUpscaleModelLoader, CFGGuider, VAEDecodeTiled, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LoraLoader, TextGenerateLTX2Prompt, ComfySwitchNode, PrimitiveBoolean, CLIPTextEncode, PrimitiveBoolean, EmptyImage, ResizeImageMaskNode, ResizeImagesByLongerEdge, LTXVPreprocess, ComfyMathExpression, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVConcatAVLatent, CreateVideo, PreviewAny, SaveVideo, MarkdownNote, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, ComfyMathExpression, PrimitiveStringMultiline]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "lora_name": "gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors", "strength_clip": 1, "strength_model": 1, "width": 97}
---

# 视频生成/文生视频/LTX2.3文生视频_2072147459652014081.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3文生视频_2072147459652014081.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
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
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `KSamplerSelect` ★核心
- `Reroute`
- `ComfyMathExpression`
- `LTXVAudioVAEDecode` ★核心
- `ComfyMathExpression`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `CFGGuider`
- `VAEDecodeTiled` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `LoraLoader` ★核心
- `TextGenerateLTX2Prompt`
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `CLIPTextEncode` ★核心
- `PrimitiveBoolean`
- `EmptyImage`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ComfyMathExpression`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `CreateVideo`
- `PreviewAny`
- `SaveVideo`
- `MarkdownNote`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfyMathExpression`
- `PrimitiveStringMultiline`

**识别到的模式**：lora

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `lora_name` = `gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（44/53）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`LTXVAudioVAELoader`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LoraLoaderModelOnly`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`ComfyMathExpression`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`VAEDecodeTiled`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LoraLoader`、`TextGenerateLTX2Prompt`、`PrimitiveBoolean`、`EmptyImage`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`CreateVideo`、`SaveVideo`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
