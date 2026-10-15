---
key: 视频生成/文生视频/LTX-2.3-Text to Video-workflow_2034124938138882049.json
name: LTX-2.3-Text to Video-workflow_2034124938138882049
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX-2.3-Text to Video-workflow_2034124938138882049.json
hash: 2916ba84bc8e427d
coverage: 0.87234
learned_at: 2026-10-15 22:44:40
nodes: [LTXVConcatAVLatent, LTXVAudioVAELoader, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LoraLoaderModelOnly, KSamplerSelect, Reroute, SamplerCustomAdvanced, LatentUpscaleModelLoader, CFGGuider, LTXVEmptyLatentAudio, LTXVConcatAVLatent, RandomNoise, LTXVSeparateAVLatent, LTXVLatentUpsampler, RandomNoise, LTXVAudioVAEDecode, CreateVideo, ManualSigmas, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVConditioning, CheckpointLoaderSimple, LTXVImgToVideoInplace, LTXVImgToVideoInplace, CLIPTextEncode, SaveVideo, PrimitiveInt, Note, Note, PrimitiveBoolean, CLIPTextEncode, EmptyLTXVLatentVideo, ComfyMathExpression, LTXVPreprocess, ComfyMathExpression, ComfyMathExpression, EmptyImage, PrimitiveStringMultiline, PrimitiveInt, ResizeImagesByLongerEdge, ResizeImageMaskNode, GetImageSize, LTXAVTextEncoderLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/文生视频/LTX-2.3-Text to Video-workflow_2034124938138882049.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX-2.3-Text to Video-workflow_2034124938138882049.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
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
- `SamplerCustomAdvanced` ★核心
- `LatentUpscaleModelLoader`
- `CFGGuider`
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
- `LTXVConditioning`
- `CheckpointLoaderSimple` ★核心
- `LTXVImgToVideoInplace`
- `LTXVImgToVideoInplace`
- `CLIPTextEncode` ★核心
- `SaveVideo`
- `PrimitiveInt`
- `Note`
- `Note`
- `PrimitiveBoolean`
- `CLIPTextEncode` ★核心
- `EmptyLTXVLatentVideo`
- `ComfyMathExpression`
- `LTXVPreprocess`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `EmptyImage`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `ResizeImagesByLongerEdge`
- `ResizeImageMaskNode`
- `GetImageSize`
- `LTXAVTextEncoderLoader`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **87%**（41/47）

**有卡**：`LTXVConcatAVLatent`、`LTXVAudioVAELoader`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LoraLoaderModelOnly`、`LatentUpscaleModelLoader`、`LTXVEmptyLatentAudio`、`RandomNoise`、`LTXVSeparateAVLatent`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`CreateVideo`、`VAEDecodeTiled`、`LTXVConditioning`、`CheckpointLoaderSimple`、`LTXVImgToVideoInplace`、`CLIPTextEncode`、`SaveVideo`、`PrimitiveBoolean`、`EmptyLTXVLatentVideo`、`ComfyMathExpression`、`LTXVPreprocess`、`EmptyImage`、`ResizeImagesByLongerEdge`、`ResizeImageMaskNode`、`GetImageSize`、`LTXAVTextEncoderLoader`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler、LTXVConcatAVLatent
