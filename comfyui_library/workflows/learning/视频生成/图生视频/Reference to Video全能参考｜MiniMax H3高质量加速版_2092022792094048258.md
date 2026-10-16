---
key: 视频生成/图生视频/Reference to Video全能参考｜MiniMax H3高质量加速版_2092022792094048258.json
name: Reference to Video全能参考｜MiniMax H3高质量加速版_2092022792094048258
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Reference to Video全能参考｜MiniMax H3高质量加速版_2092022792094048258.json
hash: 5eefea255016de30
coverage: 0.91195
learned_at: 2026-10-16 22:59:17
nodes: [KSamplerSelect, BasicGuider, VAEDecode, VAEDecodeAudio, SamplerCustomAdvanced, ComfyMathExpression, PrimitiveInt, VAELoader, VAELoader, Label (rgthree), KSamplerSelect, BasicGuider, SamplerCustomAdvanced, VAELoader, VAELoader, PrimitiveInt, CLIPLoader, ResolutionSelector, RandomNoise, BasicScheduler, LoadImage, EasyCache, VAEDecode, VAEDecodeAudio, VHS_VideoCombine, LoadImage, easy convertAnything, easy string, string_util_StrConcat, string_util_StrConcat, PreviewAny, StringConcatenate, PreviewAny, ComfyMathExpression, MiniMaxH3ReferenceToVideo, RHLLMChatNode, PrimitiveStringMultiline, ResolutionSelector, LoadImage, VHS_VideoCombine, PrimitiveStringMultiline, RandomNoise, MiniMaxH3MemoryEfficientSageAttentionPatch, LoadImage, UNETLoader, CLIPLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, BasicScheduler, MiniMaxH3ReferenceToVideo, LoadImage, easy string, LoadImage, LoadImage, MiniMaxH3PromptEnhancerT8, easy showAnything, UNETLoader, BasicGuider, SamplerCustomAdvanced, RandomNoise, CLIPLoader, VAELoader, VAELoader, LoadImage, LoadImage, LoadImage, MiniMaxH3AVDecodeT8, VHS_VideoCombine, LoraLoaderModelOnly, MiniMaxH3DualClockSamplerT8, Label (rgthree), MiniMaxH3AudioConditioningT8, CR Prompt Text, ComfyMathExpression, Label (rgthree), LoraLoaderModelOnly, Label (rgthree), PrimitiveInt, ResolutionSelector, Label (rgthree), BasicGuider, SamplerCustomAdvanced, RandomNoise, CLIPLoader, VAELoader, LoadImage, LoadImage, MiniMaxH3AVDecodeT8, VHS_VideoCombine, MiniMaxH3DualClockSamplerT8, UNETLoader, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, ComfyMathExpression, ResolutionSelector, CR Prompt Text, MiniMaxH3AudioConditioningT8, LoadImage, VAELoader, MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, PrimitiveInt, Label (rgthree), ModelAttentionBackend, Label (rgthree), CLIPLoader, VAELoader, VAELoader, VHS_VideoCombine, Label (rgthree), UNETLoader, ComfyMathExpression, ResolutionSelector, PrimitiveInt, CR Prompt Text, LoadImage, LoadImage, LoadImage, LoraLoaderModelOnly, Label (rgthree), MiniMaxH3AVDecodeT8, SamplerCustomAdvanced, RandomNoise, BasicGuider, MiniMaxH3DualClockSamplerT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, SolAttnMiniMax, Label (rgthree), Label (rgthree), 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Reference to Video全能参考｜MiniMax H3高质量加速版_2092022792094048258.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Reference to Video全能参考｜MiniMax H3高质量加速版_2092022792094048258.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（159 个）：
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
- `BasicScheduler`
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
- `孤海注释`
- `孤海注释`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（145/159）

**有卡**：`KSamplerSelect`、`BasicGuider`、`VAEDecode`、`VAEDecodeAudio`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`VAELoader`、`Label (rgthree)`、`CLIPLoader`、`ResolutionSelector`、`RandomNoise`、`BasicScheduler`、`LoadImage`、`EasyCache`、`VHS_VideoCombine`、`easy convertAnything`、`easy string`、`string_util_StrConcat`、`StringConcatenate`、`MiniMaxH3ReferenceToVideo`、`RHLLMChatNode`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`UNETLoader`、`MiniMaxH3PromptEnhancerT8`、`MiniMaxH3AVDecodeT8`、`LoraLoaderModelOnly`、`MiniMaxH3DualClockSamplerT8`、`MiniMaxH3AudioConditioningT8`、`CR Prompt Text`、`ModelAttentionBackend`、`SolAttnMiniMax`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
