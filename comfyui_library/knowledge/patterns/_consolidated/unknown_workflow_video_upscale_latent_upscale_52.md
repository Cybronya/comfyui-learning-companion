---
name: unknown_workflow_video_upscale_latent_upscale_52
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.515571
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, GetNode, H3SigmaRefiner, KSamplerSelect, LTXVSeparateAVLatent, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, PT_H3ConcatAVLatent, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [数字人/数字人/MinimaxH3数字人&MV_2113933975927476225.json, 视频生成/图生视频/Minimax H3 二采首尾帧 + 参考音_2092200990517850113.json, 视频生成/图生视频/Minimax H3 参考生视频+高动态-自用版+可生成20s+视频_2107384460193918978.json, 视频生成/图生视频/Minimax H3 图_参考生视频+高动态_2095019320052117505.json, 视频生成/图生视频/Minimax H3 图生视频（二采）+1参考音【批量管理系统API用】_2093589690120228865.json, 视频生成/图生视频/Minimax H3 图生视频（无参考音）【批量管理系统api用】_2093586371775647745.json, 视频生成/图生视频/MinimaxH3 通用流_2111286575966539778.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_52

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/MinimaxH3数字人&MV_2113933975927476225.json、视频生成/图生视频/Minimax H3 二采首尾帧 + 参考音_2092200990517850113.json、视频生成/图生视频/Minimax H3 参考生视频+高动态-自用版+可生成20s+视频_2107384460193918978.json、视频生成/图生视频/Minimax H3 图_参考生视频+高动态_2095019320052117505.json、视频生成/图生视频/Minimax H3 图生视频（二采）+1参考音【批量管理系统API用】_2093589690120228865.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：52%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `GetNode`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LTXVSeparateAVLatent`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `MinimaxH3LatentUpscaler3D`
- `PT_H3ConcatAVLatent`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 6/7 个有
- `MiniMaxLowVRAMAttention` —— 5/7 个有
- `Fast Groups Bypasser (rgthree)` —— 4/7 个有
- `ResolutionSelector` —— 4/7 个有
- `BlockSparseAttention` —— 3/7 个有
- `SplitSigmas` —— 3/7 个有
- `easy showAnything` —— 3/7 个有
- `FrameInterpolate` —— 2/7 个有
- `FrameInterpolationModelLoader` —— 2/7 个有
- `LayerColor: Brightness & Contrast` —— 2/7 个有
- `Any Switch (rgthree)` —— 1/7 个有
- `LTXVAudioVAEEncode` —— 1/7 个有
- `LTXVConcatAVLatent` —— 1/7 个有
- `LayerUtility: BooleanOperator` —— 1/7 个有
- `MiniMaxChunkFeedForward` —— 1/7 个有
- `RTXVideoFrameGeneration` —— 1/7 个有
- `RTXVideoSuperResolution` —— 1/7 个有
- `SetLatentNoiseMask` —— 1/7 个有
- `SolAttnPatch` —— 1/7 个有
- `SolidMask` —— 1/7 个有
- `SoundFlow_GetLength` —— 1/7 个有
- `VHS_LoadVideo` —— 1/7 个有
- `easy ifElse` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
