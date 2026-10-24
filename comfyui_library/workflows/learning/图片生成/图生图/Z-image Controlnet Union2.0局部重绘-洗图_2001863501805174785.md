---
key: 图片生成/图生图/Z-image Controlnet Union2.0局部重绘-洗图_2001863501805174785.json
name: Z-image Controlnet Union2.0局部重绘-洗图_2001863501805174785
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-image Controlnet Union2.0局部重绘-洗图_2001863501805174785.json
hash: 5d606eddf81aaf5c
coverage: 0.736842
learned_at: 2026-10-23 11:30:17
nodes: [CLIPLoader, UNETLoader, VAELoader, ImageConcatMulti, QwenImageDiffsynthControlnet, ModelPatchLoader, ConditioningZeroOut, InpaintModelConditioning, ModelSamplingAuraFlow, AIO_Preprocessor, Canny, ImageAndMaskPreview_UTK, ImageConcatMulti, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, VAEDecode, KSampler, SetLatentNoiseMask, AIO_Preprocessor, Note, Note, Note, easy anythingIndexSwitch, PreviewImage, easy int, Note, ImageConcatMulti, Reroute, SaveImage, MarkdownNote, SaveImage, Note, LoadImage, MarkdownNote, CR Prompt Text, easy int, GrowMaskWithBlur]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 193496481074405, "steps": 10}
---

# 图片生成/图生图/Z-image Controlnet Union2.0局部重绘-洗图_2001863501805174785.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-image Controlnet Union2.0局部重绘-洗图_2001863501805174785.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `ImageConcatMulti`
- `QwenImageDiffsynthControlnet`
- `ModelPatchLoader`
- `ConditioningZeroOut`
- `InpaintModelConditioning`
- `ModelSamplingAuraFlow`
- `AIO_Preprocessor`
- `Canny`
- `ImageAndMaskPreview_UTK`
- `ImageConcatMulti`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `SetLatentNoiseMask`
- `AIO_Preprocessor`
- `Note`
- `Note`
- `Note`
- `easy anythingIndexSwitch`
- `PreviewImage`
- `easy int`
- `Note`
- `ImageConcatMulti`
- `Reroute`
- `SaveImage`
- `MarkdownNote`
- `SaveImage`
- `Note`
- `LoadImage`
- `MarkdownNote`
- `CR Prompt Text`
- `easy int`
- `GrowMaskWithBlur`

## 关键参数

- `seed` = `193496481074405`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **74%**（28/38）

**有卡**：`CLIPLoader`、`UNETLoader`、`VAELoader`、`ImageConcatMulti`、`QwenImageDiffsynthControlnet`、`ModelPatchLoader`、`ConditioningZeroOut`、`InpaintModelConditioning`、`ModelSamplingAuraFlow`、`AIO_Preprocessor`、`Canny`、`ImageAndMaskPreview_UTK`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`VAEDecode`、`KSampler`、`SetLatentNoiseMask`、`easy anythingIndexSwitch`、`easy int`、`SaveImage`、`LoadImage`、`CR Prompt Text`、`GrowMaskWithBlur`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader
