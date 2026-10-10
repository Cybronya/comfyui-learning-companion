---
key: comfyui-workflow-templates-json/video_minimax_h3_r2v.json
name: video_minimax_h3_r2v
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_minimax_h3_r2v.json
hash: afeea99e9fd5a145
official: true
coverage: 0.689655
learned_at: 2026-10-10 22:50:30
nodes: [SaveVideo, ResolutionSelector, MarkdownNote, MarkdownNote, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, BasicGuider, UNETLoader, CLIPLoader, RandomNoise, CreateVideo, ComfyMathExpression, PrimitiveFloat, MiniMaxH3ReferenceToVideo, LoadImage, PrimitiveStringMultiline, LoadImage, MarkdownNote, ComfySwitchNode, ComfySwitchNode, PrimitiveInt, PrimitiveInt, LoraLoaderModelOnly, PrimitiveBoolean]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/video_minimax_h3_r2v.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_minimax_h3_r2v.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（29 个）：
- `SaveVideo`
- `ResolutionSelector`
- `MarkdownNote`
- `MarkdownNote`
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `UNETLoader` ★核心
- `CLIPLoader`
- `RandomNoise`
- `CreateVideo`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `MiniMaxH3ReferenceToVideo`
- `LoadImage`
- `PrimitiveStringMultiline`
- `LoadImage`
- `MarkdownNote`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveBoolean`

## 知识

覆盖率 **69%**（20/29）

**有卡**：`SaveVideo`、`ResolutionSelector`、`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`BasicGuider`、`UNETLoader`、`CLIPLoader`、`RandomNoise`、`CreateVideo`、`ComfyMathExpression`、`MiniMaxH3ReferenceToVideo`、`LoadImage`、`LoraLoaderModelOnly`、`PrimitiveBoolean`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
