---
key: 平台全量/qwen-image2.1局部重绘（遮罩）_2117851080687177730.json
name: qwen-image2.1局部重绘（遮罩）_2117851080687177730
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/qwen-image2.1局部重绘（遮罩）_2117851080687177730.json
hash: 579c268849cc7ced
coverage: 0.933333
learned_at: 2026-11-14 01:16:26
nodes: [LoadImage, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, TextEncodeQwenImage21, CLIPLoader, SaveImage, CFGGuider, RandomNoise, VAELoader, KSamplerSelect, ManualSigmas, Image Comparer (rgthree), SamplerCustomAdvanced, VAEDecode, TextInput_]
patterns: []
missing: []
---

# 平台全量/qwen-image2.1局部重绘（遮罩）_2117851080687177730.json

> 来源文件 `comfyui_library/workflows/平台全量/qwen-image2.1局部重绘（遮罩）_2117851080687177730.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `SaveImage`
- `CFGGuider`
- `RandomNoise`
- `VAELoader`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `Image Comparer (rgthree)`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `TextInput_`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`TextEncodeQwenImage21`、`CLIPLoader`、`SaveImage`、`CFGGuider`、`RandomNoise`、`VAELoader`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`VAEDecode`、`TextInput_`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
