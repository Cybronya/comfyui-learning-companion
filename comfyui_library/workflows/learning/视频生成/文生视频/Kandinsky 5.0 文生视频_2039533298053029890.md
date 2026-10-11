---
key: 视频生成/文生视频/Kandinsky 5.0 文生视频_2039533298053029890.json
name: Kandinsky 5.0 文生视频_2039533298053029890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Kandinsky 5.0 文生视频_2039533298053029890.json
hash: edacc08810e7d69b
coverage: 0.846154
learned_at: 2026-10-11 19:49:34
nodes: [DualCLIPLoader, VAELoader, VAEDecode, ModelSamplingSD3, KSampler, Kandinsky5ImageToVideo, CreateVideo, UNETLoader, MarkdownNote, MarkdownNote, SaveVideo, CLIPTextEncode, CLIPTextEncode]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 938540819118548, "steps": 50}
---

# 视频生成/文生视频/Kandinsky 5.0 文生视频_2039533298053029890.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Kandinsky 5.0 文生视频_2039533298053029890.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（13 个）：
- `DualCLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `KSampler` ★核心
- `Kandinsky5ImageToVideo`
- `CreateVideo`
- `UNETLoader` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `SaveVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `seed` = `938540819118548`
- `steps` = `50`
- `cfg` = `5`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`DualCLIPLoader`、`VAELoader`、`VAEDecode`、`ModelSamplingSD3`、`KSampler`、`Kandinsky5ImageToVideo`、`CreateVideo`、`UNETLoader`、`SaveVideo`、`CLIPTextEncode`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、UNETLoader、SaveVideo、CreateVideo、DualCLIPLoader
