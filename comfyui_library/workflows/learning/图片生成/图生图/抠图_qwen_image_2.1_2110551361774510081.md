---
key: 图片生成/图生图/抠图_qwen_image_2.1_2110551361774510081.json
name: 抠图_qwen_image_2.1_2110551361774510081
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/抠图_qwen_image_2.1_2110551361774510081.json
hash: 6be9e62aa62163d8
coverage: 0.8125
learned_at: 2026-10-23 12:55:08
nodes: [JjkText, LoraLoaderModelOnly, QwenImage21Cache, JjkText, CR Text Replace, LoadImage, KSamplerSelect, SamplerCustom, VAEDecode, SaveImage, Image Comparer (rgthree), TextEncodeQwenImage21, ManualSigmas, VAELoader, CLIPLoader, UNETLoader]
patterns: []
missing: []
---

# 图片生成/图生图/抠图_qwen_image_2.1_2110551361774510081.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/抠图_qwen_image_2.1_2110551361774510081.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（16 个）：
- `JjkText`
- `LoraLoaderModelOnly` ★核心
- `QwenImage21Cache`
- `JjkText`
- `CR Text Replace`
- `LoadImage`
- `KSamplerSelect` ★核心
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `TextEncodeQwenImage21`
- `ManualSigmas`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心

## 知识

覆盖率 **81%**（13/16）

**有卡**：`LoraLoaderModelOnly`、`QwenImage21Cache`、`CR Text Replace`、`LoadImage`、`KSamplerSelect`、`SamplerCustom`、`VAEDecode`、`SaveImage`、`TextEncodeQwenImage21`、`ManualSigmas`、`VAELoader`、`CLIPLoader`、`UNETLoader`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
