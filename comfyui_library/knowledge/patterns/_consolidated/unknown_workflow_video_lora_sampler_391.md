---
name: unknown_workflow_video_lora_sampler_391
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.933
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, ConditioningZeroOut, FlashVSR_SM_KSampler, FlashVSR_SM_Model, H3SigmaRefiner, KSamplerSelect, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, ModelPreviewOverrideKJ, PreviewImage, PrimitiveFloat, RHHiddenNodes, SelfLiftAvatarH3Sampler, Text, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/高清去油版MinimaxH3-T1_2105922330722660354.json, 视频生成/图生视频/高清去油版MinimaxH3-T2_2105926309791752193.json, 视频生成/图生视频/高清去油版MinimaxH3-T3_2105926378402181122.json, 视频生成/图生视频/高画质minimaxH3-T1_2105599117824192514.json, 视频生成/图生视频/高画质minimaxH3-T2_2105603655398420481.json, 视频生成/图生视频/高画质minimaxH3-T3_2105610995262648321.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_391

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/高清去油版MinimaxH3-T1_2105922330722660354.json、视频生成/图生视频/高清去油版MinimaxH3-T2_2105926309791752193.json、视频生成/图生视频/高清去油版MinimaxH3-T3_2105926378402181122.json、视频生成/图生视频/高画质minimaxH3-T1_2105599117824192514.json、视频生成/图生视频/高画质minimaxH3-T2_2105603655398420481.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `FlashVSR_SM_KSampler`
- `FlashVSR_SM_Model`
- `H3SigmaRefiner`
- `KSamplerSelect`
- `LTXVSeparateAVLatent`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PreviewImage`
- `PrimitiveFloat`
- `RHHiddenNodes`
- `SelfLiftAvatarH3Sampler`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1.22651e+09 | 3.47579e+08 - 2.0952e+09 | 6 | 56% |
| Prompt 约束强度(CFG) | randomize | - | 6 | 100% |
| 采样算法 | 2 | 2 - 2 | 6 | 100% |
| 调度器 | 3.5 | 3.5 - 3.5 | 6 | 100% |
| 重绘幅度 | 11 | 11 - 11 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 1.22651e+09，观测区间 3.47579e+08 - 2.0952e+09，6 个样本
- Prompt 约束强度(CFG) 最常用 randomize，6 个样本，一致性 100%
- 采样算法 中位数 2，观测区间 2 - 2，6 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，6 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 11 - 11，6 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 2.0952e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
