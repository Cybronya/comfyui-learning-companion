---
key: 图片生成/图生图/Qwen-Image-2.1-一键抠图_图层拆分_2112447865481162754.json
name: Qwen-Image-2.1-一键抠图_图层拆分_2112447865481162754
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1-一键抠图_图层拆分_2112447865481162754.json
hash: 8b3f5844d3cc4c74
coverage: 0.894737
learned_at: 2026-10-23 11:16:27
nodes: [CLIPLoader, PrimitiveStringMultiline, UNETLoader, CFGGuider, KSamplerSelect, CustomSigmas, RandomNoise, TextEncodeQwenImage21, SamplerCustomAdvanced, VAELoader, VAEDecode, easy cleanGpuUsed, SaveImage, Note, QwenImage21Cache, QwenImage21SageAttentionT8, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/Qwen-Image-2.1-一键抠图_图层拆分_2112447865481162754.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1-一键抠图_图层拆分_2112447865481162754.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `CustomSigmas`
- `RandomNoise`
- `TextEncodeQwenImage21`
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `SaveImage`
- `Note`
- `QwenImage21Cache`
- `QwenImage21SageAttentionT8`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`CLIPLoader`、`UNETLoader`、`CFGGuider`、`KSamplerSelect`、`CustomSigmas`、`RandomNoise`、`TextEncodeQwenImage21`、`SamplerCustomAdvanced`、`VAELoader`、`VAEDecode`、`easy cleanGpuUsed`、`SaveImage`、`QwenImage21Cache`、`QwenImage21SageAttentionT8`、`LoraLoaderModelOnly`、`LoadImage`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
