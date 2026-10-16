---
key: 视频生成/图生视频/Reference to Video高质量加速｜MiniMax H3全能参考生成_2092211916549738497.json
name: Reference to Video高质量加速｜MiniMax H3全能参考生成_2092211916549738497
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Reference to Video高质量加速｜MiniMax H3全能参考生成_2092211916549738497.json
hash: e9086c7125b5b35a
coverage: 0.90411
learned_at: 2026-10-16 22:59:17
nodes: [KSamplerSelect, BasicGuider, VAEDecode, VAEDecodeAudio, SamplerCustomAdvanced, ComfyMathExpression, PrimitiveInt, VAELoader, VAELoader, KSamplerSelect, BasicGuider, SamplerCustomAdvanced, VAELoader, VAELoader, PrimitiveInt, CLIPLoader, ResolutionSelector, RandomNoise, BasicScheduler, LoadImage, EasyCache, VAEDecode, VAEDecodeAudio, VHS_VideoCombine, LoadImage, easy convertAnything, easy string, string_util_StrConcat, string_util_StrConcat, PreviewAny, StringConcatenate, PreviewAny, ComfyMathExpression, MiniMaxH3ReferenceToVideo, RHLLMChatNode, PrimitiveStringMultiline, ResolutionSelector, LoadImage, VHS_VideoCombine, PrimitiveStringMultiline, RandomNoise, MiniMaxH3MemoryEfficientSageAttentionPatch, LoadImage, UNETLoader, CLIPLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, BasicScheduler, MiniMaxH3ReferenceToVideo, LoadImage, easy string, LoadImage, LoadImage, MiniMaxH3PromptEnhancerT8, easy showAnything, UNETLoader, BasicGuider, SamplerCustomAdvanced, RandomNoise, CLIPLoader, VAELoader, VAELoader, LoadImage, LoadImage, LoadImage, MiniMaxH3AVDecodeT8, VHS_VideoCombine, LoraLoaderModelOnly, MiniMaxH3DualClockSamplerT8, MiniMaxH3AudioConditioningT8, CR Prompt Text, ComfyMathExpression, LoraLoaderModelOnly, PrimitiveInt, ResolutionSelector, BasicGuider, SamplerCustomAdvanced, RandomNoise, CLIPLoader, VAELoader, LoadImage, LoadImage, MiniMaxH3AVDecodeT8, VHS_VideoCombine, MiniMaxH3DualClockSamplerT8, UNETLoader, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, ComfyMathExpression, ResolutionSelector, CR Prompt Text, MiniMaxH3AudioConditioningT8, LoadImage, VAELoader, MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, PrimitiveInt, ModelAttentionBackend, CLIPLoader, VAELoader, VAELoader, VHS_VideoCombine, UNETLoader, ComfyMathExpression, ResolutionSelector, PrimitiveInt, CR Prompt Text, LoadImage, LoadImage, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, SamplerCustomAdvanced, RandomNoise, BasicGuider, MiniMaxH3DualClockSamplerT8, MiniMaxH3AudioConditioningT8, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, SolAttnMiniMax, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Reference to Video高质量加速｜MiniMax H3全能参考生成_2092211916549738497.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Reference to Video高质量加速｜MiniMax H3全能参考生成_2092211916549738497.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（146 个）：
- `KSamplerSelect` ★核心
- `BasicGuider`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `ComfyMathExpression`
- `PrimitiveInt`
- `VAELoader`
- `VAELoader`
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
- `MiniMaxH3AudioConditioningT8`
- `CR Prompt Text`
- `ComfyMathExpression`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveInt`
- `ResolutionSelector`
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
- `ModelAttentionBackend`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `ComfyMathExpression`
- `ResolutionSelector`
- `PrimitiveInt`
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3AVDecodeT8`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `BasicGuider`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `SolAttnMiniMax`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
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
- `LoraLoaderModelOnly` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **90%**（132/146）

**有卡**：`KSamplerSelect`、`BasicGuider`、`VAEDecode`、`VAEDecodeAudio`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`VAELoader`、`CLIPLoader`、`ResolutionSelector`、`RandomNoise`、`BasicScheduler`、`LoadImage`、`EasyCache`、`VHS_VideoCombine`、`easy convertAnything`、`easy string`、`string_util_StrConcat`、`StringConcatenate`、`MiniMaxH3ReferenceToVideo`、`RHLLMChatNode`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`UNETLoader`、`MiniMaxH3PromptEnhancerT8`、`MiniMaxH3AVDecodeT8`、`LoraLoaderModelOnly`、`MiniMaxH3DualClockSamplerT8`、`MiniMaxH3AudioConditioningT8`、`CR Prompt Text`、`ModelAttentionBackend`、`SolAttnMiniMax`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
