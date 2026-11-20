---
key: 数字人/数字人/完美扩图！ Qwen 2.1 无痕阔图！孤海版  自动高清！_2116421360078639105.json
name: 完美扩图！ Qwen 2.1 无痕阔图！孤海版  自动高清！_2116421360078639105
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/完美扩图！ Qwen 2.1 无痕阔图！孤海版  自动高清！_2116421360078639105.json
hash: 80fcc03bd17bec5f
coverage: 0.775
learned_at: 2026-11-02 19:17:02
nodes: [LoadImageGoohai, DF_Text_Box, 图像缩放V2_孤海, TextEncodeQwenImage21GH, CLIPLoader, VAELoader, UNETLoader, KSamplerSelect, ManualSigmas, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, BasicGuider, VAEDecode, Image Comparer (rgthree), GH_MaskCropV2, GH_CropRestore, GoohaiUniversalSlider, 数学运算_孤海, 长边短边, CR Text Concatenate, easy string, 数学运算_孤海, 孤海遮罩分析, SaveImage, 孤海外补画板可视化, ImageScaleToTotalPixels, PreviewImage, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, Note, INTConstant, Image Comparer (rgthree), SaveImage, PreviewImage, PreviewImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Reroute]
patterns: []
missing: []
---

# 数字人/数字人/完美扩图！ Qwen 2.1 无痕阔图！孤海版  自动高清！_2116421360078639105.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/完美扩图！ Qwen 2.1 无痕阔图！孤海版  自动高清！_2116421360078639105.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
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
- `数学运算_孤海`
- `孤海遮罩分析`
- `SaveImage`
- `孤海外补画板可视化`
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `Note`
- `INTConstant`
- `Image Comparer (rgthree)`
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Reroute`

## 知识

覆盖率 **78%**（31/40）

**有卡**：`LoadImageGoohai`、`DF_Text_Box`、`图像缩放V2_孤海`、`TextEncodeQwenImage21GH`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`KSamplerSelect`、`ManualSigmas`、`LoraLoaderModelOnly`、`RandomNoise`、`SamplerCustomAdvanced`、`BasicGuider`、`VAEDecode`、`GH_MaskCropV2`、`GH_CropRestore`、`GoohaiUniversalSlider`、`数学运算_孤海`、`长边短边`、`CR Text Concatenate`、`easy string`、`孤海遮罩分析`、`SaveImage`、`孤海外补画板可视化`、`ImageScaleToTotalPixels`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`INTConstant`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、SeedVR2LoadDiTModel
