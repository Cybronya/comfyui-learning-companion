---
name: unknown_workflow_video_upscale_latent_upscale_54
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.485429
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, GetNode, H3SigmaRefiner, KSamplerSelect, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, PT_H3ConcatAVLatent, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/SG+10EROS_V1双采极速高清_2117952691287707649.json, 数字人/数字人/MinimaxH3数字人&MV_2113933975927476225.json, 视频生成/图生视频/Minimax H3 二采首尾帧 + 参考音_2092200990517850113.json, 视频生成/图生视频/Minimax H3 参考生视频+高动态-自用版+可生成20s+视频_2107384460193918978.json, 视频生成/图生视频/Minimax H3 图_参考生视频+高动态_2095019320052117505.json, 视频生成/图生视频/Minimax H3 图生视频（二采）+1参考音【批量管理系统API用】_2093589690120228865.json, 视频生成/图生视频/Minimax H3 图生视频（无参考音）【批量管理系统api用】_2093586371775647745.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_54

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/SG+10EROS_V1双采极速高清_2117952691287707649.json、数字人/数字人/MinimaxH3数字人&MV_2113933975927476225.json、视频生成/图生视频/Minimax H3 二采首尾帧 + 参考音_2092200990517850113.json、视频生成/图生视频/Minimax H3 参考生视频+高动态-自用版+可生成20s+视频_2107384460193918978.json、视频生成/图生视频/Minimax H3 图_参考生视频+高动态_2095019320052117505.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：49%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `GetNode`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LTXVSeparateAVLatent`
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
- `ComfyMathExpression` —— 6/7 个有
- `LayerUtility: PurgeVRAM V2` —— 6/7 个有
- `LoadAudio` —— 6/7 个有
- `MiniMaxLowVRAMAttention` —— 5/7 个有
- `ResolutionSelector` —— 5/7 个有
- `Fast Groups Bypasser (rgthree)` —— 4/7 个有
- `BlockSparseAttention` —— 3/7 个有
- `SplitSigmas` —— 3/7 个有
- `easy showAnything` —— 3/7 个有
- `FrameInterpolate` —— 2/7 个有
- `FrameInterpolationModelLoader` —— 2/7 个有
- `LayerColor: Brightness & Contrast` —— 2/7 个有
- `Any Switch (rgthree)` —— 1/7 个有
- `CFGGuider` —— 1/7 个有
- `GetVideoComponents` —— 1/7 个有
- `LTXVAudioVAEEncode` —— 1/7 个有
- `LTXVConcatAVLatent` —— 1/7 个有
- `LazySwitchKJ` —— 1/7 个有
- `LoadVideo` —— 1/7 个有
- `MathExpression|pysssss` —— 1/7 个有
- `MiniMaxChunkFeedForward` —— 1/7 个有
- `ModelAttentionBackend` —— 1/7 个有
- `SetLatentNoiseMask` —— 1/7 个有
- `SolAttnPatch` —— 1/7 个有
- `SolidMask` —— 1/7 个有
- `SoundFlow_GetLength` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
