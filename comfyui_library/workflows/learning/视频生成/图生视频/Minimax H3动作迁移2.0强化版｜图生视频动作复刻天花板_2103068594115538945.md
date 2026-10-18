---
key: 视频生成/图生视频/Minimax H3动作迁移2.0强化版｜图生视频动作复刻天花板_2103068594115538945.json
name: Minimax H3动作迁移2.0强化版｜图生视频动作复刻天花板_2103068594115538945
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Minimax H3动作迁移2.0强化版｜图生视频动作复刻天花板_2103068594115538945.json
hash: a64e8a1fb2bd7d5d
coverage: 0.566176
learned_at: 2026-10-17 02:29:10
nodes: [SetNode, VAELoader, SetNode, SetNode, GetNode, SetNode, Reroute, Reroute, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, MiniMaxH3ReferenceToVideo, SetNode, SetNode, SamplerCustomAdvanced, SetNode, BasicGuider, SetNode, SetNode, VAEDecode, GetNode, LTXVConcatAVLatent, SamplerCustomAdvanced, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, VAEDecode, ComfyMathExpression, LoadAudio, LoadAudio, LoadAudio, SetNode, SetNode, LoadImage, SetNode, LoadImage, SetNode, SetNode, LoadImage, SetNode, MiniMaxH3MemoryEfficientSageAttentionPatch, BasicScheduler, SplitSigmas, LoadImage, KSamplerSelect, GetNode, GetNode, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, easy float, UNETLoader, CLIPLoader, VAELoader, VAEDecodeAudio, ResolutionSelector, VHS_VideoCombine, GetNode, GetNode, GetNode, VHS_VideoCombine, SetNode, LoadImage, MinimaxH3LatentUpscaler3D, VAEDecodeAudio, RandomNoise, PrimitiveFloat, VHS_LoadVideo, LoadImage, Text, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Minimax H3动作迁移2.0强化版｜图生视频动作复刻天花板_2103068594115538945.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Minimax H3动作迁移2.0强化版｜图生视频动作复刻天花板_2103068594115538945.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（136 个）：
- `SetNode`
- `VAELoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `Reroute`
- `Reroute`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `MiniMaxH3ReferenceToVideo`
- `SetNode`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `BasicGuider`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `GetNode`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `VAEDecode` ★核心
- `ComfyMathExpression`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `SetNode`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `SetNode`
- `LoadImage`
- `SetNode`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `BasicScheduler`
- `SplitSigmas`
- `LoadImage`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy float`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `ResolutionSelector`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `LoadImage`
- `MinimaxH3LatentUpscaler3D`
- `VAEDecodeAudio` ★核心
- `RandomNoise`
- `PrimitiveFloat`
- `VHS_LoadVideo`
- `LoadImage`
- `Text`
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

覆盖率 **57%**（77/136）

**有卡**：`VAELoader`、`MiniMaxH3ReferenceToVideo`、`SamplerCustomAdvanced`、`BasicGuider`、`VAEDecode`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`ComfyMathExpression`、`LoadAudio`、`LoadImage`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`BasicScheduler`、`SplitSigmas`、`KSamplerSelect`、`LoraLoaderModelOnly`、`easy float`、`UNETLoader`、`CLIPLoader`、`VAEDecodeAudio`、`ResolutionSelector`、`VHS_VideoCombine`、`MinimaxH3LatentUpscaler3D`、`RandomNoise`、`VHS_LoadVideo`、`Text`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
