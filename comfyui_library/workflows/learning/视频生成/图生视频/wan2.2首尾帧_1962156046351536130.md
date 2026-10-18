---
key: 视频生成/图生视频/wan2.2首尾帧_1962156046351536130.json
name: wan2.2首尾帧_1962156046351536130.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2首尾帧_1962156046351536130.json
hash: fe478fc5166a1ac6
coverage: 0.842105
learned_at: 2026-10-15 22:31:30
nodes: [CLIPLoader, ModelSamplingSD3, ModelSamplingSD3, MarkdownNote, CLIPTextEncode, VAELoader, Note, VAEDecode, Note, CreateVideo, SaveVideo, KSamplerAdvanced, KSamplerAdvanced, LoadImage, LoadImage, WanFirstLastFrameToVideo, CLIPTextEncode, UNETLoader, UNETLoader]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 4, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 视频生成/图生视频/wan2.2首尾帧_1962156046351536130.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1962156046351536130.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（19 个）：
- `CLIPLoader`
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `Note`
- `VAEDecode` ★核心
- `Note`
- `CreateVideo`
- `SaveVideo`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `LoadImage`
- `WanFirstLastFrameToVideo`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `UNETLoader` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `20`
- `sampler_name` = `4`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`CLIPLoader`、`ModelSamplingSD3`、`CLIPTextEncode`、`VAELoader`、`VAEDecode`、`CreateVideo`、`SaveVideo`、`KSamplerAdvanced`、`LoadImage`、`WanFirstLastFrameToVideo`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、SaveVideo
