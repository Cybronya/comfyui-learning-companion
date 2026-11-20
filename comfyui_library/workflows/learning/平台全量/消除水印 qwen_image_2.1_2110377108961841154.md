---
key: 平台全量/消除水印 qwen_image_2.1_2110377108961841154.json
name: 消除水印 qwen_image_2.1_2110377108961841154
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/消除水印 qwen_image_2.1_2110377108961841154.json
hash: 2d72bda59cedc5b4
coverage: 0.928571
learned_at: 2026-11-14 02:20:10
nodes: [SaveImage, CLIPLoader, KSamplerSelect, ManualSigmas, UNETLoader, QwenImage21Cache, VAELoader, Image Comparer (rgthree), SamplerCustom, VAEDecode, LoadImage, TextEncodeQwenImage21, Int, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 平台全量/消除水印 qwen_image_2.1_2110377108961841154.json

> 来源文件 `comfyui_library/workflows/平台全量/消除水印 qwen_image_2.1_2110377108961841154.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（14 个）：
- `SaveImage`
- `CLIPLoader`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `VAELoader`
- `Image Comparer (rgthree)`
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `TextEncodeQwenImage21`
- `Int`
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **93%**（13/14）

**有卡**：`SaveImage`、`CLIPLoader`、`KSamplerSelect`、`ManualSigmas`、`UNETLoader`、`QwenImage21Cache`、`VAELoader`、`SamplerCustom`、`VAEDecode`、`LoadImage`、`TextEncodeQwenImage21`、`Int`、`LoraLoaderModelOnly`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
