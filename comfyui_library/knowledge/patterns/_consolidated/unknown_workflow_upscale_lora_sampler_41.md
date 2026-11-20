---
name: unknown_workflow_upscale_lora_sampler_41
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.987
common_nodes: [CheckpointLoaderSimple, ConditioningZeroOut, ImageResizeAdvanced, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/单图编辑-直出4K-Qwen-Rapid-AIO-v23_1999284905509089281.json, 图片生成/图生图/双图编辑-直出4K-Qwen-Rapid-AIO-v23_1999309343193526273.json, 图片生成/图生图/双图编辑-直出4K-Qwen-Rapid-AIO-v23_2025863225870393345.json, 图片生成/图生图/双图编辑-直出4K-Qwen-Rapid-AIO-v23_2048396518369009665.json, 图片生成/图生图/定zhi muscle promax_2036107087352172546.json, 平台全量/Qwen-双图编辑-4K直出_2028386278059810817.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_41

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/单图编辑-直出4K-Qwen-Rapid-AIO-v23_1999284905509089281.json、图片生成/图生图/双图编辑-直出4K-Qwen-Rapid-AIO-v23_1999309343193526273.json、图片生成/图生图/双图编辑-直出4K-Qwen-Rapid-AIO-v23_2025863225870393345.json、图片生成/图生图/双图编辑-直出4K-Qwen-Rapid-AIO-v23_2048396518369009665.json、图片生成/图生图/定zhi muscle promax_2036107087352172546.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 6 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `ImageResizeAdvanced`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 5/6 个有
- `LayerUtility: ImageReel` —— 5/6 个有
- `LayerUtility: ImageReelComposit` —— 5/6 个有
- `SaveImage` —— 5/6 个有
- `easy cleanGpuUsed` —— 5/6 个有
- `easy clearCacheAll` —— 5/6 个有
- `CompressImages` —— 3/6 个有
- `SaveLatent` —— 2/6 个有
- `GroupSwitcher` —— 1/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `SwitchImageByIndex` —— 1/6 个有
- `Text` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 6 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.8 | 6 | 74% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta57 | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，6 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.8，6 个样本
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta57，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（7/6 个样本）：Steps较低可能导致细节不足
