---
key: comfyui-workflow-templates-json/hidream_e1_full.json
name: hidream_e1_full
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/hidream_e1_full.json
hash: 6dabd49facf3b61e
official: true
coverage: 0.833333
learned_at: 2026-10-07 21:35:29
nodes: [RandomNoise, UNETLoader, QuadrupleCLIPLoader, VAELoader, CLIPTextEncode, LoadImage, ImageScale, Note, InstructPixToPixConditioning, Reroute, DualCFGGuider, KSamplerSelect, BasicScheduler, VAEDecode, SamplerCustomAdvanced, SaveImage, CLIPTextEncode, MarkdownNote]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/hidream_e1_full.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/hidream_e1_full.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `RandomNoise`
- `UNETLoader` ★核心
- `QuadrupleCLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `ImageScale`
- `Note`
- `InstructPixToPixConditioning`
- `Reroute`
- `DualCFGGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `MarkdownNote`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`RandomNoise`、`UNETLoader`、`QuadrupleCLIPLoader`、`VAELoader`、`CLIPTextEncode`、`LoadImage`、`ImageScale`、`InstructPixToPixConditioning`、`DualCFGGuider`、`KSamplerSelect`、`BasicScheduler`、`VAEDecode`、`SamplerCustomAdvanced`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、DualCFGGuider
