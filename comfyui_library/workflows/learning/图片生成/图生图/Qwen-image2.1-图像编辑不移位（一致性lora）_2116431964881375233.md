---
key: 图片生成/图生图/Qwen-image2.1-图像编辑不移位（一致性lora）_2116431964881375233.json
name: Qwen-image2.1-图像编辑不移位（一致性lora）_2116431964881375233
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-图像编辑不移位（一致性lora）_2116431964881375233.json
hash: f065713fbae613bd
coverage: 0.857143
learned_at: 2026-11-02 19:12:55
nodes: [UNETLoader, CLIPLoader, TextEncodeQwenImage21, KSamplerSelect, ManualSigmas, VAELoader, SamplerCustom, VAEDecode, LoraLoaderModelOnly, Image Comparer (rgthree), LoadImage, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, PrimitiveInt]
patterns: []
missing: []
---

# 图片生成/图生图/Qwen-image2.1-图像编辑不移位（一致性lora）_2116431964881375233.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-图像编辑不移位（一致性lora）_2116431964881375233.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `VAELoader`
- `SamplerCustom` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `PrimitiveInt`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`UNETLoader`、`CLIPLoader`、`TextEncodeQwenImage21`、`KSamplerSelect`、`ManualSigmas`、`VAELoader`、`SamplerCustom`、`VAEDecode`、`LoraLoaderModelOnly`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`SaveImage`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect
