---
key: 视频生成/文生视频/Y-LTX-2.3-Image or Text to Video -Workflow_2033882686305079298.json
name: Y-LTX-2.3-Image or Text to Video -Workflow_2033882686305079298
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Y-LTX-2.3-Image or Text to Video -Workflow_2033882686305079298.json
hash: da47c90906c16b6c
coverage: 0.811321
learned_at: 2026-10-15 22:47:17
nodes: [LTXVConcatAVLatent, LTXVAudioVAELoader, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LoraLoaderModelOnly, KSamplerSelect, Reroute, EmptyLTXVLatentVideo, SamplerCustomAdvanced, LatentUpscaleModelLoader, CFGGuider, PreviewAny, LTXVEmptyLatentAudio, LTXVConcatAVLatent, RandomNoise, LTXVSeparateAVLatent, LTXVLatentUpsampler, RandomNoise, LTXVAudioVAEDecode, CreateVideo, ManualSigmas, LTXVSeparateAVLatent, VAEDecodeTiled, ComfyMathExpression, ComfyMathExpression, SaveVideo, TextGenerateLTX2Prompt, CLIPTextEncode, LTXVConditioning, LTXAVTextEncoderLoader, LoraLoader, CheckpointLoaderSimple, LTXVImgToVideoInplace, LTXVImgToVideoInplace, Note, PrimitiveBoolean, PrimitiveStringMultiline, CLIPTextEncode, ResizeImagesByLongerEdge, LTXVPreprocess, LoadImage, PrimitiveInt, PrimitiveInt, PrimitiveInt, Note, PrimitiveInt, ComfyMathExpression, GetImageSize, ResizeImageMaskNode, Note]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "lora_name": "gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors", "strength_clip": 1, "strength_model": 1, "width": 97}
---

# 视频生成/文生视频/Y-LTX-2.3-Image or Text to Video -Workflow_2033882686305079298.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Y-LTX-2.3-Image or Text to Video -Workflow_2033882686305079298.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `LTXVConcatAVLatent`
- `LTXVAudioVAELoader`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `Reroute`
- `EmptyLTXVLatentVideo`
- `SamplerCustomAdvanced` ★核心
- `LatentUpscaleModelLoader`
- `CFGGuider`
- `PreviewAny`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVLatentUpsampler` ★核心
- `RandomNoise`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `SaveVideo`
- `TextGenerateLTX2Prompt`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXAVTextEncoderLoader`
- `LoraLoader` ★核心
- `CheckpointLoaderSimple` ★核心
- `LTXVImgToVideoInplace`
- `LTXVImgToVideoInplace`
- `Note`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `Note`
- `PrimitiveInt`
- `ComfyMathExpression`
- `GetImageSize`
- `ResizeImageMaskNode`
- `Note`

**识别到的模式**：lora

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `lora_name` = `gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **81%**（43/53）

**有卡**：`LTXVConcatAVLatent`、`LTXVAudioVAELoader`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LoraLoaderModelOnly`、`EmptyLTXVLatentVideo`、`LatentUpscaleModelLoader`、`LTXVEmptyLatentAudio`、`RandomNoise`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`CreateVideo`、`VAEDecodeTiled`、`ComfyMathExpression`、`SaveVideo`、`TextGenerateLTX2Prompt`、`CLIPTextEncode`、`LTXVConditioning`、`LTXAVTextEncoderLoader`、`LoraLoader`、`CheckpointLoaderSimple`、`LTXVImgToVideoInplace`、`PrimitiveBoolean`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`LoadImage`、`GetImageSize`、`ResizeImageMaskNode`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
