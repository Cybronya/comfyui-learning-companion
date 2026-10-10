---
key: 视频生成/文生视频/LTX2.3 图文生视频工作流（自动提示词全配置可调适配12G ）_2030943530058784769.json
name: LTX2.3 图文生视频工作流（自动提示词全配置可调适配12G ）_2030943530058784769
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 图文生视频工作流（自动提示词全配置可调适配12G ）_2030943530058784769.json
hash: 193cc79191e93684
coverage: 0.602273
learned_at: 2026-10-11 03:16:46
nodes: [LTXVSeparateAVLatent, CFGGuider, SamplerCustomAdvanced, LoadImage, LTXVConcatAVLatent, LTXVConditioning, VAEDecodeTiled, SetNode, SimpleCalculatorKJ, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, GetNode, RandomNoise, SamplerCustomAdvanced, CFGGuider, LTXVLatentUpsampler, KSamplerSelect, LTXVConcatAVLatent, LTXVImgToVideoInplace, GetNode, RandomNoise, GetNode, GetNode, GetImageSize, EmptyImage, GetNode, GetNode, GetNode, ImageScaleBy, PrimitiveFloat, SetNode, GetNode, GetNode, SetNode, SetNode, PrimitiveBoolean, SetNode, LTXVAudioVAEDecode, CreateVideo, LTXVSeparateAVLatent, SaveVideo, MarkdownNote, INTConstant, INTConstant, INTConstant, SetNode, ResizeImagesByLongerEdge, CLIPTextEncode, GetNode, LTXVPreprocess, LTXVImgToVideoInplace, SetNode, CR Text, CLIPTextEncode, KSamplerSelect, GetNode, MarkdownNote, ManualSigmas, ManualSigmas, SetNode, SetNode, LatentUpscaleModelLoader, DualCLIPLoader, UnetLoaderGGUF, UNETLoader, VAELoaderKJ, VAELoaderKJ, Note, Note, Note, Note, llama_cpp_instruct_adv, Note, Note, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, llama_cpp_model_loader, ShowText|pysssss, GetNode, CM_FloatToInt, SetNode, SetNode, SetNode, ModelPatchTorchSettings, PathchSageAttentionKJ, LTXVChunkFeedForward, LoraLoaderModelOnly]
patterns: []
missing: [CR Text]
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 97}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3 图文生视频工作流（自动提示词全配置可调适配12G ）_2030943530058784769.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 图文生视频工作流（自动提示词全配置可调适配12G ）_2030943530058784769.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（88 个）：
- `LTXVSeparateAVLatent`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LoadImage`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `VAEDecodeTiled` ★核心
- `SetNode`
- `SimpleCalculatorKJ`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `GetNode`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `LTXVLatentUpsampler` ★核心
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `GetNode`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `GetImageSize`
- `EmptyImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageScaleBy`
- `PrimitiveFloat`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `PrimitiveBoolean`
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `CreateVideo`
- `LTXVSeparateAVLatent`
- `SaveVideo`
- `MarkdownNote`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `CLIPTextEncode` ★核心
- `GetNode`
- `LTXVPreprocess`
- `LTXVImgToVideoInplace`
- `SetNode`
- `CR Text`
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `GetNode`
- `MarkdownNote`
- `ManualSigmas`
- `ManualSigmas`
- `SetNode`
- `SetNode`
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `UnetLoaderGGUF` ★核心
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `VAELoaderKJ`
- `Note`
- `Note`
- `Note`
- `Note`
- `llama_cpp_instruct_adv`
- `Note`
- `Note`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `llama_cpp_model_loader`
- `ShowText|pysssss`
- `GetNode`
- `CM_FloatToInt`
- `SetNode`
- `SetNode`
- `SetNode`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **60%**（53/88）

**有卡**：`LTXVSeparateAVLatent`、`CFGGuider`、`SamplerCustomAdvanced`、`LoadImage`、`LTXVConcatAVLatent`、`LTXVConditioning`、`VAEDecodeTiled`、`SimpleCalculatorKJ`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`RandomNoise`、`LTXVLatentUpsampler`、`KSamplerSelect`、`LTXVImgToVideoInplace`、`GetImageSize`、`EmptyImage`、`ImageScaleBy`、`PrimitiveBoolean`、`LTXVAudioVAEDecode`、`CreateVideo`、`SaveVideo`、`INTConstant`、`ResizeImagesByLongerEdge`、`CLIPTextEncode`、`LTXVPreprocess`、`ManualSigmas`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`UnetLoaderGGUF`、`UNETLoader`、`VAELoaderKJ`、`llama_cpp_instruct_adv`、`CheckpointLoaderSimple`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`llama_cpp_model_loader`、`CM_FloatToInt`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`LoraLoaderModelOnly`

**缺卡**（1）：`CR Text`

**用到的条目**：LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
