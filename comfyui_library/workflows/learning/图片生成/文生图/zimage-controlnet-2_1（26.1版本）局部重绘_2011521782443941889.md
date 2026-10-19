---
key: 图片生成/文生图/zimage-controlnet-2_1（26.1版本）局部重绘_2011521782443941889.json
name: zimage-controlnet-2_1（26.1版本）局部重绘_2011521782443941889
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/zimage-controlnet-2_1（26.1版本）局部重绘_2011521782443941889.json
hash: 05a7adf7a9b7ccf6
coverage: 0.9
learned_at: 2026-10-19 22:01:17
nodes: [easy imageSizeBySide, PreviewImage, GrowMaskWithBlur, LayerUtility: ImageScaleByAspectRatio V2, KSampler, VAEDecode, SaveImage, ConditioningZeroOut, CLIPTextEncode, Image Comparer (rgthree), QwenImageDiffsynthControlnet, InpaintModelConditioning, SetLatentNoiseMask, ModelPatchLoader, AIO_Preprocessor, UNETLoader, CLIPLoader, VAELoader, LoadImage, CR Prompt Text]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 774473835827374, "steps": 10}
---

# 图片生成/文生图/zimage-controlnet-2_1（26.1版本）局部重绘_2011521782443941889.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/zimage-controlnet-2_1（26.1版本）局部重绘_2011521782443941889.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `easy imageSizeBySide`
- `PreviewImage`
- `GrowMaskWithBlur`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `QwenImageDiffsynthControlnet`
- `InpaintModelConditioning`
- `SetLatentNoiseMask`
- `ModelPatchLoader`
- `AIO_Preprocessor`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `CR Prompt Text`

## 关键参数

- `seed` = `774473835827374`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`easy imageSizeBySide`、`GrowMaskWithBlur`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`VAEDecode`、`SaveImage`、`ConditioningZeroOut`、`CLIPTextEncode`、`QwenImageDiffsynthControlnet`、`InpaintModelConditioning`、`SetLatentNoiseMask`、`ModelPatchLoader`、`AIO_Preprocessor`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader
