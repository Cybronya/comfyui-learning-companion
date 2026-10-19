---
key: 数字人/数字人/QwenImage2.1 高清改图工作流_2110163424536784897.json
name: QwenImage2.1 高清改图工作流_2110163424536784897
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/QwenImage2.1 高清改图工作流_2110163424536784897.json
hash: 155136d7fd624aa9
coverage: 0.736842
learned_at: 2026-10-19 00:41:04
nodes: [SamplerCustom, VAEDecode, SaveImage, Image Comparer (rgthree), Note, Note, Image Comparer (rgthree), KSamplerSelect, CLIPLoader, VAELoader, UNETLoader, UNETLoader, LoadImage, TextEncodeQwenImage21, QwenImage21Cache, VAEEncode, ManualSigmas, LoraLoaderModelOnly, JjkText]
patterns: []
missing: []
---

# 数字人/数字人/QwenImage2.1 高清改图工作流_2110163424536784897.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/QwenImage2.1 高清改图工作流_2110163424536784897.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（19 个）：
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `Note`
- `Note`
- `Image Comparer (rgthree)`
- `KSamplerSelect` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `VAEEncode` ★核心
- `ManualSigmas`
- `LoraLoaderModelOnly` ★核心
- `JjkText`

## 知识

覆盖率 **74%**（14/19）

**有卡**：`SamplerCustom`、`VAEDecode`、`SaveImage`、`KSamplerSelect`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoadImage`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`VAEEncode`、`ManualSigmas`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
