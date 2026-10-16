---
key: 视频生成/图生视频/DaSiWa8.1-Wan2.2双图参考首尾帧AI漫剧_2010412985205923842.json
name: DaSiWa8.1-Wan2.2双图参考首尾帧AI漫剧_2010412985205923842.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2010412985205923842.json
hash: 63e65fffa57bf91e
coverage: 0.896552
learned_at: 2026-10-15 22:34:16
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, ModelSamplingSD3, ModelSamplingSD3, CLIPLoader, VAELoader, UNETLoader, UNETLoader, CLIPTextEncode, Int, PrimitiveString, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, VAEDecode, easy cleanGpuUsed, PainterI2V, KSamplerAdvanced, KSamplerAdvanced, SimpleMath+, LoadImage, VHS_VideoCombine, ImageConcatMulti, CR Text, Note, RHHiddenNodes, easy showAnything, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/DaSiWa8.1-Wan2.2双图参考首尾帧AI漫剧_2010412985205923842.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2010412985205923842.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（29 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `Int`
- `PrimitiveString`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `PainterI2V`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SimpleMath+`
- `LoadImage`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `CR Text`
- `Note`
- `RHHiddenNodes`
- `easy showAnything`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `6`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`CLIPTextEncode`、`Int`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`easy cleanGpuUsed`、`PainterI2V`、`KSamplerAdvanced`、`SimpleMath+`、`LoadImage`、`VHS_VideoCombine`、`ImageConcatMulti`、`CR Text`、`RHHiddenNodes`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、ImageConcatMulti
