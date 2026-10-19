---
key: 图片生成/文生图/flux2文生图1.0_1998240533703196674.json
name: flux2文生图1.0_1998240533703196674
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/flux2文生图1.0_1998240533703196674.json
hash: 3d75b7e8a44482b6
coverage: 0.842105
learned_at: 2026-10-19 21:47:16
nodes: [Flux2Scheduler, BasicGuider, KSamplerSelect, FluxGuidance, RandomNoise, VAEDecode, CR Seed, INTConstant, SamplerCustomAdvanced, EmptyFlux2LatentImage, PrimitiveNode, SaveImage, CLIPLoader, VAELoader, MarkdownNote, CLIPTextEncode, CR Text, PrimitiveNode, UNETLoader]
patterns: []
missing: []
---

# 图片生成/文生图/flux2文生图1.0_1998240533703196674.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/flux2文生图1.0_1998240533703196674.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `Flux2Scheduler`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `FluxGuidance`
- `RandomNoise`
- `VAEDecode` ★核心
- `CR Seed`
- `INTConstant`
- `SamplerCustomAdvanced` ★核心
- `EmptyFlux2LatentImage`
- `PrimitiveNode`
- `SaveImage`
- `CLIPLoader`
- `VAELoader`
- `MarkdownNote`
- `CLIPTextEncode` ★核心
- `CR Text`
- `PrimitiveNode`
- `UNETLoader` ★核心

## 知识

覆盖率 **84%**（16/19）

**有卡**：`Flux2Scheduler`、`BasicGuider`、`KSamplerSelect`、`FluxGuidance`、`RandomNoise`、`VAEDecode`、`CR Seed`、`INTConstant`、`SamplerCustomAdvanced`、`EmptyFlux2LatentImage`、`SaveImage`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`CR Text`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、CLIPLoader、FluxGuidance、KSamplerSelect、SamplerCustomAdvanced
