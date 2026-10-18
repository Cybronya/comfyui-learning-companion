---
key: 视频生成/图生视频/Wan2.1首尾帧工作流（ComfyUI官方版）_1935900536141246465.json
name: Wan2.1首尾帧工作流（ComfyUI官方版）_1935900536141246465.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1首尾帧工作流（ComfyUI官方版）_1935900536141246465.json
hash: 4bd6ef3a34101ffd
coverage: 0.941176
learned_at: 2026-10-15 22:30:24
nodes: [VAELoader, CLIPVisionEncode, CLIPVisionLoader, CLIPVisionEncode, ModelSamplingSD3, VAEDecode, WanFirstLastFrameToVideo, MarkdownNote, CLIPTextEncode, UNETLoader, CLIPLoader, CLIPTextEncode, LoadImage, LoadImage, KSampler, VHS_VideoCombine, Label (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 3, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 1012535162155917, "steps": 20}
---

# 视频生成/图生视频/Wan2.1首尾帧工作流（ComfyUI官方版）_1935900536141246465.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1935900536141246465.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（17 个）：
- `VAELoader`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `WanFirstLastFrameToVideo`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoadImage`
- `KSampler` ★核心
- `VHS_VideoCombine`
- `Label (rgthree)`

## 关键参数

- `seed` = `1012535162155917`
- `steps` = `20`
- `cfg` = `3`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **94%**（16/17）

**有卡**：`VAELoader`、`CLIPVisionEncode`、`CLIPVisionLoader`、`ModelSamplingSD3`、`VAEDecode`、`WanFirstLastFrameToVideo`、`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`、`LoadImage`、`KSampler`、`VHS_VideoCombine`、`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CLIPVisionEncode
