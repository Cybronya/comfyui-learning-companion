---
key: 视频生成/文生视频/Wan2.2 Smooth + Qwen3 VL反推扩写图生视频V2_1982707054148231169.json
name: Wan2.2 Smooth + Qwen3 VL反推扩写图生视频V2_1982707054148231169
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 Smooth + Qwen3 VL反推扩写图生视频V2_1982707054148231169.json
hash: b75c5fa58e62314e
coverage: 0.534483
learned_at: 2026-10-11 02:45:02
nodes: [UnetLoaderGGUF, UnetLoaderGGUF, Note, Note, Note, CLIPTextEncode, ImageResizeKJv2, CLIPVisionEncode, ModelSamplingSD3, Note, VAELoader, Seed (rgthree), WanImageToVideo, Note, Note, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, Note, UNETLoader, ModelSamplingSD3, CLIPVisionLoader, KSamplerAdvanced, easy showAnything, CLIPLoader, KSamplerAdvanced, Pick From Batch (mtb), easy cleanGpuUsed, VAEDecode, ImageScaleBy, Note, LoadImage, VHS_SelectFilename, VHS_VideoCombine, easy showAnything, Any To Any, LayerUtility: ImageScaleByAspectRatio V2, easy showAnything, Note, Note, CLIPTextEncode, easy cleanGpuUsed, TT_img_enc, TT_img_enc_v2, SaveImage, SaveImage, Note, CR Prompt Text, CR Prompt Text, CR Prompt Text, JWInteger, Text Concatenate, CR Prompt Text, VHS_VideoCombine, JWInteger, Qwen3_VQA, Text Concatenate, easy showAnything]
patterns: []
missing: [Any To Any, LayerUtility: ImageScaleByAspectRatio V2, Pick From Batch (mtb), Text Concatenate, Text Concatenate, easy cleanGpuUsed, easy cleanGpuUsed, CR Prompt Text, CR Prompt Text, CR Prompt Text, CR Prompt Text, Seed (rgthree)]
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
discoveries: [次要节点 `Any To Any` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `Pick From Batch (mtb)` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Wan2.2 Smooth + Qwen3 VL反推扩写图生视频V2_1982707054148231169.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 Smooth + Qwen3 VL反推扩写图生视频V2_1982707054148231169.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `UnetLoaderGGUF` ★核心
- `UnetLoaderGGUF` ★核心
- `Note`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `CLIPVisionEncode`
- `ModelSamplingSD3`
- `Note`
- `VAELoader`
- `Seed (rgthree)`
- `WanImageToVideo`
- `Note`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `CLIPVisionLoader`
- `KSamplerAdvanced` ★核心
- `easy showAnything`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `Pick From Batch (mtb)`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `ImageScaleBy`
- `Note`
- `LoadImage`
- `VHS_SelectFilename`
- `VHS_VideoCombine`
- `easy showAnything`
- `Any To Any`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy showAnything`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `TT_img_enc`
- `TT_img_enc_v2`
- `SaveImage`
- `SaveImage`
- `Note`
- `CR Prompt Text`
- `CR Prompt Text`
- `CR Prompt Text`
- `JWInteger`
- `Text Concatenate`
- `CR Prompt Text`
- `VHS_VideoCombine`
- `JWInteger`
- `Qwen3_VQA`
- `Text Concatenate`
- `easy showAnything`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **53%**（31/58）

**有卡**：`UnetLoaderGGUF`、`CLIPTextEncode`、`ImageResizeKJv2`、`CLIPVisionEncode`、`ModelSamplingSD3`、`VAELoader`、`WanImageToVideo`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPVisionLoader`、`KSamplerAdvanced`、`CLIPLoader`、`VAEDecode`、`ImageScaleBy`、`LoadImage`、`VHS_SelectFilename`、`VHS_VideoCombine`、`TT_img_enc`、`TT_img_enc_v2`、`SaveImage`、`JWInteger`、`Qwen3_VQA`

**缺卡**（12）：`Any To Any`、`LayerUtility: ImageScaleByAspectRatio V2`、`Pick From Batch (mtb)`、`Text Concatenate`、`Text Concatenate`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`、`Seed (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

## 学习发现

- 次要节点 `Any To Any` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `Pick From Batch (mtb)` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
