---
key: 图片生成/图生图/移除遮挡物体 抠图 透明背景 qwen image Image Cutout, Transparen_2112712324380454914.json
name: 移除遮挡物体 抠图 透明背景 qwen image Image Cutout, Transparen_2112712324380454914
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/移除遮挡物体 抠图 透明背景 qwen image Image Cutout, Transparen_2112712324380454914.json
hash: b761b48d389d8fbf
coverage: 0.777778
learned_at: 2026-10-23 13:20:08
nodes: [KSamplerSelect, ManualSigmas, VAELoader, QwenImage21Cache, CLIPLoader, SamplerCustom, TextEncodeQwenImage21, UNETLoader, CR Text Replace, ShowText|pysssss, Int, LoraLoaderModelOnly, VAEDecode, SaveImage, Image Comparer (rgthree), JjkText, LoadImage, JjkText]
patterns: []
missing: []
---

# 图片生成/图生图/移除遮挡物体 抠图 透明背景 qwen image Image Cutout, Transparen_2112712324380454914.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/移除遮挡物体 抠图 透明背景 qwen image Image Cutout, Transparen_2112712324380454914.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（18 个）：
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `VAELoader`
- `QwenImage21Cache`
- `CLIPLoader`
- `SamplerCustom` ★核心
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `CR Text Replace`
- `ShowText|pysssss`
- `Int`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `JjkText`
- `LoadImage`
- `JjkText`

## 知识

覆盖率 **78%**（14/18）

**有卡**：`KSamplerSelect`、`ManualSigmas`、`VAELoader`、`QwenImage21Cache`、`CLIPLoader`、`SamplerCustom`、`TextEncodeQwenImage21`、`UNETLoader`、`CR Text Replace`、`Int`、`LoraLoaderModelOnly`、`VAEDecode`、`SaveImage`、`LoadImage`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
