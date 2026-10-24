---
key: 图片生成/图生图/（自用）Z-image Controlnet Union2.0+Inpaint局部重绘洗图_2000610350284275714.json
name: （自用）Z-image Controlnet Union2.0+Inpaint局部重绘洗图_2000610350284275714
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/（自用）Z-image Controlnet Union2.0+Inpaint局部重绘洗图_2000610350284275714.json
hash: 95d7cbfee6172194
coverage: 0.864865
learned_at: 2026-10-23 13:38:26
nodes: [EmptySD3LatentImage, MarkdownNote, GetImageSize, QwenImageDiffsynthControlnet, CLIPLoader, UNETLoader, ModelPatchLoader, VAELoader, KSampler, CLIPTextEncode, ConditioningZeroOut, InpaintModelConditioning, ModelSamplingAuraFlow, Note, ImageConcatMulti, SetLatentNoiseMask, ImageScaleToMaxDimension, Canny, Note, Note, Note, ImageAndMaskPreview_UTK, GrowMaskWithBlur, AIO_Preprocessor, LoadImage, SaveImage, SaveImage, TT_img_enc, SaveImage, TT_img_enc_v2, CR Prompt Text, AIO_Preprocessor, easy anythingIndexSwitch, VAEDecode, SaveImage, DuckHideNode, CR Prompt Text]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 481191865238522, "steps": 10}
---

# 图片生成/图生图/（自用）Z-image Controlnet Union2.0+Inpaint局部重绘洗图_2000610350284275714.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/（自用）Z-image Controlnet Union2.0+Inpaint局部重绘洗图_2000610350284275714.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
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
- `ImageConcatMulti`
- `SetLatentNoiseMask`
- `ImageScaleToMaxDimension`
- `Canny`
- `Note`
- `Note`
- `Note`
- `ImageAndMaskPreview_UTK`
- `GrowMaskWithBlur`
- `AIO_Preprocessor`
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `TT_img_enc`
- `SaveImage`
- `TT_img_enc_v2`
- `CR Prompt Text`
- `AIO_Preprocessor`
- `easy anythingIndexSwitch`
- `VAEDecode` ★核心
- `SaveImage`
- `DuckHideNode`
- `CR Prompt Text`

## 关键参数

- `seed` = `481191865238522`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（32/37）

**有卡**：`EmptySD3LatentImage`、`GetImageSize`、`QwenImageDiffsynthControlnet`、`CLIPLoader`、`UNETLoader`、`ModelPatchLoader`、`VAELoader`、`KSampler`、`CLIPTextEncode`、`ConditioningZeroOut`、`InpaintModelConditioning`、`ModelSamplingAuraFlow`、`ImageConcatMulti`、`SetLatentNoiseMask`、`ImageScaleToMaxDimension`、`Canny`、`ImageAndMaskPreview_UTK`、`GrowMaskWithBlur`、`AIO_Preprocessor`、`LoadImage`、`SaveImage`、`TT_img_enc`、`TT_img_enc_v2`、`CR Prompt Text`、`easy anythingIndexSwitch`、`VAEDecode`、`DuckHideNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader
