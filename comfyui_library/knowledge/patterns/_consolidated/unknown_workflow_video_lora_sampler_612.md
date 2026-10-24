---
name: unknown_workflow_video_lora_sampler_612
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.666667
common_nodes: [BasicGuider, BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, GetNode, ImageScaleToMaxDimension, KSamplerSelect, LTXAVTextEncoderLoader, LTXVConditioning, LTXVLoopingSampler, LTXVSpatioTemporalTiledVAEDecode, LoadImage, LoraLoaderModelOnly, ManualSigmas, MiniMaxH3SigmaShift, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, SolAttnPatch, SpectrumApplyMiniMaxH3, UNETLoader, VAEDecode, VAEDecodeAudio, VAEEncodeTiled, VAELoader, VHS_VideoCombine, VisualizeSigmasKJ, easy cleanGpuUsed, easy clearCacheAll]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax 4步 LoRa 加速 首尾帧视频 + Ltx 视频放大工作流_2085659057788121090.json, 视频生成/图生视频/MiniMax H3  ref-多参考注入 - 4步加速 视频生成+LTX放大工作流_2085936299189563393.json, 视频生成/文生视频/MiniMax H3+新4步LoRaV1.1+首尾帧视频 + LTX2.5 视频超分工作流_2092489232135839745.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_612

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/MiniMax 4步 LoRa 加速 首尾帧视频 + Ltx 视频放大工作流_2085659057788121090.json、视频生成/图生视频/MiniMax H3  ref-多参考注入 - 4步加速 视频生成+LTX放大工作流_2085936299189563393.json、视频生成/文生视频/MiniMax H3+新4步LoRaV1.1+首尾帧视频 + LTX2.5 视频超分工作流_2092489232135839745.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `GetNode`
- `ImageScaleToMaxDimension`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVConditioning`
- `LTXVLoopingSampler`
- `LTXVSpatioTemporalTiledVAEDecode`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MiniMaxH3SigmaShift`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `SolAttnPatch`
- `SpectrumApplyMiniMaxH3`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAEEncodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ImageToVideo` —— 2/3 个有
- `ResizeImageMaskNode` —— 2/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `LTXVAudioVAELoader` —— 1/3 个有
- `MiniMaxH3ReferenceToVideo` —— 1/3 个有
- `VHS_LoadAudio` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
