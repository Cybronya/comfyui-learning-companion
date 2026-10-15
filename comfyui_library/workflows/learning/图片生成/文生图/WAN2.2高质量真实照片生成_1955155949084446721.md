---
key: 图片生成/文生图/WAN2.2高质量真实照片生成_1955155949084446721.json
name: WAN2.2高质量真实照片生成_1955155949084446721
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/WAN2.2高质量真实照片生成_1955155949084446721.json
hash: 0a1c45f79578d2c4
coverage: 0.666667
learned_at: 2026-10-10 20:59:13
nodes: [CLIPTextEncode, CLIPTextEncode, VAEDecode, CLIPLoader, CLIPTextEncode, LatentUpscaleBy, LoraLoaderModelOnly, CLIPLoader, CLIPTextEncode, Note, VAEDecode, VAELoader, LoraLoaderModelOnly, Note, KSampler, KSampler, UnetLoaderGGUF, Note, Text Concatenate, CLIPTextEncode, Note, Note, String, VAELoader, EmptyHunyuanLatentVideo, CLIPLoader, LoraLoaderModelOnly, Note, VAEDecode, VAEDecode, PreviewImage, PreviewImage, Note, Note, ClownsharKSampler_Beta, PreviewImage, Image Comparer (rgthree), SaveImage, PreviewImage, Image Sharpen FS, Image Sharpen FS, SaveImage, LoraLoaderModelOnly, UnetLoaderGGUF, LatentUpscaleBy, UnetLoaderGGUF, ClownsharKSampler_Beta, CLIPTextEncode, easy showAnything, Image Comparer (rgthree), LoraLoaderModelOnly, UnetLoaderGGUF, Text, Text]
patterns: []
missing: [Image Sharpen FS, Image Sharpen FS, Text Concatenate]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 20, "denoise": 1.0000000000000002, "sampler_name": 10, "scheduler": 1, "seed": 0.30000000000000004, "steps": "bong_tangent"}
discoveries: [次要节点 `Image Sharpen FS` 知识库中没有该节点类型的任何知识, 次要节点 `Image Sharpen FS` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/WAN2.2高质量真实照片生成_1955155949084446721.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/WAN2.2高质量真实照片生成_1955155949084446721.json`

## 结构

**节点**（54 个）：
- `CLIPTextEncode`
- `CLIPTextEncode`
- `VAEDecode`
- `CLIPLoader`
- `CLIPTextEncode`
- `LatentUpscaleBy`
- `LoraLoaderModelOnly`
- `CLIPLoader`
- `CLIPTextEncode`
- `Note`
- `VAEDecode`
- `VAELoader`
- `LoraLoaderModelOnly`
- `Note`
- `KSampler`
- `KSampler`
- `UnetLoaderGGUF`
- `Note`
- `Text Concatenate`
- `CLIPTextEncode`
- `Note`
- `Note`
- `String`
- `VAELoader`
- `EmptyHunyuanLatentVideo`
- `CLIPLoader`
- `LoraLoaderModelOnly`
- `Note`
- `VAEDecode`
- `VAEDecode`
- `PreviewImage`
- `PreviewImage`
- `Note`
- `Note`
- `ClownsharKSampler_Beta`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `PreviewImage`
- `Image Sharpen FS`
- `Image Sharpen FS`
- `SaveImage`
- `LoraLoaderModelOnly`
- `UnetLoaderGGUF`
- `LatentUpscaleBy`
- `UnetLoaderGGUF`
- `ClownsharKSampler_Beta`
- `CLIPTextEncode`
- `easy showAnything`
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly`
- `UnetLoaderGGUF`
- `Text`
- `Text`

## 关键参数

- `cfg` = `20`
- `denoise` = `1.0000000000000002`
- `sampler_name` = `10`
- `scheduler` = `1`
- `seed` = `0.30000000000000004`
- `steps` = `bong_tangent`

## 知识

覆盖率 **67%**（36/54）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`CLIPLoader`、`LatentUpscaleBy`、`LoraLoaderModelOnly`、`Note`、`VAELoader`、`KSampler`、`UnetLoaderGGUF`、`Text Concatenate`、`String`、`EmptyHunyuanLatentVideo`、`PreviewImage`、`ClownsharKSampler_Beta`

**缺卡**（3）：`Image Sharpen FS`、`Image Sharpen FS`、`Text Concatenate`

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
