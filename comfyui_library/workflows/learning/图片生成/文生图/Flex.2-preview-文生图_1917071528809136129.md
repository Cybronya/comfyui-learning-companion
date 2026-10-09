---
key: 图片生成/文生图/Flex.2-preview-文生图_1917071528809136129.json
name: Flex.2-preview-文生图_1917071528809136129.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flex.2-preview-文生图_1917071528809136129.json
hash: 91b7ecb1545be558
coverage: 0.909091
learned_at: 2026-10-07 22:07:54
nodes: [DualCLIPLoader, VAELoader, UNETLoader, LoraLoaderModelOnly, CLIPTextEncode, Flex2Conditioner, KSampler, VAEDecode, SaveImage, CLIPTextEncode, SDXLEmptyLatentSizePicker+]
patterns: []
missing: [SDXLEmptyLatentSizePicker+]
parameters: {"batch_size": 0, "cfg": 1, "denoise": 1, "height": 1, "sampler_name": "deis", "scheduler": "beta", "seed": 1069316588336707, "steps": 25, "width": "768x1280 (0.6)"}
discoveries: [核心节点 `SDXLEmptyLatentSizePicker+` 仅有 VAE/Checkpoint/Resolution 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/Flex.2-preview-文生图_1917071528809136129.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1917071528809136129.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（11 个）：
- `DualCLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Flex2Conditioner`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `SDXLEmptyLatentSizePicker+` ★核心

## 关键参数

- `seed` = `1069316588336707`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `deis`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `768x1280 (0.6)`
- `height` = `1`
- `batch_size` = `0`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`DualCLIPLoader`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`Flex2Conditioner`、`KSampler`、`VAEDecode`、`SaveImage`

**缺卡**（1）：`SDXLEmptyLatentSizePicker+`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、DualCLIPLoader、SaveImage

## 学习发现

- 核心节点 `SDXLEmptyLatentSizePicker+` 仅有 VAE/Checkpoint/Resolution 的通用知识，没有该节点自己的说明
