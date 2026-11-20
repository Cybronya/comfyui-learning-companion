---
key: 平台全量/万物迁移 qwen_image_2.1_turbo_1922162142739382273.json
name: 万物迁移 qwen_image_2.1_turbo_1922162142739382273
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/万物迁移 qwen_image_2.1_turbo_1922162142739382273.json
hash: 0cab53389c232256
coverage: 0.733333
learned_at: 2026-11-14 01:31:08
nodes: [CLIPLoader, VAELoader, UNETLoader, VAEDecode, Image Comparer (rgthree), KSamplerSelect, TextEncodeQwenImage21GH, LoadImageGoohai, GH_MaskCropV2, 图像缩放V2_孤海, ManualSigmas, GH_CropRestore, GulfSeaImageMergeMask, SaveImage, LayerUtility: ColorImage, PreviewImage, PreviewImage, 孤海注释, 孤海注释, 孤海注释, LoraLoaderModelOnly, QwenImage21Cache, SamplerCustom, GH_MaskCropV2, LoadImageGoohai, PreviewImage, 孤海注释, LoadImage, LoadImage, GetImageSize]
patterns: []
missing: []
---

# 平台全量/万物迁移 qwen_image_2.1_turbo_1922162142739382273.json

> 来源文件 `comfyui_library/workflows/平台全量/万物迁移 qwen_image_2.1_turbo_1922162142739382273.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `KSamplerSelect` ★核心
- `TextEncodeQwenImage21GH`
- `LoadImageGoohai`
- `GH_MaskCropV2`
- `图像缩放V2_孤海`
- `ManualSigmas`
- `GH_CropRestore`
- `GulfSeaImageMergeMask`
- `SaveImage`
- `LayerUtility: ColorImage`
- `PreviewImage`
- `PreviewImage`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `LoraLoaderModelOnly` ★核心
- `QwenImage21Cache`
- `SamplerCustom` ★核心
- `GH_MaskCropV2`
- `LoadImageGoohai`
- `PreviewImage`
- `孤海注释`
- `LoadImage`
- `LoadImage`
- `GetImageSize`

## 知识

覆盖率 **73%**（22/30）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`VAEDecode`、`KSamplerSelect`、`TextEncodeQwenImage21GH`、`LoadImageGoohai`、`GH_MaskCropV2`、`图像缩放V2_孤海`、`ManualSigmas`、`GH_CropRestore`、`GulfSeaImageMergeMask`、`SaveImage`、`LayerUtility: ColorImage`、`LoraLoaderModelOnly`、`QwenImage21Cache`、`SamplerCustom`、`LoadImage`、`GetImageSize`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader、KSamplerSelect
