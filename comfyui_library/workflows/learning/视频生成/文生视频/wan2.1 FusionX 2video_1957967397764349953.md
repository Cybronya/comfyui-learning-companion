---
key: 视频生成/文生视频/wan2.1 FusionX 2video_1957967397764349953.json
name: wan2.1 FusionX 2video_1957967397764349953.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1957967397764349953.json
hash: 2dbfb8061d351dcd
coverage: 1
learned_at: 2026-10-15 22:43:41
nodes: [ModelSamplingSD3, CLIPVisionLoader, CLIPLoader, VAELoader, CLIPTextEncode, CLIPTextEncode, ImageResize+, CLIPVisionEncode, LoadImage, UNETLoader, VAEDecode, KSampler, WanImageToVideo, RIFE VFI, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "normal", "seed": 242276946169535, "steps": 10}
---

# 视频生成/文生视频/wan2.1 FusionX 2video_1957967397764349953.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1957967397764349953.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（16 个）：
- `ModelSamplingSD3`
- `CLIPVisionLoader`
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ImageResize+`
- `CLIPVisionEncode`
- `LoadImage`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `WanImageToVideo`
- `RIFE VFI`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `242276946169535`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **100%**（16/16）

**有卡**：`ModelSamplingSD3`、`CLIPVisionLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ImageResize+`、`CLIPVisionEncode`、`LoadImage`、`UNETLoader`、`VAEDecode`、`KSampler`、`WanImageToVideo`、`RIFE VFI`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode
