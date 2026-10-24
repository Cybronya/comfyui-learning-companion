---
key: 图片生成/图生图/qwen_image_2.1自然无缝扩图_2087728590073978882.json
name: qwen_image_2.1自然无缝扩图_2087728590073978882
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen_image_2.1自然无缝扩图_2087728590073978882.json
hash: 949050ce1cf96e78
coverage: 1
learned_at: 2026-10-23 11:43:55
nodes: [ImpactInt, ConstrainImage|pysssss, LoadImage, SamplerCustom, ImpactInt, VAEDecode, ImpactInt, VAELoader, CLIPLoader, LayerUtility: ExtendCanvasV2, TextEncodeQwenImage21, UNETLoader, VAEEncode, KSamplerSelect, ManualSigmas, ImpactInt, ImpactInt, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/qwen_image_2.1自然无缝扩图_2087728590073978882.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen_image_2.1自然无缝扩图_2087728590073978882.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `ImpactInt`
- `ConstrainImage|pysssss`
- `LoadImage`
- `SamplerCustom` ★核心
- `ImpactInt`
- `VAEDecode` ★核心
- `ImpactInt`
- `VAELoader`
- `CLIPLoader`
- `LayerUtility: ExtendCanvasV2`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `ImpactInt`
- `ImpactInt`
- `SaveImage`

## 知识

覆盖率 **100%**（18/18）

**有卡**：`ImpactInt`、`ConstrainImage|pysssss`、`LoadImage`、`SamplerCustom`、`VAEDecode`、`VAELoader`、`CLIPLoader`、`LayerUtility: ExtendCanvasV2`、`TextEncodeQwenImage21`、`UNETLoader`、`VAEEncode`、`KSamplerSelect`、`ManualSigmas`、`SaveImage`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustom
