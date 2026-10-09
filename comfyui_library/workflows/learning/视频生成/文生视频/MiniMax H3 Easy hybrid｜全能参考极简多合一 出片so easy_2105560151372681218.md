---
key: 视频生成/文生视频/MiniMax H3 Easy hybrid｜全能参考极简多合一 出片so easy_2105560151372681218.json
name: MiniMax H3 Easy hybrid｜全能参考极简多合一 出片so easy_2105560151372681218
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 Easy hybrid｜全能参考极简多合一 出片so easy_2105560151372681218.json
hash: d4b581b5133a0158
coverage: 0.933333
learned_at: 2026-10-10 00:07:18
nodes: [MiniMaxH3EasyOutput, BasicGuider, RandomNoise, SamplerCustomAdvanced, VAEDecodeAudio, VAEDecode, CreateVideo, KSamplerSelect, MiniMaxH3MemoryEfficientSageAttentionPatch, SaveVideo, MiniMaxH3Easy, BasicScheduler, PathchSageAttentionKJ, MiniMaxH3EasyLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, MiniMaxH3EasyMediaLoader, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/MiniMax H3 Easy hybrid｜全能参考极简多合一 出片so easy_2105560151372681218.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3 Easy hybrid｜全能参考极简多合一 出片so easy_2105560151372681218.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（60 个）：
- `MiniMaxH3EasyOutput`
- `BasicGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `CreateVideo`
- `KSamplerSelect` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `SaveVideo`
- `MiniMaxH3Easy`
- `BasicScheduler`
- `PathchSageAttentionKJ`
- `MiniMaxH3EasyLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3EasyMediaLoader`
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

覆盖率 **93%**（56/60）

**有卡**：`MiniMaxH3EasyOutput`、`BasicGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`VAEDecodeAudio`、`VAEDecode`、`CreateVideo`、`KSamplerSelect`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`SaveVideo`、`MiniMaxH3Easy`、`BasicScheduler`、`PathchSageAttentionKJ`、`MiniMaxH3EasyLoader`、`LoraLoaderModelOnly`、`MiniMaxH3EasyMediaLoader`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
