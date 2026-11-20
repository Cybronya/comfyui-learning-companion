---
key: 平台全量/qwen-image2.1扩图-2k高清出图_2117590562235838465.json
name: qwen-image2.1扩图-2k高清出图_2117590562235838465
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/qwen-image2.1扩图-2k高清出图_2117590562235838465.json
hash: 9122ff6a5e400497
coverage: 0.875
learned_at: 2026-11-14 01:16:27
nodes: [LoadImage, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, TextEncodeQwenImage21, RandomNoise, CLIPLoader, CFGGuider, Image Comparer (rgthree), SamplerCustomAdvanced, VAEDecode, VAELoader, KSamplerSelect, ManualSigmas, ImagePadForOutpaint, PreviewImage, SaveImage]
patterns: []
missing: []
---

# 平台全量/qwen-image2.1扩图-2k高清出图_2117590562235838465.json

> 来源文件 `comfyui_library/workflows/平台全量/qwen-image2.1扩图-2k高清出图_2117590562235838465.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `RandomNoise`
- `CLIPLoader`
- `CFGGuider`
- `Image Comparer (rgthree)`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `ImagePadForOutpaint`
- `PreviewImage`
- `SaveImage`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`TextEncodeQwenImage21`、`RandomNoise`、`CLIPLoader`、`CFGGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`VAELoader`、`KSamplerSelect`、`ManualSigmas`、`ImagePadForOutpaint`、`SaveImage`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
