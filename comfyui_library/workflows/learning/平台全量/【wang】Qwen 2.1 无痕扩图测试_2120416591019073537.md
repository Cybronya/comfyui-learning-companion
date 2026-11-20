---
key: 平台全量/【wang】Qwen 2.1 无痕扩图测试_2120416591019073537.json
name: 【wang】Qwen 2.1 无痕扩图测试_2120416591019073537
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【wang】Qwen 2.1 无痕扩图测试_2120416591019073537.json
hash: bae7de90fe2ef89e
coverage: 0.862069
learned_at: 2026-11-14 01:22:30
nodes: [LoadImageGoohai, DF_Text_Box, 图像缩放V2_孤海, TextEncodeQwenImage21GH, CLIPLoader, VAELoader, UNETLoader, KSamplerSelect, ManualSigmas, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, BasicGuider, VAEDecode, Image Comparer (rgthree), GH_MaskCropV2, GH_CropRestore, GoohaiUniversalSlider, 数学运算_孤海, 长边短边, CR Text Concatenate, easy string, 孤海注释, 数学运算_孤海, 孤海遮罩分析, SaveImage, 孤海外补画板可视化, Note, 孤海注释]
patterns: []
missing: []
---

# 平台全量/【wang】Qwen 2.1 无痕扩图测试_2120416591019073537.json

> 来源文件 `comfyui_library/workflows/平台全量/【wang】Qwen 2.1 无痕扩图测试_2120416591019073537.json`

## 结构

**生成流程**：Model → Sampling → Decode → Output → Other

**节点**（29 个）：
- `LoadImageGoohai`
- `DF_Text_Box`
- `图像缩放V2_孤海`
- `TextEncodeQwenImage21GH`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `GH_MaskCropV2`
- `GH_CropRestore`
- `GoohaiUniversalSlider`
- `数学运算_孤海`
- `长边短边`
- `CR Text Concatenate`
- `easy string`
- `孤海注释`
- `数学运算_孤海`
- `孤海遮罩分析`
- `SaveImage`
- `孤海外补画板可视化`
- `Note`
- `孤海注释`

## 知识

覆盖率 **86%**（25/29）

**有卡**：`LoadImageGoohai`、`DF_Text_Box`、`图像缩放V2_孤海`、`TextEncodeQwenImage21GH`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`KSamplerSelect`、`ManualSigmas`、`LoraLoaderModelOnly`、`RandomNoise`、`SamplerCustomAdvanced`、`BasicGuider`、`VAEDecode`、`GH_MaskCropV2`、`GH_CropRestore`、`GoohaiUniversalSlider`、`数学运算_孤海`、`长边短边`、`CR Text Concatenate`、`easy string`、`孤海遮罩分析`、`SaveImage`、`孤海外补画板可视化`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、TextEncodeQwenImage21GH
