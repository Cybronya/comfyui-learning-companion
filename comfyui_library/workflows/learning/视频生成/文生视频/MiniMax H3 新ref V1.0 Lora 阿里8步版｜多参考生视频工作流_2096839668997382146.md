---
key: 视频生成/文生视频/MiniMax H3 新ref V1.0 Lora 阿里8步版｜多参考生视频工作流_2096839668997382146.json
name: MiniMax H3 新ref V1.0 Lora 阿里8步版｜多参考生视频工作流_2096839668997382146
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 新ref V1.0 Lora 阿里8步版｜多参考生视频工作流_2096839668997382146.json
hash: 36a4d270703c5a5a
coverage: 0.872093
learned_at: 2026-10-15 22:45:42
nodes: [KSamplerSelect, BasicGuider, ComfyMathExpression, SetNode, GetNode, VAEDecodeAudio, SetNode, PathchSageAttentionKJ, MiniMaxH3SigmaShift, RandomNoise, CLIPLoader, VAELoader, VAELoader, SamplerCustomAdvanced, UNETLoader, VHS_LoadVideo, SetNode, VAEDecode, VHS_LoadVideo, PrimitiveFloat, MiniMaxH3ReferenceToVideo, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, LoadAudio, LoadAudio, LoadAudio, VHS_LoadVideo, VHS_VideoCombine, LoadImage, PrimitiveFloat, PrimitiveStringMultiline, LoadImage, LoadImage, LoadImage, BasicScheduler, ResolutionSelector, LoraLoaderModelOnly, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/MiniMax H3 新ref V1.0 Lora 阿里8步版｜多参考生视频工作流_2096839668997382146.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3 新ref V1.0 Lora 阿里8步版｜多参考生视频工作流_2096839668997382146.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（86 个）：
- `KSamplerSelect` ★核心
- `BasicGuider`
- `ComfyMathExpression`
- `SetNode`
- `GetNode`
- `VAEDecodeAudio` ★核心
- `SetNode`
- `PathchSageAttentionKJ`
- `MiniMaxH3SigmaShift`
- `RandomNoise`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `VHS_LoadVideo`
- `SetNode`
- `VAEDecode` ★核心
- `VHS_LoadVideo`
- `PrimitiveFloat`
- `MiniMaxH3ReferenceToVideo`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `LoadImage`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `BasicScheduler`
- `ResolutionSelector`
- `LoraLoaderModelOnly` ★核心
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

覆盖率 **87%**（75/86）

**有卡**：`KSamplerSelect`、`BasicGuider`、`ComfyMathExpression`、`VAEDecodeAudio`、`PathchSageAttentionKJ`、`MiniMaxH3SigmaShift`、`RandomNoise`、`CLIPLoader`、`VAELoader`、`SamplerCustomAdvanced`、`UNETLoader`、`VHS_LoadVideo`、`VAEDecode`、`MiniMaxH3ReferenceToVideo`、`LoadImage`、`LoadAudio`、`VHS_VideoCombine`、`BasicScheduler`、`ResolutionSelector`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
