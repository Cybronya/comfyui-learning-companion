---
name: unknown_workflow_sampler_unet_vae_19
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.717765
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Minimax-H3-T2V 开源版本+文生视频_2084249084893945858.json, 视频生成/文生视频/Minimax-H3-文生视频-sage+cache双重加速（5秒3.5分钟）_2084572415069351938.json, 视频生成/文生视频/Minimax-H3-文生视频BF16高质量768P-双重加速（T8-cache）_2085387569700888577.json, 视频生成/文生视频/Minimax-H3-文生视频（Lightx2v加速）_2085988885787660289.json, 视频生成/文生视频/Minimax-H3-文生视频（Lightx2v正式版）_2087549637837283330.json, 视频生成/文生视频/Minimax-H3_T2V（文生视频_本地可用）_2084287507390353409.json, 视频生成/文生视频/Minimax-H3文生视频8步工作流_2095380668011343873.json, 视频生成/文生视频/MinimaxH3-文生视频（高质量）_2085617922352963586.json, 视频生成/文生视频/MinimaxH3文生视频 量化加速版_2084540140541792258.json, 视频生成/文生视频/MinimaxH3文生视频 量化加速版_2084680217980915713.json, 视频生成/文生视频/MinimaxH3首尾帧2倍速V2_2086280974836527106.json, 视频生成/文生视频/MinimaxH3首尾帧2倍速_2085198819909791746.json, 视频生成/文生视频/Minimax文生视频(2倍速！量化加速版)_2084823710980206594.json, 视频生成/文生视频/乡野爬山好风光_2087832652211638274.json, 视频生成/文生视频/极速版-MiniMax H3全能单图&多图&首尾&宫格图-动态去高躁_2088657311995879425.json, 视频生成/文生视频/极速版-MiniMax H3全能单图&多图&首尾&宫格图_2085050902129504257.json, 视频生成/文生视频/极速版-MiniMax H3全能单图&多图&首尾&宫格图_2087936662021173250.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_19

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/文生视频/Minimax-H3-T2V 开源版本+文生视频_2084249084893945858.json、视频生成/文生视频/Minimax-H3-文生视频-sage+cache双重加速（5秒3.5分钟）_2084572415069351938.json、视频生成/文生视频/Minimax-H3-文生视频BF16高质量768P-双重加速（T8-cache）_2085387569700888577.json、视频生成/文生视频/Minimax-H3-文生视频（Lightx2v加速）_2085988885787660289.json、视频生成/文生视频/Minimax-H3-文生视频（Lightx2v正式版）_2087549637837283330.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 17 个 workflow 都包含：
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
- `CreateVideo` —— 14/17 个有
- `SaveVideo` —— 14/17 个有
- `MiniMaxH3ImageToVideo` —— 13/17 个有
- `PathchSageAttentionKJ` —— 11/17 个有
- `CR Prompt Text` —— 8/17 个有
- `EasyCache` —— 8/17 个有
- `GetNode` —— 7/17 个有
- `SetNode` —— 7/17 个有
- `LoadImage` —— 6/17 个有
- `LoraLoaderModelOnly` —— 6/17 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 6/17 个有
- `MiniMaxH3BlockCacheT8` —— 5/17 个有
- `MiniMaxH3ReferenceToVideo` —— 4/17 个有
- `SolAttnPatch` —— 4/17 个有
- `Int` —— 3/17 个有
- `ModelPatchTorchSettings` —— 3/17 个有
- `Text` —— 3/17 个有
- `VHS_VideoCombine` —— 3/17 个有
- `Float` —— 2/17 个有
- `RTXVideoSuperResolution` —— 2/17 个有
- `ExtendIntermediateSigmas` —— 1/17 个有
- `Fast Groups Bypasser (rgthree)` —— 1/17 个有
- `H3SigmaRefiner` —— 1/17 个有
- `ModelAttentionBackend` —— 1/17 个有
- `PrimitiveStringMultiline` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
