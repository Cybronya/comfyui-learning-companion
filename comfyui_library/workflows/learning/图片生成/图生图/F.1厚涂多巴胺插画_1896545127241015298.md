---
key: 图片生成/图生图/F.1厚涂多巴胺插画_1896545127241015298.json
name: F.1厚涂多巴胺插画_1896545127241015298
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/F.1厚涂多巴胺插画_1896545127241015298.json
hash: dbaa6d625dcece49
coverage: 0.913043
learned_at: 2026-10-23 10:52:38
nodes: [ImageResizeKJ, ModelSamplingFlux, DepthAnythingV2Preprocessor, Note, EmptyLatentImage, Miaoshouai_Tagger, Power Lora Loader (rgthree), workflow/模型, PulidEvaClipLoader, PulidFluxModelLoader, PulidInsightFaceLoader, ApplyPulidFlux, Note, workflow/clip, CLIPVisionLoader, StyleModelLoader, ReduxAdvanced, InpaintModelConditioning, FluxGuidance, KSampler, VAEDecode, LoadImage, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 3.5, "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "simple", "seed": 357446481942610, "steps": 20, "width": 512}
---

# 图片生成/图生图/F.1厚涂多巴胺插画_1896545127241015298.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/F.1厚涂多巴胺插画_1896545127241015298.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `ImageResizeKJ`
- `ModelSamplingFlux`
- `DepthAnythingV2Preprocessor`
- `Note`
- `EmptyLatentImage` ★核心
- `Miaoshouai_Tagger`
- `Power Lora Loader (rgthree)`
- `workflow/模型`
- `PulidEvaClipLoader`
- `PulidFluxModelLoader`
- `PulidInsightFaceLoader`
- `ApplyPulidFlux`
- `Note`
- `workflow/clip`
- `CLIPVisionLoader`
- `StyleModelLoader`
- `ReduxAdvanced`
- `InpaintModelConditioning`
- `FluxGuidance`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `SaveImage`

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `357446481942610`
- `steps` = `20`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`ImageResizeKJ`、`ModelSamplingFlux`、`DepthAnythingV2Preprocessor`、`EmptyLatentImage`、`Miaoshouai_Tagger`、`Power Lora Loader (rgthree)`、`workflow/模型`、`PulidEvaClipLoader`、`PulidFluxModelLoader`、`PulidInsightFaceLoader`、`ApplyPulidFlux`、`workflow/clip`、`CLIPVisionLoader`、`StyleModelLoader`、`ReduxAdvanced`、`InpaintModelConditioning`、`FluxGuidance`、`KSampler`、`VAEDecode`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、EmptyLatentImage、LoadImage、DepthAnythingV2Preprocessor、FluxGuidance、StyleModelLoader、Power Lora Loader (rgthree)
