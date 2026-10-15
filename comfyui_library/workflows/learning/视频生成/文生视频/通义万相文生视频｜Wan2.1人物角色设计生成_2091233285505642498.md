---
key: 视频生成/文生视频/通义万相文生视频｜Wan2.1人物角色设计生成_2091233285505642498.json
name: 通义万相文生视频｜Wan2.1人物角色设计生成_2091233285505642498
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/通义万相文生视频｜Wan2.1人物角色设计生成_2091233285505642498.json
hash: d5b0d2c48a22db0f
coverage: 0.891892
learned_at: 2026-10-15 22:49:04
nodes: [CLIPTextEncode, VAEDecode, VHS_VideoCombine, KSampler, WanVideoTeaCacheKJ, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, EmptyHunyuanLatentVideo, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/通义万相文生视频｜Wan2.1人物角色设计生成_2091233285505642498.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/通义万相文生视频｜Wan2.1人物角色设计生成_2091233285505642498.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（37 个）：
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `KSampler` ★核心
- `WanVideoTeaCacheKJ`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
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

覆盖率 **89%**（33/37）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`VHS_VideoCombine`、`KSampler`、`WanVideoTeaCacheKJ`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyHunyuanLatentVideo`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
