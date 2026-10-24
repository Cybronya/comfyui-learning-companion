---
key: 图片生成/图生图/Qwen Image 2.1 手机随拍证件照生成_2112886121754615810.json
name: Qwen Image 2.1 手机随拍证件照生成_2112886121754615810
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 手机随拍证件照生成_2112886121754615810.json
hash: 40adf43bdd5b2ddd
coverage: 0.84
learned_at: 2026-10-23 11:12:44
nodes: [KSampler, VAEDecode, QwenImage21SpectrumT8, RestoreQwenImage21GH, TextEncodeQwenImage21GH, QwenImage21SageAttentionT8, QwenImage21BlockCacheT8, CLIPLoader, VAELoader, UNETLoader, Reroute, Reroute, 孤海注释, GoohaiRatioAndResolution, IDPhotoClothingSelector_孤海, Text Concatenate, CR Prompt Text, LoadImage, SplitImageWithAlpha, GuHai_IDPhotoCrop, PreviewImage, SaveImage, DF_Text_Box, SingleImageLayoutNode, IDPhotoClothingSelector_孤海]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 738146731718229, "steps": 30}
---

# 图片生成/图生图/Qwen Image 2.1 手机随拍证件照生成_2112886121754615810.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 手机随拍证件照生成_2112886121754615810.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `KSampler` ★核心
- `VAEDecode` ★核心
- `QwenImage21SpectrumT8`
- `RestoreQwenImage21GH`
- `TextEncodeQwenImage21GH`
- `QwenImage21SageAttentionT8`
- `QwenImage21BlockCacheT8`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `Reroute`
- `Reroute`
- `孤海注释`
- `GoohaiRatioAndResolution`
- `IDPhotoClothingSelector_孤海`
- `Text Concatenate`
- `CR Prompt Text`
- `LoadImage`
- `SplitImageWithAlpha`
- `GuHai_IDPhotoCrop`
- `PreviewImage`
- `SaveImage`
- `DF_Text_Box`
- `SingleImageLayoutNode`
- `IDPhotoClothingSelector_孤海`

## 关键参数

- `seed` = `738146731718229`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **84%**（21/25）

**有卡**：`KSampler`、`VAEDecode`、`QwenImage21SpectrumT8`、`RestoreQwenImage21GH`、`TextEncodeQwenImage21GH`、`QwenImage21SageAttentionT8`、`QwenImage21BlockCacheT8`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`GoohaiRatioAndResolution`、`IDPhotoClothingSelector_孤海`、`Text Concatenate`、`CR Prompt Text`、`LoadImage`、`SplitImageWithAlpha`、`GuHai_IDPhotoCrop`、`SaveImage`、`DF_Text_Box`、`SingleImageLayoutNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、LoadImage、UNETLoader、TextEncodeQwenImage21GH、CR Prompt Text
