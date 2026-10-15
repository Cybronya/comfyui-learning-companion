---
key: 图片生成/文生图/千问洗图神器Qwen-Image-ControlNet-Union_1969044313470607361.json
name: 千问洗图神器Qwen-Image-ControlNet-Union_1969044313470607361
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/千问洗图神器Qwen-Image-ControlNet-Union_1969044313470607361.json
hash: 1a193fda7810c541
coverage: 0.568182
learned_at: 2026-10-10 20:59:39
nodes: [ImpactSwitch, ImpactMinMax, PreviewImage, PreviewImage, PreviewImage, PreviewImage, Note, Note, Note, Note, ControlNetApplyAdvanced, KSampler, LayerUtility: PurgeVRAM V2, VAEEncode, CR Text, CR Text Concatenate, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, easy int, easy int, LoadImage, VAEDecode, CLIPLoader, VAELoader, ImpactConditionalBranch, CLIPTextEncode, CLIPTextEncode, ModelSamplingAuraFlow, SeedVR2GGUF, RH_Captioner, CR Text, easy boolean, Note, easy float, SaveImage, UnetLoaderGGUF, ControlNetLoader, LayerUtility: ImageScaleByAspectRatio V2, DWPreprocessor, AnyLineArtPreprocessor_aux, CannyEdgePreprocessor, DepthAnythingPreprocessor, LoadImage]
patterns: [image_to_image]
missing: [CR Text, CR Text, CR Text Concatenate, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, easy boolean, easy float, easy int, easy int]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "controlnet_strength": 1.0000000000000002, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta57", "seed": 557223418395068, "steps": 8}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy float` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/千问洗图神器Qwen-Image-ControlNet-Union_1969044313470607361.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/千问洗图神器Qwen-Image-ControlNet-Union_1969044313470607361.json`

## 结构

**节点**（44 个）：
- `ImpactSwitch`
- `ImpactMinMax`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `Note`
- `Note`
- `Note`
- `Note`
- `ControlNetApplyAdvanced`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `VAEEncode`
- `CR Text`
- `CR Text Concatenate`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoadImage`
- `easy int`
- `easy int`
- `LoadImage`
- `VAEDecode`
- `CLIPLoader`
- `VAELoader`
- `ImpactConditionalBranch`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `ModelSamplingAuraFlow`
- `SeedVR2GGUF`
- `RH_Captioner`
- `CR Text`
- `easy boolean`
- `Note`
- `easy float`
- `SaveImage`
- `UnetLoaderGGUF`
- `ControlNetLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `DWPreprocessor`
- `AnyLineArtPreprocessor_aux`
- `CannyEdgePreprocessor`
- `DepthAnythingPreprocessor`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `cfg` = `1`
- `controlnet_strength` = `1.0000000000000002`
- `denoise` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta57`
- `seed` = `557223418395068`
- `steps` = `8`

## 知识

覆盖率 **57%**（25/44）

**有卡**：`ImpactSwitch`、`ImpactMinMax`、`PreviewImage`、`Note`、`ControlNetApplyAdvanced`、`KSampler`、`LayerUtility: PurgeVRAM V2`、`VAEEncode`、`CR Text`、`CR Text Concatenate`、`LoraLoaderModelOnly`、`LoadImage`、`easy int`、`VAEDecode`、`CLIPLoader`、`VAELoader`

**缺卡**（9）：`CR Text`、`CR Text`、`CR Text Concatenate`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM V2`、`easy boolean`、`easy float`、`easy int`、`easy int`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识
- 次要节点 `easy float` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- 次要节点 `easy int` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
