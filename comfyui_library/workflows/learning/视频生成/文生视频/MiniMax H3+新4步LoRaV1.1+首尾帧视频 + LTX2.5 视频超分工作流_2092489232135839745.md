---
key: 视频生成/文生视频/MiniMax H3+新4步LoRaV1.1+首尾帧视频 + LTX2.5 视频超分工作流_2092489232135839745.json
name: MiniMax H3+新4步LoRaV1.1+首尾帧视频 + LTX2.5 视频超分工作流_2092489232135839745
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3+新4步LoRaV1.1+首尾帧视频 + LTX2.5 视频超分工作流_2092489232135839745.json
hash: 33d7f3c2989caf61
coverage: 0.632353
learned_at: 2026-10-11 21:30:22
nodes: [KSamplerSelect, BasicGuider, ComfyMathExpression, GetNode, GetNode, GetNode, SetNode, GetNode, Note, SetNode, easy clearCacheAll, MarkdownNote, MarkdownNote, SetNode, RandomNoise, VAEDecodeAudio, VAEDecode, easy cleanGpuUsed, GetNode, GetNode, SetNode, MiniMaxH3ImageToVideo, ImageScaleToMaxDimension, PrimitiveFloat, PrimitiveFloat, MarkdownNote, SamplerCustomAdvanced, MiniMaxH3SigmaShift, CLIPTextEncode, BasicScheduler, VisualizeSigmasKJ, RandomNoise, KSamplerSelect, LoadImage, VAELoader, VAELoader, CLIPLoader, VAELoader, VAELoader, SetNode, SetNode, Note, LoraLoaderModelOnly, LTXAVTextEncoderLoader, VHS_VideoCombine, VHS_VideoCombine, Note, SpectrumApplyMiniMaxH3, SolAttnPatch, UNETLoader, UNETLoader, LoraLoaderModelOnly, LTXVSpatioTemporalTiledVAEDecode, LTXVLoopingSampler, VAEEncodeTiled, LTXVConditioning, CFGGuider, ManualSigmas, LoraLoaderModelOnly, BasicScheduler, PathchSageAttentionKJ, LoadImage, ResizeImageMaskNode, ResizeImageMaskNode, SetNode, SetNode, ResolutionSelector, PrimitiveStringMultiline]
patterns: []
missing: [easy cleanGpuUsed, easy clearCacheAll]
discoveries: [次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/MiniMax H3+新4步LoRaV1.1+首尾帧视频 + LTX2.5 视频超分工作流_2092489232135839745.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3+新4步LoRaV1.1+首尾帧视频 + LTX2.5 视频超分工作流_2092489232135839745.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（68 个）：
- `KSamplerSelect` ★核心
- `BasicGuider`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `Note`
- `SetNode`
- `easy clearCacheAll`
- `MarkdownNote`
- `MarkdownNote`
- `SetNode`
- `RandomNoise`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `SetNode`
- `MiniMaxH3ImageToVideo`
- `ImageScaleToMaxDimension`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `MarkdownNote`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3SigmaShift`
- `CLIPTextEncode` ★核心
- `BasicScheduler`
- `VisualizeSigmasKJ`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `LoadImage`
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LTXAVTextEncoderLoader`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Note`
- `SpectrumApplyMiniMaxH3`
- `SolAttnPatch`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LTXVSpatioTemporalTiledVAEDecode` ★核心
- `LTXVLoopingSampler` ★核心
- `VAEEncodeTiled` ★核心
- `LTXVConditioning`
- `CFGGuider`
- `ManualSigmas`
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `PathchSageAttentionKJ`
- `LoadImage`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `SetNode`
- `SetNode`
- `ResolutionSelector`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **63%**（43/68）

**有卡**：`KSamplerSelect`、`BasicGuider`、`ComfyMathExpression`、`RandomNoise`、`VAEDecodeAudio`、`VAEDecode`、`MiniMaxH3ImageToVideo`、`ImageScaleToMaxDimension`、`SamplerCustomAdvanced`、`MiniMaxH3SigmaShift`、`CLIPTextEncode`、`BasicScheduler`、`VisualizeSigmasKJ`、`LoadImage`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`LTXAVTextEncoderLoader`、`VHS_VideoCombine`、`SpectrumApplyMiniMaxH3`、`SolAttnPatch`、`UNETLoader`、`LTXVSpatioTemporalTiledVAEDecode`、`LTXVLoopingSampler`、`VAEEncodeTiled`、`LTXVConditioning`、`CFGGuider`、`ManualSigmas`、`PathchSageAttentionKJ`、`ResizeImageMaskNode`、`ResolutionSelector`

**缺卡**（2）：`easy cleanGpuUsed`、`easy clearCacheAll`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader

## 学习发现

- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
