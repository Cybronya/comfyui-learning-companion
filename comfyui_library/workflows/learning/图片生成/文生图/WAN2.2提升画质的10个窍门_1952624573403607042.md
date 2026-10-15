---
key: 图片生成/文生图/WAN2.2提升画质的10个窍门_1952624573403607042.json
name: WAN2.2提升画质的10个窍门_1952624573403607042
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/WAN2.2提升画质的10个窍门_1952624573403607042.json
hash: 2841b4a0ddbd4e88
coverage: 0.586207
learned_at: 2026-10-15 22:27:34
nodes: [VAELoader, VAEDecode, VAEDecode, CLIPLoader, MarkdownNote, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, CLIPTextEncode, LoraLoaderModelOnly, MarkdownNote, MarkdownNote, PreviewImage, SaveImage, MarkdownNote, MarkdownNote, PreviewImage, KSamplerAdvanced, CLIPTextEncode, MarkdownNote, UNETLoader, MarkdownNote, KSamplerAdvanced, Note Plus (mtb), Label (rgthree), EmptyHunyuanLatentVideo, PrimitiveInt, PrimitiveInt, MarkdownNote]
patterns: []
missing: []
parameters: {"cfg": 30, "denoise": "bong_tangent", "sampler_name": 1, "scheduler": "res_2s", "seed": "enable", "steps": "fixed"}
---

# 图片生成/文生图/WAN2.2提升画质的10个窍门_1952624573403607042.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/WAN2.2提升画质的10个窍门_1952624573403607042.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（29 个）：
- `VAELoader`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `PreviewImage`
- `SaveImage`
- `MarkdownNote`
- `MarkdownNote`
- `PreviewImage`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `UNETLoader` ★核心
- `MarkdownNote`
- `KSamplerAdvanced` ★核心
- `Note Plus (mtb)`
- `Label (rgthree)`
- `EmptyHunyuanLatentVideo`
- `PrimitiveInt`
- `PrimitiveInt`
- `MarkdownNote`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `30`
- `sampler_name` = `1`
- `scheduler` = `res_2s`
- `denoise` = `bong_tangent`

## 知识

覆盖率 **59%**（17/29）

**有卡**：`VAELoader`、`VAEDecode`、`CLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPTextEncode`、`SaveImage`、`KSamplerAdvanced`、`Note Plus (mtb)`、`Label (rgthree)`、`EmptyHunyuanLatentVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、EmptyHunyuanLatentVideo
