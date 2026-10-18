---
key: 视频生成/图生视频/wan2.1_fun图生视频(动作迁移)超稳定版_2046063628947820545.json
name: wan2.1_fun图生视频(动作迁移)超稳定版_2046063628947820545.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.1_fun图生视频(动作迁移)超稳定版_2046063628947820545.json
hash: 92197690b960b2d7
coverage: 0.805556
learned_at: 2026-10-15 22:36:54
nodes: [CLIPLoader, VAELoader, UNETLoader, WanVideoTeaCacheKJ, CLIPTextEncode, ModelSamplingSD3, CLIPTextEncode, KSampler, VAEDecodeTiled, CLIPVisionLoader, CLIPVisionEncode, VHS_VideoCombine, RIFE VFI, Fast Groups Bypasser (rgthree), WanFunControlToVideo, EmptyHunyuanLatentVideo, ImageResizeKJ, RHHiddenNodes, ImageResizeKJ, ShowText|pysssss, RHHiddenNodes, Int, Int, Int, Int, VHS_VideoCombine, Int, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, SkipLayerGuidanceWanVideo, CR Upscale Image, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 826321538917707, "steps": 20}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/wan2.1_fun图生视频(动作迁移)超稳定版_2046063628947820545.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046063628947820545.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（36 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `WanVideoTeaCacheKJ`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecodeTiled` ★核心
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `VHS_VideoCombine`
- `RIFE VFI`
- `Fast Groups Bypasser (rgthree)`
- `WanFunControlToVideo`
- `EmptyHunyuanLatentVideo`
- `ImageResizeKJ`
- `RHHiddenNodes`
- `ImageResizeKJ`
- `ShowText|pysssss`
- `RHHiddenNodes`
- `Int`
- `Int`
- `Int`
- `Int`
- `VHS_VideoCombine`
- `Int`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `SkipLayerGuidanceWanVideo`
- `CR Upscale Image`
- `LoadImage`
- `VHS_LoadVideo`

## 关键参数

- `seed` = `826321538917707`
- `steps` = `20`
- `cfg` = `5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **81%**（29/36）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`WanVideoTeaCacheKJ`、`CLIPTextEncode`、`ModelSamplingSD3`、`KSampler`、`VAEDecodeTiled`、`CLIPVisionLoader`、`CLIPVisionEncode`、`VHS_VideoCombine`、`RIFE VFI`、`WanFunControlToVideo`、`EmptyHunyuanLatentVideo`、`ImageResizeKJ`、`RHHiddenNodes`、`Int`、`SkipLayerGuidanceWanVideo`、`CR Upscale Image`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：KSampler、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、SkipLayerGuidanceWanVideo、VAEDecodeTiled

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
