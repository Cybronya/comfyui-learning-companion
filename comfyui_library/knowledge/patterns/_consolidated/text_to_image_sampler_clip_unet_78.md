---
name: text_to_image_sampler_clip_unet_78
type: Text To Image
frequency: 9
level: moderate
coverage: 0.845444
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/z-image-base 多采样器对比工作流_2016377804211888130.json, 图片生成/文生图/z-image-turbo 文生图_1997981712913195009.json, 图片生成/文生图/z-image-turbo-基础工作流_2010586668142698498.json, 图片生成/文生图/z-image文生图工作流_1998291742837366786.json, 图片生成/文生图/z-image文生图工作流_2089710476165992450.json, 图片生成/文生图/z-image文生图工作流_2098948533117345794.json, 图片生成/文生图/z-image文生图工作流_2099060664231874562.json, 图片生成/文生图/【尺素】krea2 turbo文生图_2069950720853499905.json, 图片生成/文生图/文生图Krea2_2080302375230857217.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_78

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/z-image-base 多采样器对比工作流_2016377804211888130.json、图片生成/文生图/z-image-turbo 文生图_1997981712913195009.json、图片生成/文生图/z-image-turbo-基础工作流_2010586668142698498.json、图片生成/文生图/z-image文生图工作流_1998291742837366786.json、图片生成/文生图/z-image文生图工作流_2089710476165992450.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 6/9 个有
- `GetNode` —— 2/9 个有
- `SetNode` —— 2/9 个有
- `TTResolutionSelector` —— 2/9 个有
- `EmptyImage` —— 1/9 个有
- `INTConstant` —— 1/9 个有
- `PreviewImage` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 8 - 50 | 9 | 12% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 9 | 49% |
| 采样算法 | euler | - | 9 | 67% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 1024 | 512 - 1080 | 9 | 76% |
| 高度 | 1536 | 512 - 1920 | 9 | 66% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 8 - 50，9 个样本，取值分散，一致性仅 12%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，9 个样本，取值分散，一致性仅 49%
- 采样算法 最常用 euler，9 个样本，一致性 67%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 512 - 1080，9 个样本
- 高度 中位数 1536，观测区间 512 - 1920，9 个样本
- 高发问题（6/9 个样本）：Steps较低可能导致细节不足
