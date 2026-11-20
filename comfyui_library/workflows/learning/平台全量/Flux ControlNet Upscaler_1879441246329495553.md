---
key: 平台全量/Flux ControlNet Upscaler_1879441246329495553.json
name: Flux ControlNet Upscaler_1879441246329495553
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Flux ControlNet Upscaler_1879441246329495553.json
hash: 1873e896306278a2
coverage: 0.857143
learned_at: 2026-11-14 00:27:34
nodes: [VAEEncode, CLIPTextEncode, CLIPTextEncode, easy imageSize, ReroutePrimitive|pysssss, ReroutePrimitive|pysssss, ReroutePrimitive|pysssss, ReroutePrimitive|pysssss, ImpactSwitch, ReroutePrimitive|pysssss, ReroutePrimitive|pysssss, CR Set Value On Boolean, ReroutePrimitive|pysssss, ImpactSwitch, KSampler, LoadImage, ImageScaleBy, ControlNetApplyAdvanced, UNETLoader, UnetLoaderGGUF, SaveImage, VAEDecode, Image Comparer (rgthree), easy imageSize, DualCLIPLoader, DualCLIPLoaderGGUF, Florence2Run, easy showAnything, ControlNetLoader, FluxGuidance, VAELoader, Note, SimpleMathBoolean+, DownloadAndLoadFlorence2Lora, DownloadAndLoadFlorence2Model]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "controlnet_strength": 0.6, "denoise": 1, "sampler_name": "dpmpp_2m", "scheduler": "sgm_uniform", "seed": 953999074754702, "steps": 28}
---

# 平台全量/Flux ControlNet Upscaler_1879441246329495553.json

> 来源文件 `comfyui_library/workflows/平台全量/Flux ControlNet Upscaler_1879441246329495553.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy imageSize`
- `ReroutePrimitive|pysssss`
- `ReroutePrimitive|pysssss`
- `ReroutePrimitive|pysssss`
- `ReroutePrimitive|pysssss`
- `ImpactSwitch`
- `ReroutePrimitive|pysssss`
- `ReroutePrimitive|pysssss`
- `CR Set Value On Boolean`
- `ReroutePrimitive|pysssss`
- `ImpactSwitch`
- `KSampler` ★核心
- `LoadImage`
- `ImageScaleBy`
- `ControlNetApplyAdvanced` ★核心
- `UNETLoader` ★核心
- `UnetLoaderGGUF` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `easy imageSize`
- `DualCLIPLoader`
- `DualCLIPLoaderGGUF`
- `Florence2Run`
- `easy showAnything`
- `ControlNetLoader`
- `FluxGuidance`
- `VAELoader`
- `Note`
- `SimpleMathBoolean+`
- `DownloadAndLoadFlorence2Lora`
- `DownloadAndLoadFlorence2Model`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `953999074754702`
- `steps` = `28`
- `cfg` = `1`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `controlnet_strength` = `0.6`

## 知识

覆盖率 **86%**（30/35）

**有卡**：`VAEEncode`、`CLIPTextEncode`、`easy imageSize`、`ReroutePrimitive|pysssss`、`CR Set Value On Boolean`、`KSampler`、`LoadImage`、`ImageScaleBy`、`ControlNetApplyAdvanced`、`UNETLoader`、`UnetLoaderGGUF`、`SaveImage`、`VAEDecode`、`DualCLIPLoader`、`DualCLIPLoaderGGUF`、`Florence2Run`、`ControlNetLoader`、`FluxGuidance`、`VAELoader`、`SimpleMathBoolean+`、`DownloadAndLoadFlorence2Lora`、`DownloadAndLoadFlorence2Model`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced、ControlNetLoader
