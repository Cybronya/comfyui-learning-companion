---
name: unknown_workflow_upscale_lora_sampler_13
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.862357
common_nodes: [CR Prompt Text, CheckpointLoaderSimple, ConditioningKrea2Rebalance, KSampler, LoraLoaderModelOnly, RHHiddenNodes, SaveImage, ShowText|pysssss, VAEDecode, WujiCleaner, WujiSuperEditor, WujiUpscaler]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/最强图像反推Krea2-Turbo-HD双采样深度反推_2083764897527189505.json, 图片生成/图生图/最强图像反推Krea2-Turbo-HD双采样深度反推_2084915723654230017.json, 图片生成/图生图/最强图像反推Krea2-Turbo-HD双采样深度反推_2085298004457779202.json, 图片生成/图生图/最强图像反推Krea2-Turbo-HD双采样深度反推_2088182066977533953.json, 图片生成/图生图/最强图像反推Krea2-Turbo-HD双采样深度反推_2088191351677607938.json, 图片生成/图生图/最强图像反推Krea2-Turbo-HD双采样深度反推_2088193918348390401.json, 图片生成/图生图/最强图像反推Krea2-Turbo-HD双采样深度反推_2091702620602851329.json, 图片生成/图生图/最强图像反推Krea2-Turbo-HD双采样深度反推_2091834276198313985.json, 图片生成/文生图/双重曝光艺术Krea2，名人、小说、影视、节日、地名均可_2085180691586830337.json, 图片生成/文生图/双重曝光艺术Krea2，名人、小说、影视、节日、地名均可_2088511028723277825.json, 图片生成/文生图/双重曝光艺术照Krea2，虚实构图艺术感拉满_2090251305397870594.json, 图片生成/文生图/最强图像反推Krea2-Turbo-HD双采样深度反推_2087805499344506881.json, 图片生成/文生图/最强图像反推Krea2-Turbo-HD双采样深度反推_2087812584857751553.json, 图片生成/文生图/最强图像反推Krea2-Turbo-HD双采样深度反推_2088189215996727297.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_13

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/最强图像反推Krea2-Turbo-HD双采样深度反推_2083764897527189505.json、图片生成/图生图/最强图像反推Krea2-Turbo-HD双采样深度反推_2084915723654230017.json、图片生成/图生图/最强图像反推Krea2-Turbo-HD双采样深度反推_2085298004457779202.json、图片生成/图生图/最强图像反推Krea2-Turbo-HD双采样深度反推_2088182066977533953.json、图片生成/图生图/最强图像反推Krea2-Turbo-HD双采样深度反推_2088191351677607938.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 14 个 workflow 都包含：
- `CR Prompt Text`
- `CheckpointLoaderSimple`
- `ConditioningKrea2Rebalance`
- `KSampler`
- `LoraLoaderModelOnly`
- `RHHiddenNodes`
- `SaveImage`
- `ShowText|pysssss`
- `VAEDecode`
- `WujiCleaner`
- `WujiSuperEditor`
- `WujiUpscaler`

**可变部分**（部分 workflow 才有）：
- `DepthAnythingV2Preprocessor` —— 11/14 个有
- `Krea2ControlApply` —— 11/14 个有
- `Krea2ControlImageEncode` —— 11/14 个有
- `Krea2ControlLoRALoader` —— 11/14 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 11/14 个有
- `LoadImage` —— 11/14 个有
- `PreviewImage` —— 11/14 个有
- `Int` —— 3/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 14 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 79% |
| 调度器 | sgm_uniform | - | 14 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 0.4 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 28/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 79%
- 调度器 最常用 sgm_uniform，14 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.4，14 个样本，取值集中（一致性 100%）
- 高发问题（28/14 个样本）：Steps较低可能导致细节不足
