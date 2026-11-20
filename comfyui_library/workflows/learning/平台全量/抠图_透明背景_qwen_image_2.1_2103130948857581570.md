---
key: 平台全量/抠图_透明背景_qwen_image_2.1_2103130948857581570.json
name: 抠图_透明背景_qwen_image_2.1_2103130948857581570
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/抠图_透明背景_qwen_image_2.1_2103130948857581570.json
hash: 0af6b8b02c5212f5
coverage: 0.777778
learned_at: 2026-11-14 02:06:34
nodes: [LoadImage, SaveImage, JjkText, KSamplerSelect, ManualSigmas, VAELoader, QwenImage21Cache, JjkText, CLIPLoader, SamplerCustom, TextEncodeQwenImage21, VAEDecode, Image Comparer (rgthree), UNETLoader, CR Text Replace, ShowText|pysssss, Int, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 平台全量/抠图_透明背景_qwen_image_2.1_2103130948857581570.json

> 来源文件 `comfyui_library/workflows/平台全量/抠图_透明背景_qwen_image_2.1_2103130948857581570.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（18 个）：
- `LoadImage`
- `SaveImage`
- `JjkText`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `VAELoader`
- `QwenImage21Cache`
- `JjkText`
- `CLIPLoader`
- `SamplerCustom` ★核心
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `CR Text Replace`
- `ShowText|pysssss`
- `Int`
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **78%**（14/18）

**有卡**：`LoadImage`、`SaveImage`、`KSamplerSelect`、`ManualSigmas`、`VAELoader`、`QwenImage21Cache`、`CLIPLoader`、`SamplerCustom`、`TextEncodeQwenImage21`、`VAEDecode`、`UNETLoader`、`CR Text Replace`、`Int`、`LoraLoaderModelOnly`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
