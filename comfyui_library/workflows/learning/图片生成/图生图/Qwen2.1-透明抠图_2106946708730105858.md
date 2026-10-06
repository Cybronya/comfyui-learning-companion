---
key: 图片生成/图生图/Qwen2.1-透明抠图_2106946708730105858.json
name: Qwen2.1-透明抠图_2106946708730105858
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1-透明抠图_2106946708730105858.json
hash: 3d89d53534e70209
coverage: 0.916667
learned_at: 2026-10-07 02:41:29
nodes: [SaveImage, VAEDecode, BasicGuider, QwenImage21FunPDDLoader, SamplerCustomAdvanced, RandomNoise, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, LoadImage, PrimitiveInt]
patterns: []
missing: []
---

# 图片生成/图生图/Qwen2.1-透明抠图_2106946708730105858.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1-透明抠图_2106946708730105858.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（12 个）：
- `SaveImage`
- `VAEDecode` ★核心
- `BasicGuider`
- `QwenImage21FunPDDLoader`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `LoadImage`
- `PrimitiveInt`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`SaveImage`、`VAEDecode`、`BasicGuider`、`QwenImage21FunPDDLoader`、`SamplerCustomAdvanced`、`RandomNoise`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`LoadImage`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、SamplerCustomAdvanced、SaveImage
