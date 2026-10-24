---
key: 图片生成/图生图/HiDream-E1.1 FP8版工作流_1947629622461673473.json
name: HiDream-E1.1 FP8版工作流_1947629622461673473
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/HiDream-E1.1 FP8版工作流_1947629622461673473.json
hash: 2cd61d80e2ac62c8
coverage: 0.842105
learned_at: 2026-10-23 11:02:59
nodes: [CLIPTextEncode, SaveImage, QuadrupleCLIPLoader, VAELoader, BasicScheduler, KSamplerSelect, DualCFGGuider, RandomNoise, VAEDecode, SamplerCustomAdvanced, InstructPixToPixConditioning, PrimitiveNode, PrimitiveNode, Reroute, ImageScaleToTotalPixels, CFGNorm, UNETLoader, LoadImage, CLIPTextEncode]
patterns: []
missing: []
---

# 图片生成/图生图/HiDream-E1.1 FP8版工作流_1947629622461673473.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/HiDream-E1.1 FP8版工作流_1947629622461673473.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `CLIPTextEncode` ★核心
- `SaveImage`
- `QuadrupleCLIPLoader`
- `VAELoader`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `DualCFGGuider`
- `RandomNoise`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `InstructPixToPixConditioning`
- `PrimitiveNode`
- `PrimitiveNode`
- `Reroute`
- `ImageScaleToTotalPixels`
- `CFGNorm`
- `UNETLoader` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **84%**（16/19）

**有卡**：`CLIPTextEncode`、`SaveImage`、`QuadrupleCLIPLoader`、`VAELoader`、`BasicScheduler`、`KSamplerSelect`、`DualCFGGuider`、`RandomNoise`、`VAEDecode`、`SamplerCustomAdvanced`、`InstructPixToPixConditioning`、`ImageScaleToTotalPixels`、`CFGNorm`、`UNETLoader`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGNorm、KSamplerSelect、SamplerCustomAdvanced
