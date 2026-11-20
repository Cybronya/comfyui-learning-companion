---
key: 平台全量/FLUX.1 - Ultimate Txt2Img with Upscale - Optimized_1861723634426425345.json
name: FLUX.1 - Ultimate Txt2Img with Upscale - Optimized_1861723634426425345
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/FLUX.1 - Ultimate Txt2Img with Upscale - Optimized_1861723634426425345.json
hash: 7e2b26bd262f7cb1
coverage: 0.711111
learned_at: 2026-11-14 00:25:00
nodes: [PreviewImage, Fast Groups Muter (rgthree), Image Comparer (rgthree), RepeatLatentBatch, PreviewImage, KSampler, FluxGuidance, DownloadAndLoadDepthAnythingV2Model, DepthAnything_V2, Canny, String Literal, Anything Everywhere, Note, LatentUpscaleBy, Anything Everywhere, RH_Captioner, ShowText|pysssss, CLIPTextEncode, Note, SystemNotification|pysssss, InstructPixToPixConditioning, easy cleanGpuUsed, easy cleanGpuUsed, FluxGuidance, LatentUpscaleBy, CLIPTextEncode, VAEDecode, SaveImage, SystemNotification|pysssss, SaveImage, RepeatLatentBatch, VAEDecode, CLIPTextEncode, PreviewImage, InstructPixToPixConditioning, CLIPTextEncode, KSampler, UNETLoader, UNETLoader, Anything Everywhere, LoadImage, DualCLIPLoader, Anything Everywhere3, VAELoader, Note]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 959001072333385, "steps": 20}
---

# 平台全量/FLUX.1 - Ultimate Txt2Img with Upscale - Optimized_1861723634426425345.json

> 来源文件 `comfyui_library/workflows/平台全量/FLUX.1 - Ultimate Txt2Img with Upscale - Optimized_1861723634426425345.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `PreviewImage`
- `Fast Groups Muter (rgthree)`
- `Image Comparer (rgthree)`
- `RepeatLatentBatch`
- `PreviewImage`
- `KSampler` ★核心
- `FluxGuidance`
- `DownloadAndLoadDepthAnythingV2Model`
- `DepthAnything_V2`
- `Canny`
- `String Literal`
- `Anything Everywhere`
- `Note`
- `LatentUpscaleBy`
- `Anything Everywhere`
- `RH_Captioner`
- `ShowText|pysssss`
- `CLIPTextEncode` ★核心
- `Note`
- `SystemNotification|pysssss`
- `InstructPixToPixConditioning`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `FluxGuidance`
- `LatentUpscaleBy`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `SystemNotification|pysssss`
- `SaveImage`
- `RepeatLatentBatch`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `InstructPixToPixConditioning`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `Anything Everywhere`
- `LoadImage`
- `DualCLIPLoader`
- `Anything Everywhere3`
- `VAELoader`
- `Note`

## 关键参数

- `seed` = `959001072333385`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **71%**（32/45）

**有卡**：`RepeatLatentBatch`、`KSampler`、`FluxGuidance`、`DownloadAndLoadDepthAnythingV2Model`、`DepthAnything_V2`、`Canny`、`String Literal`、`LatentUpscaleBy`、`RH_Captioner`、`CLIPTextEncode`、`SystemNotification|pysssss`、`InstructPixToPixConditioning`、`easy cleanGpuUsed`、`VAEDecode`、`SaveImage`、`UNETLoader`、`LoadImage`、`DualCLIPLoader`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、Canny、DepthAnything_V2
