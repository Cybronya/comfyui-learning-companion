---
key: 视频生成/图生视频/Wan2.2 Remix i2v 2.1 图生视频VBVR逻辑推理强化工作流_2027033853302411266.json
name: Wan2.2 Remix i2v 2.1 图生视频VBVR逻辑推理强化工作流_2027033853302411266.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2027033853302411266.json
hash: 04321858d74849c6
coverage: 0.764706
learned_at: 2026-10-15 22:35:16
nodes: [INTConstant, ModelSamplingSD3, INTConstant, ModelSamplingSD3, WanImageToVideo, INTConstant, CLIPTextEncode, KSamplerAdvanced, INTConstant, Seed (rgthree), INTConstant, LoadImage, ImageResize+, SetNode, Note, VHS_VideoCombine, CLIPTextEncode, UNETLoader, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, VAEDecode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, KSamplerAdvanced, ShowText|pysssss, llama_cpp_model_loader, GetNode, JjkText, llama_cpp_instruct_adv, SetNode, GetNode, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 12, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2 Remix i2v 2.1 图生视频VBVR逻辑推理强化工作流_2027033853302411266.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2027033853302411266.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（34 个）：
- `INTConstant`
- `ModelSamplingSD3`
- `INTConstant`
- `ModelSamplingSD3`
- `WanImageToVideo`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `Seed (rgthree)`
- `INTConstant`
- `LoadImage`
- `ImageResize+`
- `SetNode`
- `Note`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `KSamplerAdvanced` ★核心
- `ShowText|pysssss`
- `llama_cpp_model_loader`
- `GetNode`
- `JjkText`
- `llama_cpp_instruct_adv`
- `SetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `12`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **76%**（26/34）

**有卡**：`INTConstant`、`ModelSamplingSD3`、`WanImageToVideo`、`CLIPTextEncode`、`KSamplerAdvanced`、`Seed (rgthree)`、`LoadImage`、`ImageResize+`、`VHS_VideoCombine`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`llama_cpp_model_loader`、`llama_cpp_instruct_adv`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
