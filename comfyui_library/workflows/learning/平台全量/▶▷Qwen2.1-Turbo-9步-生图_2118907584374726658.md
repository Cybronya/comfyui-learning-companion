---
key: 平台全量/▶▷Qwen2.1-Turbo-9步-生图_2118907584374726658.json
name: ▶▷Qwen2.1-Turbo-9步-生图_2118907584374726658
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/▶▷Qwen2.1-Turbo-9步-生图_2118907584374726658.json
hash: a5d5972511c23384
coverage: 0.758621
learned_at: 2026-11-14 01:21:00
nodes: [SaveImage, VAEDecode, SamplerCustomAdvanced, KSamplerSelect, RandomNoise, CFGGuider, ComfySwitchNode, Label (rgthree), TextGenerate, ManualSigmas, Seed (rgthree), TextEncodeQwenImage21, UNETLoader, CLIPLoader, VAELoader, QwenImage21Cache, ResolutionSelector, CLIPLoader, PrimitiveStringMultiline, easy showAnything, EmptyLatentImage, Label (rgthree), PrimitiveStringMultiline, Fast Groups Bypasser (rgthree), Label (rgthree), Note, Label (rgthree), Note, Label (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 平台全量/▶▷Qwen2.1-Turbo-9步-生图_2118907584374726658.json

> 来源文件 `comfyui_library/workflows/平台全量/▶▷Qwen2.1-Turbo-9步-生图_2118907584374726658.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（29 个）：
- `SaveImage`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `ComfySwitchNode`
- `Label (rgthree)`
- `TextGenerate`
- `ManualSigmas`
- `Seed (rgthree)`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `ResolutionSelector`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `Label (rgthree)`
- `PrimitiveStringMultiline`
- `Fast Groups Bypasser (rgthree)`
- `Label (rgthree)`
- `Note`
- `Label (rgthree)`
- `Note`
- `Label (rgthree)`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **76%**（22/29）

**有卡**：`SaveImage`、`VAEDecode`、`SamplerCustomAdvanced`、`KSamplerSelect`、`RandomNoise`、`CFGGuider`、`Label (rgthree)`、`TextGenerate`、`ManualSigmas`、`Seed (rgthree)`、`TextEncodeQwenImage21`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`ResolutionSelector`、`EmptyLatentImage`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、QwenImage21Cache、UNETLoader
