---
name: unknown_workflow_video_lora_sampler_126
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.9945
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, EnhancedLoadDiffusionModel, Int, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3ImageToVideo, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, SamplerCustomAdvanced, Text, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/MInimaxH3_i2AV_bf16-lightx2v_1.0-Flashvsr高清画质_2101303792682749953.json, 视频生成/动作迁移/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速v2_2087445019107090434.json, 视频生成/图生视频/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速_2087442235926335490.json, 视频生成/图生视频/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速v2_2087941851805470722.json, 视频生成/图生视频/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速v2_2099789060956053506.json, 视频生成/图生视频/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速v2_2100044654115905537.json, 视频生成/图生视频/MInimaxH3_i2AV_bf16-lightx2v_1.0-Flashvsr高清画质_2087477812772036610.json, 视频生成/图生视频/MInimaxH3_i2AV_bf16-lightx2v_1.0-Flashvsr高清画质_2091802269355433986.json, 视频生成/图生视频/MInimaxH3_i2AV_bf16-lightx2v_1.0-Flashvsr高清画质_2100063481834852353.json, 视频生成/图生视频/MInimaxH3_i2AV_bf16-lightx2v_1.0-Flashvsr高清画质_2100141839650217986.json, 视频生成/图生视频/MinimaxH3八步加速极速版T2_2088826644688629762.json, 视频生成/图生视频/高清图生视频_2087823632620937217.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_126

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/MInimaxH3_i2AV_bf16-lightx2v_1.0-Flashvsr高清画质_2101303792682749953.json、视频生成/动作迁移/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速v2_2087445019107090434.json、视频生成/图生视频/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速_2087442235926335490.json、视频生成/图生视频/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速v2_2087941851805470722.json、视频生成/图生视频/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速v2_2099789060956053506.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 12 个 workflow 都包含：
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
- `RandomNoise`
- `SamplerCustomAdvanced`
- `Text`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `RHHiddenNodes` —— 11/12 个有
- `DF_Get_image_size` —— 7/12 个有
- `FlashVSR_SM_KSampler` —— 7/12 个有
- `FlashVSR_SM_Model` —— 7/12 个有
- `GetImageRangeFromBatch` —— 7/12 个有
- `JWInteger` —— 7/12 个有
- `LayerUtility: PurgeVRAM V2` —— 7/12 个有
- `CreateVideo` —— 5/12 个有
- `SaveVideo` —— 5/12 个有
- `AnyBooleanSwitch` —— 1/12 个有
- `ComfyMathExpression` —— 1/12 个有
- `EmptyImage` —— 1/12 个有
- `PreviewImage` —— 1/12 个有
- `PrimitiveFloat` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 2.73608e+08 | 7.7008e+07 - 1.25877e+09 | 7 | 18% |
| Prompt 约束强度(CFG) | randomize | - | 7 | 100% |
| 采样算法 | 2 | 2 - 2 | 7 | 100% |
| 调度器 | 3.5 | 3.5 - 3.5 | 7 | 100% |
| 重绘幅度 | 11 | 11 - 11 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 2.73608e+08，观测区间 7.7008e+07 - 1.25877e+09，7 个样本，取值分散，一致性仅 18%
- Prompt 约束强度(CFG) 最常用 randomize，7 个样本，一致性 100%
- 采样算法 中位数 2，观测区间 2 - 2，7 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，7 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 11 - 11，7 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 1.25877e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
