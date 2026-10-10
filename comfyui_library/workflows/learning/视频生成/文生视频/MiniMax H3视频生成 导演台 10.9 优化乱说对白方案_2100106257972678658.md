---
key: 视频生成/文生视频/MiniMax H3视频生成 导演台 10.9 优化乱说对白方案_2100106257972678658.json
name: MiniMax H3视频生成 导演台 10.9 优化乱说对白方案_2100106257972678658
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3视频生成 导演台 10.9 优化乱说对白方案_2100106257972678658.json
hash: 2bdd926c10ac98b3
coverage: 0.85
learned_at: 2026-10-10 23:03:27
nodes: [UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, VAELoader, PathchSageAttentionKJ, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, KSampler, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, EmptyLatentImage, VAEDecode, CLIPTextEncode, CLIPLoader, JjkText, CLIPTextEncode, solarL_SaveImagesToZip, LoraLoaderModelOnly, Note, MarkdownNote, MarkdownNote, Note, MiniMaxH3Director, VHS_VideoCombine, MarkdownNote, SaveImage, LoadImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/MiniMax H3视频生成 导演台 10.9 优化乱说对白方案_2100106257972678658.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3视频生成 导演台 10.9 优化乱说对白方案_2100106257972678658.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（40 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `PathchSageAttentionKJ`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
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
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `MarkdownNote`
- `MarkdownNote`
- `Note`
- `MiniMaxH3Director`
- `VHS_VideoCombine`
- `MarkdownNote`
- `SaveImage`
- `LoadImage`

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

覆盖率 **85%**（34/40）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`PathchSageAttentionKJ`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`KSampler`、`EmptyLatentImage`、`VAEDecode`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`MiniMaxH3Director`、`VHS_VideoCombine`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
