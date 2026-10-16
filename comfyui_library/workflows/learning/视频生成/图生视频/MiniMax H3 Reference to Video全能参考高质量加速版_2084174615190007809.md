---
key: 视频生成/图生视频/MiniMax H3 Reference to Video全能参考高质量加速版_2084174615190007809.json
name: MiniMax H3 Reference to Video全能参考高质量加速版_2084174615190007809
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3 Reference to Video全能参考高质量加速版_2084174615190007809.json
hash: ef4400b3e5b5a035
coverage: 0.895522
learned_at: 2026-10-16 19:52:14
nodes: [KSamplerSelect, BasicGuider, VAEDecode, VAEDecodeAudio, SamplerCustomAdvanced, ComfyMathExpression, PrimitiveInt, VAELoader, VAELoader, Label (rgthree), KSamplerSelect, BasicGuider, SamplerCustomAdvanced, Note, VAELoader, VAELoader, PrimitiveInt, CLIPLoader, ResolutionSelector, RandomNoise, BasicScheduler, LoadImage, EasyCache, VAEDecode, VAEDecodeAudio, VHS_VideoCombine, LoadImage, easy convertAnything, easy string, string_util_StrConcat, string_util_StrConcat, PreviewAny, StringConcatenate, PreviewAny, ComfyMathExpression, MiniMaxH3ReferenceToVideo, RHLLMChatNode, PrimitiveStringMultiline, ResolutionSelector, LoadImage, VHS_VideoCombine, PrimitiveStringMultiline, RandomNoise, MiniMaxH3MemoryEfficientSageAttentionPatch, LoadImage, UNETLoader, CLIPLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, Note, BasicScheduler, Note, MarkdownNote, MiniMaxH3ReferenceToVideo, LoadImage, easy string, LoadImage, LoadImage, MiniMaxH3PromptEnhancerT8, easy showAnything, UNETLoader, BasicGuider, SamplerCustomAdvanced, RandomNoise, CLIPLoader, VAELoader, VAELoader, LoadImage, LoadImage, LoadImage, MiniMaxH3AVDecodeT8, VHS_VideoCombine, LoraLoaderModelOnly, MiniMaxH3DualClockSamplerT8, Label (rgthree), MiniMaxH3AudioConditioningT8, CR Prompt Text, ComfyMathExpression, Label (rgthree), LoraLoaderModelOnly, Label (rgthree), PrimitiveInt, ResolutionSelector, Label (rgthree), BasicGuider, SamplerCustomAdvanced, RandomNoise, CLIPLoader, VAELoader, LoadImage, LoadImage, MiniMaxH3AVDecodeT8, VHS_VideoCombine, MiniMaxH3DualClockSamplerT8, UNETLoader, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, ComfyMathExpression, ResolutionSelector, CR Prompt Text, MiniMaxH3AudioConditioningT8, LoadImage, VAELoader, MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, PrimitiveInt, Label (rgthree), ModelAttentionBackend, Label (rgthree), CLIPLoader, VAELoader, VAELoader, VHS_VideoCombine, Label (rgthree), UNETLoader, ComfyMathExpression, ResolutionSelector, PrimitiveInt, CR Prompt Text, LoadImage, LoadImage, LoadImage, LoraLoaderModelOnly, Label (rgthree), MiniMaxH3AVDecodeT8, SamplerCustomAdvanced, RandomNoise, BasicGuider, MiniMaxH3DualClockSamplerT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, SolAttnMiniMax, Label (rgthree), Label (rgthree)]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax H3 Reference to Video全能参考高质量加速版_2084174615190007809.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3 Reference to Video全能参考高质量加速版_2084174615190007809.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（134 个）：
- `KSamplerSelect` ★核心
- `BasicGuider`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `ComfyMathExpression`
- `PrimitiveInt`
- `VAELoader`
- `VAELoader`
- `Label (rgthree)`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `Note`
- `VAELoader`
- `VAELoader`
- `PrimitiveInt`
- `CLIPLoader`
- `ResolutionSelector`
- `RandomNoise`
- `BasicScheduler`
- `LoadImage`
- `EasyCache`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `easy convertAnything`
- `easy string`
- `string_util_StrConcat`
- `string_util_StrConcat`
- `PreviewAny`
- `StringConcatenate`
- `PreviewAny`
- `ComfyMathExpression`
- `MiniMaxH3ReferenceToVideo`
- `RHLLMChatNode`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `LoadImage`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `Note`
- `BasicScheduler`
- `Note`
- `MarkdownNote`
- `MiniMaxH3ReferenceToVideo`
- `LoadImage`
- `easy string`
- `LoadImage`
- `LoadImage`
- `MiniMaxH3PromptEnhancerT8`
- `easy showAnything`
- `UNETLoader` ★核心
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `MiniMaxH3AVDecodeT8`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3DualClockSamplerT8` ★核心
- `Label (rgthree)`
- `MiniMaxH3AudioConditioningT8`
- `CR Prompt Text`
- `ComfyMathExpression`
- `Label (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `Label (rgthree)`
- `PrimitiveInt`
- `ResolutionSelector`
- `Label (rgthree)`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `MiniMaxH3AVDecodeT8`
- `VHS_VideoCombine`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ComfyMathExpression`
- `ResolutionSelector`
- `CR Prompt Text`
- `MiniMaxH3AudioConditioningT8`
- `LoadImage`
- `VAELoader`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `UNETLoader` ★核心
- `PrimitiveInt`
- `Label (rgthree)`
- `ModelAttentionBackend`
- `Label (rgthree)`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `VHS_VideoCombine`
- `Label (rgthree)`
- `UNETLoader` ★核心
- `ComfyMathExpression`
- `ResolutionSelector`
- `PrimitiveInt`
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `Label (rgthree)`
- `MiniMaxH3AVDecodeT8`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `BasicGuider`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `SolAttnMiniMax`
- `Label (rgthree)`
- `Label (rgthree)`

## 知识

覆盖率 **90%**（120/134）

**有卡**：`KSamplerSelect`、`BasicGuider`、`VAEDecode`、`VAEDecodeAudio`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`VAELoader`、`Label (rgthree)`、`CLIPLoader`、`ResolutionSelector`、`RandomNoise`、`BasicScheduler`、`LoadImage`、`EasyCache`、`VHS_VideoCombine`、`easy convertAnything`、`easy string`、`string_util_StrConcat`、`StringConcatenate`、`MiniMaxH3ReferenceToVideo`、`RHLLMChatNode`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`UNETLoader`、`MiniMaxH3PromptEnhancerT8`、`MiniMaxH3AVDecodeT8`、`LoraLoaderModelOnly`、`MiniMaxH3DualClockSamplerT8`、`MiniMaxH3AudioConditioningT8`、`CR Prompt Text`、`ModelAttentionBackend`、`SolAttnMiniMax`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
