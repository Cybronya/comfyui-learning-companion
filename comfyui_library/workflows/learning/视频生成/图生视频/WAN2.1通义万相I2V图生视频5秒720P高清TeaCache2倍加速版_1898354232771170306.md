---
key: 视频生成/图生视频/WAN2.1通义万相I2V图生视频5秒720P高清TeaCache2倍加速版_1898354232771170306.json
name: WAN2.1通义万相I2V图生视频5秒720P高清TeaCache2倍加速版_1898354232771170306.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.1通义万相I2V图生视频5秒720P高清TeaCache2倍加速版_1898354232771170306.json
hash: 158cd9a62f53650a
coverage: 1
learned_at: 2026-10-15 22:29:20
nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, VAELoader, CLIPVisionLoader, CLIPTextEncode, VAEDecode, KSampler, LoadImage, VHS_VideoCombine, UnetLoaderGGUF, WanImageToVideo, WanVideoTeaCacheKJ]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 171955302310558, "steps": 20}
---

# 视频生成/图生视频/WAN2.1通义万相I2V图生视频5秒720P高清TeaCache2倍加速版_1898354232771170306.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1898354232771170306.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（13 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `VAELoader`
- `CLIPVisionLoader`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `LoadImage`
- `VHS_VideoCombine`
- `UnetLoaderGGUF` ★核心
- `WanImageToVideo`
- `WanVideoTeaCacheKJ`

## 关键参数

- `seed` = `171955302310558`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`CLIPVisionEncode`、`VAELoader`、`CLIPVisionLoader`、`VAEDecode`、`KSampler`、`LoadImage`、`VHS_VideoCombine`、`UnetLoaderGGUF`、`WanImageToVideo`、`WanVideoTeaCacheKJ`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、CLIPVisionEncode、CLIPVisionLoader
