---
key: 视频生成/文生视频/LTX 2.3  图生视频+ 文生视频 二合一工作流_2034848874736656385.json
name: LTX 2.3  图生视频+ 文生视频 二合一工作流_2034848874736656385
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX 2.3  图生视频+ 文生视频 二合一工作流_2034848874736656385.json
hash: 0235ff5adaf78877
coverage: 0.797101
learned_at: 2026-10-11 03:48:34
nodes: [RandomNoise, RandomNoise, LTXVConcatAVLatent, KSamplerSelect, ManualSigmas, CFGGuider, SamplerCustomAdvanced, LTXVCropGuides, ResizeImagesByLongerEdge, LTXVImgToVideoInplace, LTXVPreprocess, ResizeImageMaskNode, PrimitiveInt, LTXVSeparateAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, PrimitiveInt, VAELoader, VAELoaderKJ, DualCLIPLoader, KSamplerSelect, CFGGuider, LTXVConditioning, ManualSigmas, LTXVAudioVAEDecode, VAEDecodeTiled, CLIPTextEncode, LTXVConcatAVLatent, LTXVImgToVideoInplace, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXVLatentUpsampler, PrimitiveInt, SimpleCalculatorKJ, ComfyMathExpression, ComfyMathExpression, TextInput_, llama_cpp_parameters, CreateVideo, ComfyMathExpression, Reroute, Fast Groups Bypasser (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), MarkdownNote, MarkdownNote, MarkdownNote, TextInput_, LatentUpscaleModelLoader, INTConstant, PrimitiveBoolean, LoadImage, PrimitiveStringMultiline, llama_cpp_instruct_adv, CLIPTextEncode, LTX2_NAG, JoinStrings, llama_cpp_unload_model, LayerUtility: PurgeVRAM V2, SaveVideo, RH_LLMAPI_NODE, ShowText|pysssss, llama_cpp_model_loader, LTXVChunkFeedForward, PathchSageAttentionKJ, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly]
patterns: []
missing: [Label (rgthree), Label (rgthree), Label (rgthree), LayerUtility: PurgeVRAM V2]
parameters: {"batch_size": 1, "height": 25, "width": 97}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX 2.3  图生视频+ 文生视频 二合一工作流_2034848874736656385.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX 2.3  图生视频+ 文生视频 二合一工作流_2034848874736656385.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `RandomNoise`
- `RandomNoise`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `ResizeImagesByLongerEdge`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `ResizeImageMaskNode`
- `PrimitiveInt`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `PrimitiveInt`
- `VAELoader`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `LTXVConditioning`
- `ManualSigmas`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVLatentUpsampler` ★核心
- `PrimitiveInt`
- `SimpleCalculatorKJ`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `TextInput_`
- `llama_cpp_parameters`
- `CreateVideo`
- `ComfyMathExpression`
- `Reroute`
- `Fast Groups Bypasser (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `TextInput_`
- `LatentUpscaleModelLoader`
- `INTConstant`
- `PrimitiveBoolean`
- `LoadImage`
- `PrimitiveStringMultiline`
- `llama_cpp_instruct_adv`
- `CLIPTextEncode` ★核心
- `LTX2_NAG`
- `JoinStrings`
- `llama_cpp_unload_model`
- `LayerUtility: PurgeVRAM V2`
- `SaveVideo`
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `llama_cpp_model_loader`
- `LTXVChunkFeedForward`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **80%**（55/69）

**有卡**：`RandomNoise`、`LTXVConcatAVLatent`、`KSamplerSelect`、`ManualSigmas`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`ResizeImagesByLongerEdge`、`LTXVImgToVideoInplace`、`LTXVPreprocess`、`ResizeImageMaskNode`、`LTXVSeparateAVLatent`、`VAELoader`、`VAELoaderKJ`、`DualCLIPLoader`、`LTXVConditioning`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`CLIPTextEncode`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVLatentUpsampler`、`SimpleCalculatorKJ`、`ComfyMathExpression`、`TextInput_`、`llama_cpp_parameters`、`CreateVideo`、`LatentUpscaleModelLoader`、`INTConstant`、`PrimitiveBoolean`、`LoadImage`、`llama_cpp_instruct_adv`、`LTX2_NAG`、`JoinStrings`、`llama_cpp_unload_model`、`SaveVideo`、`RH_LLMAPI_NODE`、`llama_cpp_model_loader`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`UNETLoader`、`LoraLoaderModelOnly`

**缺卡**（4）：`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`LayerUtility: PurgeVRAM V2`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
