---
key: 图片生成/文生图/Z-image Controlnet Union 1.0 Vs 2.0对比工作流_2000525274498428929.json
name: Z-image Controlnet Union 1.0 Vs 2.0对比工作流_2000525274498428929
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image Controlnet Union 1.0 Vs 2.0对比工作流_2000525274498428929.json
hash: 4fb33f2c7593248c
coverage: 0.921053
learned_at: 2026-10-19 21:47:05
nodes: [VAELoader, ConditioningZeroOut, EmptySD3LatentImage, Note, MarkdownNote, CLIPTextEncode, CLIPLoader, ModelSamplingAuraFlow, UNETLoader, LoadImage, CR Prompt Text, ModelPatchLoader, QwenImageDiffsynthControlnet, QwenImageDiffsynthControlnet, ModelPatchLoader, ModelSamplingAuraFlow, KSampler, KSampler, ImageConcatMulti, ImageConcatMulti, GetImageSize, PreviewImage, Canny, AIO_Preprocessor, AIO_Preprocessor, ImageScaleToMaxDimension, SaveImage, SaveImage, ImageConcatMulti, SaveImage, VAEDecode, VAEDecode, AddLabel, AddLabel, AddLabel, SaveImage, easy anythingIndexSwitch, AddLabel]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 507021552696742, "steps": 10}
---

# 图片生成/文生图/Z-image Controlnet Union 1.0 Vs 2.0对比工作流_2000525274498428929.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image Controlnet Union 1.0 Vs 2.0对比工作流_2000525274498428929.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
- `VAELoader`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `Note`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `LoadImage`
- `CR Prompt Text`
- `ModelPatchLoader`
- `QwenImageDiffsynthControlnet`
- `QwenImageDiffsynthControlnet`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `KSampler` ★核心
- `ImageConcatMulti`
- `ImageConcatMulti`
- `GetImageSize`
- `PreviewImage`
- `Canny`
- `AIO_Preprocessor`
- `AIO_Preprocessor`
- `ImageScaleToMaxDimension`
- `SaveImage`
- `SaveImage`
- `ImageConcatMulti`
- `SaveImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `AddLabel`
- `AddLabel`
- `AddLabel`
- `SaveImage`
- `easy anythingIndexSwitch`
- `AddLabel`

## 关键参数

- `seed` = `507021552696742`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（35/38）

**有卡**：`VAELoader`、`ConditioningZeroOut`、`EmptySD3LatentImage`、`CLIPTextEncode`、`CLIPLoader`、`ModelSamplingAuraFlow`、`UNETLoader`、`LoadImage`、`CR Prompt Text`、`ModelPatchLoader`、`QwenImageDiffsynthControlnet`、`KSampler`、`ImageConcatMulti`、`GetImageSize`、`Canny`、`AIO_Preprocessor`、`ImageScaleToMaxDimension`、`SaveImage`、`VAEDecode`、`AddLabel`、`easy anythingIndexSwitch`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader
