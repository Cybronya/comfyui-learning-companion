---
key: 图片生成/图生图/【遇见AI】stable cascade inpaint重绘_2033462703301337089.json
name: 【遇见AI】stable cascade inpaint重绘_2033462703301337089
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】stable cascade inpaint重绘_2033462703301337089.json
hash: aac1dfd3b9881f86
coverage: 1
learned_at: 2026-10-23 11:52:20
nodes: [CLIPTextEncode, StableCascade_StageB_Conditioning, VAEDecode, workflow>StableCascadeInpaintCnet, LoadImage, ControlNetApplyAdvanced, CheckpointLoaderSimple, CheckpointLoaderSimple, ControlNetLoader, StableCascade_EmptyLatentImage, CLIPTextEncode, KSampler, KSampler, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 42, "cfg": 1.1, "checkpoint": "stable_cascade_stage_b.safetensors", "controlnet_strength": 1, "denoise": 1, "height": 1024, "sampler_name": "euler_ancestral", "scheduler": "simple", "seed": 986665208911565, "steps": 10, "width": 1024}
---

# 图片生成/图生图/【遇见AI】stable cascade inpaint重绘_2033462703301337089.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】stable cascade inpaint重绘_2033462703301337089.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `CLIPTextEncode` ★核心
- `StableCascade_StageB_Conditioning`
- `VAEDecode` ★核心
- `workflow>StableCascadeInpaintCnet`
- `LoadImage`
- `ControlNetApplyAdvanced` ★核心
- `CheckpointLoaderSimple` ★核心
- `CheckpointLoaderSimple` ★核心
- `ControlNetLoader`
- `StableCascade_EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `SaveImage`

## 关键参数

- `controlnet_strength` = `1`
- `checkpoint` = `stable_cascade_stage_b.safetensors`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `42`
- `seed` = `986665208911565`
- `steps` = `10`
- `cfg` = `1.1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`CLIPTextEncode`、`StableCascade_StageB_Conditioning`、`VAEDecode`、`workflow>StableCascadeInpaintCnet`、`LoadImage`、`ControlNetApplyAdvanced`、`CheckpointLoaderSimple`、`ControlNetLoader`、`StableCascade_EmptyLatentImage`、`KSampler`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced、ControlNetLoader、StableCascade_EmptyLatentImage
