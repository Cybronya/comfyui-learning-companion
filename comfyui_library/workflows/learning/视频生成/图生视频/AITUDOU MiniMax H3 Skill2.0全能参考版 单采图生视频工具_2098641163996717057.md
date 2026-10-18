---
key: 视频生成/图生视频/AITUDOU MiniMax H3 Skill2.0全能参考版 单采图生视频工具_2098641163996717057.json
name: AITUDOU MiniMax H3 Skill2.0全能参考版 单采图生视频工具_2098641163996717057
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/AITUDOU MiniMax H3 Skill2.0全能参考版 单采图生视频工具_2098641163996717057.json
hash: 8eed2fb12e4e6d87
coverage: 0.529412
learned_at: 2026-10-17 01:44:20
nodes: [SetNode, VAELoader, SetNode, VAELoader, SetNode, SetNode, GetNode, GetNode, GetNode, VAEDecodeAudio, VAEDecode, KSamplerSelect, SetNode, ComfyMathExpression, SetNode, CLIPLoader, SetNode, SetNode, LoadImage, LoadImage, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, LoraLoaderModelOnly, SetNode, SamplerCustomAdvanced, RandomNoise, BasicGuider, GetNode, SetNode, GetNode, SetNode, SplitSigmas, MiniMaxH3MemoryEfficientSageAttentionPatch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, MiniMaxH3ReferenceToVideo, AudioSeparation, AudioSeparation, SetNode, AudioSeparation, LoadAudio, SetNode, GetNode, GetNode, BasicScheduler, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, GetNode, GetNode, LoadImage, LoadImage, SetNode, UNETLoader, Fast Groups Bypasser (rgthree), SetNode, GetNode, GetNode, LoadImage, LoadImage, LoadImage, LoadAudio, LoadImage, LoadImage, VHS_VideoCombine, ResolutionSelector, LoadAudio, Float, Text, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/AITUDOU MiniMax H3 Skill2.0全能参考版 单采图生视频工具_2098641163996717057.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/AITUDOU MiniMax H3 Skill2.0全能参考版 单采图生视频工具_2098641163996717057.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（119 个）：
- `SetNode`
- `VAELoader`
- `SetNode`
- `VAELoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `SetNode`
- `ComfyMathExpression`
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `BasicGuider`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SplitSigmas`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
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
- `MiniMaxH3ReferenceToVideo`
- `AudioSeparation`
- `AudioSeparation`
- `SetNode`
- `AudioSeparation`
- `LoadAudio`
- `SetNode`
- `GetNode`
- `GetNode`
- `BasicScheduler`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `UNETLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadAudio`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `ResolutionSelector`
- `LoadAudio`
- `Float`
- `Text`
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
- `SaveImage`

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

覆盖率 **53%**（63/119）

**有卡**：`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`ComfyMathExpression`、`CLIPLoader`、`LoadImage`、`LoraLoaderModelOnly`、`SamplerCustomAdvanced`、`RandomNoise`、`BasicGuider`、`SplitSigmas`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3ReferenceToVideo`、`AudioSeparation`、`LoadAudio`、`BasicScheduler`、`UNETLoader`、`VHS_VideoCombine`、`ResolutionSelector`、`Float`、`Text`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
