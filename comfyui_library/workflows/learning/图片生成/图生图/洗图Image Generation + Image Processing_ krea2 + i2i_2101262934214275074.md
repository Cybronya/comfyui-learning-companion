---
key: 图片生成/图生图/洗图Image Generation + Image Processing_ krea2 + i2i_2101262934214275074.json
name: 洗图Image Generation + Image Processing_ krea2 + i2i_2101262934214275074
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/洗图Image Generation + Image Processing_ krea2 + i2i_2101262934214275074.json
hash: a37979d134888bdb
coverage: 0.9375
learned_at: 2026-10-21 00:54:46
nodes: [KSamplerSelect, RandomNoise, BasicGuider, CLIPTextEncode, VAEEncode, CLIPLoader, VAEDecode, UNETLoader, VAELoader, ImageResizeKJv2, AILab_QwenVL, SamplerCustomAdvanced, BasicScheduler, LoadImage, SaveImage, PrimitiveInt]
patterns: []
missing: []
---

# 图片生成/图生图/洗图Image Generation + Image Processing_ krea2 + i2i_2101262934214275074.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/洗图Image Generation + Image Processing_ krea2 + i2i_2101262934214275074.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `KSamplerSelect` ★核心
- `RandomNoise`
- `BasicGuider`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `ImageResizeKJv2`
- `AILab_QwenVL`
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `LoadImage`
- `SaveImage`
- `PrimitiveInt`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`KSamplerSelect`、`RandomNoise`、`BasicGuider`、`CLIPTextEncode`、`VAEEncode`、`CLIPLoader`、`VAEDecode`、`UNETLoader`、`VAELoader`、`ImageResizeKJv2`、`AILab_QwenVL`、`SamplerCustomAdvanced`、`BasicScheduler`、`LoadImage`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
