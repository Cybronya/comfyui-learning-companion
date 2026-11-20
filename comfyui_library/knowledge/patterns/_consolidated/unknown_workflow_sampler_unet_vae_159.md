---
name: unknown_workflow_sampler_unet_vae_159
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.5795
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, LoadImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image2.1 角色四视图生成（短剧通用）_2109421554764439554.json, 图片生成/图生图/Qwen-image2.1 空间折叠流之万法编辑_2103006271149531137.json, 图片生成/图生图/Qwen2.1 抠图V2_2107650772061220865.json, 图片生成/图生图/qwen2.1图片编辑_2104273369309995009.json, 图片生成/图生图/角色资产四视图极速版Qwen image 2.1 4(8)步加速_2103425351551635458.json, 图片生成/文生图/Qwen-image2.1_空间折叠流之万法编辑_2105586769449275394.json, 图片生成/文生图/Qwen-image2.1_空间折叠流之万法编辑_2108373842572959745.json, 图片生成/文生图/心然·寻源-qwen-iamge2.1图像编辑_2101982996449554433.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_159

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen Image2.1 角色四视图生成（短剧通用）_2109421554764439554.json、图片生成/图生图/Qwen-image2.1 空间折叠流之万法编辑_2103006271149531137.json、图片生成/图生图/Qwen2.1 抠图V2_2107650772061220865.json、图片生成/图生图/qwen2.1图片编辑_2104273369309995009.json、图片生成/图生图/角色资产四视图极速版Qwen image 2.1 4(8)步加速_2103425351551635458.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 7/8 个有
- `GetNode` —— 6/8 个有
- `SetNode` —— 6/8 个有
- `ComfySwitchNode` —— 5/8 个有
- `Text` —— 5/8 个有
- `忽略多组孤海` —— 4/8 个有
- `CR Prompt Text` —— 2/8 个有
- `BatchImagesNode` —— 1/8 个有
- `Int` —— 1/8 个有
- `LoraLoaderModelOnly` —— 1/8 个有
- `Seed (rgthree)` —— 1/8 个有
- `TextGenerateLTX2Prompt` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 35 | 8 - 40 | 8 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 8 | 28% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1024 | 1024 - 2048 | 8 | 71% |
| 高度 | 1024 | 1024 - 1280 | 8 | 92% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 35，观测区间 8 - 40，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，8 个样本，取值分散，一致性仅 28%
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 2048，8 个样本
- 高度 中位数 1024，观测区间 1024 - 1280，8 个样本，取值集中（一致性 92%）
