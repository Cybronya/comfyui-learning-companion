---
key: 视频生成/文生视频/smoothMix2.0文生视频_1983518201407578113.json
name: smoothMix2.0文生视频_1983518201407578113
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/smoothMix2.0文生视频_1983518201407578113.json
hash: 12949b63bcd2427c
coverage: 0.461538
learned_at: 2026-10-11 02:45:03
nodes: [Note, Pick From Batch (mtb), Note, ImageScaleBy, ImageScaleBy, RIFE VFI, easy cleanGpuUsed, CLIPTextEncode, VHS_VideoCombine, Label (rgthree), Note, Label (rgthree), CLIPTextEncode, PreviewImage, Note, Note, WanImageToVideo, ModelSamplingSD3, Note, VHS_VideoCombine, SaveImage, ModelSamplingSD3, Power Lora Loader (rgthree), Power Lora Loader (rgthree), Seed (rgthree), KSamplerAdvanced, Note, Note, Note, mxSlider2D, KSamplerAdvanced, VAEDecode, easy cleanGpuUsed, VAELoader, CLIPLoader, Label (rgthree), PrimitiveStringMultiline, UNETLoader, UNETLoader]
patterns: []
missing: [Label (rgthree), Label (rgthree), Label (rgthree), Pick From Batch (mtb), RIFE VFI, easy cleanGpuUsed, easy cleanGpuUsed, Power Lora Loader (rgthree), Power Lora Loader (rgthree), Seed (rgthree)]
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Pick From Batch (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明, 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
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

覆盖率 **46%**（18/39）

**有卡**：`ImageScaleBy`、`CLIPTextEncode`、`VHS_VideoCombine`、`WanImageToVideo`、`ModelSamplingSD3`、`SaveImage`、`KSamplerAdvanced`、`mxSlider2D`、`VAEDecode`、`VAELoader`、`CLIPLoader`、`UNETLoader`

**缺卡**（10）：`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Pick From Batch (mtb)`、`RIFE VFI`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`Power Lora Loader (rgthree)`、`Power Lora Loader (rgthree)`、`Seed (rgthree)`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、SaveImage、ImageScaleBy

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Pick From Batch (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
- 次要节点 `Power Lora Loader (rgthree)` 仅有 LoRA 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
