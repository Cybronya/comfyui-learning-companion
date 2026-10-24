---
key: 图片生成/图生图/Wan2.1 图生图洗图+修复工作流_1945503532646637569.json
name: Wan2.1 图生图洗图+修复工作流_1945503532646637569
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.1 图生图洗图+修复工作流_1945503532646637569.json
hash: ac0e5c31e6ce809f
coverage: 1
learned_at: 2026-10-23 11:27:48
nodes: [ModelSamplingSD3, CLIPLoader, LayerUtility: PurgeVRAM, UNETLoader, CLIPTextEncode, CLIPTextEncode, KSampler, SaveImage, VAEDecode, ImageConcanate, VAELoader, VAEEncode, LoraLoaderModelOnly, LoadImage, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 0.25000000000000006, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 610434630889128, "steps": 10}
---

# 图片生成/图生图/Wan2.1 图生图洗图+修复工作流_1945503532646637569.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.1 图生图洗图+修复工作流_1945503532646637569.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `ModelSamplingSD3`
- `CLIPLoader`
- `LayerUtility: PurgeVRAM`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `ImageConcanate`
- `VAELoader`
- `VAEEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `610434630889128`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.25000000000000006`

## 知识

覆盖率 **100%**（15/15）

**有卡**：`ModelSamplingSD3`、`CLIPLoader`、`LayerUtility: PurgeVRAM`、`UNETLoader`、`CLIPTextEncode`、`KSampler`、`SaveImage`、`VAEDecode`、`ImageConcanate`、`VAELoader`、`VAEEncode`、`LoraLoaderModelOnly`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
