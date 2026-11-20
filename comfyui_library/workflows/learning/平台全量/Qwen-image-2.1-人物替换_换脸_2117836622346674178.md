---
key: 平台全量/Qwen-image-2.1-人物替换_换脸_2117836622346674178.json
name: Qwen-image-2.1-人物替换_换脸_2117836622346674178
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-image-2.1-人物替换_换脸_2117836622346674178.json
hash: e91ad346271b4abc
coverage: 0.866667
learned_at: 2026-11-14 00:52:05
nodes: [PreviewImage, Image Comparer (rgthree), LoadImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, Text Concatenate, LoadImage, RandomNoise, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, ImageScaleToTotalPixels, CLIPLoader, ManualSigmas, VAEEncode, KSamplerSelect, StringConstantMultiline, SamplerCustomAdvanced, CFGGuider, VAEDecode, SaveImage, TextEncodeQwenImage21, Text Concatenate, TextGenerateLTX2Prompt, CLIPLoader, easy showAnything, LayerUtility: TextBox, LayerUtility: TextBox, BatchImagesNode, Note]
patterns: []
missing: []
---

# 平台全量/Qwen-image-2.1-人物替换_换脸_2117836622346674178.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-image-2.1-人物替换_换脸_2117836622346674178.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `PreviewImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Text Concatenate`
- `LoadImage`
- `RandomNoise`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageScaleToTotalPixels`
- `CLIPLoader`
- `ManualSigmas`
- `VAEEncode` ★核心
- `KSamplerSelect` ★核心
- `StringConstantMultiline`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `VAEDecode` ★核心
- `SaveImage`
- `TextEncodeQwenImage21`
- `Text Concatenate`
- `TextGenerateLTX2Prompt`
- `CLIPLoader`
- `easy showAnything`
- `LayerUtility: TextBox`
- `LayerUtility: TextBox`
- `BatchImagesNode`
- `Note`

## 知识

覆盖率 **87%**（26/30）

**有卡**：`LoadImage`、`UNETLoader`、`LoraLoaderModelOnly`、`Text Concatenate`、`RandomNoise`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageScaleToTotalPixels`、`CLIPLoader`、`ManualSigmas`、`VAEEncode`、`KSamplerSelect`、`StringConstantMultiline`、`SamplerCustomAdvanced`、`CFGGuider`、`VAEDecode`、`SaveImage`、`TextEncodeQwenImage21`、`TextGenerateLTX2Prompt`、`LayerUtility: TextBox`、`BatchImagesNode`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGGuider
