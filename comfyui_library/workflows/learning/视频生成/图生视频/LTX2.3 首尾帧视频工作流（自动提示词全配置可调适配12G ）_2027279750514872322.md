---
key: 视频生成/图生视频/LTX2.3 首尾帧视频工作流（自动提示词全配置可调适配12G ）_2027279750514872322.json
name: LTX2.3 首尾帧视频工作流（自动提示词全配置可调适配12G ）_2027279750514872322.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3 首尾帧视频工作流（自动提示词全配置可调适配12G ）_2027279750514872322.json
hash: 13ecb926b10d4f41
coverage: 0.62766
learned_at: 2026-10-15 22:35:16
nodes: [VAEDecodeTiled, SetNode, GetNode, CFGGuider, LTXVLatentUpsampler, LTXVConcatAVLatent, GetNode, GetNode, PrimitiveFloat, SetNode, GetNode, SetNode, PrimitiveBoolean, SetNode, LTXVAudioVAEDecode, CreateVideo, LTXVSeparateAVLatent, MarkdownNote, CLIPTextEncode, LTXVPreprocess, SetNode, ResizeImagesByLongerEdge, GetImageSize, SimpleCalculatorKJ, SetNode, ImageScaleBy, EmptyImage, LTXVPreprocess, SetNode, SetNode, SetNode, LatentUpscaleModelLoader, SetNode, GetNode, GetNode, GetNode, LTXVImgToVideoInplaceKJ, SamplerCustomAdvanced, LTXVConditioning, GetNode, LTXVSeparateAVLatent, KSamplerSelect, CLIPTextEncode, DualCLIPLoader, ResizeImagesByLongerEdge, RandomNoise, RandomNoise, KSamplerSelect, KSamplerSelect, INTConstant, MarkdownNote, UnetLoaderGGUF, UNETLoader, VAELoaderKJ, VAELoaderKJ, LoadImage, LoadImage, SaveVideo, INTConstant, INTConstant, GetNode, SetNode, llama_cpp_model_loader, CFGGuider, EmptyLTXVLatentVideo, GetNode, LTXVImgToVideoInplaceKJ, LTXVConcatAVLatent, LTXVEmptyLatentAudio, ImageConcatMulti, CR Text, ManualSigmas, ManualSigmas, Note, Note, Note, Note, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, ShowText|pysssss, llama_cpp_instruct_adv, SamplerCustomAdvanced, Note, GetNode, CM_FloatToInt, GetNode, Note, ModelPatchTorchSettings, PathchSageAttentionKJ, SetNode, SetNode, LTXVChunkFeedForward, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
---

# 视频生成/图生视频/LTX2.3 首尾帧视频工作流（自动提示词全配置可调适配12G ）_2027279750514872322.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2027279750514872322.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（94 个）：
- `VAEDecodeTiled` ★核心
- `SetNode`
- `GetNode`
- `CFGGuider`
- `LTXVLatentUpsampler` ★核心
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `PrimitiveFloat`
- `SetNode`
- `GetNode`
- `SetNode`
- `PrimitiveBoolean`
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `LTXVSeparateAVLatent`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `LTXVPreprocess`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `GetImageSize`
- `SimpleCalculatorKJ`
- `SetNode`
- `ImageScaleBy`
- `EmptyImage`
- `LTXVPreprocess`
- `SetNode`
- `SetNode`
- `SetNode`
- `LatentUpscaleModelLoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `SamplerCustomAdvanced` ★核心
- `LTXVConditioning`
- `GetNode`
- `LTXVSeparateAVLatent`
- `KSamplerSelect` ★核心
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `ResizeImagesByLongerEdge`
- `RandomNoise`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `INTConstant`
- `MarkdownNote`
- `UnetLoaderGGUF` ★核心
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `LoadImage`
- `LoadImage`
- `SaveVideo`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `SetNode`
- `llama_cpp_model_loader`
- `CFGGuider`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `ImageConcatMulti`
- `CR Text`
- `ManualSigmas`
- `ManualSigmas`
- `Note`
- `Note`
- `Note`
- `Note`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `ShowText|pysssss`
- `llama_cpp_instruct_adv`
- `SamplerCustomAdvanced` ★核心
- `Note`
- `GetNode`
- `CM_FloatToInt`
- `GetNode`
- `Note`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `SetNode`
- `SetNode`
- `LTXVChunkFeedForward`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **63%**（59/94）

**有卡**：`VAEDecodeTiled`、`CFGGuider`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`PrimitiveBoolean`、`LTXVAudioVAEDecode`、`CreateVideo`、`LTXVSeparateAVLatent`、`CLIPTextEncode`、`LTXVPreprocess`、`ResizeImagesByLongerEdge`、`GetImageSize`、`SimpleCalculatorKJ`、`ImageScaleBy`、`EmptyImage`、`LatentUpscaleModelLoader`、`LTXVImgToVideoInplaceKJ`、`SamplerCustomAdvanced`、`LTXVConditioning`、`KSamplerSelect`、`DualCLIPLoader`、`RandomNoise`、`INTConstant`、`UnetLoaderGGUF`、`UNETLoader`、`VAELoaderKJ`、`LoadImage`、`SaveVideo`、`llama_cpp_model_loader`、`EmptyLTXVLatentVideo`、`LTXVEmptyLatentAudio`、`ImageConcatMulti`、`CR Text`、`ManualSigmas`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`llama_cpp_instruct_adv`、`CM_FloatToInt`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`LoraLoaderModelOnly`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
