---
key: 图片生成/图生图/【遇见AI】SD1.5基础图生图工作流_2011358352109998082.json
name: 【遇见AI】SD1.5基础图生图工作流_2011358352109998082
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/【遇见AI】SD1.5基础图生图工作流_2011358352109998082.json
hash: f11dc8abcd56838f
coverage: 1
learned_at: 2026-10-23 11:52:10
nodes: [VAEDecode, CLIPTextEncode, KSampler, VAEEncode, SaveImage, CheckpointLoaderSimple, LoadImage, CLIPTextEncode]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 8, "checkpoint": "1.5D-majicMIX realistic 麦橘写实_v7.safetensors", "denoise": 0.6, "sampler_name": "euler", "scheduler": "normal", "seed": 1032865448705234, "steps": 20}
---

# 图片生成/图生图/【遇见AI】SD1.5基础图生图工作流_2011358352109998082.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/【遇见AI】SD1.5基础图生图工作流_2011358352109998082.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Output → Other

**节点**（8 个）：
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEEncode` ★核心
- `SaveImage`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1032865448705234`
- `steps` = `20`
- `cfg` = `8`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `0.6`
- `checkpoint` = `1.5D-majicMIX realistic 麦橘写实_v7.safetensors`

## 知识

覆盖率 **100%**（8/8）

**有卡**：`VAEDecode`、`CLIPTextEncode`、`KSampler`、`VAEEncode`、`SaveImage`、`CheckpointLoaderSimple`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、VAEEncode、SaveImage、sd15-t2i-basic
