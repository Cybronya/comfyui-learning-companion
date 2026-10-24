---
name: unknown_workflow_lora_sampler_checkpoint_7
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.862
common_nodes: [CheckpointLoaderSimple, INTConstant, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, QwenImageIntegratedKSampler, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/千问 人物换装编辑_2006669489634545666.json, 图片生成/图生图/千问 图生图_2006002962352787458.json, 图片生成/图生图/千问 图生图（姿势迁移）_2006661453499080705.json, 音频生成/音频生成/rgy8wguiweghuwgw_2009824672728227841.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_checkpoint_7

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/千问 人物换装编辑_2006669489634545666.json、图片生成/图生图/千问 图生图_2006002962352787458.json、图片生成/图生图/千问 图生图（姿势迁移）_2006661453499080705.json、音频生成/音频生成/rgy8wguiweghuwgw_2009824672728227841.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `INTConstant`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImageIntegratedKSampler`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `QwenImageControlNetIntegratedLoader` —— 3/4 个有
- `CR Prompt Text` —— 1/4 个有
- `LayerColor: AutoAdjustV2` —— 1/4 个有
- `LayerUtility: ImageReel` —— 1/4 个有
- `LayerUtility: ImageReelComposit` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 图生图 image-to-image | - | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | 512 | 512 - 512 | 4 | 100% |
| 调度器 | 768 | 768 - 768 | 4 | 100% |
| 重绘幅度 | 3.92917e+14 | 1.77292e+14 - 7.16239e+14 | 4 | 45% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 图生图 image-to-image，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 调度器 中位数 768，观测区间 768 - 768，4 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 3.92917e+14，观测区间 1.77292e+14 - 7.16239e+14，4 个样本，取值分散，一致性仅 45%
- 风险：重绘幅度 观测到 7.16239e+14，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
