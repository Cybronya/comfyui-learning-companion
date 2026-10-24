---
key: 图片生成/图生图/洗图Image Generation + Image Processing_ krea2 + i2i_2112738893312380929.json
name: 洗图Image Generation + Image Processing_ krea2 + i2i_2112738893312380929
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/洗图Image Generation + Image Processing_ krea2 + i2i_2112738893312380929.json
hash: d62ca54261b8746c
coverage: 0.9375
learned_at: 2026-10-23 13:11:50
nodes: [KSamplerSelect, RandomNoise, BasicGuider, CLIPTextEncode, VAEEncode, CLIPLoader, VAEDecode, UNETLoader, VAELoader, ImageResizeKJv2, AILab_QwenVL, SamplerCustomAdvanced, BasicScheduler, PrimitiveInt, SaveImage, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/洗图Image Generation + Image Processing_ krea2 + i2i_2112738893312380929.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/洗图Image Generation + Image Processing_ krea2 + i2i_2112738893312380929.json`

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
- `PrimitiveInt`
- `SaveImage`
- `LoadImage`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`KSamplerSelect`、`RandomNoise`、`BasicGuider`、`CLIPTextEncode`、`VAEEncode`、`CLIPLoader`、`VAEDecode`、`UNETLoader`、`VAELoader`、`ImageResizeKJv2`、`AILab_QwenVL`、`SamplerCustomAdvanced`、`BasicScheduler`、`SaveImage`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
