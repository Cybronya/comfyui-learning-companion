---
key: 图片生成/图生图/Z-image Controlnet Union2.0+Inpaint局部重绘多重控制洗图_2000538829650096130.json
name: Z-image Controlnet Union2.0+Inpaint局部重绘多重控制洗图_2000538829650096130
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-image Controlnet Union2.0+Inpaint局部重绘多重控制洗图_2000538829650096130.json
hash: 0b9aaae44d838169
coverage: 0.8
learned_at: 2026-10-23 11:30:16
nodes: [EmptySD3LatentImage, MarkdownNote, GetImageSize, QwenImageDiffsynthControlnet, CLIPLoader, UNETLoader, ModelPatchLoader, VAELoader, KSampler, CLIPTextEncode, ConditioningZeroOut, InpaintModelConditioning, ModelSamplingAuraFlow, Note, LoadImage, GrowMaskWithBlur, SaveImage, VAEDecode, ImageAndMaskPreview_UTK, ImageConcatMulti, ImageConcatMulti, CR Prompt Text, PreviewImage, SetLatentNoiseMask, ImageConcatMulti, SaveImage, PreviewImage, AIO_Preprocessor, ImageScaleToMaxDimension, easy anythingIndexSwitch, Canny, Note, Note, Note, AIO_Preprocessor]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 321437397140236, "steps": 10}
---

# 图片生成/图生图/Z-image Controlnet Union2.0+Inpaint局部重绘多重控制洗图_2000538829650096130.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-image Controlnet Union2.0+Inpaint局部重绘多重控制洗图_2000538829650096130.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `EmptySD3LatentImage`
- `MarkdownNote`
- `GetImageSize`
- `QwenImageDiffsynthControlnet`
- `CLIPLoader`
- `UNETLoader` ★核心
- `ModelPatchLoader`
- `VAELoader`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `InpaintModelConditioning`
- `ModelSamplingAuraFlow`
- `Note`
- `LoadImage`
- `GrowMaskWithBlur`
- `SaveImage`
- `VAEDecode` ★核心
- `ImageAndMaskPreview_UTK`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `CR Prompt Text`
- `PreviewImage`
- `SetLatentNoiseMask`
- `ImageConcatMulti`
- `SaveImage`
- `PreviewImage`
- `AIO_Preprocessor`
- `ImageScaleToMaxDimension`
- `easy anythingIndexSwitch`
- `Canny`
- `Note`
- `Note`
- `Note`
- `AIO_Preprocessor`

## 关键参数

- `seed` = `321437397140236`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（28/35）

**有卡**：`EmptySD3LatentImage`、`GetImageSize`、`QwenImageDiffsynthControlnet`、`CLIPLoader`、`UNETLoader`、`ModelPatchLoader`、`VAELoader`、`KSampler`、`CLIPTextEncode`、`ConditioningZeroOut`、`InpaintModelConditioning`、`ModelSamplingAuraFlow`、`LoadImage`、`GrowMaskWithBlur`、`SaveImage`、`VAEDecode`、`ImageAndMaskPreview_UTK`、`ImageConcatMulti`、`CR Prompt Text`、`SetLatentNoiseMask`、`AIO_Preprocessor`、`ImageScaleToMaxDimension`、`easy anythingIndexSwitch`、`Canny`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader
