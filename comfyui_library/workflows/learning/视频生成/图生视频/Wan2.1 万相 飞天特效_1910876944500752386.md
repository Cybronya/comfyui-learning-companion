---
key: 视频生成/图生视频/Wan2.1 万相 飞天特效_1910876944500752386.json
name: Wan2.1 万相 飞天特效_1910876944500752386.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1910876944500752386.json
hash: 3211d186e3439934
coverage: 1
learned_at: 2026-10-15 22:29:30
nodes: [CLIPVisionLoader, ImageResizeKJ, VAEDecode, WanVideoEnhanceAVideoKJ, KSampler, VHS_VideoCombine, CLIPLoader, WanImageToVideo, CLIPTextEncode, CLIPVisionEncode, WanVideoTeaCacheKJ, UnetLoaderGGUF, LoraLoaderModelOnly, LoadImage, CLIPTextEncode, VAELoader]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 579286949466819, "steps": 20}
---

# 视频生成/图生视频/Wan2.1 万相 飞天特效_1910876944500752386.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1910876944500752386.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（16 个）：
- `CLIPVisionLoader`
- `ImageResizeKJ`
- `VAEDecode` ★核心
- `WanVideoEnhanceAVideoKJ`
- `KSampler` ★核心
- `VHS_VideoCombine`
- `CLIPLoader`
- `WanImageToVideo`
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `WanVideoTeaCacheKJ`
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `VAELoader`

## 关键参数

- `seed` = `579286949466819`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`CLIPVisionLoader`、`ImageResizeKJ`、`VAEDecode`、`WanVideoEnhanceAVideoKJ`、`KSampler`、`VHS_VideoCombine`、`CLIPLoader`、`WanImageToVideo`、`CLIPTextEncode`、`CLIPVisionEncode`、`WanVideoTeaCacheKJ`、`UnetLoaderGGUF`、`LoraLoaderModelOnly`、`LoadImage`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、CLIPVisionEncode
