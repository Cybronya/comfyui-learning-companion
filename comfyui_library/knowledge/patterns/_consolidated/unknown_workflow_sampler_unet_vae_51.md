---
name: unknown_workflow_sampler_unet_vae_51
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.72325
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Minimax-H3 文生视频_2084501246035185665.json, 视频生成/文生视频/Minimax-H3-T2V 开源版本+文生视频_2084249084893945858.json, 视频生成/文生视频/Minimax-H3-文生视频-sage+cache双重加速（5秒3.5分钟）_2084572415069351938.json, 视频生成/文生视频/Minimax-H3-文生视频BF16高质量768P-双重加速（T8-cache）_2085387569700888577.json, 视频生成/文生视频/Minimax-H3-文生视频（Lightx2v加速）_2085988885787660289.json, 视频生成/文生视频/Minimax-H3_T2V（文生视频_本地可用）_2084287507390353409.json, 视频生成/文生视频/Minimax-H3文生视频8步工作流_2095380668011343873.json, 视频生成/文生视频/Minimax-h3-文生视频_2084913245437128706.json, 视频生成/文生视频/MinimaxH3-文生视频（高质量）_2085617922352963586.json, 视频生成/文生视频/MinimaxH3文生视频 量化加速版_2084540140541792258.json, 视频生成/文生视频/MinimaxH3文生视频 量化加速版_2084680217980915713.json, 视频生成/文生视频/MinimaxH3首尾帧2倍速V2_2086280974836527106.json, 视频生成/文生视频/MinimaxH3首尾帧2倍速_2085198819909791746.json, 视频生成/文生视频/极速版-MiniMax H3全能单图&多图&首尾&宫格图-动态去高躁_2088657311995879425.json, 视频生成/文生视频/极速版-MiniMax H3全能单图&多图&首尾&宫格图_2085050902129504257.json, 视频生成/文生视频/极速版-MiniMax H3全能单图&多图&首尾&宫格图_2087936662021173250.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_51

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/文生视频/Minimax-H3 文生视频_2084501246035185665.json、视频生成/文生视频/Minimax-H3-T2V 开源版本+文生视频_2084249084893945858.json、视频生成/文生视频/Minimax-H3-文生视频-sage+cache双重加速（5秒3.5分钟）_2084572415069351938.json、视频生成/文生视频/Minimax-H3-文生视频BF16高质量768P-双重加速（T8-cache）_2085387569700888577.json、视频生成/文生视频/Minimax-H3-文生视频（Lightx2v加速）_2085988885787660289.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 16 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3ImageToVideo` —— 13/16 个有
- `CreateVideo` —— 12/16 个有
- `SaveVideo` —— 12/16 个有
- `PathchSageAttentionKJ` —— 11/16 个有
- `GetNode` —— 7/16 个有
- `SetNode` —— 7/16 个有
- `CR Prompt Text` —— 6/16 个有
- `EasyCache` —— 6/16 个有
- `LoadImage` —— 5/16 个有
- `LoraLoaderModelOnly` —— 5/16 个有
- `MiniMaxH3BlockCacheT8` —— 5/16 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 4/16 个有
- `SolAttnPatch` —— 4/16 个有
- `VHS_VideoCombine` —— 4/16 个有
- `Int` —— 3/16 个有
- `MiniMaxH3ReferenceToVideo` —— 3/16 个有
- `ModelPatchTorchSettings` —— 3/16 个有
- `Text` —— 3/16 个有
- `Float` —— 2/16 个有
- `PrimitiveStringMultiline` —— 2/16 个有
- `RTXVideoSuperResolution` —— 2/16 个有
- `ExtendIntermediateSigmas` —— 1/16 个有
- `H3SigmaRefiner` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
