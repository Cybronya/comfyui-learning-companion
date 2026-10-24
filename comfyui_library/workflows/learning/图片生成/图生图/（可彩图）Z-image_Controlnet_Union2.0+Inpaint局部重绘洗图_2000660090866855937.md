---
key: 图片生成/图生图/（可彩图）Z-image_Controlnet_Union2.0+Inpaint局部重绘洗图_2000660090866855937.json
name: （可彩图）Z-image_Controlnet_Union2.0+Inpaint局部重绘洗图_2000660090866855937
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（可彩图）Z-image_Controlnet_Union2.0+Inpaint局部重绘洗图_2000660090866855937.json
hash: 196b8f47bfff630f
coverage: 0.785714
learned_at: 2026-10-23 13:37:33
nodes: [CLIPLoader, UNETLoader, VAELoader, AIO_Preprocessor, AIO_Preprocessor, easy anythingIndexSwitch, Note, Note, Note, ImageAndMaskPreview_UTK, easy imagePixelPerfect, EmptySD3LatentImage, ModelPatchLoader, CLIPTextEncode, ModelSamplingAuraFlow, QwenImageDiffsynthControlnet, InpaintModelConditioning, ConditioningZeroOut, SetLatentNoiseMask, Note, Canny, KSampler, GetImageSize, CR Prompt Text, LayerUtility: ImageScaleByAspectRatio V2, ImageConcanate, SaveImage, MaskToImage, GrowMaskWithBlur, SaveImage, PrimitiveNode, PrimitiveNode, PreviewImage, ImageBlend, LoadImage, Note, VAEDecode, SaveImage, ImageConcanate, TT_img_enc_v2, Note, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 628895845229996, "steps": 10}
---

# 图片生成/图生图/（可彩图）Z-image_Controlnet_Union2.0+Inpaint局部重绘洗图_2000660090866855937.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（可彩图）Z-image_Controlnet_Union2.0+Inpaint局部重绘洗图_2000660090866855937.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（42 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `easy anythingIndexSwitch`
- `Note`
- `Note`
- `Note`
- `ImageAndMaskPreview_UTK`
- `easy imagePixelPerfect`
- `EmptySD3LatentImage`
- `ModelPatchLoader`
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `QwenImageDiffsynthControlnet`
- `InpaintModelConditioning`
- `ConditioningZeroOut`
- `SetLatentNoiseMask`
- `Note`
- `Canny`
- `KSampler` ★核心
- `GetImageSize`
- `CR Prompt Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageConcanate`
- `SaveImage`
- `MaskToImage`
- `GrowMaskWithBlur`
- `SaveImage`
- `PrimitiveNode`
- `PrimitiveNode`
- `PreviewImage`
- `ImageBlend`
- `LoadImage`
- `Note`
- `VAEDecode` ★核心
- `SaveImage`
- `ImageConcanate`
- `TT_img_enc_v2`
- `Note`
- `SaveImage`

## 关键参数

- `seed` = `628895845229996`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **79%**（33/42）

**有卡**：`CLIPLoader`、`UNETLoader`、`VAELoader`、`AIO_Preprocessor`、`easy anythingIndexSwitch`、`ImageAndMaskPreview_UTK`、`easy imagePixelPerfect`、`EmptySD3LatentImage`、`ModelPatchLoader`、`CLIPTextEncode`、`ModelSamplingAuraFlow`、`QwenImageDiffsynthControlnet`、`InpaintModelConditioning`、`ConditioningZeroOut`、`SetLatentNoiseMask`、`Canny`、`KSampler`、`GetImageSize`、`CR Prompt Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageConcanate`、`SaveImage`、`MaskToImage`、`GrowMaskWithBlur`、`ImageBlend`、`LoadImage`、`VAEDecode`、`TT_img_enc_v2`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader
