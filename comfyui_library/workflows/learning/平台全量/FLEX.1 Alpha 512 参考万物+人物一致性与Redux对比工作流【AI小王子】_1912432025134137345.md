---
key: 平台全量/FLEX.1 Alpha 512 参考万物+人物一致性与Redux对比工作流【AI小王子】_1912432025134137345.json
name: FLEX.1 Alpha 512 参考万物+人物一致性与Redux对比工作流【AI小王子】_1912432025134137345
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/FLEX.1 Alpha 512 参考万物+人物一致性与Redux对比工作流【AI小王子】_1912432025134137345.json
hash: 9fff41076a8570e4
coverage: 0.875
learned_at: 2026-11-14 00:24:28
nodes: [StyleModelApply, ConditioningZeroOut, VAEDecode, SaveImage, VAEDecode, Image Comparer (rgthree), Image Comparer (rgthree), SaveImage, SaveImage, AddLabel, AddLabel, AddLabel, ImageConcatMulti, PrimitiveNode, PrimitiveNode, VAEEncode, CLIPTextEncode, ImageResizeKJ, CLIPVisionEncode, StyleModelApply, CLIPVisionEncode, CLIPTextEncode, ConditioningZeroOut, KSampler, KSampler, LoadImage, CheckpointLoaderSimple, CLIPVisionLoader, StyleModelLoader, CheckpointLoaderSimple, CLIPVisionLoader, StyleModelLoader]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "checkpoint": "Flex.1-alpha.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 117048625273919, "steps": 20}
---

# 平台全量/FLEX.1 Alpha 512 参考万物+人物一致性与Redux对比工作流【AI小王子】_1912432025134137345.json

> 来源文件 `comfyui_library/workflows/平台全量/FLEX.1 Alpha 512 参考万物+人物一致性与Redux对比工作流【AI小王子】_1912432025134137345.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `StyleModelApply`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SaveImage`
- `AddLabel`
- `AddLabel`
- `AddLabel`
- `ImageConcatMulti`
- `PrimitiveNode`
- `PrimitiveNode`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageResizeKJ`
- `CLIPVisionEncode`
- `StyleModelApply`
- `CLIPVisionEncode`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `KSampler` ★核心
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `CLIPVisionLoader`
- `StyleModelLoader`
- `CheckpointLoaderSimple` ★核心
- `CLIPVisionLoader`
- `StyleModelLoader`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `117048625273919`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `Flex.1-alpha.safetensors`

## 知识

覆盖率 **88%**（28/32）

**有卡**：`StyleModelApply`、`ConditioningZeroOut`、`VAEDecode`、`SaveImage`、`AddLabel`、`ImageConcatMulti`、`VAEEncode`、`CLIPTextEncode`、`ImageResizeKJ`、`CLIPVisionEncode`、`KSampler`、`LoadImage`、`CheckpointLoaderSimple`、`CLIPVisionLoader`、`StyleModelLoader`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、LoadImage、CLIPVisionEncode、VAEEncode
