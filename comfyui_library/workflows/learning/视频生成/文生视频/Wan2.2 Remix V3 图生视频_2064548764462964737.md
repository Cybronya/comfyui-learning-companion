---
key: 视频生成/文生视频/Wan2.2 Remix V3 图生视频_2064548764462964737.json
name: Wan2.2 Remix V3 图生视频_2064548764462964737
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 Remix V3 图生视频_2064548764462964737.json
hash: 664c445b118b54e2
coverage: 0.828571
learned_at: 2026-10-11 20:21:31
nodes: [ModelSamplingSD3, LoraLoaderModelOnly, PathchSageAttentionKJ, ModelSamplingSD3, ModelPatchTorchSettings, PathchSageAttentionKJ, ModelPatchTorchSettings, KSamplerAdvanced, VAELoader, LoraLoaderModelOnly, CLIPLoader, KSamplerAdvanced, CLIPVisionLoader, VAEDecode, CLIPVisionEncode, WanImageToVideo, CLIPTextEncode, SimpleMath+, INTConstant, ImageScaleBy, UNETLoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, VHS_VideoCombine, RIFE VFI, easy cleanGpuUsed, VHS_VideoCombine, Wan22PromptSelector, Text Concatenate, INTConstant, LoadImage, CR Text]
patterns: []
missing: [CR Text, LayerUtility: ImageScaleByAspectRatio V2, RIFE VFI, SimpleMath+, Text Concatenate, easy cleanGpuUsed]
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/Wan2.2 Remix V3 图生视频_2064548764462964737.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 Remix V3 图生视频_2064548764462964737.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（35 个）：
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `KSamplerAdvanced` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `CLIPVisionLoader`
- `VAEDecode` ★核心
- `CLIPVisionEncode`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `INTConstant`
- `ImageScaleBy`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `RIFE VFI`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `Wan22PromptSelector`
- `Text Concatenate`
- `INTConstant`
- `LoadImage`
- `CR Text`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **83%**（29/35）

**有卡**：`ModelSamplingSD3`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`KSamplerAdvanced`、`VAELoader`、`CLIPLoader`、`CLIPVisionLoader`、`VAEDecode`、`CLIPVisionEncode`、`WanImageToVideo`、`CLIPTextEncode`、`INTConstant`、`ImageScaleBy`、`UNETLoader`、`VHS_VideoCombine`、`Wan22PromptSelector`、`LoadImage`

**缺卡**（6）：`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`RIFE VFI`、`SimpleMath+`、`Text Concatenate`、`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
