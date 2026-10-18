---
key: 视频生成/图生视频/UNET加载器跑wan2.1视频_1935624782786527233.json
name: UNET加载器跑wan2.1视频_1935624782786527233.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/UNET加载器跑wan2.1视频_1935624782786527233.json
hash: 9890d91b0399740b
coverage: 1
learned_at: 2026-10-15 22:30:23
nodes: [CLIPLoader, CLIPTextEncode, WanImageToVideo, WanVideoTeaCacheKJ, WanVideoEnhanceAVideoKJ, UNETLoader, WanVideoModelLoader, KSampler, VAEDecode, VHS_VideoCombine, VAELoader, CLIPVisionLoader, CLIPVisionEncode, ImageResizeKJ, LoadImage, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 768217825292868, "steps": 20}
---

# 视频生成/图生视频/UNET加载器跑wan2.1视频_1935624782786527233.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1935624782786527233.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（16 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `WanVideoTeaCacheKJ`
- `WanVideoEnhanceAVideoKJ`
- `UNETLoader` ★核心
- `WanVideoModelLoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `VAELoader`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `ImageResizeKJ`
- `LoadImage`
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `768217825292868`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`WanImageToVideo`、`WanVideoTeaCacheKJ`、`WanVideoEnhanceAVideoKJ`、`UNETLoader`、`WanVideoModelLoader`、`KSampler`、`VAEDecode`、`VHS_VideoCombine`、`VAELoader`、`CLIPVisionLoader`、`CLIPVisionEncode`、`ImageResizeKJ`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode
