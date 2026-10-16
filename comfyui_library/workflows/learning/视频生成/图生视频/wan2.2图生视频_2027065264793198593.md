---
key: 视频生成/图生视频/wan2.2图生视频_2027065264793198593.json
name: wan2.2图生视频_2027065264793198593.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2027065264793198593.json
hash: dc1366ccacf4bca7
coverage: 0.565217
learned_at: 2026-10-15 22:35:16
nodes: [ModelPatchTorchSettings, ModelPatchTorchSettings, ModelSamplingSD3, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, PathchSageAttentionKJ, PathchSageAttentionKJ, SetNode, UNETLoader, GetNode, GetNode, PreviewImage, SetNode, GetNode, GetNode, Note, Note, INTConstant, INTConstant, SetNode, SetNode, Note, SetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, VAEDecode, CLIPTextEncode, LoadImage, INTConstant, ModelSamplingSD3, Anything Everywhere, SetNode, VAELoader, CLIPLoader, easy cleanGpuUsed, VHS_VideoCombine, Reroute, Reroute, UNETLoader, PainterI2VAdvanced, GetNode, CR Text, LayerUtility: TextJoin, CR Text]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/wan2.2图生视频_2027065264793198593.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2027065264793198593.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（46 个）：
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `SetNode`
- `UNETLoader` ★核心
- `GetNode`
- `GetNode`
- `PreviewImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `Note`
- `Note`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `Note`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `INTConstant`
- `ModelSamplingSD3`
- `Anything Everywhere`
- `SetNode`
- `VAELoader`
- `CLIPLoader`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `Reroute`
- `Reroute`
- `UNETLoader` ★核心
- `PainterI2VAdvanced`
- `GetNode`
- `CR Text`
- `LayerUtility: TextJoin`
- `CR Text`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **57%**（26/46）

**有卡**：`ModelPatchTorchSettings`、`ModelSamplingSD3`、`KSamplerAdvanced`、`CLIPTextEncode`、`PathchSageAttentionKJ`、`UNETLoader`、`INTConstant`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`LoadImage`、`VAELoader`、`CLIPLoader`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`PainterI2VAdvanced`、`CR Text`、`LayerUtility: TextJoin`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、INTConstant
