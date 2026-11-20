---
key: 平台全量/Flux Redux + PuLID Face Swap - Clone any portrait_1861717216457527298.json
name: Flux Redux + PuLID Face Swap - Clone any portrait_1861717216457527298
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux Redux + PuLID Face Swap - Clone any portrait_1861717216457527298.json
hash: e0c0e2b54419f774
coverage: 1
learned_at: 2026-11-14 00:28:02
nodes: [VAEDecode, SaveImage, StyleModelApply, CLIPTextEncodeFlux, FluxGuidance, CLIPTextEncode, LoadImage, EmptyLatentImage, LoadImage, PulidFluxModelLoader, PulidFluxInsightFaceLoader, PulidFluxEvaClipLoader, KSampler, ApplyPulidFlux, ImageScale, CLIPVisionEncode, DF_Get_image_size, UNETLoader, DualCLIPLoader, VAELoader, StyleModelLoader, CLIPVisionLoader]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "normal", "seed": 1042187356202896, "steps": 25, "width": 1024}
---

# 平台全量/Flux Redux + PuLID Face Swap - Clone any portrait_1861717216457527298.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux Redux + PuLID Face Swap - Clone any portrait_1861717216457527298.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `VAEDecode` ★核心
- `SaveImage`
- `StyleModelApply`
- `CLIPTextEncodeFlux` ★核心
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `PulidFluxModelLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxEvaClipLoader`
- `KSampler` ★核心
- `ApplyPulidFlux`
- `ImageScale`
- `CLIPVisionEncode`
- `DF_Get_image_size`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `StyleModelLoader`
- `CLIPVisionLoader`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1042187356202896`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`VAEDecode`、`SaveImage`、`StyleModelApply`、`CLIPTextEncodeFlux`、`FluxGuidance`、`CLIPTextEncode`、`LoadImage`、`EmptyLatentImage`、`PulidFluxModelLoader`、`PulidFluxInsightFaceLoader`、`PulidFluxEvaClipLoader`、`KSampler`、`ApplyPulidFlux`、`ImageScale`、`CLIPVisionEncode`、`DF_Get_image_size`、`UNETLoader`、`DualCLIPLoader`、`VAELoader`、`StyleModelLoader`、`CLIPVisionLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、EmptyLatentImage、LoadImage、FluxGuidance
