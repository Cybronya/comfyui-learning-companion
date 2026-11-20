---
name: unknown_workflow_video_sampler_unet_45
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8448
common_nodes: [CLIPLoader, ComfyMathExpression, LoadImage, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/Minimax_H3 多图参考短剧制作，加速工作流_2088187262285729793.json, 视频生成/图生视频/Minimax_H3_多图参考加速工作流_2099764393121771521.json, 视频生成/图生视频/Minimax_H3_多图参考加速工作流_2099848729263169538.json, 视频生成/图生视频/【疯了的动态】Dasiwa_单采样25步无加速lora_2096793272898383874.json, 视频生成/图生视频/单图Minimax H3_2084901814679461889.json, 视频生成/图生视频/单采H3视频生成_2115310666943918081.json, 视频生成/图生视频/单采H3视频生成_2116705017553051649.json, 视频生成/图生视频/单采H3视频生成_2116718997881319426.json, 视频生成/图生视频/多参生成视频_2110673932587200514.json, 视频生成/文生视频/Minimax_H3 多图参考加速工作流_2085701590907969537.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_45

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/Minimax_H3 多图参考短剧制作，加速工作流_2088187262285729793.json、视频生成/图生视频/Minimax_H3_多图参考加速工作流_2099764393121771521.json、视频生成/图生视频/Minimax_H3_多图参考加速工作流_2099848729263169538.json、视频生成/图生视频/【疯了的动态】Dasiwa_单采样25步无加速lora_2096793272898383874.json、视频生成/图生视频/单图Minimax H3_2084901814679461889.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `ComfyMathExpression`
- `LoadImage`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 9/10 个有
- `KSamplerSelect` —— 9/10 个有
- `LoraLoaderModelOnly` —— 9/10 个有
- `ModelAttentionBackend` —— 9/10 个有
- `LoadAudio` —— 8/10 个有
- `BasicGuider` —— 6/10 个有
- `SolAttnMiniMax` —— 6/10 个有
- `LoraLoaderBypassModelOnly` —— 5/10 个有
- `CFGGuider` —— 4/10 个有
- `ConditioningZeroOut` —— 4/10 个有
- `INTConstant` —— 4/10 个有
- `MiniMaxH3SigmaShift` —— 4/10 个有
- `忽略多组孤海` —— 4/10 个有
- `H3AudioRefineSampler` —— 3/10 个有
- `H3FrozenVideoCache` —— 3/10 个有
- `MiniMaxH3TurboSampler` —— 3/10 个有
- `SolAttnPatch` —— 3/10 个有
- `MiniMaxH3MultiRateSamplerEXPT8` —— 1/10 个有
- `ModelPreviewOverrideKJ` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
