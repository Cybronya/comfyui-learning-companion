---
key: 视频生成/文生视频/MiniMax_H3三合一_V2｜ComfyUI0.33_Core｜LightX2V_v1_4Ste_2088301834657157121.json
name: MiniMax_H3三合一_V2｜ComfyUI0.33_Core｜LightX2V_v1_4Ste_2088301834657157121
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax_H3三合一_V2｜ComfyUI0.33_Core｜LightX2V_v1_4Ste_2088301834657157121.json
hash: 1509427d6a86451c
coverage: 0.758065
learned_at: 2026-10-15 22:46:30
nodes: [UNETLoader, UNETLoader, KSamplerSelect, VAEDecodeAudio, RandomNoise, BasicGuider, VAEDecode, MiniMaxH3ImageToVideo, RandomNoise, BasicGuider, VAEDecode, VAEDecodeAudio, CreateVideo, SamplerCustomAdvanced, VAELoader, VAELoader, ComfyMathExpression, ResolutionSelector, MarkdownNote, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadVideo, LoadVideo, LoadImage, LoadVideo, CLIPLoader, GetVideoComponents, GetVideoComponents, GetVideoComponents, LoadAudio, LoadAudio, LoadAudio, BasicGuider, RandomNoise, VAEDecode, VAEDecodeAudio, SamplerCustomAdvanced, CreateVideo, LoadImage, MarkdownNote, MiniMaxH3SigmaShift, MiniMaxH3SigmaShift, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ImageToVideo, ResolutionSelector, ComfySwitchNode, MiniMaxH3ReferenceToVideo, ResolutionSelector, MarkdownNote, LoadImage, PrimitiveInt, ComfyMathExpression, PrimitiveInt, GetVideoComponents, MiniMaxH3ImageToVideo, MiniMaxH3ImageToVideo, ImageResizeKJv2, VAEEncode, VAEEncodeAudio, MiniMaxH3ReferenceToVideo, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, ComfySwitchNode, PT_H3ConcatAVLatent, KSamplerSelect, ComfySwitchNode, CreateVideo, SaveVideo, MarkdownNote, BasicScheduler, SamplerCustomAdvanced, CreateVideo, ComfyMathExpression, ComfyMathExpression, ComfySwitchNode, ComfySwitchNode, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, SamplerCustomAdvanced, BasicScheduler, BasicScheduler, BasicScheduler, VAEDecode, BasicGuider, MarkdownNote, MarkdownNote, MarkdownNote, LoadImage, MarkdownNote, MarkdownNote, MarkdownNote, LoadImage, LoadImage, LoadImage, WidgetToString, WidgetToString, WidgetToString, WidgetToString, WidgetToString, ComfySwitchNode, ComfySwitchNode, Get Date Time String (JPS), StringFunction|pysssss, StringFunction|pysssss, StringFunction|pysssss, SaveText|pysssss, ShowText|pysssss, MarkdownNote, KSamplerSelect, BasicScheduler, KSamplerSelect, BasicScheduler, MiniMaxH3SigmaShift, LoraLoaderBypassModelOnly, PrimitiveStringMultiline, PrimitiveFloat]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMax_H3三合一_V2｜ComfyUI0.33_Core｜LightX2V_v1_4Ste_2088301834657157121.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax_H3三合一_V2｜ComfyUI0.33_Core｜LightX2V_v1_4Ste_2088301834657157121.json`

## 结构

**生成流程**：Model → Encode → Latent → Sampling → Decode → Process → Output → Other

**节点**（124 个）：
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `KSamplerSelect` ★核心
- `VAEDecodeAudio` ★核心
- `RandomNoise`
- `BasicGuider`
- `VAEDecode` ★核心
- `MiniMaxH3ImageToVideo`
- `RandomNoise`
- `BasicGuider`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `CreateVideo`
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `VAELoader`
- `ComfyMathExpression`
- `ResolutionSelector`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadVideo`
- `LoadVideo`
- `LoadImage`
- `LoadVideo`
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
- `LoadImage`
- `MarkdownNote`
- `MiniMaxH3SigmaShift`
- `MiniMaxH3SigmaShift`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ImageToVideo`
- `ResolutionSelector`
- `ComfySwitchNode`
- `MiniMaxH3ReferenceToVideo`
- `ResolutionSelector`
- `MarkdownNote`
- `LoadImage`
- `PrimitiveInt`
- `ComfyMathExpression`
- `PrimitiveInt`
- `GetVideoComponents`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3ImageToVideo`
- `ImageResizeKJv2`
- `VAEEncode` ★核心
- `VAEEncodeAudio` ★核心
- `MiniMaxH3ReferenceToVideo`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `PT_H3ConcatAVLatent`
- `KSamplerSelect` ★核心
- `ComfySwitchNode`
- `CreateVideo`
- `SaveVideo`
- `MarkdownNote`
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `CreateVideo`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderModelOnly` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `BasicScheduler`
- `BasicScheduler`
- `VAEDecode` ★核心
- `BasicGuider`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `WidgetToString`
- `WidgetToString`
- `WidgetToString`
- `WidgetToString`
- `WidgetToString`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `Get Date Time String (JPS)`
- `StringFunction|pysssss`
- `StringFunction|pysssss`
- `StringFunction|pysssss`
- `SaveText|pysssss`
- `ShowText|pysssss`
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `MiniMaxH3SigmaShift`
- `LoraLoaderBypassModelOnly` ★核心
- `PrimitiveStringMultiline`
- `PrimitiveFloat`

## 知识

覆盖率 **76%**（94/124）

**有卡**：`UNETLoader`、`KSamplerSelect`、`VAEDecodeAudio`、`RandomNoise`、`BasicGuider`、`VAEDecode`、`MiniMaxH3ImageToVideo`、`CreateVideo`、`SamplerCustomAdvanced`、`VAELoader`、`ComfyMathExpression`、`ResolutionSelector`、`LoadImage`、`LoadVideo`、`CLIPLoader`、`GetVideoComponents`、`LoadAudio`、`MiniMaxH3SigmaShift`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3ReferenceToVideo`、`ImageResizeKJv2`、`VAEEncode`、`VAEEncodeAudio`、`PT_H3ConcatAVLatent`、`SaveVideo`、`BasicScheduler`、`LoraLoaderModelOnly`、`WidgetToString`、`Get Date Time String (JPS)`、`StringFunction|pysssss`、`SaveText|pysssss`、`LoraLoaderBypassModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
