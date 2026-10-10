---
key: comfyui-workflow-templates-json/video_minimax_h3_multiframe_reference.json
name: video_minimax_h3_multiframe_reference
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/comfyui-workflow-templates-json/video_minimax_h3_multiframe_reference.json
hash: a0526a9f0d67f3fa
official: true
coverage: 0.682927
learned_at: 2026-10-10 22:50:29
nodes: [SaveVideo, ResolutionSelector, MarkdownNote, MarkdownNote, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, BasicGuider, UNETLoader, CLIPLoader, RandomNoise, CreateVideo, ComfyMathExpression, PrimitiveFloat, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, MarkdownNote, ComfySwitchNode, ComfySwitchNode, PrimitiveInt, PrimitiveInt, LoraLoaderModelOnly, PrimitiveBoolean, MiniMaxH3AddGuide, ComfyMathExpression, PrimitiveFloat, LoadImage, LoadImage, PrimitiveFloat, ComfyMathExpression, MiniMaxH3AddGuide, LoadImage, LoadImage, PrimitiveFloat, MiniMaxH3AddGuide, ComfyMathExpression, MarkdownNote]
patterns: []
missing: []
---

# comfyui-workflow-templates-json/video_minimax_h3_multiframe_reference.json

> 来源文件 `comfyui_library/workflows/comfyui-workflow-templates-json/video_minimax_h3_multiframe_reference.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（41 个）：
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
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `PrimitiveInt`
- `PrimitiveInt`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveBoolean`
- `MiniMaxH3AddGuide`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `LoadImage`
- `LoadImage`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `MiniMaxH3AddGuide`
- `LoadImage`
- `LoadImage`
- `PrimitiveFloat`
- `MiniMaxH3AddGuide`
- `ComfyMathExpression`
- `MarkdownNote`

## 知识

覆盖率 **68%**（28/41）

**有卡**：`SaveVideo`、`ResolutionSelector`、`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`BasicGuider`、`UNETLoader`、`CLIPLoader`、`RandomNoise`、`CreateVideo`、`ComfyMathExpression`、`MiniMaxH3ReferenceToVideo`、`LoraLoaderModelOnly`、`PrimitiveBoolean`、`MiniMaxH3AddGuide`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
