---
key: 图片生成/文生图/wan2.2文生图_图生图超真实工作流（高射炮打蚊子系列五）_1950505463844687874.json
name: wan2.2文生图_图生图超真实工作流（高射炮打蚊子系列五）_1950505463844687874
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2文生图_图生图超真实工作流（高射炮打蚊子系列五）_1950505463844687874.json
hash: 511da7bc4206ebf5
coverage: 0.731707
learned_at: 2026-10-10 20:59:27
nodes: [CLIPLoader, CLIPTextEncode, Text Concatenate, CLIPTextEncode, UNETLoader, PathchSageAttentionKJ, EmptyHunyuanLatentVideo, VAEEncode, CR Simple Image Compare, Primitive integer [Crystools], Primitive integer [Crystools], Note, Primitive integer [Crystools], Note, Text Multiline, RH_Captioner, PathchSageAttentionKJ, KSamplerAdvanced, ImageScaleDownToSize, VAELoader, SaveImage, VAEDecode, LoraLoaderModelOnly, easy anythingIndexSwitch, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecode, easy anythingIndexSwitch, easy showAnything, GetImageSizeAndCount, LoadImage, SaveImage]
patterns: []
missing: [CR Simple Image Compare, Primitive integer [Crystools], Primitive integer [Crystools], Primitive integer [Crystools], Text Concatenate, Text Multiline, easy anythingIndexSwitch, easy anythingIndexSwitch]
parameters: {"cfg": 12, "denoise": "bong_tangent", "sampler_name": 1, "scheduler": "res_2s", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `CR Simple Image Compare` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识, 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/wan2.2文生图_图生图超真实工作流（高射炮打蚊子系列五）_1950505463844687874.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2文生图_图生图超真实工作流（高射炮打蚊子系列五）_1950505463844687874.json`

## 结构

**节点**（41 个）：
- `CLIPLoader`
- `CLIPTextEncode`
- `Text Concatenate`
- `CLIPTextEncode`
- `UNETLoader`
- `PathchSageAttentionKJ`
- `EmptyHunyuanLatentVideo`
- `VAEEncode`
- `CR Simple Image Compare`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Note`
- `Primitive integer [Crystools]`
- `Note`
- `Text Multiline`
- `RH_Captioner`
- `PathchSageAttentionKJ`
- `KSamplerAdvanced`
- `ImageScaleDownToSize`
- `VAELoader`
- `SaveImage`
- `VAEDecode`
- `LoraLoaderModelOnly`
- `easy anythingIndexSwitch`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `VAEDecode`
- `easy anythingIndexSwitch`
- `easy showAnything`
- `GetImageSizeAndCount`
- `LoadImage`
- `SaveImage`

## 关键参数

- `cfg` = `12`
- `denoise` = `bong_tangent`
- `sampler_name` = `1`
- `scheduler` = `res_2s`
- `seed` = `disable`
- `steps` = `fixed`

## 知识

覆盖率 **73%**（30/41）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`Text Concatenate`、`UNETLoader`、`PathchSageAttentionKJ`、`EmptyHunyuanLatentVideo`、`VAEEncode`、`CR Simple Image Compare`、`Primitive integer [Crystools]`、`Note`、`Text Multiline`、`RH_Captioner`、`KSamplerAdvanced`、`ImageScaleDownToSize`、`VAELoader`、`SaveImage`、`VAEDecode`、`LoraLoaderModelOnly`、`easy anythingIndexSwitch`、`ModelSamplingSD3`

**缺卡**（8）：`CR Simple Image Compare`、`Primitive integer [Crystools]`、`Primitive integer [Crystools]`、`Primitive integer [Crystools]`、`Text Concatenate`、`Text Multiline`、`easy anythingIndexSwitch`、`easy anythingIndexSwitch`

## 学习发现

- 次要节点 `CR Simple Image Compare` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy anythingIndexSwitch` 知识库中没有该节点类型的任何知识
