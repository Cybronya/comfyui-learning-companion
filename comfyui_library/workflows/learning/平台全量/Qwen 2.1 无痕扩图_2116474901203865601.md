---
key: 平台全量/Qwen 2.1 无痕扩图_2116474901203865601.json
name: Qwen 2.1 无痕扩图_2116474901203865601
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen 2.1 无痕扩图_2116474901203865601.json
hash: cf9da633d9a1509b
coverage: 0.925926
learned_at: 2026-11-14 00:49:10
nodes: [LoadImageGoohai, DF_Text_Box, 图像缩放V2_孤海, TextEncodeQwenImage21GH, CLIPLoader, VAELoader, UNETLoader, KSamplerSelect, ManualSigmas, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, BasicGuider, VAEDecode, Image Comparer (rgthree), GH_MaskCropV2, GH_CropRestore, GoohaiUniversalSlider, 数学运算_孤海, 长边短边, CR Text Concatenate, easy string, 孤海注释, 数学运算_孤海, 孤海遮罩分析, SaveImage, 孤海外补画板可视化]
patterns: []
missing: []
---

# 平台全量/Qwen 2.1 无痕扩图_2116474901203865601.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen 2.1 无痕扩图_2116474901203865601.json`

## 结构

**生成流程**：Model → Sampling → Decode → Output → Other

**节点**（27 个）：
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

## 知识

覆盖率 **93%**（25/27）

**有卡**：`LoadImageGoohai`、`DF_Text_Box`、`图像缩放V2_孤海`、`TextEncodeQwenImage21GH`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`KSamplerSelect`、`ManualSigmas`、`LoraLoaderModelOnly`、`RandomNoise`、`SamplerCustomAdvanced`、`BasicGuider`、`VAEDecode`、`GH_MaskCropV2`、`GH_CropRestore`、`GoohaiUniversalSlider`、`数学运算_孤海`、`长边短边`、`CR Text Concatenate`、`easy string`、`孤海遮罩分析`、`SaveImage`、`孤海外补画板可视化`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、TextEncodeQwenImage21GH
