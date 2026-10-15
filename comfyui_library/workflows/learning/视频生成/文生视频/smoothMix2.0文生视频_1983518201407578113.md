---
key: 视频生成/文生视频/smoothMix2.0文生视频_1983518201407578113.json
name: smoothMix2.0文生视频_1983518201407578113
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/smoothMix2.0文生视频_1983518201407578113.json
hash: 12949b63bcd2427c
coverage: 0.717949
learned_at: 2026-10-15 22:47:31
nodes: [Note, Pick From Batch (mtb), Note, ImageScaleBy, ImageScaleBy, RIFE VFI, easy cleanGpuUsed, CLIPTextEncode, VHS_VideoCombine, Label (rgthree), Note, Label (rgthree), CLIPTextEncode, PreviewImage, Note, Note, WanImageToVideo, ModelSamplingSD3, Note, VHS_VideoCombine, SaveImage, ModelSamplingSD3, Power Lora Loader (rgthree), Power Lora Loader (rgthree), Seed (rgthree), KSamplerAdvanced, Note, Note, Note, mxSlider2D, KSamplerAdvanced, VAEDecode, easy cleanGpuUsed, VAELoader, CLIPLoader, Label (rgthree), PrimitiveStringMultiline, UNETLoader, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/文生视频/smoothMix2.0文生视频_1983518201407578113.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/smoothMix2.0文生视频_1983518201407578113.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `Note`
- `Pick From Batch (mtb)`
- `Note`
- `ImageScaleBy`
- `ImageScaleBy`
- `RIFE VFI`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `Label (rgthree)`
- `Note`
- `Label (rgthree)`
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `Note`
- `Note`
- `WanImageToVideo`
- `ModelSamplingSD3`
- `Note`
- `VHS_VideoCombine`
- `SaveImage`
- `ModelSamplingSD3`
- `Power Lora Loader (rgthree)`
- `Power Lora Loader (rgthree)`
- `Seed (rgthree)`
- `KSamplerAdvanced` ★核心
- `Note`
- `Note`
- `Note`
- `mxSlider2D`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `VAELoader`
- `CLIPLoader`
- `Label (rgthree)`
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **72%**（28/39）

**有卡**：`Pick From Batch (mtb)`、`ImageScaleBy`、`RIFE VFI`、`easy cleanGpuUsed`、`CLIPTextEncode`、`VHS_VideoCombine`、`Label (rgthree)`、`WanImageToVideo`、`ModelSamplingSD3`、`SaveImage`、`Power Lora Loader (rgthree)`、`Seed (rgthree)`、`KSamplerAdvanced`、`mxSlider2D`、`VAEDecode`、`VAELoader`、`CLIPLoader`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Seed (rgthree)、Power Lora Loader (rgthree)
