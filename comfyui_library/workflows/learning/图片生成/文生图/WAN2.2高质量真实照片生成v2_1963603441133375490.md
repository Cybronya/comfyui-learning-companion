---
key: 图片生成/文生图/WAN2.2高质量真实照片生成v2_1963603441133375490.json
name: WAN2.2高质量真实照片生成v2_1963603441133375490.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/WAN2.2高质量真实照片生成v2_1963603441133375490.json
hash: 03c2db234adceca3
coverage: 0.694915
learned_at: 2026-10-07 23:54:32
nodes: [CLIPTextEncode, CLIPTextEncode, VAEDecode, CLIPLoader, CLIPTextEncode, LoraLoaderModelOnly, CLIPLoader, CLIPTextEncode, Note, VAEDecode, VAELoader, LoraLoaderModelOnly, Note, KSampler, KSampler, Note, Text Concatenate, Note, Note, VAELoader, EmptyHunyuanLatentVideo, CLIPLoader, Note, VAEDecode, VAEDecode, PreviewImage, PreviewImage, Note, Note, ClownsharKSampler_Beta, PreviewImage, Image Comparer (rgthree), SaveImage, PreviewImage, Image Sharpen FS, Image Sharpen FS, SaveImage, LoraLoaderModelOnly, UnetLoaderGGUF, LatentUpscaleBy, UnetLoaderGGUF, ClownsharKSampler_Beta, CLIPTextEncode, easy showAnything, Image Comparer (rgthree), UnetLoaderGGUF, CLIPTextEncode, String, Text, Text, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LatentUpscaleBy, UnetLoaderGGUF, UNETLoader, UNETLoader, UNETLoader]
patterns: []
missing: [Image Sharpen FS, Image Sharpen FS, Text Concatenate]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 20, "denoise": 1.0000000000000002, "sampler_name": 10, "scheduler": 1, "seed": 0.30000000000000004, "steps": "bong_tangent"}
discoveries: [次要节点 `Image Sharpen FS` 知识库中没有该节点类型的任何知识, 次要节点 `Image Sharpen FS` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/WAN2.2高质量真实照片生成v2_1963603441133375490.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1963603441133375490.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `Note`
- `VAEDecode` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `KSampler` ★核心
- `KSampler` ★核心
- `Note`
- `Text Concatenate`
- `Note`
- `Note`
- `VAELoader`
- `EmptyHunyuanLatentVideo`
- `CLIPLoader`
- `Note`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `PreviewImage`
- `Note`
- `Note`
- `ClownsharKSampler_Beta` ★核心
- `PreviewImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `PreviewImage`
- `Image Sharpen FS`
- `Image Sharpen FS`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `UnetLoaderGGUF` ★核心
- `LatentUpscaleBy`
- `UnetLoaderGGUF` ★核心
- `ClownsharKSampler_Beta` ★核心
- `CLIPTextEncode` ★核心
- `easy showAnything`
- `Image Comparer (rgthree)`
- `UnetLoaderGGUF` ★核心
- `CLIPTextEncode` ★核心
- `String`
- `Text`
- `Text`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LatentUpscaleBy`
- `UnetLoaderGGUF` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `0.30000000000000004`
- `steps` = `bong_tangent`
- `cfg` = `20`
- `sampler_name` = `10`
- `scheduler` = `1`
- `denoise` = `1.0000000000000002`

## 知识

覆盖率 **69%**（41/59）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`CLIPLoader`、`LoraLoaderModelOnly`、`VAELoader`、`KSampler`、`EmptyHunyuanLatentVideo`、`ClownsharKSampler_Beta`、`SaveImage`、`UnetLoaderGGUF`、`LatentUpscaleBy`、`String`、`Text`、`UNETLoader`

**缺卡**（3）：`Image Sharpen FS`、`Image Sharpen FS`、`Text Concatenate`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、ClownsharKSampler_Beta

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Image Sharpen FS` 知识库中没有该节点类型的任何知识
- 次要节点 `Image Sharpen FS` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
