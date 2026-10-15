---
key: 图片生成/文生图/wan2.2双噪文生图-极致逼真_1951536173342773249.json
name: wan2.2双噪文生图-极致逼真_1951536173342773249
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2双噪文生图-极致逼真_1951536173342773249.json
hash: f6b1217bdb851ea1
coverage: 0.607143
learned_at: 2026-10-10 20:59:27
nodes: [SetNode, SetNode, ModelPassThrough, GetNode, CLIPTextEncode, LoraLoaderModelOnly, Label (rgthree), Label (rgthree), Anything Everywhere, Anything Everywhere, CLIPTextEncode, KSamplerAdvanced, EmptyLatentImage, ModelPassThrough, GetNode, LoraLoaderModelOnly, MarkdownNote, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, PreviewImage, KSamplerAdvanced, Note Plus (mtb)]
patterns: []
missing: [Label (rgthree), Label (rgthree), Note Plus (mtb)]
parameters: {"batch_size": 1, "cfg": 30, "denoise": "bong_tangent", "height": 1088, "sampler_name": 3, "scheduler": "res_2s", "seed": "enable", "steps": "randomize", "width": 1920}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/wan2.2双噪文生图-极致逼真_1951536173342773249.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2双噪文生图-极致逼真_1951536173342773249.json`

## 结构

**节点**（28 个）：
- `SetNode`
- `SetNode`
- `ModelPassThrough`
- `GetNode`
- `CLIPTextEncode`
- `LoraLoaderModelOnly`
- `Label (rgthree)`
- `Label (rgthree)`
- `Anything Everywhere`
- `Anything Everywhere`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `EmptyLatentImage`
- `ModelPassThrough`
- `GetNode`
- `LoraLoaderModelOnly`
- `MarkdownNote`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `PreviewImage`
- `KSamplerAdvanced`
- `Note Plus (mtb)`

## 关键参数

- `batch_size` = `1`
- `cfg` = `30`
- `denoise` = `bong_tangent`
- `height` = `1088`
- `sampler_name` = `3`
- `scheduler` = `res_2s`
- `seed` = `enable`
- `steps` = `randomize`
- `width` = `1920`

## 知识

覆盖率 **61%**（17/28）

**有卡**：`SetNode`、`ModelPassThrough`、`GetNode`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`Label (rgthree)`、`Anything Everywhere`、`KSamplerAdvanced`、`EmptyLatentImage`、`MarkdownNote`

**缺卡**（3）：`Label (rgthree)`、`Label (rgthree)`、`Note Plus (mtb)`

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Note Plus (mtb)` 知识库中没有该节点类型的任何知识
