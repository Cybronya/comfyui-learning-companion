---
key: 图片生成/图生图/【上新】Flux+depth+lora+example_1860177783379947522.json
name: 【上新】Flux+depth+lora+example_1860177783379947522
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【上新】Flux+depth+lora+example_1860177783379947522.json
hash: 722fc50f819c1d25
coverage: 0.85
learned_at: 2026-10-23 11:49:16
nodes: [Label (rgthree), Label (rgthree), KSampler, FluxGuidance, VAELoader, DualCLIPLoader, InstructPixToPixConditioning, LoraLoaderModelOnly, CLIPTextEncode, SaveImage, VAEDecode, CLIPTextEncode, DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, PreviewImage, RH_Captioner, ShowText|pysssss, PreviewImage, LoadImage, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 766806618276646, "steps": 20}
---

# 图片生成/图生图/【上新】Flux+depth+lora+example_1860177783379947522.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【上新】Flux+depth+lora+example_1860177783379947522.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（20 个）：
- `Label (rgthree)`
- `Label (rgthree)`
- `KSampler` ★核心
- `FluxGuidance`
- `VAELoader`
- `DualCLIPLoader`
- `InstructPixToPixConditioning`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `PreviewImage`
- `RH_Captioner`
- `ShowText|pysssss`
- `PreviewImage`
- `LoadImage`
- `UNETLoader` ★核心

## 关键参数

- `seed` = `766806618276646`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`Label (rgthree)`、`KSampler`、`FluxGuidance`、`VAELoader`、`DualCLIPLoader`、`InstructPixToPixConditioning`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`SaveImage`、`VAEDecode`、`DepthAnything_V2`、`DownloadAndLoadDepthAnythingV2Model`、`RH_Captioner`、`LoadImage`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、LoadImage、DepthAnything_V2
