---
key: 视频生成/图生视频/MinimaxH3lightx2vlora图生视频工作流多重提速ENG加速ENG4步海螺ENG_2087126062730924033.json
name: MinimaxH3lightx2vlora图生视频工作流多重提速ENG加速ENG4步海螺ENG_2087126062730924033
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MinimaxH3lightx2vlora图生视频工作流多重提速ENG加速ENG4步海螺ENG_2087126062730924033.json
hash: fd5bb52afb3344e5
coverage: 0.830189
learned_at: 2026-10-16 21:07:25
nodes: [KSamplerSelect, BasicGuider, RandomNoise, SamplerCustomAdvanced, CreateVideo, VAEDecodeAudio, VAEDecode, ComfyMathExpression, BasicScheduler, VAELoader, VAELoader, UNETLoader, CLIPLoader, LoraLoaderModelOnly, SaveVideo, MiniMaxH3MemoryEfficientSageAttentionPatch, MarkdownNote, LoadImage, MiniMaxH3ImageToVideo, PrimitiveFloat, PrimitiveFloat, ResolutionSelector, MarkdownNote, Note, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, Note, 孤海注释]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/MinimaxH3lightx2vlora图生视频工作流多重提速ENG加速ENG4步海螺ENG_2087126062730924033.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MinimaxH3lightx2vlora图生视频工作流多重提速ENG加速ENG4步海螺ENG_2087126062730924033.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（53 个）：
- `KSamplerSelect` ★核心
- `BasicGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `CreateVideo`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `ComfyMathExpression`
- `BasicScheduler`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `SaveVideo`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MarkdownNote`
- `LoadImage`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `ResolutionSelector`
- `MarkdownNote`
- `Note`
- `孤海注释`
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
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `Note`
- `孤海注释`

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

覆盖率 **83%**（44/53）

**有卡**：`KSamplerSelect`、`BasicGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`CreateVideo`、`VAEDecodeAudio`、`VAEDecode`、`ComfyMathExpression`、`BasicScheduler`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`SaveVideo`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoadImage`、`MiniMaxH3ImageToVideo`、`ResolutionSelector`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
