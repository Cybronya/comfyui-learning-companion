---
key: 图片生成/图生图/qwen-image-2.1｜换装（编辑后人物一致性无偏差，服装光影匹配原图光影）｜+ outfit Swap LoRA（无需写提示词，全自动提示词）_2106870412671016962.json
name: qwen-image-2.1｜换装（编辑后人物一致性无偏差，服装光影匹配原图光影）｜+ outfit Swap LoRA（无需写提示词，全自动提示词）_2106870412671016962
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image-2.1｜换装（编辑后人物一致性无偏差，服装光影匹配原图光影）｜+ outfit Swap LoRA（无需写提示词，全自动提示词）_2106870412671016962.json
hash: 39686ee69994f015
coverage: 0.631579
learned_at: 2026-10-15 22:25:36
nodes: [ComfySwitchNode, UNETLoader, LoraLoaderModelOnly, ComfySwitchNode, RegexMatch, TextGenerate, RegexReplace, JjkText, PrimitiveBoolean, JjkText, JjkText, TextGenerate, ComfySwitchNode, JjkText, JjkText, RegexMatch, TextGenerate, JjkText, LoadImage, VAEDecode, KSampler, SplitImageWithAlpha, VAELoader, CLIPLoader, LoadImage, StringFormat, JjkShowText, Note, Label (rgthree), Label (rgthree), Label (rgthree), TextEncodeQwenImage21, Note, QwenImage21Cache, Note, Note, Image Comparer (rgthree), SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 371892550278457, "steps": 25}
---

# 图片生成/图生图/qwen-image-2.1｜换装（编辑后人物一致性无偏差，服装光影匹配原图光影）｜+ outfit Swap LoRA（无需写提示词，全自动提示词）_2106870412671016962.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-image-2.1｜换装（编辑后人物一致性无偏差，服装光影匹配原图光影）｜+ outfit Swap LoRA（无需写提示词，全自动提示词）_2106870412671016962.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `ComfySwitchNode`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ComfySwitchNode`
- `RegexMatch`
- `TextGenerate`
- `RegexReplace`
- `JjkText`
- `PrimitiveBoolean`
- `JjkText`
- `JjkText`
- `TextGenerate`
- `ComfySwitchNode`
- `JjkText`
- `JjkText`
- `RegexMatch`
- `TextGenerate`
- `JjkText`
- `LoadImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SplitImageWithAlpha`
- `VAELoader`
- `CLIPLoader`
- `LoadImage`
- `StringFormat`
- `JjkShowText`
- `Note`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `TextEncodeQwenImage21`
- `Note`
- `QwenImage21Cache`
- `Note`
- `Note`
- `Image Comparer (rgthree)`
- `SaveImage`

## 关键参数

- `seed` = `371892550278457`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **63%**（24/38）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`RegexMatch`、`TextGenerate`、`RegexReplace`、`PrimitiveBoolean`、`LoadImage`、`VAEDecode`、`KSampler`、`SplitImageWithAlpha`、`VAELoader`、`CLIPLoader`、`StringFormat`、`JjkShowText`、`Label (rgthree)`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache
