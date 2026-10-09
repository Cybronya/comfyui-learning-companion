---
key: 图片生成/文生图/千问洗图神器Qwen-Image-ControlNet-Union_1969044313470607361.json
name: 千问洗图神器Qwen-Image-ControlNet-Union_1969044313470607361.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/千问洗图神器Qwen-Image-ControlNet-Union_1969044313470607361.json
hash: 1a193fda7810c541
coverage: 0.568182
learned_at: 2026-10-09 02:01:39
nodes: [ImpactSwitch, ImpactMinMax, PreviewImage, PreviewImage, PreviewImage, PreviewImage, Note, Note, Note, Note, ControlNetApplyAdvanced, KSampler, LayerUtility: PurgeVRAM V2, VAEEncode, CR Text, CR Text Concatenate, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, easy int, easy int, LoadImage, VAEDecode, CLIPLoader, VAELoader, ImpactConditionalBranch, CLIPTextEncode, CLIPTextEncode, ModelSamplingAuraFlow, SeedVR2GGUF, RH_Captioner, CR Text, easy boolean, Note, easy float, SaveImage, UnetLoaderGGUF, ControlNetLoader, LayerUtility: ImageScaleByAspectRatio V2, DWPreprocessor, AnyLineArtPreprocessor_aux, CannyEdgePreprocessor, DepthAnythingPreprocessor, LoadImage]
patterns: [image_to_image]
missing: [CR Text, CR Text, CR Text Concatenate, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, easy boolean, easy float, easy int, easy int]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "controlnet_strength": 1.0000000000000002, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta57", "seed": 557223418395068, "steps": 8}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy boolean` 知识库中没有该节点类型的任何知识, 次要节点 `easy float` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, 次要节点 `easy int` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/千问洗图神器Qwen-Image-ControlNet-Union_1969044313470607361.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1969044313470607361.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

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
- `ControlNetApplyAdvanced` ★核心
- `KSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `VAEEncode` ★核心
- `CR Text`
- `CR Text Concatenate`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `easy int`
- `easy int`
- `LoadImage`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `ImpactConditionalBranch`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `SeedVR2GGUF`
- `RH_Captioner`
- `CR Text`
- `easy boolean`
- `Note`
- `easy float`
- `SaveImage`
- `UnetLoaderGGUF` ★核心
- `ControlNetLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `DWPreprocessor`
- `AnyLineArtPreprocessor_aux`
- `CannyEdgePreprocessor`
- `DepthAnythingPreprocessor`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `controlnet_strength` = `1.0000000000000002`
- `seed` = `557223418395068`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta57`
- `denoise` = `1`

## 知识

覆盖率 **57%**（25/44）

**有卡**：`ImpactMinMax`、`ControlNetApplyAdvanced`、`KSampler`、`VAEEncode`、`LoraLoaderModelOnly`、`LoadImage`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`ImpactConditionalBranch`、`CLIPTextEncode`、`ModelSamplingAuraFlow`、`SeedVR2GGUF`、`RH_Captioner`、`SaveImage`、`UnetLoaderGGUF`、`ControlNetLoader`、`DWPreprocessor`、`AnyLineArtPreprocessor_aux`、`CannyEdgePreprocessor`、`DepthAnythingPreprocessor`

**缺卡**（9）：`CR Text`、`CR Text`、`CR Text Concatenate`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM V2`、`easy boolean`、`easy float`、`easy int`、`easy int`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、ControlNetApplyAdvanced

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
