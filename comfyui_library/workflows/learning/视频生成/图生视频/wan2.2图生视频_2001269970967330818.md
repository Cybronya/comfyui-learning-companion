---
key: 视频生成/图生视频/wan2.2图生视频_2001269970967330818.json
name: wan2.2图生视频_2001269970967330818.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2001269970967330818.json
hash: 5511b7be53cdb990
coverage: 0.638298
learned_at: 2026-10-15 22:33:45
nodes: [PathchSageAttentionKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, ModelPatchTorchSettings, Reroute, ModelSamplingSD3, VAEDecode, ModelSamplingSD3, WanImageToVideo, Qwen3_VQA, easy showAnything, Note, Int, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, CLIPTextEncode, CLIPLoader, UNETLoader, PreviewImage, easy cleanGpuUsed, RIFE VFI, VHS_VideoCombine, KSamplerAdvanced, UNETLoader, VHS_VideoCombine, SetNode, Note, SetNode, GetNode, Int, GetNode, Note, SetNode, INTConstant, GetNode, GetNode, Note, SetNode, INTConstant, GetNode, GetNode, ImageLoader]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2图生视频_2001269970967330818.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2001269970967330818.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `Reroute`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `WanImageToVideo`
- `Qwen3_VQA`
- `easy showAnything`
- `Note`
- `Int`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `PreviewImage`
- `easy cleanGpuUsed`
- `RIFE VFI`
- `VHS_VideoCombine`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `SetNode`
- `Note`
- `SetNode`
- `GetNode`
- `Int`
- `GetNode`
- `Note`
- `SetNode`
- `INTConstant`
- `GetNode`
- `GetNode`
- `Note`
- `SetNode`
- `INTConstant`
- `GetNode`
- `GetNode`
- `ImageLoader`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **64%**（30/47）

**有卡**：`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`ModelSamplingSD3`、`VAEDecode`、`WanImageToVideo`、`Qwen3_VQA`、`Int`、`VAELoader`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`CLIPLoader`、`UNETLoader`、`easy cleanGpuUsed`、`RIFE VFI`、`VHS_VideoCombine`、`INTConstant`、`ImageLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、KSamplerAdvanced、Int
