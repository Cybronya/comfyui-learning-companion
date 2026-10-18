---
key: 视频生成/文生视频/万相wan2.1-T2v-文生视频放大补帧（详细讲解使用）_1907817176102019074.json
name: 万相wan2.1-T2v-文生视频放大补帧（详细讲解使用）_1907817176102019074.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/万相wan2.1-T2v-文生视频放大补帧（详细讲解使用）_1907817176102019074.json
hash: 3bac13e45ff150ab
coverage: 0.65625
learned_at: 2026-10-15 22:43:21
nodes: [RandomNoise, CFGGuider, VHS_VideoCombine, RIFE VFI, workflow>1, Anything Everywhere, VAEDecode, CLIPTextEncode, KSamplerSelect, Note, Note, Note, Note, Note, PreviewImage, Note, VHS_VideoCombine, SamplerCustomAdvanced, CLIPLoader, Anything Everywhere, VAELoader, Anything Everywhere, BasicScheduler, workflow>2, CLIPTextEncode, CR Upscale Image, UNETLoader, PreviewImage, Int, Int, EmptyHunyuanLatentVideo, Int]
patterns: []
missing: []
---

# 视频生成/文生视频/万相wan2.1-T2v-文生视频放大补帧（详细讲解使用）_1907817176102019074.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1907817176102019074.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `RandomNoise`
- `CFGGuider`
- `VHS_VideoCombine`
- `RIFE VFI`
- `workflow>1`
- `Anything Everywhere`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `KSamplerSelect` ★核心
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `PreviewImage`
- `Note`
- `VHS_VideoCombine`
- `SamplerCustomAdvanced` ★核心
- `CLIPLoader`
- `Anything Everywhere`
- `VAELoader`
- `Anything Everywhere`
- `BasicScheduler`
- `workflow>2`
- `CLIPTextEncode` ★核心
- `CR Upscale Image`
- `UNETLoader` ★核心
- `PreviewImage`
- `Int`
- `Int`
- `EmptyHunyuanLatentVideo`
- `Int`

## 知识

覆盖率 **66%**（21/32）

**有卡**：`RandomNoise`、`CFGGuider`、`VHS_VideoCombine`、`RIFE VFI`、`workflow>1`、`VAEDecode`、`CLIPTextEncode`、`KSamplerSelect`、`SamplerCustomAdvanced`、`CLIPLoader`、`VAELoader`、`BasicScheduler`、`workflow>2`、`CR Upscale Image`、`UNETLoader`、`Int`、`EmptyHunyuanLatentVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
