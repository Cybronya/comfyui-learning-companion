---
key: 视频生成/图生视频/万相Wan2.1-i2v-图生视频（详细讲解使用）_1907390680300154882.json
name: 万相Wan2.1-i2v-图生视频（详细讲解使用）_1907390680300154882.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/万相Wan2.1-i2v-图生视频（详细讲解使用）_1907390680300154882.json
hash: 60591b43a835ba0f
coverage: 0.62963
learned_at: 2026-10-15 22:29:27
nodes: [Anything Everywhere, Anything Everywhere, Anything Everywhere, VAEDecode, CFGGuider, RandomNoise, Note, Note, Anything Everywhere, KSamplerSelect, SamplerCustomAdvanced, LoadImage, Note, Note, UNETLoader, workflow>3, VAELoader, CLIPLoader, workflow>6, CLIPTextEncode, Note, CLIPTextEncode, Note, BasicScheduler, workflow>4, VHS_VideoCombine, workflow>5]
patterns: []
missing: []
---

# 视频生成/图生视频/万相Wan2.1-i2v-图生视频（详细讲解使用）_1907390680300154882.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1907390680300154882.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（27 个）：
- `Anything Everywhere`
- `Anything Everywhere`
- `Anything Everywhere`
- `VAEDecode` ★核心
- `CFGGuider`
- `RandomNoise`
- `Note`
- `Note`
- `Anything Everywhere`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `LoadImage`
- `Note`
- `Note`
- `UNETLoader` ★核心
- `workflow>3`
- `VAELoader`
- `CLIPLoader`
- `workflow>6`
- `CLIPTextEncode` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `Note`
- `BasicScheduler`
- `workflow>4`
- `VHS_VideoCombine`
- `workflow>5`

## 知识

覆盖率 **63%**（17/27）

**有卡**：`VAEDecode`、`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`SamplerCustomAdvanced`、`LoadImage`、`UNETLoader`、`workflow>3`、`VAELoader`、`CLIPLoader`、`workflow>6`、`CLIPTextEncode`、`BasicScheduler`、`workflow>4`、`VHS_VideoCombine`、`workflow>5`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
