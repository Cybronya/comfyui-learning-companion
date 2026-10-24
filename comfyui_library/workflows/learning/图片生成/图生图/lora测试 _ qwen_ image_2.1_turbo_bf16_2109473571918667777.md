---
key: 图片生成/图生图/lora测试 _ qwen_ image_2.1_turbo_bf16_2109473571918667777.json
name: lora测试 _ qwen_ image_2.1_turbo_bf16_2109473571918667777
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/lora测试 _ qwen_ image_2.1_turbo_bf16_2109473571918667777.json
hash: 99f8f170035b7fa3
coverage: 0.786667
learned_at: 2026-10-23 11:40:55
nodes: [KSamplerSelect, ManualSigmas, VAELoader, JjkText, CLIPLoader, Int, UNETLoader, VAEDecode, LoraLoaderModelOnly, Anything Everywhere3, TextEncodeQwenImage21, GetNode, SetNode, QwenImage21Cache, VAEDecode, GetNode, SamplerCustom, LoraLoaderModelOnly, ShowText|pysssss, CR Text Replace, Anything Everywhere3, SaveImage, QwenImage21Cache, VAEDecode, GetNode, SamplerCustom, QwenImage21Cache, VAEDecode, GetNode, SamplerCustom, SaveImage, SaveImage, LoraLoaderModelOnly, LoraLoaderModelOnly, QwenImage21Cache, VAEDecode, GetNode, SamplerCustom, QwenImage21Cache, VAEDecode, GetNode, SamplerCustom, SaveImage, QwenImage21Cache, VAEDecode, GetNode, SamplerCustom, QwenImage21Cache, VAEDecode, GetNode, SamplerCustom, SaveImage, SaveImage, SaveImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, QwenImage21Cache, VAEDecode, GetNode, SamplerCustom, QwenImage21Cache, VAEDecode, GetNode, SamplerCustom, SaveImage, SaveImage, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, SamplerCustom, QwenImage21Cache, SaveImage, JjkText, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/lora测试 _ qwen_ image_2.1_turbo_bf16_2109473571918667777.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/lora测试 _ qwen_ image_2.1_turbo_bf16_2109473571918667777.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（75 个）：
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `VAELoader`
- `JjkText`
- `CLIPLoader`
- `Int`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `Anything Everywhere3`
- `TextEncodeQwenImage21`
- `GetNode`
- `SetNode`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `GetNode`
- `SamplerCustom` ★核心
- `LoraLoaderModelOnly` ★核心
- `ShowText|pysssss`
- `CR Text Replace`
- `Anything Everywhere3`
- `SaveImage`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `GetNode`
- `SamplerCustom` ★核心
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `GetNode`
- `SamplerCustom` ★核心
- `SaveImage`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `GetNode`
- `SamplerCustom` ★核心
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `GetNode`
- `SamplerCustom` ★核心
- `SaveImage`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `GetNode`
- `SamplerCustom` ★核心
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `GetNode`
- `SamplerCustom` ★核心
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `GetNode`
- `SamplerCustom` ★核心
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `GetNode`
- `SamplerCustom` ★核心
- `SaveImage`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SamplerCustom` ★核心
- `QwenImage21Cache`
- `SaveImage`
- `JjkText`
- `LoadImage`

## 知识

覆盖率 **79%**（59/75）

**有卡**：`KSamplerSelect`、`ManualSigmas`、`VAELoader`、`CLIPLoader`、`Int`、`UNETLoader`、`VAEDecode`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`SamplerCustom`、`CR Text Replace`、`SaveImage`、`LoadImage`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
