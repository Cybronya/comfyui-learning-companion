---
name: unknown_workflow_upscale_latent_upscale_sampler_17
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.4612
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [easy getNode, easy int, easy setNode, easy loraStack, easy loraStackApply]
members: [视频生成/图生视频/MiniMax H3-单模双采放大工作流_8G显存版__2106241845180329986.json, 视频生成/图生视频/MiniMax H3-多参考生视频-优化版_2098769440409219073.json, 视频生成/图生视频/MinimaxH3满血FP16+剪枝int8+浅空间放大二采工作流v4_2092911777758662657.json, 视频生成/文生视频/MINImax-H3_单人音乐MV制作_2094691958299123714.json, 视频生成/文生视频/minimaxH3混合模型不油腻_sigma强化+潜空间放大高清直出_2086021060973125633.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_17

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3-单模双采放大工作流_8G显存版__2106241845180329986.json、视频生成/图生视频/MiniMax H3-多参考生视频-优化版_2098769440409219073.json、视频生成/图生视频/MinimaxH3满血FP16+剪枝int8+浅空间放大二采工作流v4_2092911777758662657.json、视频生成/文生视频/MINImax-H3_单人音乐MV制作_2094691958299123714.json、视频生成/文生视频/minimaxH3混合模型不油腻_sigma强化+潜空间放大高清直出_2086021060973125633.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：46%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 4/5 个有
- `GetNode` —— 4/5 个有
- `ModelAttentionBackend` —— 4/5 个有
- `ModelPreviewOverrideKJ` —— 4/5 个有
- `SaveVideo` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `VAEDecodeAudio` —— 4/5 个有
- `H3SigmaRefiner` —— 3/5 个有
- `LoadAudio` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `PrimitiveStringMultiline` —— 3/5 个有
- `easy float` —— 3/5 个有
- `INTConstant` —— 2/5 个有
- `PathchSageAttentionKJ` —— 2/5 个有
- `ResizeShortestToNode` —— 2/5 个有
- `SolAttnMiniMax` —— 2/5 个有
- `Text Multiline` —— 2/5 个有
- `VHS_LoadVideo` —— 2/5 个有
- `VHS_VideoCombine` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `easy loraStack` —— 2/5 个有
- `easy loraStackApply` —— 2/5 个有
- `LoraLoaderBypassModelOnly` —— 1/5 个有
- `MuyeTextEditOutput` —— 1/5 个有
- `PreviewAudio` —— 1/5 个有
- `RHLLMChatNode` —— 1/5 个有
- `SoundFlow_GetLength` —— 1/5 个有
- `TrimAudioDuration` —— 1/5 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/5 个有
- `easy getNode` —— 1/5 个有
- `easy int` —— 1/5 个有
- `easy setNode` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：easy getNode、easy int、easy setNode、easy loraStack、easy loraStackApply
