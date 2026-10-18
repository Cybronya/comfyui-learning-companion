---
key: 视频生成/图生视频/LTX2.3 数字人艾希&李小小《我们都是数字人》播客生产工作流 V3.00331_2038794251055669250.json
name: LTX2.3 数字人艾希&李小小《我们都是数字人》播客生产工作流 V3.00331_2038794251055669250.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 数字人艾希&李小小《我们都是数字人》播客生产工作流 V3.00331_2038794251055669250.json
hash: eba2377aa6c85b1a
coverage: 0.875
learned_at: 2026-10-15 22:36:04
nodes: [LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, LTXVLatentUpsampler, KSamplerSelect, Reroute, LTXVAudioVAEDecode, CLIPTextEncode, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, ComfyMathExpression, ComfyMathExpression, LTXVAudioVAELoader, CheckpointLoaderSimple, CFGGuider, LTXVConditioning, EmptyLTXVLatentVideo, LatentUpscaleModelLoader, RandomNoise, RandomNoise, LTXAVTextEncoderLoader, ManualSigmas, CLIPTextEncode, CreateVideo, LTXVConcatAVLatent, ResizeImagesByLongerEdge, LTXVPreprocess, ResizeImagesByLongerEdge, ResizeImageMaskNode, LTXVImgToVideoInplace, Resize, ResizeImagesByLongerEdge, Resize, LTXVPreprocess, PrimitiveInt, ComfyMathExpression, ComfyMathExpression, FloatConstant, LTXVPreprocess, LTXVImgToVideoInplaceKJ, easy showAnything, PrimitiveInt, SaveVideo, LoadImage, LoadImage, PrimitiveStringMultiline, LoadImage, LoadImage, RH_LLMAPI_Pro_Node, LoraLoaderModelOnly, LoraLoaderModelOnly, PrimitiveStringMultiline, LoraLoaderModelOnly, LoraLoaderModelOnly, PrimitiveInt, PrimitiveInt, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3 数字人艾希&李小小《我们都是数字人》播客生产工作流 V3.00331_2038794251055669250.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2038794251055669250.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（64 个）：
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
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
- `Resize`
- `ResizeImagesByLongerEdge`
- `Resize`
- `LTXVPreprocess`
- `PrimitiveInt`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `FloatConstant`
- `LTXVPreprocess`
- `LTXVImgToVideoInplaceKJ`
- `easy showAnything`
- `PrimitiveInt`
- `SaveVideo`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`
- `RH_LLMAPI_Pro_Node`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`

## 知识

覆盖率 **88%**（56/64）

**有卡**：`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`CLIPTextEncode`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`ComfyMathExpression`、`LTXVAudioVAELoader`、`CheckpointLoaderSimple`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LatentUpscaleModelLoader`、`RandomNoise`、`LTXAVTextEncoderLoader`、`CreateVideo`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`ResizeImageMaskNode`、`LTXVImgToVideoInplace`、`Resize`、`FloatConstant`、`LTXVImgToVideoInplaceKJ`、`SaveVideo`、`LoadImage`、`RH_LLMAPI_Pro_Node`、`LoraLoaderModelOnly`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
