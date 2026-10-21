---
name: unknown_workflow_video_lora_sampler_417
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 1
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, EnhancedLoadDiffusionModel, Int, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3ImageToVideo, MiniMaxH3MemoryEfficientSageAttentionPatch, RHHiddenNodes, RandomNoise, SamplerCustomAdvanced, Text, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/MInimaxH3_i2AV_bf16-lightx2v_1.0正式版8步加速_2087456117239668737.json, 视频生成/图生视频/MinimaxH3八步加速极速版T1_2088232222376681473.json, 视频生成/图生视频/MinimaxH3八步加速极速版T2_2088826644688629762.json, 视频生成/图生视频/minimaxH3快乐的小孩_2088616677788446722.json, 视频生成/图生视频/高清图生视频_2087823632620937217.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_417

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/MInimaxH3_i2AV_bf16-lightx2v_1.0正式版8步加速_2087456117239668737.json、视频生成/图生视频/MinimaxH3八步加速极速版T1_2088232222376681473.json、视频生成/图生视频/MinimaxH3八步加速极速版T2_2088826644688629762.json、视频生成/图生视频/minimaxH3快乐的小孩_2088616677788446722.json、视频生成/图生视频/高清图生视频_2087823632620937217.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `EnhancedLoadDiffusionModel`
- `Int`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RHHiddenNodes`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `Text`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `DF_Get_image_size` —— 2/5 个有
- `FlashVSR_SM_KSampler` —— 2/5 个有
- `FlashVSR_SM_Model` —— 2/5 个有
- `GetImageRangeFromBatch` —— 2/5 个有
- `JWInteger` —— 2/5 个有
- `LayerUtility: PurgeVRAM V2` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6.67887e+08 | - | 2 | 12% |
| Prompt 约束强度(CFG) | randomize | - | 2 | 100% |
| 采样算法 | 2 | - | 2 | 100% |
| 调度器 | 3.5 | - | 2 | 100% |
| 重绘幅度 | 11 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 6.67887e+08，样本不足，未给区间，2 个样本，取值分散，一致性仅 12%
- Prompt 约束强度(CFG) 最常用 randomize，2 个样本，一致性 100%
- 采样算法 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 1.25877e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
