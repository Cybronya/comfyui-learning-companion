---
name: unknown_workflow_video_lora_sampler_670
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.678
common_nodes: [BasicGuider, BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, GetNode, ImageScaleToMaxDimension, KSamplerSelect, LTXAVTextEncoderLoader, LTXVConditioning, LTXVLoopingSampler, LTXVSpatioTemporalTiledVAEDecode, LoadImage, LoraLoaderModelOnly, ManualSigmas, MiniMaxH3SigmaShift, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAEEncodeTiled, VAELoader, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/MiniMax-H3 V2V 视频到视频内容替换工作流_2086848877948399617.json, 视频生成/图生视频/MiniMax 4步 LoRa 加速 首尾帧视频 + Ltx 视频放大工作流_2085659057788121090.json, 视频生成/图生视频/MiniMax H3  ref-多参考注入 - 4步加速 视频生成+LTX放大工作流_2085936299189563393.json, 视频生成/文生视频/MiniMax H3+新4步LoRaV1.1+首尾帧视频 + LTX2.5 视频超分工作流_2092489232135839745.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_670

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/MiniMax-H3 V2V 视频到视频内容替换工作流_2086848877948399617.json、视频生成/图生视频/MiniMax 4步 LoRa 加速 首尾帧视频 + Ltx 视频放大工作流_2085659057788121090.json、视频生成/图生视频/MiniMax H3  ref-多参考注入 - 4步加速 视频生成+LTX放大工作流_2085936299189563393.json、视频生成/文生视频/MiniMax H3+新4步LoRaV1.1+首尾帧视频 + LTX2.5 视频超分工作流_2092489232135839745.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 4 个 workflow 都包含：
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
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAEEncodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `SolAttnPatch` —— 3/4 个有
- `SpectrumApplyMiniMaxH3` —— 3/4 个有
- `VisualizeSigmasKJ` —— 3/4 个有
- `easy clearCacheAll` —— 3/4 个有
- `CheckpointLoaderSimple` —— 2/4 个有
- `LTXVAudioVAELoader` —— 2/4 个有
- `MiniMaxH3ImageToVideo` —— 2/4 个有
- `MiniMaxH3ReferenceToVideo` —— 2/4 个有
- `ResizeImageMaskNode` —— 2/4 个有
- `AIO_Preprocessor` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `VHS_LoadAudio` —— 1/4 个有
- `VHS_LoadVideo` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
