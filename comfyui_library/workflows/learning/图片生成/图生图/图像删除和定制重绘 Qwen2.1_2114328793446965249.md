---
key: 图片生成/图生图/图像删除和定制重绘 Qwen2.1_2114328793446965249.json
name: 图像删除和定制重绘 Qwen2.1_2114328793446965249
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图像删除和定制重绘 Qwen2.1_2114328793446965249.json
hash: 7d3826ce2e3a50a8
coverage: 0.844444
learned_at: 2026-10-26 22:05:37
nodes: [CLIPLoader, VAELoader, UNETLoader, VAEDecode, Image Comparer (rgthree), LoraLoaderModelOnly, 忽略多组孤海, TextEncodeQwenImage21GH, GH_MaskCropV2, 图像缩放V2_孤海, BasicGuider, ManualSigmas, Get Image Size, GH_CropRestore, GulfSeaImageMergeMask, LayerUtility: ColorImage, GoohaiUniversalSlider, 图像缩放范围孤海, SamplerCustomAdvanced, GoohaiAnyExists, PreviewImage, GoohaiDisplayAny, BasicGuider, TextEncodeQwenImage21GH, GetNode, QwenImagePromptOptimizer, SamplerCustomAdvanced, 图像缩放V2_孤海, LoraLoaderModelOnly, PreviewImage, MaskPreview, PreviewImage, VAEDecode, GH_CropRestore, RandomNoise, easy ifElse, SaveImage, KSamplerSelect, 图像缩放范围孤海, Get Image Size, GH_MaskCropV2, SetNode, LoadImageGoohai, LoadImage, DF_Text_Box]
patterns: []
missing: []
---

# 图片生成/图生图/图像删除和定制重绘 Qwen2.1_2114328793446965249.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图像删除和定制重绘 Qwen2.1_2114328793446965249.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `忽略多组孤海`
- `TextEncodeQwenImage21GH`
- `GH_MaskCropV2`
- `图像缩放V2_孤海`
- `BasicGuider`
- `ManualSigmas`
- `Get Image Size`
- `GH_CropRestore`
- `GulfSeaImageMergeMask`
- `LayerUtility: ColorImage`
- `GoohaiUniversalSlider`
- `图像缩放范围孤海`
- `SamplerCustomAdvanced` ★核心
- `GoohaiAnyExists`
- `PreviewImage`
- `GoohaiDisplayAny`
- `BasicGuider`
- `TextEncodeQwenImage21GH`
- `GetNode`
- `QwenImagePromptOptimizer`
- `SamplerCustomAdvanced` ★核心
- `图像缩放V2_孤海`
- `LoraLoaderModelOnly` ★核心
- `PreviewImage`
- `MaskPreview`
- `PreviewImage`
- `VAEDecode` ★核心
- `GH_CropRestore`
- `RandomNoise`
- `easy ifElse`
- `SaveImage`
- `KSamplerSelect` ★核心
- `图像缩放范围孤海`
- `Get Image Size`
- `GH_MaskCropV2`
- `SetNode`
- `LoadImageGoohai`
- `LoadImage`
- `DF_Text_Box`

## 知识

覆盖率 **84%**（38/45）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`VAEDecode`、`LoraLoaderModelOnly`、`忽略多组孤海`、`TextEncodeQwenImage21GH`、`GH_MaskCropV2`、`图像缩放V2_孤海`、`BasicGuider`、`ManualSigmas`、`Get Image Size`、`GH_CropRestore`、`GulfSeaImageMergeMask`、`LayerUtility: ColorImage`、`GoohaiUniversalSlider`、`图像缩放范围孤海`、`SamplerCustomAdvanced`、`GoohaiAnyExists`、`GoohaiDisplayAny`、`QwenImagePromptOptimizer`、`MaskPreview`、`RandomNoise`、`SaveImage`、`KSamplerSelect`、`LoadImageGoohai`、`LoadImage`、`DF_Text_Box`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
