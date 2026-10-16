---
key: 视频生成/图生视频/Remix双采加速参考生视频｜MiniMax-H3 Latent Upscaler_2093484648100884482.json
name: Remix双采加速参考生视频｜MiniMax-H3 Latent Upscaler_2093484648100884482
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Remix双采加速参考生视频｜MiniMax-H3 Latent Upscaler_2093484648100884482.json
hash: 11e7264d81ef00f5
coverage: 0.907692
learned_at: 2026-10-16 23:42:22
nodes: [MiniMaxH3DualClockSamplerT8, SamplerCustomAdvanced, ComfyMathExpression, VAELoader, SolAttnMiniMax, ModelAttentionBackend, BasicGuider, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, MiniMaxH3AudioConditioningT8, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, BasicGuider, MiniMaxH3AudioConditioningT8, MiniMaxH3AVDecodeT8, VHS_VideoCombine, MiniMaxH3TwoPassDetailMixerT8Advanced, VAELoader, CLIPLoader, UNETLoader, SamplerCustomAdvanced, LoraLoaderBypassModelOnly, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, CR Prompt Text, MiniMaxH3LearnedLatentUpscaleT8Advanced, PrimitiveFloat, PrimitiveFloat, ResolutionSelector, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Remix双采加速参考生视频｜MiniMax-H3 Latent Upscaler_2093484648100884482.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Remix双采加速参考生视频｜MiniMax-H3 Latent Upscaler_2093484648100884482.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（65 个）：
- `MiniMaxH3DualClockSamplerT8` ★核心
- `SamplerCustomAdvanced` ★核心
- `ComfyMathExpression`
- `VAELoader`
- `SolAttnMiniMax`
- `ModelAttentionBackend`
- `BasicGuider`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `BasicGuider`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3AVDecodeT8`
- `VHS_VideoCombine`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `SamplerCustomAdvanced` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `ResolutionSelector`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
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
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `JjkText`
- `EmptyLatentImage` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
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

覆盖率 **91%**（59/65）

**有卡**：`MiniMaxH3DualClockSamplerT8`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`VAELoader`、`SolAttnMiniMax`、`ModelAttentionBackend`、`BasicGuider`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`RandomNoise`、`MiniMaxH3AudioConditioningT8`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`MiniMaxH3AVDecodeT8`、`VHS_VideoCombine`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`CLIPLoader`、`UNETLoader`、`LoraLoaderBypassModelOnly`、`LoadImage`、`CR Prompt Text`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`ResolutionSelector`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
