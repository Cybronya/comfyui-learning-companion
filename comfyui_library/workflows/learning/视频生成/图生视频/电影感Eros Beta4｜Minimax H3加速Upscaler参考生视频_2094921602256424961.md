---
key: 视频生成/图生视频/电影感Eros Beta4｜Minimax H3加速Upscaler参考生视频_2094921602256424961.json
name: 电影感Eros Beta4｜Minimax H3加速Upscaler参考生视频_2094921602256424961
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/电影感Eros Beta4｜Minimax H3加速Upscaler参考生视频_2094921602256424961.json
hash: b8ee6b8a2c12673b
coverage: 0.923077
learned_at: 2026-10-17 00:03:23
nodes: [ModelAttentionBackend, MiniMaxH3MemoryEfficientSageAttentionPatch, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VAELoader, VAELoader, BasicGuider, MiniMaxH3AVDecodeT8, SamplerCustomAdvanced, SamplerCustomAdvanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, BasicGuider, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3DualClockSamplerT8, SolAttnMiniMax, MiniMaxH3AudioConditioningT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, LoadImage, VHS_VideoCombine, ComfyMathExpression, PrimitiveFloat, LoadImage, LoadImage, MiniMaxH3AudioConditioningT8, VHS_VideoCombine, ResolutionSelector, RandomNoise, UNETLoader, LoraLoaderBypassModelOnly, CLIPLoader, CR Prompt Text, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/电影感Eros Beta4｜Minimax H3加速Upscaler参考生视频_2094921602256424961.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/电影感Eros Beta4｜Minimax H3加速Upscaler参考生视频_2094921602256424961.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（65 个）：
- `ModelAttentionBackend`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VAELoader`
- `VAELoader`
- `BasicGuider`
- `MiniMaxH3AVDecodeT8`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `BasicGuider`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `SolAttnMiniMax`
- `MiniMaxH3AudioConditioningT8`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `LoadImage`
- `VHS_VideoCombine`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `LoadImage`
- `LoadImage`
- `MiniMaxH3AudioConditioningT8`
- `VHS_VideoCombine`
- `ResolutionSelector`
- `RandomNoise`
- `UNETLoader` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `CLIPLoader`
- `CR Prompt Text`
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

覆盖率 **92%**（60/65）

**有卡**：`ModelAttentionBackend`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoadImage`、`VAELoader`、`BasicGuider`、`MiniMaxH3AVDecodeT8`、`SamplerCustomAdvanced`、`MiniMaxH3TwoPassLatentReconcileT8Advanced`、`MiniMaxH3TwoPassDetailMixerT8Advanced`、`MiniMaxH3LearnedTwoPassParityPlanT8Advanced`、`MiniMaxH3DualClockSamplerT8`、`SolAttnMiniMax`、`MiniMaxH3AudioConditioningT8`、`MiniMaxH3LearnedLatentUpscaleT8Advanced`、`VHS_VideoCombine`、`ComfyMathExpression`、`ResolutionSelector`、`RandomNoise`、`UNETLoader`、`LoraLoaderBypassModelOnly`、`CLIPLoader`、`CR Prompt Text`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
