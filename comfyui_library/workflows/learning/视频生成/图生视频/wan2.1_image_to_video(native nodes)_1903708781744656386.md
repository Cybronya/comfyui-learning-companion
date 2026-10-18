---
key: 视频生成/图生视频/wan2.1_image_to_video(native nodes)_1903708781744656386.json
name: wan2.1_image_to_video(native nodes)_1903708781744656386.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.1_image_to_video(native nodes)_1903708781744656386.json
hash: 06ed655a8eccf10d
coverage: 0.941176
learned_at: 2026-10-15 22:29:25
nodes: [KSampler, CLIPTextEncode, CLIPTextEncode, WanImageToVideo, VAEDecodeTiled, PreviewImage, VHS_VideoCombine, WanVideoTeaCacheKJ, UNETLoader, CLIPLoader, CLIPVisionLoader, LoraLoaderModelOnly, ImageResizeKJ, VAELoader, RIFE VFI, LoadImage, CLIPVisionEncode]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 882416881818678, "steps": 30}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/wan2.1_image_to_video(native nodes)_1903708781744656386.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1903708781744656386.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `VAEDecodeTiled` ★核心
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoTeaCacheKJ`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPVisionLoader`
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJ`
- `VAELoader`
- `RIFE VFI`
- `LoadImage`
- `CLIPVisionEncode`

## 关键参数

- `seed` = `882416881818678`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`KSampler`、`CLIPTextEncode`、`WanImageToVideo`、`VAEDecodeTiled`、`VHS_VideoCombine`、`WanVideoTeaCacheKJ`、`UNETLoader`、`CLIPLoader`、`CLIPVisionLoader`、`LoraLoaderModelOnly`、`ImageResizeKJ`、`VAELoader`、`RIFE VFI`、`LoadImage`、`CLIPVisionEncode`

**用到的条目**：KSampler、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、VAEDecodeTiled

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
