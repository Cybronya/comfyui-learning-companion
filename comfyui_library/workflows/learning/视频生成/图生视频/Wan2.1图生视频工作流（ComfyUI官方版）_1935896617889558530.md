---
key: 视频生成/图生视频/Wan2.1图生视频工作流（ComfyUI官方版）_1935896617889558530.json
name: Wan2.1图生视频工作流（ComfyUI官方版）_1935896617889558530.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1935896617889558530.json
hash: b270a1c7dfb09f67
coverage: 1
learned_at: 2026-10-15 22:30:24
nodes: [CLIPLoader, CLIPVisionLoader, CLIPTextEncode, CLIPTextEncode, WanImageToVideo, UNETLoader, CLIPVisionEncode, VAELoader, KSampler, VAEDecode, VHS_VideoCombine, LoadImage, Label (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 329848519773328, "steps": 30}
---

# 视频生成/图生视频/Wan2.1图生视频工作流（ComfyUI官方版）_1935896617889558530.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1935896617889558530.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（13 个）：
- `CLIPLoader`
- `CLIPVisionLoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `WanImageToVideo`
- `UNETLoader` ★核心
- `CLIPVisionEncode`
- `VAELoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `Label (rgthree)`

## 关键参数

- `seed` = `329848519773328`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`CLIPLoader`、`CLIPVisionLoader`、`CLIPTextEncode`、`WanImageToVideo`、`UNETLoader`、`CLIPVisionEncode`、`VAELoader`、`KSampler`、`VAEDecode`、`VHS_VideoCombine`、`LoadImage`、`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode
