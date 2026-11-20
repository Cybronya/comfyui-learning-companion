---
key: 平台全量/QwenImage2.1-turbo-多图编辑-LoRA_2118169836537868289.json
name: QwenImage2.1-turbo-多图编辑-LoRA_2118169836537868289
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/QwenImage2.1-turbo-多图编辑-LoRA_2118169836537868289.json
hash: d8e9c9123ac9d5a3
coverage: 0.75
learned_at: 2026-11-14 00:53:21
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, VAELoader, LoadImage, LoadImage, CLIPLoader, TextEncodeQwenImage21, UNETLoader, QwenImage21Cache, RandomNoise, KSamplerSelect, VAEDecode, SaveImage, BasicGuider, SamplerCustomAdvanced, ManualSigmas, EmptyLatentImage, ComfySwitchNode, PrimitiveBoolean, Fast Groups Bypasser (rgthree), Note, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveStringMultiline, QwenImageLoraLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "lora_name": "DAGAO_qwen2_1_c1-st2000.safetensors", "strength_clip": 1, "strength_model": 1, "width": 1024}
---

# 平台全量/QwenImage2.1-turbo-多图编辑-LoRA_2118169836537868289.json

> 来源文件 `comfyui_library/workflows/平台全量/QwenImage2.1-turbo-多图编辑-LoRA_2118169836537868289.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（28 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `QwenImageLoraLoader` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `lora_name` = `DAGAO_qwen2_1_c1-st2000.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **75%**（21/28）

**有卡**：`LoadImage`、`VAELoader`、`CLIPLoader`、`TextEncodeQwenImage21`、`UNETLoader`、`QwenImage21Cache`、`RandomNoise`、`KSamplerSelect`、`VAEDecode`、`SaveImage`、`BasicGuider`、`SamplerCustomAdvanced`、`ManualSigmas`、`EmptyLatentImage`、`PrimitiveBoolean`、`QwenImageLoraLoader`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache、UNETLoader
