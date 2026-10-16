---
key: 视频生成/图生视频/LTX2.3-五图生视频15秒电商展示变装-全自动提示词_2051660543777361922.json
name: LTX2.3-五图生视频15秒电商展示变装-全自动提示词_2051660543777361922.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2051660543777361922.json
hash: 67ca8a82d01bb93f
coverage: 0.927536
learned_at: 2026-10-15 22:37:23
nodes: [LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, PathchSageAttentionKJ, ModelPatchTorchSettings, LTXVChunkFeedForward, LTXVAudioVAELoader, LTXAVTextEncoderLoader, LoraLoaderModelOnly, CreateVideo, LTXVAudioVAEDecode, SamplerCustomAdvanced, RandomNoise, LTXVSeparateAVLatent, LTXVSeparateAVLatent, LTXVCropGuides, ManualSigmas, CFGGuider, RandomNoise, CheckpointLoaderSimple, LTXVConditioning, LTXVImgToVideoInplace, LTXVLatentUpsampler, VAEDecodeTiled, DualCLIPLoader, EmptyLTXVLatentVideo, LatentUpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, ComfyMathExpression, ComfyMathExpression, LTXVEmptyLatentAudio, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, RH_LLMAPI_Pro_Node, easy showAnything, CLIPTextEncode, PreviewAny, LTXVImgToVideoInplaceKJ, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, FloatConstant, CLIPTextEncode, TextGenerateLTX2Prompt, FloatConstant, FloatConstant, FloatConstant, FloatConstant, PrimitiveInt, CR Prompt Text, CR Prompt Text, SaveVideo, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LTXVConcatAVLatent, ComfyMathExpression, PrimitiveInt, PrimitiveInt]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3-五图生视频15秒电商展示变装-全自动提示词_2051660543777361922.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2051660543777361922.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `LoraLoaderModelOnly` ★核心
- `CreateVideo`
- `LTXVAudioVAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `ManualSigmas`
- `CFGGuider`
- `RandomNoise`
- `CheckpointLoaderSimple` ★核心
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `VAEDecodeTiled` ★核心
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `LatentUpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVEmptyLatentAudio` ★核心
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `RH_LLMAPI_Pro_Node`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `LTXVImgToVideoInplaceKJ`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `FloatConstant`
- `CLIPTextEncode` ★核心
- `TextGenerateLTX2Prompt`
- `FloatConstant`
- `FloatConstant`
- `FloatConstant`
- `FloatConstant`
- `PrimitiveInt`
- `CR Prompt Text`
- `CR Prompt Text`
- `SaveVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LTXVConcatAVLatent`
- `ComfyMathExpression`
- `PrimitiveInt`
- `PrimitiveInt`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **93%**（64/69）

**有卡**：`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`LoraLoaderModelOnly`、`CreateVideo`、`LTXVAudioVAEDecode`、`RandomNoise`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`CheckpointLoaderSimple`、`LTXVConditioning`、`LTXVImgToVideoInplace`、`LTXVLatentUpsampler`、`VAEDecodeTiled`、`DualCLIPLoader`、`EmptyLTXVLatentVideo`、`LatentUpscaleModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ComfyMathExpression`、`LTXVEmptyLatentAudio`、`SimpleMath+`、`RH_LLMAPI_Pro_Node`、`CLIPTextEncode`、`LTXVImgToVideoInplaceKJ`、`LoadImage`、`FloatConstant`、`TextGenerateLTX2Prompt`、`CR Prompt Text`、`SaveVideo`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced、LTXVLatentUpsampler
