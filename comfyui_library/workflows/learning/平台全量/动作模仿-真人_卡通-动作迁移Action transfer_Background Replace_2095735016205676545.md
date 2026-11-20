---
key: 平台全量/动作模仿-真人_卡通-动作迁移Action transfer_Background Replace_2095735016205676545.json
name: 动作模仿-真人_卡通-动作迁移Action transfer_Background Replace_2095735016205676545
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/动作模仿-真人_卡通-动作迁移Action transfer_Background Replace_2095735016205676545.json
hash: 3c8751bbcce3f66a
coverage: 0.666667
learned_at: 2026-11-14 01:44:23
nodes: [BasicScheduler, MiniMaxH3ReferenceToVideo, KSamplerSelect, RandomNoise, MiniMaxH3SigmaShift, CLIPLoader, PrimitiveFloat, BasicGuider, VAELoader, VAELoader, SamplerCustomAdvanced, MarkdownNote, MarkdownNote, ComfyMathExpression, PathchSageAttentionKJ, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, UNETLoader, VHS_LoadVideo, Reroute, VAEDecode, Reroute, VHS_VideoCombine, MarkdownNote, LoadImage, MarkdownNote, ResolutionSelector, MarkdownNote, CR Text, LoadImage, LoadImage, CR Text, VHS_VideoCombine, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/动作模仿-真人_卡通-动作迁移Action transfer_Background Replace_2095735016205676545.json

> 来源文件 `comfyui_library/workflows/平台全量/动作模仿-真人_卡通-动作迁移Action transfer_Background Replace_2095735016205676545.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Other

**节点**（36 个）：
- `BasicScheduler`
- `MiniMaxH3ReferenceToVideo`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `MiniMaxH3SigmaShift`
- `CLIPLoader`
- `PrimitiveFloat`
- `BasicGuider`
- `VAELoader`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `ComfyMathExpression`
- `PathchSageAttentionKJ`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader` ★核心
- `VHS_LoadVideo`
- `Reroute`
- `VAEDecode` ★核心
- `Reroute`
- `VHS_VideoCombine`
- `MarkdownNote`
- `LoadImage`
- `MarkdownNote`
- `ResolutionSelector`
- `MarkdownNote`
- `CR Text`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `VHS_VideoCombine`
- `VHS_LoadVideo`

## 知识

覆盖率 **67%**（24/36）

**有卡**：`BasicScheduler`、`MiniMaxH3ReferenceToVideo`、`KSamplerSelect`、`RandomNoise`、`MiniMaxH3SigmaShift`、`CLIPLoader`、`BasicGuider`、`VAELoader`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`PathchSageAttentionKJ`、`UNETLoader`、`VHS_LoadVideo`、`VAEDecode`、`VHS_VideoCombine`、`LoadImage`、`ResolutionSelector`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
