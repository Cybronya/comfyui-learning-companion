---
key: 视频生成/图生视频/【老金驿站】Wan2.1图生视频CFGZeroStar加强版_1896469685087109121.json
name: 【老金驿站】Wan2.1图生视频CFGZeroStar加强版_1896469685087109121.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1896469685087109121.json
hash: 08c1c371b5651815
coverage: 0.941176
learned_at: 2026-10-15 22:29:18
nodes: [LoadImage, WanImageToVideo, VAELoader, VHS_VideoCombine, RIFE VFI, VHS_VideoCombine, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CLIPLoader, UNETLoader, VAEDecodeTiled, ImageResizeKJ, CLIPTextEncode, KSampler, Reroute, CFGZeroStarAndInit]
patterns: []
missing: []
problems: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 529887889715652, "steps": 30}
discoveries: [[high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/【老金驿站】Wan2.1图生视频CFGZeroStar加强版_1896469685087109121.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1896469685087109121.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（17 个）：
- `LoadImage`
- `WanImageToVideo`
- `VAELoader`
- `VHS_VideoCombine`
- `RIFE VFI`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAEDecodeTiled` ★核心
- `ImageResizeKJ`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `Reroute`
- `CFGZeroStarAndInit`

## 关键参数

- `seed` = `529887889715652`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`LoadImage`、`WanImageToVideo`、`VAELoader`、`VHS_VideoCombine`、`RIFE VFI`、`CLIPTextEncode`、`CLIPVisionEncode`、`CLIPVisionLoader`、`CLIPLoader`、`UNETLoader`、`VAEDecodeTiled`、`ImageResizeKJ`、`KSampler`、`CFGZeroStarAndInit`

**用到的条目**：KSampler、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGZeroStarAndInit、VAEDecodeTiled

## 参数体检

发现 1 个问题：
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
