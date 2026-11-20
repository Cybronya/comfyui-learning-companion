---
key: 平台全量/MinimaxH3动作迁移Alissonerdx双Lora结合v2_2120088484382859266.json
name: MinimaxH3动作迁移Alissonerdx双Lora结合v2_2120088484382859266
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/MinimaxH3动作迁移Alissonerdx双Lora结合v2_2120088484382859266.json
hash: 2e44048e686b7a60
coverage: 0.385827
learned_at: 2026-11-14 00:46:02
nodes: [SetNode, SetNode, SetNode, SetNode, GetNode, ComfyNumberConvert, SetNode, SetNode, PrimitiveInt, CLIPLoader, CLIPLoader, VAELoader, VAELoader, GetNode, ComfyMathExpression, MiniMaxH3SigmaShift, GetNode, PrimitiveFloat, UNETLoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, ImageResizeKJv2, GetImageSize, GetNode, SetNode, VAEDecode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, VHS_VideoInfo, SetNode, GetNode, MiniMaxH3AddGuide, BasicGuider, GetNode, ModelPreviewOverrideKJ, SetNode, SetNode, SetNode, GetNode, GetNode, VAEDecode, GetNode, SetNode, LTXVSeparateAVLatent, MarkdownNote, SetNode, SetNode, CFGGuider, ModelPreviewOverrideKJ, RandomNoise, SetNode, SamplerCustomAdvanced, SamplerCustomAdvanced, GetNode, MiniMaxH3ReferenceToVideo, StringConcatenate, GetNode, VHS_VideoCombine, GetNode, SetNode, SetNode, GetNode, GetNode, SetNode, ManualSigmas, GetNode, ModelAttentionBackend, GetNode, GetNode, LoadImage, LoraLoaderModelOnly, SetNode, MiniMaxH3AddGuide, GetNode, ManualSigmas, GetNode, LoraLoaderModelOnly, GetNode, MiniMaxH3ReferenceToVideo, GetNode, LoraLoaderModelOnly, KSamplerSelect, BasicScheduler, ResolutionSelector, MarkdownNote, LoadImage, ResizeImageMaskNode, LoadImage, ResizeImageMaskNode, LoadImage, ResizeImageMaskNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, PrimitiveStringMultiline, MarkdownNote, VHS_LoadVideo, GetNode, ImageResizeKJv2, BFSMiniMaxH3NativeTemporal, GetNode, LoraLoaderModelOnly, GetNode, LoraLoaderModelOnly, easy cleanGpuUsed, MarkdownNote]
patterns: []
missing: []
---

# 平台全量/MinimaxH3动作迁移Alissonerdx双Lora结合v2_2120088484382859266.json

> 来源文件 `comfyui_library/workflows/平台全量/MinimaxH3动作迁移Alissonerdx双Lora结合v2_2120088484382859266.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（127 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `ComfyNumberConvert`
- `SetNode`
- `SetNode`
- `PrimitiveInt`
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `GetNode`
- `ComfyMathExpression`
- `MiniMaxH3SigmaShift`
- `GetNode`
- `PrimitiveFloat`
- `UNETLoader` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `GetImageSize`
- `GetNode`
- `SetNode`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `GetNode`
- `MiniMaxH3AddGuide`
- `BasicGuider`
- `GetNode`
- `ModelPreviewOverrideKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `SetNode`
- `LTXVSeparateAVLatent`
- `MarkdownNote`
- `SetNode`
- `SetNode`
- `CFGGuider`
- `ModelPreviewOverrideKJ`
- `RandomNoise`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `MiniMaxH3ReferenceToVideo`
- `StringConcatenate`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ManualSigmas`
- `GetNode`
- `ModelAttentionBackend`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `MiniMaxH3AddGuide`
- `GetNode`
- `ManualSigmas`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `MiniMaxH3ReferenceToVideo`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `ResolutionSelector`
- `MarkdownNote`
- `LoadImage`
- `ResizeImageMaskNode`
- `LoadImage`
- `ResizeImageMaskNode`
- `LoadImage`
- `ResizeImageMaskNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `VHS_LoadVideo`
- `GetNode`
- `ImageResizeKJv2`
- `BFSMiniMaxH3NativeTemporal`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `easy cleanGpuUsed`
- `MarkdownNote`

## 知识

覆盖率 **39%**（49/127）

**有卡**：`ComfyNumberConvert`、`CLIPLoader`、`VAELoader`、`ComfyMathExpression`、`MiniMaxH3SigmaShift`、`UNETLoader`、`ImageResizeKJv2`、`GetImageSize`、`VAEDecode`、`VHS_VideoInfo`、`MiniMaxH3AddGuide`、`BasicGuider`、`ModelPreviewOverrideKJ`、`LTXVSeparateAVLatent`、`CFGGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`MiniMaxH3ReferenceToVideo`、`StringConcatenate`、`VHS_VideoCombine`、`ManualSigmas`、`ModelAttentionBackend`、`LoadImage`、`LoraLoaderModelOnly`、`KSamplerSelect`、`BasicScheduler`、`ResolutionSelector`、`ResizeImageMaskNode`、`VHS_LoadVideo`、`BFSMiniMaxH3NativeTemporal`、`easy cleanGpuUsed`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、CFGGuider
