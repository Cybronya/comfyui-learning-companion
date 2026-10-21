---
name: text_to_image_sampler_clip_unet_132
type: Text To Image
frequency: 3
level: strong
coverage: 0.904667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, Text, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image 批量生图+SD放大_1994350300851019778.json, 图片生成/文生图/Z-image文生图_1993877093876514818.json, 图片生成/文生图/z-image文生图zimage动漫真人物品电商图提示词llm优化精细图片直出10秒出图片大模型优化_2011741632940482562.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_132

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-image 批量生图+SD放大_1994350300851019778.json、图片生成/文生图/Z-image文生图_1993877093876514818.json、图片生成/文生图/z-image文生图zimage动漫真人物品电商图提示词llm优化精细图片直出10秒出图片大模型优化_2011741632940482562.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `Text`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ImpactSwitch` —— 2/3 个有
- `PreviewAny` —— 2/3 个有
- `RH_LLMAPI_NODE` —— 2/3 个有
- `Int` —— 1/3 个有
- `UltimateSDUpscale` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有
- `easy promptList` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 9 - 10 | 3 | 95% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024 | 720 - 1024 | 3 | 84% |
| 高度 | 1280 | 1280 - 1920 | 3 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 9 - 10，3 个样本，取值集中（一致性 95%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 720 - 1024，3 个样本，取值集中（一致性 84%）
- 高度 中位数 1280，观测区间 1280 - 1920，3 个样本
