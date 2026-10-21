---
name: unknown_workflow_upscale_latent_upscale_lora_40
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.682625
common_nodes: [CLIPLoader, ComfyMathExpression, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MinimaxH3LatentUpscaler3D, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMaxH3_图生视频_双采CFG0.5_1.5_SAGE_2110265220198395905.json, 视频生成/图生视频/Minimax-H3-多参图生视频+双采+Lantent upscale放大_2091376603443064833.json, 视频生成/图生视频/MinimaxH3_高动态_Singularity-(新)分段采样进阶工作流_2104944269617352706.json, 视频生成/图生视频/minimax h3_ref2va-dasiwa-zs05可选双采_2092257046572920834.json, 视频生成/图生视频/小脸不崩！打斗不糊！H3 sigma强化+潜空间放大工作流（不油啦！）_2089513420025589761.json, 视频生成/图生视频/海螺H3 小脸不崩！动态不糊！人物不油！Minimax H3开源双模双采短剧漫剧图生视频_2091875924642975746.json, 视频生成/图生视频/短剧助手：MiniMax H3 双模双采资源面板加载生成视频_2093912808089014274.json, 视频生成/文生视频/MiniMax-H3 极限复杂大动态与人脸去油腻工作流_2096278728602112001.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_40

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MiniMaxH3_图生视频_双采CFG0.5_1.5_SAGE_2110265220198395905.json、视频生成/图生视频/Minimax-H3-多参图生视频+双采+Lantent upscale放大_2091376603443064833.json、视频生成/图生视频/MinimaxH3_高动态_Singularity-(新)分段采样进阶工作流_2104944269617352706.json、视频生成/图生视频/minimax h3_ref2va-dasiwa-zs05可选双采_2092257046572920834.json、视频生成/图生视频/小脸不崩！打斗不糊！H3 sigma强化+潜空间放大工作流（不油啦！）_2089513420025589761.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 7/8 个有
- `BasicScheduler` —— 7/8 个有
- `LoadImage` —— 7/8 个有
- `ResolutionSelector` —— 7/8 个有
- `CreateVideo` —— 6/8 个有
- `ModelAttentionBackend` —— 6/8 个有
- `ModelPreviewOverrideKJ` —— 6/8 个有
- `PrimitiveStringMultiline` —— 6/8 个有
- `SaveVideo` —— 6/8 个有
- `GetNode` —— 5/8 个有
- `SetNode` —— 5/8 个有
- `H3SigmaRefiner` —— 3/8 个有
- `Label (rgthree)` —— 3/8 个有
- `ManualSigmas` —— 3/8 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 3/8 个有
- `MiniMaxLowVRAMAttention` —— 3/8 个有
- `ConditioningZeroOut` —— 2/8 个有
- `PathchSageAttentionKJ` —— 2/8 个有
- `VHS_VideoCombine` —— 2/8 个有
- `VRAM_Debug` —— 2/8 个有
- `easy cleanGpuUsed` —— 2/8 个有
- `Anything Everywhere` —— 1/8 个有
- `Anything Everywhere3` —— 1/8 个有
- `CFGGuider` —— 1/8 个有
- `CR Prompt Text` —— 1/8 个有
- `ComfySwitchNode` —— 1/8 个有
- `DF_Integer` —— 1/8 个有
- `DisableNoise` —— 1/8 个有
- `MiniMaxChunkFeedForward` —— 1/8 个有
- `MiniMaxH3MediaLoaderFantastic` —— 1/8 个有
- `MiniMaxH3ReferenceSplitter` —— 1/8 个有
- `StringConcatenate` —— 1/8 个有
- `UniBlockSwap` —— 1/8 个有
- `布尔孤海` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
