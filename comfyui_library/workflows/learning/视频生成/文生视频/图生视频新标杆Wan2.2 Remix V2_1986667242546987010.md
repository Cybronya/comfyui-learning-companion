---
key: 视频生成/文生视频/图生视频新标杆Wan2.2 Remix V2_1986667242546987010.json
name: 图生视频新标杆Wan2.2 Remix V2_1986667242546987010
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/图生视频新标杆Wan2.2 Remix V2_1986667242546987010.json
hash: a6520f3570a567a3
coverage: 0.657143
learned_at: 2026-10-11 02:45:04
nodes: [CR Prompt Text, CR Prompt Text, JWInteger, JWInteger, VHS_VideoCombine, CR Prompt Text, Qwen3_VQA, VHS_SelectFilename, Any To Any, easy showAnything, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, easy cleanGpuUsed, UNETLoader, VAELoader, easy showAnything, ImageResizeKJv2, easy cleanGpuUsed, Text Concatenate, LoadImage, Text Concatenate, CLIPVisionLoader, UNETLoader, CLIPTextEncode, CLIPTextEncode, ImageScaleBy, WanImageToVideo, Seed (rgthree), CLIPVisionEncode, KSamplerAdvanced, KSamplerAdvanced, ModelSamplingSD3, ModelSamplingSD3, VHS_VideoCombine, CLIPLoader]
patterns: []
missing: [Any To Any, LayerUtility: ImageScaleByAspectRatio V2, Text Concatenate, Text Concatenate, easy cleanGpuUsed, easy cleanGpuUsed, CR Prompt Text, CR Prompt Text, CR Prompt Text, Seed (rgthree)]
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `Any To Any` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/图生视频新标杆Wan2.2 Remix V2_1986667242546987010.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/图生视频新标杆Wan2.2 Remix V2_1986667242546987010.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（35 个）：
- `CR Prompt Text`
- `CR Prompt Text`
- `JWInteger`
- `JWInteger`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `Qwen3_VQA`
- `VHS_SelectFilename`
- `Any To Any`
- `easy showAnything`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `VAELoader`
- `easy showAnything`
- `ImageResizeKJv2`
- `easy cleanGpuUsed`
- `Text Concatenate`
- `LoadImage`
- `Text Concatenate`
- `CLIPVisionLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageScaleBy`
- `WanImageToVideo`
- `Seed (rgthree)`
- `CLIPVisionEncode`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VHS_VideoCombine`
- `CLIPLoader`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **66%**（23/35）

**有卡**：`JWInteger`、`VHS_VideoCombine`、`Qwen3_VQA`、`VHS_SelectFilename`、`VAEDecode`、`UNETLoader`、`VAELoader`、`ImageResizeKJv2`、`LoadImage`、`CLIPVisionLoader`、`CLIPTextEncode`、`ImageScaleBy`、`WanImageToVideo`、`CLIPVisionEncode`、`KSamplerAdvanced`、`ModelSamplingSD3`、`CLIPLoader`

**缺卡**（10）：`Any To Any`、`LayerUtility: ImageScaleByAspectRatio V2`、`Text Concatenate`、`Text Concatenate`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`Seed (rgthree)`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode

## 学习发现

- 次要节点 `Any To Any` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
