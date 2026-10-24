---
key: 图片生成/图生图/千问Qwen-Edit2509多图融合-多实例1.0-test_2000486442172284930.json
name: 千问Qwen-Edit2509多图融合-多实例1.0-test_2000486442172284930
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/千问Qwen-Edit2509多图融合-多实例1.0-test_2000486442172284930.json
hash: b374f60e657990b7
coverage: 0.661017
learned_at: 2026-10-23 12:30:02
nodes: [SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, PreviewImage, MarkdownNote, easy cleanGpuUsed, ImageConcanate, VAEDecode, ImageConcanate, ImageConcanate, FluxKontextImageScale, FluxKontextImageScale, MarkdownNote, EmptySD3LatentImage, LoadImage, PreviewImage, MarkdownNote, MarkdownNote, easy clearCacheAll, ImageConcanate, ImageConcanate, ImageConcanate, FluxKontextImageScale, FluxKontextImageScale, FluxKontextImageScale, MarkdownNote, EmptySD3LatentImage, easy cleanGpuUsed, CFGNorm, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, MarkdownNote, MarkdownNote, FluxKontextImageScale, TextEncodeQwenImageEditPlus, LoadImage, TextEncodeQwenImageEditPlus, KSampler, KSampler, LoadImage, CR Seed, MarkdownNote, LoadImage, LoadImage, LoadImage, CLIPLoader, VAELoader, VAEDecode, SaveImage, PreviewImage, PreviewImage, UNETLoader, LoraLoaderModelOnly]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1118877715456453, "steps": 30}
---

# 图片生成/图生图/千问Qwen-Edit2509多图融合-多实例1.0-test_2000486442172284930.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/千问Qwen-Edit2509多图融合-多实例1.0-test_2000486442172284930.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `MarkdownNote`
- `easy cleanGpuUsed`
- `ImageConcanate`
- `VAEDecode` ★核心
- `ImageConcanate`
- `ImageConcanate`
- `FluxKontextImageScale`
- `FluxKontextImageScale`
- `MarkdownNote`
- `EmptySD3LatentImage`
- `LoadImage`
- `PreviewImage`
- `MarkdownNote`
- `MarkdownNote`
- `easy clearCacheAll`
- `ImageConcanate`
- `ImageConcanate`
- `ImageConcanate`
- `FluxKontextImageScale`
- `FluxKontextImageScale`
- `FluxKontextImageScale`
- `MarkdownNote`
- `EmptySD3LatentImage`
- `easy cleanGpuUsed`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `MarkdownNote`
- `MarkdownNote`
- `FluxKontextImageScale`
- `TextEncodeQwenImageEditPlus`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `KSampler` ★核心
- `LoadImage`
- `CR Seed`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心

## 关键参数

- `seed` = `1118877715456453`
- `steps` = `30`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **66%**（39/59）

**有卡**：`easy cleanGpuUsed`、`ImageConcanate`、`VAEDecode`、`FluxKontextImageScale`、`EmptySD3LatentImage`、`LoadImage`、`easy clearCacheAll`、`CFGNorm`、`ModelSamplingAuraFlow`、`TextEncodeQwenImageEditPlus`、`KSampler`、`CR Seed`、`CLIPLoader`、`VAELoader`、`SaveImage`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm
