---
key: 视频生成/文生视频/MiniMax H3多合一｜Turbo4 + Sage + T8 Stable｜R2V Turbo6 EXP + 二采增强版｜B站UP主@好奇漫步_2086836147753410562.json
name: MiniMax H3多合一｜Turbo4 + Sage + T8 Stable｜R2V Turbo6 EXP + 二采增强版｜B站UP主@好奇漫步_2086836147753410562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3多合一｜Turbo4 + Sage + T8 Stable｜R2V Turbo6 EXP + 二采增强版｜B站UP主@好奇漫步_2086836147753410562.json
hash: b7ba002953b4b6b8
coverage: 0.826923
learned_at: 2026-10-11 20:53:42
nodes: [SaveVideo, MiniMaxH3ImageToVideo, SaveVideo, SaveVideo, UNETLoader, UNETLoader, KSamplerSelect, BasicScheduler, BasicScheduler, SamplerCustomAdvanced, VAEDecodeAudio, RandomNoise, BasicGuider, VAEDecode, CreateVideo, MiniMaxH3ImageToVideo, RandomNoise, BasicGuider, BasicGuider, RandomNoise, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, CreateVideo, SamplerCustomAdvanced, VAELoader, VAELoader, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, MarkdownNote, ResolutionSelector, MarkdownNote, SaveVideo, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadVideo, LoadVideo, LoadImage, LoadVideo, LoadImage, CLIPLoader, GetVideoComponents, GetVideoComponents, GetVideoComponents, LoadAudio, LoadAudio, LoadAudio, BasicGuider, RandomNoise, VAEDecode, VAEDecodeAudio, SamplerCustomAdvanced, CreateVideo, VAEDecode, VAEDecodeAudio, CreateVideo, LoadImage, MarkdownNote, MarkdownNote, MarkdownNote, LoraLoaderBypassModelOnly, MiniMaxH3DualClockSamplerT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MarkdownNote, MiniMaxH3ImageToVideo, LoraLoaderModelOnly, ImageResizeKJv2, PT_H3ConcatAVLatent, KSamplerSelect, BasicScheduler, VAEEncodeAudio, VAEEncode, BasicGuider, SamplerCustomAdvanced, VAEDecode, CreateVideo, MarkdownNote, ResolutionSelector, ComfyMathExpression, ComfySwitchNode, ComfySwitchNode, MiniMaxH3ReferenceToVideo, ComfySwitchNode, PrimitiveInt, ResolutionSelector, MarkdownNote, PrimitiveInt, LoadImage, PrimitiveFloat, PrimitiveStringMultiline, LoadImage]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMax H3多合一｜Turbo4 + Sage + T8 Stable｜R2V Turbo6 EXP + 二采增强版｜B站UP主@好奇漫步_2086836147753410562.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3多合一｜Turbo4 + Sage + T8 Stable｜R2V Turbo6 EXP + 二采增强版｜B站UP主@好奇漫步_2086836147753410562.json`

## 结构

**生成流程**：Model → Encode → Latent → Sampling → Decode → Process → Output → Other

**节点**（104 个）：
- `SaveVideo`
- `MiniMaxH3ImageToVideo`
- `SaveVideo`
- `SaveVideo`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeAudio` ★核心
- `RandomNoise`
- `BasicGuider`
- `VAEDecode` ★核心
- `CreateVideo`
- `MiniMaxH3ImageToVideo`
- `RandomNoise`
- `BasicGuider`
- `BasicGuider`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `CreateVideo`
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `VAELoader`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `MarkdownNote`
- `ResolutionSelector`
- `MarkdownNote`
- `SaveVideo`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadVideo`
- `LoadVideo`
- `LoadImage`
- `LoadVideo`
- `LoadImage`
- `CLIPLoader`
- `GetVideoComponents`
- `GetVideoComponents`
- `GetVideoComponents`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `BasicGuider`
- `RandomNoise`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `CreateVideo`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `CreateVideo`
- `LoadImage`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3DualClockSamplerT8` ★核心
- `MiniMaxH3DualClockSamplerT8` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3DualClockSamplerT8` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MarkdownNote`
- `MiniMaxH3ImageToVideo`
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
- `PT_H3ConcatAVLatent`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `VAEEncodeAudio` ★核心
- `VAEEncode` ★核心
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `CreateVideo`
- `MarkdownNote`
- `ResolutionSelector`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `MiniMaxH3ReferenceToVideo`
- `ComfySwitchNode`
- `PrimitiveInt`
- `ResolutionSelector`
- `MarkdownNote`
- `PrimitiveInt`
- `LoadImage`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `LoadImage`

## 知识

覆盖率 **83%**（86/104）

**有卡**：`SaveVideo`、`MiniMaxH3ImageToVideo`、`UNETLoader`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`VAEDecodeAudio`、`RandomNoise`、`BasicGuider`、`VAEDecode`、`CreateVideo`、`VAELoader`、`ComfyMathExpression`、`ResolutionSelector`、`LoadImage`、`LoadVideo`、`CLIPLoader`、`GetVideoComponents`、`LoadAudio`、`LoraLoaderBypassModelOnly`、`MiniMaxH3DualClockSamplerT8`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`PT_H3ConcatAVLatent`、`VAEEncodeAudio`、`VAEEncode`、`MiniMaxH3ReferenceToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
