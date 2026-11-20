---
name: unknown_workflow_sampler_clip_unet_242
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.895
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Krea2文生图+SeedVR2高清放大+全节点注释_2116763962254647298.json, 图片生成/图生图/Krea2单图风格参考Style+Reference+seedvr2超清8K放大_2074739996078206977.json, 图片生成/文生图/Krea2单图风格参考Style Reference+seedvr2超清8K放大_2074388519597989889.json, 图片生成/文生图/Krea2单图风格参考seedvr2超清8K放大_2074756140059152385.json, 图片生成/文生图/Qwen-2512文生图(Yihan AIGC)_2018677340422807553.json, 图片生成/文生图/krea2风格迁移_2074377841915027457.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_242

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/反推提示词/Krea2文生图+SeedVR2高清放大+全节点注释_2116763962254647298.json、图片生成/图生图/Krea2单图风格参考Style+Reference+seedvr2超清8K放大_2074739996078206977.json、图片生成/文生图/Krea2单图风格参考Style Reference+seedvr2超清8K放大_2074388519597989889.json、图片生成/文生图/Krea2单图风格参考seedvr2超清8K放大_2074756140059152385.json、图片生成/文生图/Qwen-2512文生图(Yihan AIGC)_2018677340422807553.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 5/6 个有
- `SeedVR2LoadDiTModel` —— 5/6 个有
- `SeedVR2LoadVAEModel` —— 5/6 个有
- `SeedVR2VideoUpscaler` —— 5/6 个有
- `ConditioningZeroOut` —— 4/6 个有
- `Krea2SizePreset` —— 4/6 个有
- `Krea2StyleReference` —— 4/6 个有
- `Krea2StyleTransfer` —— 4/6 个有
- `easy int` —— 3/6 个有
- `EmptySD3LatentImage` —— 2/6 个有
- `ImageScaleBy` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 21 | 6 | 55% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 6 | 44% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 21，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，6 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（4/6 个样本）：Steps较低可能导致细节不足
