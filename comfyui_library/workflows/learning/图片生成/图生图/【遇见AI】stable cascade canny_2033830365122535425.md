---
key: 图片生成/图生图/【遇见AI】stable cascade canny_2033830365122535425.json
name: 【遇见AI】stable cascade canny_2033830365122535425
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】stable cascade canny_2033830365122535425.json
hash: 52d2bec482e91330
coverage: 0.736842
learned_at: 2026-10-23 11:52:19
nodes: [KSampler, CheckpointLoaderSimple, CLIPTextEncode, Canny, LoadImage, PreviewImage, StableCascade_EmptyLatentImage, CheckpointLoaderSimple, StableCascade_StageB_Conditioning, Note, Note, Note, Note, VAEDecode, SaveImage, KSampler, CLIPTextEncode, ControlNetApplyAdvanced, ControlNetLoader]
patterns: []
missing: []
parameters: {"batch_size": 42, "cfg": 1.1, "checkpoint": "stable_cascade_stage_b.safetensors", "controlnet_strength": 1, "denoise": 1, "height": 1536, "sampler_name": "euler_ancestral", "scheduler": "simple", "seed": 131911938926907, "steps": 10, "width": 1024}
---

# 图片生成/图生图/【遇见AI】stable cascade canny_2033830365122535425.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】stable cascade canny_2033830365122535425.json`

## 结构

**生成流程**：Model → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `Canny`
- `LoadImage`
- `PreviewImage`
- `StableCascade_EmptyLatentImage` ★核心
- `CheckpointLoaderSimple` ★核心
- `StableCascade_StageB_Conditioning`
- `Note`
- `Note`
- `Note`
- `Note`
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `ControlNetApplyAdvanced` ★核心
- `ControlNetLoader`

## 关键参数

- `seed` = `131911938926907`
- `steps` = `10`
- `cfg` = `1.1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `stable_cascade_stage_b.safetensors`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `42`
- `controlnet_strength` = `1`

## 知识

覆盖率 **74%**（14/19）

**有卡**：`KSampler`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`Canny`、`LoadImage`、`StableCascade_EmptyLatentImage`、`StableCascade_StageB_Conditioning`、`VAEDecode`、`SaveImage`、`ControlNetApplyAdvanced`、`ControlNetLoader`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ControlNetApplyAdvanced、ControlNetLoader、Canny
