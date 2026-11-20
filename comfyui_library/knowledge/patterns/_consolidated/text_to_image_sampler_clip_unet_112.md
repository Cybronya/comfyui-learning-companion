---
name: text_to_image_sampler_clip_unet_112
type: Text To Image
frequency: 7
level: weak
coverage: 0.757143
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/z-image-base 多采样器对比工作流_2016377804211888130.json, 图片生成/文生图/z-image-turbo 文生图_1997981712913195009.json, 图片生成/文生图/z-image-turbo-基础工作流_2010586668142698498.json, 图片生成/文生图/【尺素】krea2 turbo文生图_2069950720853499905.json, 图片生成/文生图/【阡陌】Z-Image最强极速文生图工作流_1993971431174242306.json, 图片生成/文生图/写实 文生图_2068912035760529409.json, 图片生成/文生图/动漫天花板ANIMA优化版V10_2067505280220483585.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_112

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/z-image-base 多采样器对比工作流_2016377804211888130.json、图片生成/文生图/z-image-turbo 文生图_1997981712913195009.json、图片生成/文生图/z-image-turbo-基础工作流_2010586668142698498.json、图片生成/文生图/【尺素】krea2 turbo文生图_2069950720853499905.json、图片生成/文生图/【阡陌】Z-Image最强极速文生图工作流_1993971431174242306.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/7 个有
- `GetNode` —— 3/7 个有
- `SetNode` —— 3/7 个有
- `INTConstant` —— 2/7 个有
- `CompressImages` —— 1/7 个有
- `JjkText` —— 1/7 个有
- `JoinStringMulti` —— 1/7 个有
- `PreviewAny` —— 1/7 个有
- `RH_LLMAPI_Pro_Node` —— 1/7 个有
- `TTResolutionSelector` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 50 | 7 | 19% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 7 | 22% |
| 采样算法 | euler | - | 7 | 43% |
| 调度器 | simple | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 1080 | 512 - 1920 | 7 | 53% |
| 高度 | 1128 | 512 - 1920 | 7 | 55% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 50，7 个样本，取值分散，一致性仅 19%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，7 个样本，取值分散，一致性仅 22%
- 采样算法 最常用 euler，7 个样本，一致性 43%
- 调度器 最常用 simple，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 512 - 1920，7 个样本
- 高度 中位数 1128，观测区间 512 - 1920，7 个样本
