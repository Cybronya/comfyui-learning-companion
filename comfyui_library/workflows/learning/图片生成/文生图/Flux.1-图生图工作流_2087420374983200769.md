---
key: 图片生成/文生图/Flux.1-图生图工作流_2087420374983200769.json
name: Flux.1-图生图工作流_2087420374983200769
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux.1-图生图工作流_2087420374983200769.json
hash: 618a1f74e739c00b
coverage: 1
learned_at: 2026-10-20 00:58:44
nodes: [VAEDecode, SaveImage, CLIPTextEncode, CLIPTextEncode, UNETLoader, DualCLIPLoader, VAEEncode, VAELoader, ImageScale, KSampler, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 97800816302235, "steps": 20}
---

# 图片生成/文生图/Flux.1-图生图工作流_2087420374983200769.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Flux.1-图生图工作流_2087420374983200769.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（11 个）：
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAEEncode` ★核心
- `VAELoader`
- `ImageScale`
- `KSampler` ★核心
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `97800816302235`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`UNETLoader`、`DualCLIPLoader`、`VAEEncode`、`VAELoader`、`ImageScale`、`KSampler`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、VAEEncode、SaveImage
