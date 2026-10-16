---
key: 视频生成/文生视频/万相wan2.2 5B文图生视频官方工作流_1950766450359324674.json
name: 万相wan2.2 5B文图生视频官方工作流_1950766450359324674.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1950766450359324674.json
hash: 6e654d0e1df3b6f0
coverage: 0.923077
learned_at: 2026-10-15 22:43:36
nodes: [CreateVideo, SaveVideo, Wan22ImageToVideoLatent, CLIPTextEncode, MarkdownNote, KSampler, ModelSamplingSD3, VAEDecode, CLIPLoader, VAELoader, UNETLoader, CLIPTextEncode, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 5, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 350947843012815, "steps": 20}
---

# 视频生成/文生视频/万相wan2.2 5B文图生视频官方工作流_1950766450359324674.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950766450359324674.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（13 个）：
- `CreateVideo`
- `SaveVideo`
- `Wan22ImageToVideoLatent`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `KSampler` ★核心
- `ModelSamplingSD3`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`

## 关键参数

- `seed` = `350947843012815`
- `steps` = `20`
- `cfg` = `5`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`CreateVideo`、`SaveVideo`、`Wan22ImageToVideoLatent`、`CLIPTextEncode`、`KSampler`、`ModelSamplingSD3`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、Wan22ImageToVideoLatent
