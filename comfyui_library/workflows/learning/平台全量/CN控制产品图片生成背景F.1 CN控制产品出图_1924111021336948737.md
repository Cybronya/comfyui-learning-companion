---
key: 平台全量/CN控制产品图片生成背景F.1 CN控制产品出图_1924111021336948737.json
name: CN控制产品图片生成背景F.1 CN控制产品出图_1924111021336948737
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/CN控制产品图片生成背景F.1 CN控制产品出图_1924111021336948737.json
hash: 403bd1345ffa932b
coverage: 1
learned_at: 2026-11-14 00:22:02
nodes: [SaveImage, ControlNetApplyAdvanced, ControlNetLoader, AIO_Preprocessor, LoadImage, IPAdapterUnifiedLoader, LoadImage, IPAdapterAdvanced, ImageCompositeMasked, SaveImage, LoadImage, ImageToMask, LoadImage, VAEDecode, KSampler, ConditioningZeroOut, VAELoader, DualCLIPLoader, UNETLoader, EmptyLatentImage, CLIPTextEncodeFlux, LP-TranslateToEN]
patterns: []
missing: []
parameters: {"batch_size": 3, "cfg": 1, "controlnet_strength": 0.7500000000000001, "denoise": 1, "height": 1152, "sampler_name": "euler", "scheduler": "simple", "seed": 415004473017248, "steps": 22, "width": 768}
---

# 平台全量/CN控制产品图片生成背景F.1 CN控制产品出图_1924111021336948737.json

> 来源文件 `comfyui_library/workflows/平台全量/CN控制产品图片生成背景F.1 CN控制产品出图_1924111021336948737.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Output → Other

**节点**（22 个）：
- `SaveImage`
- `ControlNetApplyAdvanced` ★核心
- `ControlNetLoader`
- `AIO_Preprocessor`
- `LoadImage`
- `IPAdapterUnifiedLoader`
- `LoadImage`
- `IPAdapterAdvanced`
- `ImageCompositeMasked`
- `SaveImage`
- `LoadImage`
- `ImageToMask`
- `LoadImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ConditioningZeroOut`
- `VAELoader`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncodeFlux` ★核心
- `LP-TranslateToEN`

## 关键参数

- `controlnet_strength` = `0.7500000000000001`
- `seed` = `415004473017248`
- `steps` = `22`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `768`
- `height` = `1152`
- `batch_size` = `3`

## 知识

覆盖率 **100%**（22/22）

**有卡**：`SaveImage`、`ControlNetApplyAdvanced`、`ControlNetLoader`、`AIO_Preprocessor`、`LoadImage`、`IPAdapterUnifiedLoader`、`IPAdapterAdvanced`、`ImageCompositeMasked`、`ImageToMask`、`VAEDecode`、`KSampler`、`ConditioningZeroOut`、`VAELoader`、`DualCLIPLoader`、`UNETLoader`、`EmptyLatentImage`、`CLIPTextEncodeFlux`、`LP-TranslateToEN`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage、ControlNetApplyAdvanced
