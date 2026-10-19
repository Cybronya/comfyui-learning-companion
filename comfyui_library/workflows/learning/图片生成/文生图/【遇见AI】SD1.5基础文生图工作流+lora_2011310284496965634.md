---
key: 图片生成/文生图/【遇见AI】SD1.5基础文生图工作流+lora_2011310284496965634.json
name: 【遇见AI】SD1.5基础文生图工作流+lora_2011310284496965634
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【遇见AI】SD1.5基础文生图工作流+lora_2011310284496965634.json
hash: 194cc42f0b26b3a2
coverage: 1
learned_at: 2026-10-19 22:01:21
nodes: [KSampler, VAEDecode, CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, CheckpointLoaderSimple, SaveImage, LoraLoader]
patterns: [text_to_image, lora]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "checkpoint": "1.5D-majicMIX realistic 麦橘写实_v7.safetensors", "denoise": 1, "height": 512, "lora_name": "xrs2.0.safetensors", "sampler_name": "euler", "scheduler": "normal", "seed": 149608884657966, "steps": 20, "strength_clip": 0.7000000000000002, "strength_model": 0.7000000000000002, "width": 512}
---

# 图片生成/文生图/【遇见AI】SD1.5基础文生图工作流+lora_2011310284496965634.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【遇见AI】SD1.5基础文生图工作流+lora_2011310284496965634.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output

**节点**（8 个）：
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `CheckpointLoaderSimple` ★核心
- `SaveImage`
- `LoraLoader` ★核心

**识别到的模式**：text_to_image、lora

## 关键参数

- `seed` = `149608884657966`
- `steps` = `20`
- `cfg` = `8`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `checkpoint` = `1.5D-majicMIX realistic 麦橘写实_v7.safetensors`
- `lora_name` = `xrs2.0.safetensors`
- `strength_model` = `0.7000000000000002`
- `strength_clip` = `0.7000000000000002`

## 知识

覆盖率 **100%**（8/8）

**有卡**：`KSampler`、`VAEDecode`、`CLIPTextEncode`、`EmptyLatentImage`、`CheckpointLoaderSimple`、`SaveImage`、`LoraLoader`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoraLoader、LoraLoader、SaveImage
