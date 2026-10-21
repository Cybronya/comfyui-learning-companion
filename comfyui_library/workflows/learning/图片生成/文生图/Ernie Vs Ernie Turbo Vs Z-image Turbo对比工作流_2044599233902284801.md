---
key: 图片生成/文生图/Ernie Vs Ernie Turbo Vs Z-image Turbo对比工作流_2044599233902284801.json
name: Ernie Vs Ernie Turbo Vs Z-image Turbo对比工作流_2044599233902284801
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Ernie Vs Ernie Turbo Vs Z-image Turbo对比工作流_2044599233902284801.json
hash: da3008a2765cfdce
coverage: 0.911111
learned_at: 2026-10-21 02:51:40
nodes: [UNETLoader, CLIPTextEncode, VAELoader, PreviewAny, PreviewAny, StringReplace, StringReplace, PreviewAny, StringReplace, UNETLoader, CLIPTextEncode, ConditioningZeroOut, VAEDecode, AddLabel, VAEDecode, KSampler, CLIPLoader, ConditioningZeroOut, UNETLoader, CLIPTextEncode, VAELoader, ShowAnything|Mie, VAEDecode, AddLabel, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, ImageConcatMulti, KSampler, CLIPLoader, SaveImage, CLIPLoader, Seed (rgthree), KSampler, PrimitiveStringMultiline, EmptyFlux2LatentImage, EmptyLatentImage, JWInteger, JWInteger, TextGenerate, CLIPTextEncode, SaveImage, SaveImage, SaveImage, AddLabel]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 984595656509346, "steps": 10, "width": 1920}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Ernie Vs Ernie Turbo Vs Z-image Turbo对比工作流_2044599233902284801.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Ernie Vs Ernie Turbo Vs Z-image Turbo对比工作流_2044599233902284801.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `PreviewAny`
- `PreviewAny`
- `StringReplace`
- `StringReplace`
- `PreviewAny`
- `StringReplace`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `AddLabel`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CLIPLoader`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAELoader`
- `ShowAnything|Mie`
- `VAEDecode` ★核心
- `AddLabel`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `ImageConcatMulti`
- `KSampler` ★核心
- `CLIPLoader`
- `SaveImage`
- `CLIPLoader`
- `Seed (rgthree)`
- `KSampler` ★核心
- `PrimitiveStringMultiline`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage` ★核心
- `JWInteger`
- `JWInteger`
- `TextGenerate`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `AddLabel`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `984595656509346`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`

## 知识

覆盖率 **91%**（41/45）

**有卡**：`UNETLoader`、`CLIPTextEncode`、`VAELoader`、`StringReplace`、`ConditioningZeroOut`、`VAEDecode`、`AddLabel`、`KSampler`、`CLIPLoader`、`ShowAnything|Mie`、`easy cleanGpuUsed`、`ImageConcatMulti`、`SaveImage`、`Seed (rgthree)`、`EmptyFlux2LatentImage`、`EmptyLatentImage`、`JWInteger`、`TextGenerate`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
