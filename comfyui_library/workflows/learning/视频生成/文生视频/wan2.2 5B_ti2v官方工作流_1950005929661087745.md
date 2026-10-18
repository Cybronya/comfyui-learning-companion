---
key: 视频生成/文生视频/wan2.2 5B_ti2v官方工作流_1950005929661087745.json
name: wan2.2 5B_ti2v官方工作流_1950005929661087745.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/wan2.2 5B_ti2v官方工作流_1950005929661087745.json
hash: 9f682f4319260ff1
coverage: 0.928571
learned_at: 2026-10-15 22:43:33
nodes: [CreateVideo, MarkdownNote, KSampler, UNETLoader, VAELoader, CLIPLoader, ModelSamplingSD3, LoadImage, CLIPTextEncode, CLIPTextEncode, Wan22ImageToVideoLatent, VAEDecode, SaveVideo, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 14187716038719, "steps": 20}
---

# 视频生成/文生视频/wan2.2 5B_ti2v官方工作流_1950005929661087745.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950005929661087745.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（14 个）：
- `CreateVideo`
- `MarkdownNote`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `ModelSamplingSD3`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Wan22ImageToVideoLatent`
- `VAEDecode` ★核心
- `SaveVideo`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `14187716038719`
- `steps` = `20`
- `cfg` = `5`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`CreateVideo`、`KSampler`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`ModelSamplingSD3`、`LoadImage`、`CLIPTextEncode`、`Wan22ImageToVideoLatent`、`VAEDecode`、`SaveVideo`、`VHS_VideoCombine`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、Wan22ImageToVideoLatent
