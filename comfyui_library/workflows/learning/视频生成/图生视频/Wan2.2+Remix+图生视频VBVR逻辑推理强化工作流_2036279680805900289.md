---
key: 视频生成/图生视频/Wan2.2+Remix+图生视频VBVR逻辑推理强化工作流_2036279680805900289.json
name: Wan2.2+Remix+图生视频VBVR逻辑推理强化工作流_2036279680805900289.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2036279680805900289.json
hash: 48a3d418c64b7cd0
coverage: 0.727273
learned_at: 2026-10-15 22:35:51
nodes: [VAELoader, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, GetNode, SetNode, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelPatchTorchSettings, PathchSageAttentionKJ, PathchSageAttentionKJ, INTConstant, WanImageToVideo, CLIPTextEncode, INTConstant, UNETLoader, ModelSamplingSD3, ModelSamplingSD3, INTConstant, UNETLoader, LoadImage, INTConstant, Seed (rgthree), JjkText, Note, Note, ShowText|pysssss, SetNode, LayerUtility: PurgeVRAM, llama_cpp_model_loader, JjkText, GetNode, llama_cpp_instruct_adv, Switch any [Crystools], JjkText, JjkText, Fast Groups Bypasser (rgthree), KSamplerAdvanced, KSamplerAdvanced, LayerUtility: TextJoin, VAEDecode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "normal", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2+Remix+图生视频VBVR逻辑推理强化工作流_2036279680805900289.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2036279680805900289.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（44 个）：
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelPatchTorchSettings`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `INTConstant`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `INTConstant`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `INTConstant`
- `UNETLoader` ★核心
- `LoadImage`
- `INTConstant`
- `Seed (rgthree)`
- `JjkText`
- `Note`
- `Note`
- `ShowText|pysssss`
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `llama_cpp_model_loader`
- `JjkText`
- `GetNode`
- `llama_cpp_instruct_adv`
- `Switch any [Crystools]`
- `JjkText`
- `JjkText`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LayerUtility: TextJoin`
- `VAEDecode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `normal`

## 知识

覆盖率 **73%**（32/44）

**有卡**：`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPTextEncode`、`CLIPLoader`、`LoraLoaderModelOnly`、`ModelPatchTorchSettings`、`PathchSageAttentionKJ`、`INTConstant`、`WanImageToVideo`、`UNETLoader`、`ModelSamplingSD3`、`LoadImage`、`Seed (rgthree)`、`LayerUtility: PurgeVRAM`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`、`Switch any [Crystools]`、`KSamplerAdvanced`、`LayerUtility: TextJoin`、`VAEDecode`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
