---
key: 图片生成/文生图/Zimage turbo Controlnet_2063212237803839489.json
name: Zimage turbo Controlnet_2063212237803839489
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Zimage turbo Controlnet_2063212237803839489.json
hash: 00ef9dbfaccf3ff7
coverage: 0.904762
learned_at: 2026-10-19 23:03:04
nodes: [LayerUtility: PurgeVRAM, ModelPatchLoader, Image Comparer (rgthree), ModelSamplingAuraFlow, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, VAELoader, VAEEncode, CannyEdgePreprocessor, ZImageFunControlnet, PreviewImage, LoadImage, UNETLoader, VAEDecode, CLIPTextEncode, ConditioningZeroOut, KSampler, UNETLoader, DepthAnythingPreprocessor, SaveImage, Text]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 1052066903287145, "steps": 30}
---

# 图片生成/文生图/Zimage turbo Controlnet_2063212237803839489.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Zimage turbo Controlnet_2063212237803839489.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `LayerUtility: PurgeVRAM`
- `ModelPatchLoader`
- `Image Comparer (rgthree)`
- `ModelSamplingAuraFlow`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `VAELoader`
- `VAEEncode` ★核心
- `CannyEdgePreprocessor`
- `ZImageFunControlnet`
- `PreviewImage`
- `LoadImage`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `DepthAnythingPreprocessor`
- `SaveImage`
- `Text`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1052066903287145`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（19/21）

**有卡**：`LayerUtility: PurgeVRAM`、`ModelPatchLoader`、`ModelSamplingAuraFlow`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`VAELoader`、`VAEEncode`、`CannyEdgePreprocessor`、`ZImageFunControlnet`、`LoadImage`、`UNETLoader`、`VAEDecode`、`CLIPTextEncode`、`ConditioningZeroOut`、`KSampler`、`DepthAnythingPreprocessor`、`SaveImage`、`Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader
