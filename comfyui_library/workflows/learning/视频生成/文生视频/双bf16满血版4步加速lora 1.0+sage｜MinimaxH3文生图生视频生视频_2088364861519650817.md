---
key: 视频生成/文生视频/双bf16满血版4步加速lora 1.0+sage｜MinimaxH3文生图生视频生视频_2088364861519650817.json
name: 双bf16满血版4步加速lora 1.0+sage｜MinimaxH3文生图生视频生视频_2088364861519650817
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/双bf16满血版4步加速lora 1.0+sage｜MinimaxH3文生图生视频生视频_2088364861519650817.json
hash: 3098f4d0a481d97c
coverage: 0.893617
learned_at: 2026-10-15 22:48:18
nodes: [LoadImage, PrimitiveFloat, VHS_VideoCombine, RandomNoise, SamplerCustomAdvanced, MiniMaxH3AVDecodeT8, CLIPLoader, VAELoader, BasicGuider, KSamplerSelect, ComfyMathExpression, MiniMaxH3AudioConditioningT8, CR Prompt Text, UNETLoader, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, ResolutionSelector, BasicScheduler, VAELoader, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/双bf16满血版4步加速lora 1.0+sage｜MinimaxH3文生图生视频生视频_2088364861519650817.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/双bf16满血版4步加速lora 1.0+sage｜MinimaxH3文生图生视频生视频_2088364861519650817.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（47 个）：
- `LoadImage`
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3AVDecodeT8`
- `CLIPLoader`
- `VAELoader`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `ComfyMathExpression`
- `MiniMaxH3AudioConditioningT8`
- `CR Prompt Text`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderModelOnly` ★核心
- `ResolutionSelector`
- `BasicScheduler`
- `VAELoader`
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

覆盖率 **89%**（42/47）

**有卡**：`LoadImage`、`VHS_VideoCombine`、`RandomNoise`、`SamplerCustomAdvanced`、`MiniMaxH3AVDecodeT8`、`CLIPLoader`、`VAELoader`、`BasicGuider`、`KSamplerSelect`、`ComfyMathExpression`、`MiniMaxH3AudioConditioningT8`、`CR Prompt Text`、`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderModelOnly`、`ResolutionSelector`、`BasicScheduler`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
