---
key: 视频生成/文生视频/MiniMax H3 多参极简 V3.0｜多参考长视频续接不断篇_2096843243878174721.json
name: MiniMax H3 多参极简 V3.0｜多参考长视频续接不断篇_2096843243878174721
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 多参极简 V3.0｜多参考长视频续接不断篇_2096843243878174721.json
hash: 46faedba08a1bc86
coverage: 0.876404
learned_at: 2026-10-15 22:45:38
nodes: [VAELoader, MiniMaxH3MemoryEfficientSageAttentionPatch, LTXVSeparateAVLatent, CLIPLoader, VAELoader, SamplerCustomAdvanced, ConditioningZeroOut, VAEDecodeAudio, VAEDecode, ComfyMathExpression, RandomNoise, LoraLoaderModelOnly, UNETLoader, MiniMaxH3MotionContext, Seed (rgthree), BasicGuider, KSamplerSelect, BasicScheduler, CreateVideo, ResolutionSelector, MiniMaxH3MotionContextTrim, KSampler, MinimaxH3LatentUpscaler3D, Int, Fast Groups Bypasser (rgthree), MiniMaxH3ReferenceToVideo, LTXVConcatAVLatent, VAEDecode, VAEDecodeAudio, FlashVSRNode, VHS_VideoCombine, Fast Groups Bypasser (rgthree), RH_LLMAPI_NODE, CR Text, PreviewAny, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, Text Multiline, Fast Groups Bypasser (rgthree), LoadVideoUI, PreviewVideoNode, Text Multiline, PrimitiveFloat, LoadAudioUI, LoadAudioUI, CS-MultiImageLoader, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/MiniMax H3 多参极简 V3.0｜多参考长视频续接不断篇_2096843243878174721.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3 多参极简 V3.0｜多参考长视频续接不断篇_2096843243878174721.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（89 个）：
- `VAELoader`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LTXVSeparateAVLatent`
- `CLIPLoader`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `ConditioningZeroOut`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `ComfyMathExpression`
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `MiniMaxH3MotionContext`
- `Seed (rgthree)`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `CreateVideo`
- `ResolutionSelector`
- `MiniMaxH3MotionContextTrim`
- `KSampler` ★核心
- `MinimaxH3LatentUpscaler3D`
- `Int`
- `Fast Groups Bypasser (rgthree)`
- `MiniMaxH3ReferenceToVideo`
- `LTXVConcatAVLatent`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `FlashVSRNode`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `RH_LLMAPI_NODE`
- `CR Text`
- `PreviewAny`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `Text Multiline`
- `Fast Groups Bypasser (rgthree)`
- `LoadVideoUI`
- `PreviewVideoNode`
- `Text Multiline`
- `PrimitiveFloat`
- `LoadAudioUI`
- `LoadAudioUI`
- `CS-MultiImageLoader`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
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

覆盖率 **88%**（78/89）

**有卡**：`VAELoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LTXVSeparateAVLatent`、`CLIPLoader`、`SamplerCustomAdvanced`、`ConditioningZeroOut`、`VAEDecodeAudio`、`VAEDecode`、`ComfyMathExpression`、`RandomNoise`、`LoraLoaderModelOnly`、`UNETLoader`、`MiniMaxH3MotionContext`、`Seed (rgthree)`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`CreateVideo`、`ResolutionSelector`、`MiniMaxH3MotionContextTrim`、`KSampler`、`MinimaxH3LatentUpscaler3D`、`Int`、`MiniMaxH3ReferenceToVideo`、`LTXVConcatAVLatent`、`FlashVSRNode`、`VHS_VideoCombine`、`RH_LLMAPI_NODE`、`CR Text`、`Text Multiline`、`LoadVideoUI`、`PreviewVideoNode`、`LoadAudioUI`、`CS-MultiImageLoader`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
