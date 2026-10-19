---
key: 图片生成/文生图/Z-IMAGE终极版自动洗图流+CN2.1+高清放大_2001589034491211777.json
name: Z-IMAGE终极版自动洗图流+CN2.1+高清放大_2001589034491211777
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-IMAGE终极版自动洗图流+CN2.1+高清放大_2001589034491211777.json
hash: 47d3ebda173c71df
coverage: 0.574074
learned_at: 2026-10-19 21:46:58
nodes: [ModelPatchLoader, AIO_Preprocessor, Note, Note, ModelSamplingAuraFlow, Note, INTConstant, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, easy seed, QwenImageDiffsynthControlnet, EmptyLatentImage, Reroute, Reroute, Reroute, ConditioningZeroOut, Reroute, Reroute, Reroute, Reroute, INTConstant, Reroute, Reroute, Reroute, Reroute, Reroute, LayerUtility: ImageScaleByAspectRatio V2, ShowText|pysssss, CLIPTextEncode, Reroute, Reroute, Reroute, Reroute, CLIPLoader, Qwen3_VQA, Reroute, KSamplerAdvanced, KSamplerAdvanced, ImageScaleToTotalPixels, VAEDecode, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, PreviewImage, UNETLoader, PreviewImage, AIO_Preprocessor, VAELoader, ModelSamplingAuraFlow, INTConstant, AIO_Preprocessor, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 10, "denoise": "simple", "height": 1080, "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize", "width": 1920}
---

# 图片生成/文生图/Z-IMAGE终极版自动洗图流+CN2.1+高清放大_2001589034491211777.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-IMAGE终极版自动洗图流+CN2.1+高清放大_2001589034491211777.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `ModelPatchLoader`
- `AIO_Preprocessor`
- `Note`
- `Note`
- `ModelSamplingAuraFlow`
- `Note`
- `INTConstant`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy seed`
- `QwenImageDiffsynthControlnet`
- `EmptyLatentImage` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `ConditioningZeroOut`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `INTConstant`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `CLIPLoader`
- `Qwen3_VQA`
- `Reroute`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `PreviewImage`
- `UNETLoader` ★核心
- `PreviewImage`
- `AIO_Preprocessor`
- `VAELoader`
- `ModelSamplingAuraFlow`
- `INTConstant`
- `AIO_Preprocessor`
- `LoadImage`

## 关键参数

- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`
- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **57%**（31/54）

**有卡**：`ModelPatchLoader`、`AIO_Preprocessor`、`ModelSamplingAuraFlow`、`INTConstant`、`LayerUtility: ImageReel`、`LayerUtility: ImageReelComposit`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy seed`、`QwenImageDiffsynthControlnet`、`EmptyLatentImage`、`ConditioningZeroOut`、`CLIPTextEncode`、`CLIPLoader`、`Qwen3_VQA`、`KSamplerAdvanced`、`ImageScaleToTotalPixels`、`VAEDecode`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`UNETLoader`、`VAELoader`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage、UNETLoader
