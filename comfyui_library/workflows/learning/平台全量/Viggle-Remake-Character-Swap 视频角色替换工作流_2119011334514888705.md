---
key: 平台全量/Viggle-Remake-Character-Swap 视频角色替换工作流_2119011334514888705.json
name: Viggle-Remake-Character-Swap 视频角色替换工作流_2119011334514888705
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Viggle-Remake-Character-Swap 视频角色替换工作流_2119011334514888705.json
hash: efab53e8070a8787
coverage: 0.741935
learned_at: 2026-11-14 01:03:23
nodes: [VHS_LoadVideo, PrimitiveInt, PrimitiveInt, ComfyMathExpression, PreviewAny, LoadImage, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, ComfyMathExpression, ComfyMathExpression, StringFormat, StringFormat, PreviewAny, RemakeConditioning, RemakeNoise, BasicGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, CreateVideo, SaveVideo, UNETLoader, RemakeKeyframeUntil, CLIPLoader, VAELoader, VAELoader, MarkdownNote, Label (rgthree)]
patterns: []
missing: []
---

# 平台全量/Viggle-Remake-Character-Swap 视频角色替换工作流_2119011334514888705.json

> 来源文件 `comfyui_library/workflows/平台全量/Viggle-Remake-Character-Swap 视频角色替换工作流_2119011334514888705.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（31 个）：
- `VHS_LoadVideo`
- `PrimitiveInt`
- `PrimitiveInt`
- `ComfyMathExpression`
- `PreviewAny`
- `LoadImage`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `StringFormat`
- `StringFormat`
- `PreviewAny`
- `RemakeConditioning`
- `RemakeNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `CreateVideo`
- `SaveVideo`
- `UNETLoader` ★核心
- `RemakeKeyframeUntil`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `MarkdownNote`
- `Label (rgthree)`

## 知识

覆盖率 **74%**（23/31）

**有卡**：`VHS_LoadVideo`、`ComfyMathExpression`、`LoadImage`、`StringFormat`、`RemakeConditioning`、`RemakeNoise`、`BasicGuider`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`VAEDecode`、`VAEDecodeAudio`、`CreateVideo`、`SaveVideo`、`UNETLoader`、`RemakeKeyframeUntil`、`CLIPLoader`、`VAELoader`、`Label (rgthree)`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeAudio
