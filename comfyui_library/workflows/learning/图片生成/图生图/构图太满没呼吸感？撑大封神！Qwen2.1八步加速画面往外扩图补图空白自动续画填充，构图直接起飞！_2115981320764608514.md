---
key: 图片生成/图生图/构图太满没呼吸感？撑大封神！Qwen2.1八步加速画面往外扩图补图空白自动续画填充，构图直接起飞！_2115981320764608514.json
name: 构图太满没呼吸感？撑大封神！Qwen2.1八步加速画面往外扩图补图空白自动续画填充，构图直接起飞！_2115981320764608514
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/构图太满没呼吸感？撑大封神！Qwen2.1八步加速画面往外扩图补图空白自动续画填充，构图直接起飞！_2115981320764608514.json
hash: a98889cf2ee2a45b
coverage: 0.857143
learned_at: 2026-10-30 23:25:58
nodes: [图像缩放V2_孤海, Get Image Size, GrowMaskWithBlur, SamplerCustom, KSamplerSelect, CLIPLoader, VAELoader, VAEDecode, ManualSigmas, Get Image Size, TextEncodeQwenImage21, DF_Text_Box, LoadImage, GulfSeaImageMergeMask, LoraLoaderModelOnly, LoraLoaderModelOnly, RHHiddenNodes, Text Concatenate, UNETLoader, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt, Image Comparer (rgthree), 图像缩放V2_孤海, SaveImage, SaveImage, 图像缩放V2_孤海, 孤海外补画板按方向, ImageConcatMulti, SeedVR2Conditioning, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, UNETLoader, SeedVR2Preprocess, VAEDecodeTiled, KSampler, LayerUtility: PurgeVRAM V2, VAEEncodeTiled, LayerColor: ColorAdapter, SaveImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 581778858092930, "steps": 1}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/构图太满没呼吸感？撑大封神！Qwen2.1八步加速画面往外扩图补图空白自动续画填充，构图直接起飞！_2115981320764608514.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/构图太满没呼吸感？撑大封神！Qwen2.1八步加速画面往外扩图补图空白自动续画填充，构图直接起飞！_2115981320764608514.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `图像缩放V2_孤海`
- `Get Image Size`
- `GrowMaskWithBlur`
- `SamplerCustom` ★核心
- `KSamplerSelect` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `ManualSigmas`
- `Get Image Size`
- `TextEncodeQwenImage21`
- `DF_Text_Box`
- `LoadImage`
- `GulfSeaImageMergeMask`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `RHHiddenNodes`
- `Text Concatenate`
- `UNETLoader` ★核心
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `Image Comparer (rgthree)`
- `图像缩放V2_孤海`
- `SaveImage`
- `SaveImage`
- `图像缩放V2_孤海`
- `孤海外补画板按方向`
- `ImageConcatMulti`
- `SeedVR2Conditioning`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoader`
- `UNETLoader` ★核心
- `SeedVR2Preprocess`
- `VAEDecodeTiled` ★核心
- `KSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `VAEEncodeTiled` ★核心
- `LayerColor: ColorAdapter`
- `SaveImage`

## 关键参数

- `seed` = `581778858092930`
- `steps` = `1`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（36/42）

**有卡**：`图像缩放V2_孤海`、`Get Image Size`、`GrowMaskWithBlur`、`SamplerCustom`、`KSamplerSelect`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`ManualSigmas`、`TextEncodeQwenImage21`、`DF_Text_Box`、`LoadImage`、`GulfSeaImageMergeMask`、`LoraLoaderModelOnly`、`RHHiddenNodes`、`Text Concatenate`、`UNETLoader`、`SaveImage`、`孤海外补画板按方向`、`ImageConcatMulti`、`SeedVR2Conditioning`、`LayerUtility: ImageScaleByAspectRatio V2`、`SeedVR2Preprocess`、`VAEDecodeTiled`、`KSampler`、`LayerUtility: PurgeVRAM V2`、`VAEEncodeTiled`、`LayerColor: ColorAdapter`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
