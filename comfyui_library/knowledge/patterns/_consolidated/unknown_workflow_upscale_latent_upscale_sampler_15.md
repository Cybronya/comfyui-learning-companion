---
name: unknown_workflow_upscale_latent_upscale_sampler_15
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.689125
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3-单模双采放大工作流（8G显存版）_2106241845180329986.json, 视频生成/图生视频/MiniMaxH3+lightx2v加速不油版-单双采_2084916996847792130.json, 视频生成/图生视频/MiniMax_H3_二次采样+放大文戏工作流_2096179690426949633.json, 视频生成/图生视频/MiniMax_H3_二次采样+放大武器对决工作流_2096593027769913345.json, 视频生成/图生视频/MiniMax_H3_二次采样+放大武戏工作流_2096227914462355458.json, 视频生成/图生视频/Minimax H3 多图参考 真实感极佳_2092151387793747970.json, 视频生成/图生视频/Minimax H3双模双采工作流-小脸不崩-脸不油，高动态不崩脸_2093185884203085826.json, 视频生成/图生视频/短剧助手：MiniMax H3 双模双采资源面板加载生成视频_2093912808089014274.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_15

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3-单模双采放大工作流（8G显存版）_2106241845180329986.json、视频生成/图生视频/MiniMaxH3+lightx2v加速不油版-单双采_2084916996847792130.json、视频生成/图生视频/MiniMax_H3_二次采样+放大文戏工作流_2096179690426949633.json、视频生成/图生视频/MiniMax_H3_二次采样+放大武器对决工作流_2096593027769913345.json、视频生成/图生视频/MiniMax_H3_二次采样+放大武戏工作流_2096227914462355458.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 7/8 个有
- `LoraLoaderModelOnly` —— 7/8 个有
- `GetNode` —— 6/8 个有
- `SetNode` —— 6/8 个有
- `SplitSigmas` —— 6/8 个有
- `H3SigmaRefiner` —— 5/8 个有
- `MiniMaxH3SigmaShift` —— 5/8 个有
- `ModelAttentionBackend` —— 5/8 个有
- `ModelPreviewOverrideKJ` —— 5/8 个有
- `easy cleanGpuUsed` —— 5/8 个有
- `CR Prompt Text` —— 4/8 个有
- `PrimitiveStringMultiline` —— 4/8 个有
- `MiniMaxLowVRAMAttention` —— 3/8 个有
- `孤海注释` —— 3/8 个有
- `ExtendIntermediateSigmas` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `SplitSigmasDenoise` —— 2/8 个有
- `Anything Everywhere` —— 1/8 个有
- `Anything Everywhere3` —— 1/8 个有
- `DF_Integer` —— 1/8 个有
- `MiniMaxH3MediaLoaderFantastic` —— 1/8 个有
- `MiniMaxH3ReferenceSplitter` —— 1/8 个有
- `PathchSageAttentionKJ` —— 1/8 个有
- `StringConcatenate` —— 1/8 个有
- `easy getNode` —— 1/8 个有
- `easy int` —— 1/8 个有
- `easy loraStack` —— 1/8 个有
- `easy loraStackApply` —— 1/8 个有
- `easy setNode` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
