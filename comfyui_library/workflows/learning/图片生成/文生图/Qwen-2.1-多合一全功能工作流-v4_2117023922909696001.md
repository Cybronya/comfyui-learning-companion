---
key: 图片生成/文生图/Qwen-2.1-多合一全功能工作流-v4_2117023922909696001.json
name: Qwen-2.1-多合一全功能工作流-v4_2117023922909696001
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-2.1-多合一全功能工作流-v4_2117023922909696001.json
hash: fc5c7af39c8a037c
coverage: 0.279528
learned_at: 2026-11-02 19:15:49
nodes: [LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, 忽略多组孤海, GoohaiRatioAndResolution, RestoreQwenImage21GH, GoohaiRouteBlocker, GoohaiRouteBlocker, LoraLoaderModelOnly, easy ifElse, GoohaiAnyExists, GH_MaskCropV2, GulfSeaImageMergeMask, LayerUtility: ColorImage, 图像缩放范围孤海, Get Image Size, 图像缩放V2_孤海, GH_CropRestore, LoraLoaderModelOnly, 图像缩放范围孤海, Get Image Size, GH_MaskCropV2, 图像缩放V2_孤海, GH_CropRestore, LoraLoaderModelOnly, GoohaiAnyExists, GoohaiUniversalSlider, 图像缩放V2_孤海, LoraLoaderModelOnly, GH_MaskCropV2, GH_CropRestore, GoohaiUniversalSlider, 数学运算_孤海, 长边短边, CR Text Concatenate, easy string, 数学运算_孤海, 孤海遮罩分析, 孤海外补画板可视化, UNETLoader, LoadImageGoohai, DF_Text_Box, QwenImagePromptOptimizer, GoohaiDisplayAny, CLIPLoader, VAELoader, ManualSigmas, KSamplerSelect, RandomNoise, SaveImage, ImageCompare, TextEncodeQwenImage21GH, BasicGuider, SamplerCustomAdvanced, VAEDecode, 布尔孤海, 布尔孤海, easy string, 布尔孤海, GoohaiRouteBlocker, 布尔孤海, 布尔孤海, easy ifElse, easy ifElse, easy ifElse, easy ifElse, easy ifElse, easy ifElse, easy ifElse, easy ifElse, easy ifElse, easy ifElse, easy ifElse, easy ifElse, easy ifElse, easy ifElse, easy ifElse, easy ifElse, easy ifElse, easy ifElse, easy ifElse, easy ifElse, GoohaiAnyExists, GoohaiAnyExists, GoohaiAnyExists, easy ifElse, CR Text Concatenate, easy string, easy string, easy ifElse, CR Text Concatenate, easy ifElse, 布尔孤海, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy ifElse, GetNode, GetNode]
patterns: []
missing: []
---

# 图片生成/文生图/Qwen-2.1-多合一全功能工作流-v4_2117023922909696001.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-2.1-多合一全功能工作流-v4_2117023922909696001.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（254 个）：
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `忽略多组孤海`
- `GoohaiRatioAndResolution`
- `RestoreQwenImage21GH`
- `GoohaiRouteBlocker`
- `GoohaiRouteBlocker`
- `LoraLoaderModelOnly` ★核心
- `easy ifElse`
- `GoohaiAnyExists`
- `GH_MaskCropV2`
- `GulfSeaImageMergeMask`
- `LayerUtility: ColorImage`
- `图像缩放范围孤海`
- `Get Image Size`
- `图像缩放V2_孤海`
- `GH_CropRestore`
- `LoraLoaderModelOnly` ★核心
- `图像缩放范围孤海`
- `Get Image Size`
- `GH_MaskCropV2`
- `图像缩放V2_孤海`
- `GH_CropRestore`
- `LoraLoaderModelOnly` ★核心
- `GoohaiAnyExists`
- `GoohaiUniversalSlider`
- `图像缩放V2_孤海`
- `LoraLoaderModelOnly` ★核心
- `GH_MaskCropV2`
- `GH_CropRestore`
- `GoohaiUniversalSlider`
- `数学运算_孤海`
- `长边短边`
- `CR Text Concatenate`
- `easy string`
- `数学运算_孤海`
- `孤海遮罩分析`
- `孤海外补画板可视化`
- `UNETLoader` ★核心
- `LoadImageGoohai`
- `DF_Text_Box`
- `QwenImagePromptOptimizer`
- `GoohaiDisplayAny`
- `CLIPLoader`
- `VAELoader`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `SaveImage`
- `ImageCompare`
- `TextEncodeQwenImage21GH`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `布尔孤海`
- `布尔孤海`
- `easy string`
- `布尔孤海`
- `GoohaiRouteBlocker`
- `布尔孤海`
- `布尔孤海`
- `easy ifElse`
- `easy ifElse`
- `easy ifElse`
- `easy ifElse`
- `easy ifElse`
- `easy ifElse`
- `easy ifElse`
- `easy ifElse`
- `easy ifElse`
- `easy ifElse`
- `easy ifElse`
- `easy ifElse`
- `easy ifElse`
- `easy ifElse`
- `easy ifElse`
- `easy ifElse`
- `easy ifElse`
- `easy ifElse`
- `easy ifElse`
- `easy ifElse`
- `GoohaiAnyExists`
- `GoohaiAnyExists`
- `GoohaiAnyExists`
- `easy ifElse`
- `CR Text Concatenate`
- `easy string`
- `easy string`
- `easy ifElse`
- `CR Text Concatenate`
- `easy ifElse`
- `布尔孤海`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy ifElse`
- `GetNode`
- `GetNode`

## 知识

覆盖率 **28%**（71/254）

**有卡**：`LoadImage`、`忽略多组孤海`、`GoohaiRatioAndResolution`、`RestoreQwenImage21GH`、`GoohaiRouteBlocker`、`LoraLoaderModelOnly`、`GoohaiAnyExists`、`GH_MaskCropV2`、`GulfSeaImageMergeMask`、`LayerUtility: ColorImage`、`图像缩放范围孤海`、`Get Image Size`、`图像缩放V2_孤海`、`GH_CropRestore`、`GoohaiUniversalSlider`、`数学运算_孤海`、`长边短边`、`CR Text Concatenate`、`easy string`、`孤海遮罩分析`、`孤海外补画板可视化`、`UNETLoader`、`LoadImageGoohai`、`DF_Text_Box`、`QwenImagePromptOptimizer`、`GoohaiDisplayAny`、`CLIPLoader`、`VAELoader`、`ManualSigmas`、`KSamplerSelect`、`RandomNoise`、`SaveImage`、`ImageCompare`、`TextEncodeQwenImage21GH`、`BasicGuider`、`SamplerCustomAdvanced`、`VAEDecode`、`布尔孤海`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
