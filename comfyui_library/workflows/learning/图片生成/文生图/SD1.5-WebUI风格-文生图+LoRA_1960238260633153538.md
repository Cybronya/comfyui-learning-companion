---
key: 图片生成/文生图/SD1.5-WebUI风格-文生图+LoRA_1960238260633153538.json
name: SD1.5-WebUI风格-文生图+LoRA_1960238260633153538.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/SD1.5-WebUI风格-文生图+LoRA_1960238260633153538.json
hash: 9fb8b5e94d0649d8
coverage: 1
learned_at: 2026-10-07 23:38:24
nodes: [SaveImage, VAEDecode, CheckpointLoaderSimple, LoraLoader, EmptyLatentImage, KSampler, BNK_CLIPTextEncodeAdvanced, BNK_CLIPTextEncodeAdvanced]
patterns: [lora]
missing: []
parameters: {"batch_size": 1, "cfg": 7, "checkpoint": "光影驿站画心绘影_V2.safetensors", "denoise": 1, "height": 1152, "lora_name": "songyu.safetensors", "sampler_name": "dpmpp_sde_gpu", "scheduler": "karras", "seed": 427693811755520, "steps": 25, "strength_clip": 1, "strength_model": 1.0000000000000002, "width": 768}
---

# 图片生成/文生图/SD1.5-WebUI风格-文生图+LoRA_1960238260633153538.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1960238260633153538.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output

**节点**（8 个）：
- `SaveImage`
- `VAEDecode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoraLoader` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `BNK_CLIPTextEncodeAdvanced` ★核心
- `BNK_CLIPTextEncodeAdvanced` ★核心

**识别到的模式**：lora

## 关键参数

- `checkpoint` = `光影驿站画心绘影_V2.safetensors`
- `lora_name` = `songyu.safetensors`
- `strength_model` = `1.0000000000000002`
- `strength_clip` = `1`
- `width` = `768`
- `height` = `1152`
- `batch_size` = `1`
- `seed` = `427693811755520`
- `steps` = `25`
- `cfg` = `7`
- `sampler_name` = `dpmpp_sde_gpu`
- `scheduler` = `karras`
- `denoise` = `1`

## 知识

覆盖率 **100%**（8/8）

**有卡**：`SaveImage`、`VAEDecode`、`CheckpointLoaderSimple`、`LoraLoader`、`EmptyLatentImage`、`KSampler`、`BNK_CLIPTextEncodeAdvanced`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、EmptyLatentImage、BNK_CLIPTextEncodeAdvanced、LoraLoader、LoraLoader、SaveImage
