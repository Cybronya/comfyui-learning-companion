---
key: 图片生成/文生图/wan2.2高低频双采样文生图工作流（自动提示词）V3_1950782044102119425.json
name: wan2.2高低频双采样文生图工作流（自动提示词）V3_1950782044102119425
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/wan2.2高低频双采样文生图工作流（自动提示词）V3_1950782044102119425.json
hash: 981c690097312bcd
coverage: 0.771429
learned_at: 2026-10-10 20:59:27
nodes: [LoraLoaderModelOnly, UNETLoader, UNETLoader, LoraLoaderModelOnly, CFGZeroStarAndInit, PathchSageAttentionKJ, PathchSageAttentionKJ, KSamplerAdvanced, ModelSamplingSD3, KSamplerAdvanced, ModelSamplingSD3, KSamplerAdvanced, VAELoader, VAEDecode, VAEDecode, EmptyHunyuanLatentVideo, ImpactInt, ImpactInt, ShowText|pysssss, Wan_video_prompt_generator, RH_LLMAPI_NODE, CLIPTextEncode, CLIPTextEncode, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, CR Text Concatenate, CR Text, ShowText|pysssss, easy showAnything, PreviewImage, SaveImage, Text Multiline, SaveImage, CR Simple Image Compare]
patterns: []
missing: [CR Simple Image Compare, CR Text, CR Text Concatenate, Text Multiline]
parameters: {"cfg": 10, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `CR Simple Image Compare` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/wan2.2高低频双采样文生图工作流（自动提示词）V3_1950782044102119425.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/wan2.2高低频双采样文生图工作流（自动提示词）V3_1950782044102119425.json`

## 结构

**节点**（35 个）：
- `LoraLoaderModelOnly`
- `UNETLoader`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `CFGZeroStarAndInit`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `KSamplerAdvanced`
- `VAELoader`
- `VAEDecode`
- `VAEDecode`
- `EmptyHunyuanLatentVideo`
- `ImpactInt`
- `ImpactInt`
- `ShowText|pysssss`
- `Wan_video_prompt_generator`
- `RH_LLMAPI_NODE`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `CLIPLoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `CR Text Concatenate`
- `CR Text`
- `ShowText|pysssss`
- `easy showAnything`
- `PreviewImage`
- `SaveImage`
- `Text Multiline`
- `SaveImage`
- `CR Simple Image Compare`

## 关键参数

- `cfg` = `10`
- `denoise` = `simple`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `seed` = `disable`
- `steps` = `fixed`

## 知识

覆盖率 **77%**（27/35）

**有卡**：`LoraLoaderModelOnly`、`UNETLoader`、`CFGZeroStarAndInit`、`PathchSageAttentionKJ`、`KSamplerAdvanced`、`ModelSamplingSD3`、`VAELoader`、`VAEDecode`、`EmptyHunyuanLatentVideo`、`ImpactInt`、`ShowText|pysssss`、`Wan_video_prompt_generator`、`RH_LLMAPI_NODE`、`CLIPTextEncode`、`CLIPLoader`、`CR Text Concatenate`

**缺卡**（4）：`CR Simple Image Compare`、`CR Text`、`CR Text Concatenate`、`Text Multiline`

## 学习发现

- 次要节点 `CR Simple Image Compare` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
