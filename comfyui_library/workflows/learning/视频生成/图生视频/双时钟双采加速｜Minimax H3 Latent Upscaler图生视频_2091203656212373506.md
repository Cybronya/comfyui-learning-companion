---
key: 视频生成/图生视频/双时钟双采加速｜Minimax H3 Latent Upscaler图生视频_2091203656212373506.json
name: 双时钟双采加速｜Minimax H3 Latent Upscaler图生视频_2091203656212373506
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/双时钟双采加速｜Minimax H3 Latent Upscaler图生视频_2091203656212373506.json
hash: 950df8f00555b3aa
coverage: 0.907407
learned_at: 2026-10-16 22:31:02
nodes: [CLIPLoader, UNETLoader, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, LoadImage, ComfyMathExpression, ResolutionSelector, MiniMaxH3TwoPassDetailMixerT8Advanced, PrimitiveFloat, VAELoader, VAELoader, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderBypassModelOnly, SolAttnMiniMax, ModelAttentionBackend, MiniMaxH3AudioConditioningT8, MiniMaxH3AudioConditioningT8, VHS_VideoCombine, RandomNoise, CR Prompt Text, BasicGuider, SamplerCustomAdvanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, BasicGuider, MiniMaxH3LearnedLatentUpscaleT8Advanced, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/双时钟双采加速｜Minimax H3 Latent Upscaler图生视频_2091203656212373506.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/双时钟双采加速｜Minimax H3 Latent Upscaler图生视频_2091203656212373506.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `MiniMaxH3DualClockSamplerT8` ★核心
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3AVDecodeT8`
- `LoadImage`
- `ComfyMathExpression`
- `ResolutionSelector`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `PrimitiveFloat`
- `VAELoader`
- `VAELoader`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderBypassModelOnly` ★核心
- `SolAttnMiniMax`
- `ModelAttentionBackend`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3AudioConditioningT8`
- `VHS_VideoCombine`
- `RandomNoise`
- `CR Prompt Text`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `BasicGuider`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
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

覆盖率 **91%**（49/54）

**有卡**：`CLIPLoader`、`UNETLoader`、`MiniMaxH3DualClockSamplerT8`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`SamplerCustomAdvanced`、`MiniMaxH3AVDecodeT8`、`LoadImage`、`ComfyMathExpression`、`ResolutionSelector`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`VAELoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderBypassModelOnly`、`SolAttnMiniMax`、`ModelAttentionBackend`、`MiniMaxH3AudioConditioningT8`、`VHS_VideoCombine`、`RandomNoise`、`CR Prompt Text`、`BasicGuider`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
