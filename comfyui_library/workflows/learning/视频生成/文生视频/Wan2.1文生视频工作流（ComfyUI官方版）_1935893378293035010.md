---
key: 视频生成/文生视频/Wan2.1文生视频工作流（ComfyUI官方版）_1935893378293035010.json
name: Wan2.1文生视频工作流（ComfyUI官方版）_1935893378293035010.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1935893378293035010.json
hash: a916002899c71692
coverage: 1
learned_at: 2026-10-15 22:43:29
nodes: [VAELoader, CLIPTextEncode, CLIPLoader, EmptyHunyuanLatentVideo, CLIPTextEncode, UNETLoader, KSampler, VAEDecode, VHS_VideoCombine, Label (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 225577701395309, "steps": 30}
---

# 视频生成/文生视频/Wan2.1文生视频工作流（ComfyUI官方版）_1935893378293035010.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1935893378293035010.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（10 个）：
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `EmptyHunyuanLatentVideo`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `Label (rgthree)`

## 关键参数

- `seed` = `225577701395309`
- `steps` = `30`
- `cfg` = `6`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（10/10）

**有卡**：`VAELoader`、`CLIPTextEncode`、`CLIPLoader`、`EmptyHunyuanLatentVideo`、`UNETLoader`、`KSampler`、`VAEDecode`、`VHS_VideoCombine`、`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、EmptyHunyuanLatentVideo、VHS_VideoCombine
