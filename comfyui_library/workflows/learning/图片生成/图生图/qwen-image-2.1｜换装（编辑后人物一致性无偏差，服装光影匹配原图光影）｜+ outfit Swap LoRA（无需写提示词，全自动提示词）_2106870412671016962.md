---
key: 图片生成/图生图/qwen-image-2.1｜换装（编辑后人物一致性无偏差，服装光影匹配原图光影）｜+ outfit Swap LoRA（无需写提示词，全自动提示词）_2106870412671016962.json
name: qwen-image-2.1｜换装（编辑后人物一致性无偏差，服装光影匹配原图光影）｜+ outfit Swap LoRA（无需写提示词，全自动提示词）_2106870412671016962
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image-2.1｜换装（编辑后人物一致性无偏差，服装光影匹配原图光影）｜+ outfit Swap LoRA（无需写提示词，全自动提示词）_2106870412671016962.json
hash: 39686ee69994f015
coverage: 0.289474
learned_at: 2026-10-06 21:42:06
nodes: [ComfySwitchNode, UNETLoader, LoraLoaderModelOnly, ComfySwitchNode, RegexMatch, TextGenerate, RegexReplace, JjkText, PrimitiveBoolean, JjkText, JjkText, TextGenerate, ComfySwitchNode, JjkText, JjkText, RegexMatch, TextGenerate, JjkText, LoadImage, VAEDecode, KSampler, SplitImageWithAlpha, VAELoader, CLIPLoader, LoadImage, StringFormat, JjkShowText, Note, Label (rgthree), Label (rgthree), Label (rgthree), TextEncodeQwenImage21, Note, QwenImage21Cache, Note, Note, Image Comparer (rgthree), SaveImage]
patterns: []
missing: [JjkShowText, Label (rgthree), Label (rgthree), Label (rgthree), PrimitiveBoolean, RegexMatch, RegexMatch, RegexReplace, SplitImageWithAlpha, StringFormat, TextGenerate, TextGenerate, TextGenerate]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 371892550278457, "steps": 25}
discoveries: [次要节点 `JjkShowText` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `PrimitiveBoolean` 知识库中没有该节点类型的任何知识, 次要节点 `RegexMatch` 知识库中没有该节点类型的任何知识, 次要节点 `RegexMatch` 知识库中没有该节点类型的任何知识, 次要节点 `RegexReplace` 知识库中没有该节点类型的任何知识, 次要节点 `SplitImageWithAlpha` 知识库中没有该节点类型的任何知识, 次要节点 `StringFormat` 知识库中没有该节点类型的任何知识, 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识, 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识, 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/qwen-image-2.1｜换装（编辑后人物一致性无偏差，服装光影匹配原图光影）｜+ outfit Swap LoRA（无需写提示词，全自动提示词）_2106870412671016962.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-image-2.1｜换装（编辑后人物一致性无偏差，服装光影匹配原图光影）｜+ outfit Swap LoRA（无需写提示词，全自动提示词）_2106870412671016962.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

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

覆盖率 **29%**（11/38）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`LoadImage`、`VAEDecode`、`KSampler`、`VAELoader`、`CLIPLoader`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`SaveImage`

**缺卡**（13）：`JjkShowText`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`PrimitiveBoolean`、`RegexMatch`、`RegexMatch`、`RegexReplace`、`SplitImageWithAlpha`、`StringFormat`、`TextGenerate`、`TextGenerate`、`TextGenerate`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache

## 学习发现

- 次要节点 `JjkShowText` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `PrimitiveBoolean` 知识库中没有该节点类型的任何知识
- 次要节点 `RegexMatch` 知识库中没有该节点类型的任何知识
- 次要节点 `RegexMatch` 知识库中没有该节点类型的任何知识
- 次要节点 `RegexReplace` 知识库中没有该节点类型的任何知识
- 次要节点 `SplitImageWithAlpha` 知识库中没有该节点类型的任何知识
- 次要节点 `StringFormat` 知识库中没有该节点类型的任何知识
- 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识
- 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识
- 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识
