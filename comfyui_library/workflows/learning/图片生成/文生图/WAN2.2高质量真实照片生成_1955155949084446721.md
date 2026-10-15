---
key: 图片生成/文生图/WAN2.2高质量真实照片生成_1955155949084446721.json
name: WAN2.2高质量真实照片生成_1955155949084446721
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/WAN2.2高质量真实照片生成_1955155949084446721.json
hash: 0a1c45f79578d2c4
coverage: 0.722222
learned_at: 2026-10-15 22:27:34
nodes: [CLIPTextEncode, CLIPTextEncode, VAEDecode, CLIPLoader, CLIPTextEncode, LatentUpscaleBy, LoraLoaderModelOnly, CLIPLoader, CLIPTextEncode, Note, VAEDecode, VAELoader, LoraLoaderModelOnly, Note, KSampler, KSampler, UnetLoaderGGUF, Note, Text Concatenate, CLIPTextEncode, Note, Note, String, VAELoader, EmptyHunyuanLatentVideo, CLIPLoader, LoraLoaderModelOnly, Note, VAEDecode, VAEDecode, PreviewImage, PreviewImage, Note, Note, ClownsharKSampler_Beta, PreviewImage, Image Comparer (rgthree), SaveImage, PreviewImage, Image Sharpen FS, Image Sharpen FS, SaveImage, LoraLoaderModelOnly, UnetLoaderGGUF, LatentUpscaleBy, UnetLoaderGGUF, ClownsharKSampler_Beta, CLIPTextEncode, easy showAnything, Image Comparer (rgthree), LoraLoaderModelOnly, UnetLoaderGGUF, Text, Text]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 20, "denoise": 1.0000000000000002, "sampler_name": 10, "scheduler": 1, "seed": 0.30000000000000004, "steps": "bong_tangent"}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/WAN2.2高质量真实照片生成_1955155949084446721.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/WAN2.2高质量真实照片生成_1955155949084446721.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `LatentUpscaleBy`
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
- `UnetLoaderGGUF` ★核心
- `Note`
- `Text Concatenate`
- `CLIPTextEncode` ★核心
- `Note`
- `Note`
- `String`
- `VAELoader`
- `EmptyHunyuanLatentVideo`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
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
- `LoraLoaderModelOnly` ★核心
- `UnetLoaderGGUF` ★核心
- `Text`
- `Text`

## 关键参数

- `seed` = `0.30000000000000004`
- `steps` = `bong_tangent`
- `cfg` = `20`
- `sampler_name` = `10`
- `scheduler` = `1`
- `denoise` = `1.0000000000000002`

## 知识

覆盖率 **72%**（39/54）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`CLIPLoader`、`LatentUpscaleBy`、`LoraLoaderModelOnly`、`VAELoader`、`KSampler`、`UnetLoaderGGUF`、`Text Concatenate`、`String`、`EmptyHunyuanLatentVideo`、`ClownsharKSampler_Beta`、`SaveImage`、`Image Sharpen FS`、`Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ClownsharKSampler_Beta、LatentUpscaleBy

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
