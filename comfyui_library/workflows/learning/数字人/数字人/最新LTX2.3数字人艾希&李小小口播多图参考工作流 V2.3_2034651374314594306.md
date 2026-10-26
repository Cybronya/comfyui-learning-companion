---
key: 数字人/数字人/最新LTX2.3数字人艾希&李小小口播多图参考工作流 V2.3_2034651374314594306.json
name: 最新LTX2.3数字人艾希&李小小口播多图参考工作流 V2.3_2034651374314594306
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/最新LTX2.3数字人艾希&李小小口播多图参考工作流 V2.3_2034651374314594306.json
hash: a167d27cfc8f33a0
coverage: 0.862069
learned_at: 2026-10-26 02:03:30
nodes: [LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LoraLoaderModelOnly, LTXVLatentUpsampler, KSamplerSelect, Reroute, LTXVAudioVAEDecode, CLIPTextEncode, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, ComfyMathExpression, ComfyMathExpression, LTXVAudioVAELoader, CheckpointLoaderSimple, CFGGuider, LTXVConditioning, EmptyLTXVLatentVideo, LatentUpscaleModelLoader, RandomNoise, RandomNoise, LTXAVTextEncoderLoader, ManualSigmas, CLIPTextEncode, CreateVideo, LTXVConcatAVLatent, ResizeImagesByLongerEdge, LTXVPreprocess, ResizeImagesByLongerEdge, ResizeImageMaskNode, LTXVImgToVideoInplace, ResizeImagesByLongerEdge, LTXVPreprocess, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, FloatConstant, RH_LLMAPI_Pro_Node, LTXVPreprocess, LTXVImgToVideoInplaceKJ, PrimitiveStringMultiline, PrimitiveInt, LoadImage, easy showAnything, PrimitiveStringMultiline, PrimitiveInt, PrimitiveInt, LoadImage, SaveVideo, LoadImage, ResizeAndPadImage, ResizeAndPadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 数字人/数字人/最新LTX2.3数字人艾希&李小小口播多图参考工作流 V2.3_2034651374314594306.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/最新LTX2.3数字人艾希&李小小口播多图参考工作流 V2.3_2034651374314594306.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `LoraLoaderModelOnly` ★核心
- `LTXVLatentUpsampler` ★核心
- `KSamplerSelect` ★核心
- `Reroute`
- `LTXVAudioVAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVAudioVAELoader`
- `CheckpointLoaderSimple` ★核心
- `CFGGuider`
- `LTXVConditioning`
- `EmptyLTXVLatentVideo`
- `LatentUpscaleModelLoader`
- `RandomNoise`
- `RandomNoise`
- `LTXAVTextEncoderLoader`
- `ManualSigmas`
- `CLIPTextEncode` ★核心
- `CreateVideo`
- `LTXVConcatAVLatent`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ResizeImagesByLongerEdge`
- `ResizeImageMaskNode`
- `LTXVImgToVideoInplace`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `FloatConstant`
- `RH_LLMAPI_Pro_Node`
- `LTXVPreprocess`
- `LTXVImgToVideoInplaceKJ`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `LoadImage`
- `easy showAnything`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoadImage`
- `SaveVideo`
- `LoadImage`
- `ResizeAndPadImage`
- `ResizeAndPadImage`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **86%**（50/58）

**有卡**：`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LoraLoaderModelOnly`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`ComfyMathExpression`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LatentUpscaleModelLoader`、`RandomNoise`、`LTXAVTextEncoderLoader`、`CreateVideo`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`ResizeImageMaskNode`、`LTXVImgToVideoInplace`、`FloatConstant`、`RH_LLMAPI_Pro_Node`、`LTXVImgToVideoInplaceKJ`、`LoadImage`、`SaveVideo`、`ResizeAndPadImage`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
