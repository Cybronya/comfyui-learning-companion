---
key: 平台全量/flux2-klein-auto_inpaint_advanced_2085255128151580673.json
name: flux2-klein-auto_inpaint_advanced_2085255128151580673
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/flux2-klein-auto_inpaint_advanced_2085255128151580673.json
hash: dbe1305a6a5bb979
coverage: 1
learned_at: 2026-11-14 01:11:12
nodes: [UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, KSampler, VAEDecode, VAEEncode, ReferenceLatent, ReferenceLatent, SaveImage, CLIPTextEncode, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 194522388318966, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/flux2-klein-auto_inpaint_advanced_2085255128151580673.json

> 来源文件 `comfyui_library/workflows/平台全量/flux2-klein-auto_inpaint_advanced_2085255128151580673.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `194522388318966`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（12/12）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`KSampler`、`VAEDecode`、`VAEEncode`、`ReferenceLatent`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、ReferenceLatent

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
