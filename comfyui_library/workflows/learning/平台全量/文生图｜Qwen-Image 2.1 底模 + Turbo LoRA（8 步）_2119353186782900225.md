---
key: 平台全量/文生图｜Qwen-Image 2.1 底模 + Turbo LoRA（8 步）_2119353186782900225.json
name: 文生图｜Qwen-Image 2.1 底模 + Turbo LoRA（8 步）_2119353186782900225
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/文生图｜Qwen-Image 2.1 底模 + Turbo LoRA（8 步）_2119353186782900225.json
hash: 20f9bf5e6ad1ee5c
coverage: 1
learned_at: 2026-11-14 02:12:09
nodes: [UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, RandomNoise, CFGGuider, KSamplerSelect, SamplerCustomAdvanced, VAEDecode, SaveImage, QwenImage21Cache, LoraLoaderModelOnly, ManualSigmas, EmptyHunyuanImageLatent]
patterns: []
missing: []
---

# 平台全量/文生图｜Qwen-Image 2.1 底模 + Turbo LoRA（8 步）_2119353186782900225.json

> 来源文件 `comfyui_library/workflows/平台全量/文生图｜Qwen-Image 2.1 底模 + Turbo LoRA（8 步）_2119353186782900225.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `QwenImage21Cache`
- `LoraLoaderModelOnly` ★核心
- `ManualSigmas`
- `EmptyHunyuanImageLatent`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`QwenImage21Cache`、`LoraLoaderModelOnly`、`ManualSigmas`、`EmptyHunyuanImageLatent`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、QwenImage21Cache、UNETLoader、CFGGuider
