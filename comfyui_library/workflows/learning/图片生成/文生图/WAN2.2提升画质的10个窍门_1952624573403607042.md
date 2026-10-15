---
key: 图片生成/文生图/WAN2.2提升画质的10个窍门_1952624573403607042.json
name: WAN2.2提升画质的10个窍门_1952624573403607042
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/WAN2.2提升画质的10个窍门_1952624573403607042.json
hash: 2841b4a0ddbd4e88
coverage: 0.517241
learned_at: 2026-10-10 20:59:13
nodes: [VAELoader, VAEDecode, VAEDecode, CLIPLoader, MarkdownNote, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, CLIPTextEncode, LoraLoaderModelOnly, MarkdownNote, MarkdownNote, PreviewImage, SaveImage, MarkdownNote, MarkdownNote, PreviewImage, KSamplerAdvanced, CLIPTextEncode, MarkdownNote, UNETLoader, MarkdownNote, KSamplerAdvanced, Note Plus (mtb), Label (rgthree), EmptyHunyuanLatentVideo, PrimitiveInt, PrimitiveInt, MarkdownNote]
patterns: []
missing: [Label (rgthree), Note Plus (mtb)]
parameters: {"cfg": 30, "denoise": "bong_tangent", "sampler_name": 1, "scheduler": "res_2s", "seed": "enable", "steps": "fixed"}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/WAN2.2提升画质的10个窍门_1952624573403607042.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/WAN2.2提升画质的10个窍门_1952624573403607042.json`

## 结构

**节点**（29 个）：
- `VAELoader`
- `VAEDecode`
- `VAEDecode`
- `CLIPLoader`
- `MarkdownNote`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `CLIPTextEncode`
- `LoraLoaderModelOnly`
- `MarkdownNote`
- `MarkdownNote`
- `PreviewImage`
- `SaveImage`
- `MarkdownNote`
- `MarkdownNote`
- `PreviewImage`
- `KSamplerAdvanced`
- `CLIPTextEncode`
- `MarkdownNote`
- `UNETLoader`
- `MarkdownNote`
- `KSamplerAdvanced`
- `Note Plus (mtb)`
- `Label (rgthree)`
- `EmptyHunyuanLatentVideo`
- `PrimitiveInt`
- `PrimitiveInt`
- `MarkdownNote`

## 关键参数

- `cfg` = `30`
- `denoise` = `bong_tangent`
- `sampler_name` = `1`
- `scheduler` = `res_2s`
- `seed` = `enable`
- `steps` = `fixed`

## 知识

覆盖率 **52%**（15/29）

**有卡**：`VAELoader`、`VAEDecode`、`CLIPLoader`、`MarkdownNote`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPTextEncode`、`PreviewImage`、`SaveImage`

**缺卡**（2）：`Label (rgthree)`、`Note Plus (mtb)`

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识
