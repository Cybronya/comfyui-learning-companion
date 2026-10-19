---
key: 图片生成/文生图/zimage-controlnet-2.1（26.1）人物替换工作流_2011523555053281282.json
name: zimage-controlnet-2.1（26.1）人物替换工作流_2011523555053281282
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/zimage-controlnet-2.1（26.1）人物替换工作流_2011523555053281282.json
hash: 5ed857fdd5e67518
coverage: 0.9
learned_at: 2026-10-19 22:01:17
nodes: [PreviewImage, AIO_Preprocessor, easy imageSizeBySide, CLIPTextEncode, VAEDecode, ConditioningZeroOut, SaveImage, Image Comparer (rgthree), VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, GrowMaskWithBlur, QwenImageDiffsynthControlnet, SetLatentNoiseMask, KSampler, ModelPatchLoader, UNETLoader, CLIPLoader, VAELoader, LoadImage, CR Prompt Text]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "er_sde", "scheduler": "simple", "seed": 454991803784038, "steps": 10}
---

# 图片生成/文生图/zimage-controlnet-2.1（26.1）人物替换工作流_2011523555053281282.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/zimage-controlnet-2.1（26.1）人物替换工作流_2011523555053281282.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `PreviewImage`
- `AIO_Preprocessor`
- `easy imageSizeBySide`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `SaveImage`
- `Image Comparer (rgthree)`
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GrowMaskWithBlur`
- `QwenImageDiffsynthControlnet`
- `SetLatentNoiseMask`
- `KSampler` ★核心
- `ModelPatchLoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `CR Prompt Text`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `454991803784038`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`AIO_Preprocessor`、`easy imageSizeBySide`、`CLIPTextEncode`、`VAEDecode`、`ConditioningZeroOut`、`SaveImage`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`GrowMaskWithBlur`、`QwenImageDiffsynthControlnet`、`SetLatentNoiseMask`、`KSampler`、`ModelPatchLoader`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader
