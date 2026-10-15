---
key: 图片生成/文生图/Wan_2.1_文生图_1942908235353374722.json
name: Wan_2.1_文生图_1942908235353374722
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan_2.1_文生图_1942908235353374722.json
hash: 236259536ac74a81
coverage: 0.88
learned_at: 2026-10-15 22:27:37
nodes: [CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, SaveImage, easy clearCacheAll, easy cleanGpuUsed, VAELoader, ModelSamplingSD3, FastFilmGrain, VAEDecode, Label (rgthree), MarkdownNote, Label (rgthree), Label (rgthree), WanVideoNAG, Note, Label (rgthree), Label (rgthree), Note, LoraLoader, ModelPatchTorchSettings, CLIPTextEncode, UnetLoaderGGUF, CLIPLoader, PathchSageAttentionKJ]
patterns: [lora]
missing: []
parameters: {"cfg": 1, "denoise": 1, "lora_name": "Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors", "sampler_name": "euler", "scheduler": "beta", "seed": 664505851744406, "steps": 10, "strength_clip": 1, "strength_model": 1}
---

# 图片生成/文生图/Wan_2.1_文生图_1942908235353374722.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan_2.1_文生图_1942908235353374722.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（25 个）：
- `CLIPTextEncode` ★核心
- `EmptyHunyuanLatentVideo`
- `KSampler` ★核心
- `SaveImage`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `VAELoader`
- `ModelSamplingSD3`
- `FastFilmGrain`
- `VAEDecode` ★核心
- `Label (rgthree)`
- `MarkdownNote`
- `Label (rgthree)`
- `Label (rgthree)`
- `WanVideoNAG`
- `Note`
- `Label (rgthree)`
- `Label (rgthree)`
- `Note`
- `LoraLoader` ★核心
- `ModelPatchTorchSettings`
- `CLIPTextEncode` ★核心
- `UnetLoaderGGUF` ★核心
- `CLIPLoader`
- `PathchSageAttentionKJ`

**识别到的模式**：lora

## 关键参数

- `seed` = `664505851744406`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `lora_name` = `Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **88%**（22/25）

**有卡**：`CLIPTextEncode`、`EmptyHunyuanLatentVideo`、`KSampler`、`SaveImage`、`easy clearCacheAll`、`easy cleanGpuUsed`、`VAELoader`、`ModelSamplingSD3`、`FastFilmGrain`、`VAEDecode`、`Label (rgthree)`、`WanVideoNAG`、`LoraLoader`、`ModelPatchTorchSettings`、`UnetLoaderGGUF`、`CLIPLoader`、`PathchSageAttentionKJ`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyHunyuanLatentVideo、LoraLoader、LoraLoader
