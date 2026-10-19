---
name: unknown_workflow_video_lora_sampler_118
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.990308
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, EnhancedLoadDiffusionModel, KSamplerSelect, LoadImage, LoraLoaderBypassModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, RandomNoise, SamplerCustomAdvanced, Text, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/动作迁移/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速v2_2087445019107090434.json, 视频生成/图生视频/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速_2087442235926335490.json, 视频生成/图生视频/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速v2_2087445019107090434.json, 视频生成/图生视频/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速v2_2087941851805470722.json, 视频生成/图生视频/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速v2_2099789060956053506.json, 视频生成/图生视频/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速v2_2100044654115905537.json, 视频生成/图生视频/MInimaxH3_Ref2AV_bf16-lightx2v_1.0八步加速V2_2088193284681322497.json, 视频生成/图生视频/MInimaxH3_Ref2AV_bf16-lightx2v_1.0八步加速_2088188664793878530.json, 视频生成/图生视频/MInimaxH3_i2AV_bf16-lightx2v_1.0-Flashvsr高清画质_2087477812772036610.json, 视频生成/图生视频/MInimaxH3_i2AV_bf16-lightx2v_1.0-Flashvsr高清画质_2091802269355433986.json, 视频生成/图生视频/MInimaxH3_i2AV_bf16-lightx2v_1.0-Flashvsr高清画质_2100063481834852353.json, 视频生成/图生视频/MInimaxH3_i2AV_bf16-lightx2v_1.0-Flashvsr高清画质_2100141839650217986.json, 视频生成/图生视频/minimaxH3先锋艺术_2088544149321633794.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_118

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/动作迁移/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速v2_2087445019107090434.json、视频生成/图生视频/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速_2087442235926335490.json、视频生成/图生视频/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速v2_2087445019107090434.json、视频生成/图生视频/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速v2_2087941851805470722.json、视频生成/图生视频/MInimaxH3_FL2AV_bf16-lightx2v_1.0正式版8步加速v2_2099789060956053506.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `EnhancedLoadDiffusionModel`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `Text`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `RHHiddenNodes` —— 12/13 个有
- `Int` —— 10/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/13 个有
- `MiniMaxH3ImageToVideo` —— 10/13 个有
- `CreateVideo` —— 7/13 个有
- `SaveVideo` —— 7/13 个有
- `DF_Get_image_size` —— 4/13 个有
- `FlashVSR_SM_KSampler` —— 4/13 个有
- `FlashVSR_SM_Model` —— 4/13 个有
- `GetImageRangeFromBatch` —— 4/13 个有
- `JWInteger` —— 4/13 个有
- `LayerUtility: PurgeVRAM V2` —— 4/13 个有
- `ImageConcatenateMulti_UTK` —— 3/13 个有
- `ResolutionSelector` —— 3/13 个有
- `easy MiniMaxH3ReferenceToVideoBridge` —— 3/13 个有
- `ComfyMathExpression` —— 2/13 个有
- `PrimitiveFloat` —— 2/13 个有
- `AnyBooleanSwitch` —— 1/13 个有
- `Images to RGB` —— 1/13 个有
- `InspyrenetRembg` —— 1/13 个有
- `PreviewImage` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 2.72024e+08 | 1.22474e+08 - 8.48051e+08 | 4 | 27% |
| Prompt 约束强度(CFG) | randomize | - | 4 | 100% |
| 采样算法 | 2 | 2 - 2 | 4 | 100% |
| 调度器 | 3.5 | 3.5 - 3.5 | 4 | 100% |
| 重绘幅度 | 11 | 11 - 11 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 2.72024e+08，观测区间 1.22474e+08 - 8.48051e+08，4 个样本，取值分散，一致性仅 27%
- Prompt 约束强度(CFG) 最常用 randomize，4 个样本，一致性 100%
- 采样算法 中位数 2，观测区间 2 - 2，4 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，4 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 11 - 11，4 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 8.48051e+08，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
