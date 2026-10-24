---
key: 图片生成/图生图/HiDream-E1.1 动漫转真人写实_1947636333943664641.json
name: HiDream-E1.1 动漫转真人写实_1947636333943664641
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/HiDream-E1.1 动漫转真人写实_1947636333943664641.json
hash: fa1cdff2cf46b143
coverage: 0.833333
learned_at: 2026-10-23 11:02:59
nodes: [CLIPTextEncode, SaveImage, QuadrupleCLIPLoader, VAELoader, BasicScheduler, KSamplerSelect, DualCFGGuider, RandomNoise, VAEDecode, SamplerCustomAdvanced, InstructPixToPixConditioning, PrimitiveNode, PrimitiveNode, Reroute, ImageScaleToTotalPixels, UNETLoader, LoadImage, CLIPTextEncode]
patterns: []
missing: []
---

# 图片生成/图生图/HiDream-E1.1 动漫转真人写实_1947636333943664641.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/HiDream-E1.1 动漫转真人写实_1947636333943664641.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
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
- `UNETLoader` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心

## 知识

覆盖率 **83%**（15/18）

**有卡**：`CLIPTextEncode`、`SaveImage`、`QuadrupleCLIPLoader`、`VAELoader`、`BasicScheduler`、`KSamplerSelect`、`DualCFGGuider`、`RandomNoise`、`VAEDecode`、`SamplerCustomAdvanced`、`InstructPixToPixConditioning`、`ImageScaleToTotalPixels`、`UNETLoader`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、DualCFGGuider
