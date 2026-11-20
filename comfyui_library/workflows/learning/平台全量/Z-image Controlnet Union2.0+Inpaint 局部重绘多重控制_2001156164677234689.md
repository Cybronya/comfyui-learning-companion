---
key: 平台全量/Z-image Controlnet Union2.0+Inpaint 局部重绘多重控制_2001156164677234689.json
name: Z-image Controlnet Union2.0+Inpaint 局部重绘多重控制_2001156164677234689
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Z-image Controlnet Union2.0+Inpaint 局部重绘多重控制_2001156164677234689.json
hash: 34c3563e8756e7a9
coverage: 0.823529
learned_at: 2026-11-14 01:08:18
nodes: [AIO_Preprocessor, Note, Note, AIO_Preprocessor, Canny, ImageConcatMulti, ModelPatchLoader, CLIPLoader, UNETLoader, VAELoader, Note, CR Prompt Text, easy anythingIndexSwitch, ImageScaleToMaxDimension, ImageConcatMulti, ImageConcatMulti, LoadImage, Note, EmptySD3LatentImage, ConditioningZeroOut, VAEDecode, KSampler, CLIPTextEncode, ModelSamplingAuraFlow, QwenImageDiffsynthControlnet, GetImageSize, GrowMaskWithBlur, SetLatentNoiseMask, InpaintModelConditioning, ImageAndMaskPreview_UTK, PreviewImage, Note, SaveImage, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 25166677528779, "steps": 10}
---

# 平台全量/Z-image Controlnet Union2.0+Inpaint 局部重绘多重控制_2001156164677234689.json

> 来源文件 `comfyui_library/workflows/平台全量/Z-image Controlnet Union2.0+Inpaint 局部重绘多重控制_2001156164677234689.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `AIO_Preprocessor`
- `Note`
- `Note`
- `AIO_Preprocessor`
- `Canny`
- `ImageConcatMulti`
- `ModelPatchLoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `Note`
- `CR Prompt Text`
- `easy anythingIndexSwitch`
- `ImageScaleToMaxDimension`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `LoadImage`
- `Note`
- `EmptySD3LatentImage`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `QwenImageDiffsynthControlnet`
- `GetImageSize`
- `GrowMaskWithBlur`
- `SetLatentNoiseMask`
- `InpaintModelConditioning`
- `ImageAndMaskPreview_UTK`
- `PreviewImage`
- `Note`
- `SaveImage`
- `SaveImage`

## 关键参数

- `seed` = `25166677528779`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（28/34）

**有卡**：`AIO_Preprocessor`、`Canny`、`ImageConcatMulti`、`ModelPatchLoader`、`CLIPLoader`、`UNETLoader`、`VAELoader`、`CR Prompt Text`、`easy anythingIndexSwitch`、`ImageScaleToMaxDimension`、`LoadImage`、`EmptySD3LatentImage`、`ConditioningZeroOut`、`VAEDecode`、`KSampler`、`CLIPTextEncode`、`ModelSamplingAuraFlow`、`QwenImageDiffsynthControlnet`、`GetImageSize`、`GrowMaskWithBlur`、`SetLatentNoiseMask`、`InpaintModelConditioning`、`ImageAndMaskPreview_UTK`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、UNETLoader
