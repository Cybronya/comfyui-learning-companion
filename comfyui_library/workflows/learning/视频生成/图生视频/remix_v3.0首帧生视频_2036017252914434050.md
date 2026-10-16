---
key: 视频生成/图生视频/remix_v3.0首帧生视频_2036017252914434050.json
name: remix_v3.0首帧生视频_2036017252914434050.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2036017252914434050.json
hash: 0ff016eb487b77ec
coverage: 0.939394
learned_at: 2026-10-15 22:35:51
nodes: [ModelPatchTorchSettings, ModelPatchTorchSettings, PathchSageAttentionKJ, Note, CLIPTextEncode, SimpleMath+, INTConstant, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, FloatConstant, SimpleMath+, VAEDecode, CreateVideo, VAELoader, PathchSageAttentionKJ, LoadImage, KSamplerAdvanced, INTConstant, CM_IntToFloat, CLIPVisionLoader, CLIPVisionEncode, CLIPLoader, WanImageToVideo, LayerUtility: PurgeVRAM V2, Fast Groups Bypasser (rgthree), SaveVideo, ModelSamplingSD3, ModelSamplingSD3, KSamplerAdvanced, UNETLoader, UNETLoader, INTConstant]
patterns: []
missing: []
parameters: {"cfg": 4, "denoise": "simple", "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/remix_v3.0首帧生视频_2036017252914434050.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2036017252914434050.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `Note`
- `CLIPTextEncode` ★核心
- `SimpleMath+`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`
- `FloatConstant`
- `SimpleMath+`
- `VAEDecode` ★核心
- `CreateVideo`
- `VAELoader`
- `PathchSageAttentionKJ`
- `LoadImage`
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `CM_IntToFloat`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `CLIPLoader`
- `WanImageToVideo`
- `LayerUtility: PurgeVRAM V2`
- `Fast Groups Bypasser (rgthree)`
- `SaveVideo`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `INTConstant`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `4`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **94%**（31/33）

**有卡**：`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`SimpleMath+`、`INTConstant`、`LayerUtility: ImageScaleByAspectRatio V2`、`FloatConstant`、`VAEDecode`、`CreateVideo`、`VAELoader`、`LoadImage`、`KSamplerAdvanced`、`CM_IntToFloat`、`CLIPVisionLoader`、`CLIPVisionEncode`、`CLIPLoader`、`WanImageToVideo`、`LayerUtility: PurgeVRAM V2`、`SaveVideo`、`ModelSamplingSD3`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode
