---
key: comfyui-workflow-templates-json/hidream_e1_1.json
name: hidream_e1_1
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/hidream_e1_1.json
hash: e9fc13b458ef2ec9
official: true
coverage: 0.8
learned_at: 2026-10-10 22:47:17
nodes: [CLIPTextEncode, SaveImage, BasicScheduler, KSamplerSelect, DualCFGGuider, RandomNoise, VAEDecode, SamplerCustomAdvanced, InstructPixToPixConditioning, PrimitiveNode, PrimitiveNode, Reroute, LoadImage, CLIPTextEncode, CFGNorm, ImageScaleToTotalPixels, UNETLoader, QuadrupleCLIPLoader, VAELoader, MarkdownNote]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/hidream_e1_1.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/hidream_e1_1.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `CLIPTextEncode` ★核心
- `SaveImage`
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
- `LoadImage`
- `CLIPTextEncode` ★核心
- `CFGNorm`
- `ImageScaleToTotalPixels`
- `UNETLoader` ★核心
- `QuadrupleCLIPLoader`
- `VAELoader`
- `MarkdownNote`

## 知识

覆盖率 **80%**（16/20）

**有卡**：`CLIPTextEncode`、`SaveImage`、`BasicScheduler`、`KSamplerSelect`、`DualCFGGuider`、`RandomNoise`、`VAEDecode`、`SamplerCustomAdvanced`、`InstructPixToPixConditioning`、`LoadImage`、`CFGNorm`、`ImageScaleToTotalPixels`、`UNETLoader`、`QuadrupleCLIPLoader`、`VAELoader`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、CFGNorm、KSamplerSelect、SamplerCustomAdvanced
