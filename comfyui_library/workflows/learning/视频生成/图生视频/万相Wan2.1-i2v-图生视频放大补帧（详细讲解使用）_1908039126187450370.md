---
key: 视频生成/图生视频/万相Wan2.1-i2v-图生视频放大补帧（详细讲解使用）_1908039126187450370.json
name: 万相Wan2.1-i2v-图生视频放大补帧（详细讲解使用）_1908039126187450370.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/万相Wan2.1-i2v-图生视频放大补帧（详细讲解使用）_1908039126187450370.json
hash: 0a298caf83093c6a
coverage: 0.606061
learned_at: 2026-10-15 22:29:28
nodes: [CFGGuider, RandomNoise, Note, KSamplerSelect, SamplerCustomAdvanced, BasicScheduler, LoadImage, VHS_VideoCombine, workflow>3, VAEDecode, Anything Everywhere, CR Upscale Image, CLIPTextEncode, RIFE VFI, VHS_VideoCombine, PreviewImage, PreviewImage, Note, Note, Note, VAELoader, Anything Everywhere, CLIPLoader, Anything Everywhere, Anything Everywhere, Note, UNETLoader, workflow>6, workflow>5, Note, Note, workflow>4, CLIPTextEncode]
patterns: []
missing: []
---

# 视频生成/图生视频/万相Wan2.1-i2v-图生视频放大补帧（详细讲解使用）_1908039126187450370.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1908039126187450370.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `CFGGuider`
- `RandomNoise`
- `Note`
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `LoadImage`
- `VHS_VideoCombine`
- `workflow>3`
- `VAEDecode` ★核心
- `Anything Everywhere`
- `CR Upscale Image`
- `CLIPTextEncode` ★核心
- `RIFE VFI`
- `VHS_VideoCombine`
- `PreviewImage`
- `PreviewImage`
- `Note`
- `Note`
- `Note`
- `VAELoader`
- `Anything Everywhere`
- `CLIPLoader`
- `Anything Everywhere`
- `Anything Everywhere`
- `Note`
- `UNETLoader` ★核心
- `workflow>6`
- `workflow>5`
- `Note`
- `Note`
- `workflow>4`
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **61%**（20/33）

**有卡**：`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`SamplerCustomAdvanced`、`BasicScheduler`、`LoadImage`、`VHS_VideoCombine`、`workflow>3`、`VAEDecode`、`CR Upscale Image`、`CLIPTextEncode`、`RIFE VFI`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`workflow>6`、`workflow>5`、`workflow>4`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
