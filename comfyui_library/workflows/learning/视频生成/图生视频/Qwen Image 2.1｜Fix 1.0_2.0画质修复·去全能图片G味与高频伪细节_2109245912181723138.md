---
key: 视频生成/图生视频/Qwen Image 2.1｜Fix 1.0_2.0画质修复·去全能图片G味与高频伪细节_2109245912181723138.json
name: Qwen Image 2.1｜Fix 1.0_2.0画质修复·去全能图片G味与高频伪细节_2109245912181723138
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen Image 2.1｜Fix 1.0_2.0画质修复·去全能图片G味与高频伪细节_2109245912181723138.json
hash: 9112102e01166e45
coverage: 0.487179
learned_at: 2026-10-18 00:23:46
nodes: [VAEDecode, SeedNode, EmptyLatentImage, TextEncodeQwenImage21, TextGenerate, KSamplerAdvanced, VAEDecode, KSamplerAdvanced, RegexExtract, ComfySwitchNode, StringConcatenate, PrimitiveNode, PrimitiveNode, PrimitiveNode, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, CLIPLoader, VAELoader, PrimitiveNode, TextEncodeQwenImage21, ComfySwitchNode, ComfySwitchNode, PrimitiveNode, StringConcatenate, UNETLoader, ComfySwitchNode, PrimitiveStringMultiline, PrimitiveStringMultiline, LoadImage, LoraLoaderModelOnly, Image Comparer (rgthree), Image Comparer (rgthree), SaveImage, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 20, "denoise": "simple", "height": 1600, "sampler_name": 3.5, "scheduler": "euler", "seed": "enable", "steps": "randomize", "width": 1200}
---

# 视频生成/图生视频/Qwen Image 2.1｜Fix 1.0_2.0画质修复·去全能图片G味与高频伪细节_2109245912181723138.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Qwen Image 2.1｜Fix 1.0_2.0画质修复·去全能图片G味与高频伪细节_2109245912181723138.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（39 个）：
- `VAEDecode` ★核心
- `SeedNode`
- `EmptyLatentImage` ★核心
- `TextEncodeQwenImage21`
- `TextGenerate`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `RegexExtract`
- `ComfySwitchNode`
- `StringConcatenate`
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `VAELoader`
- `PrimitiveNode`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `PrimitiveNode`
- `StringConcatenate`
- `UNETLoader` ★核心
- `ComfySwitchNode`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SaveImage`

## 关键参数

- `width` = `1200`
- `height` = `1600`
- `batch_size` = `1`
- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `3.5`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **49%**（19/39）

**有卡**：`VAEDecode`、`SeedNode`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`TextGenerate`、`KSamplerAdvanced`、`RegexExtract`、`StringConcatenate`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoadImage`、`LoraLoaderModelOnly`、`SaveImage`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader
