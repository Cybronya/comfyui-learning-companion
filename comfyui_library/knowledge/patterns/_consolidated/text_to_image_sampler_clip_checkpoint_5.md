---
name: text_to_image_sampler_clip_checkpoint_5
type: Text To Image
frequency: 15
level: moderate
coverage: 0.9458
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/【尺素】RED-Z-IMAGE-AIO文生图_2074013706979209217.json, 图片生成/文生图/【遇见AI】SDXL基础文生图工作流_2011360598709243906.json, 图片生成/文生图/人物立绘_2039073481756774402.json, 图片生成/文生图/元气少女_2044022472999182337.json, 图片生成/文生图/冷冬圣诞夜漫画风_2096584608396693506.json, 图片生成/文生图/别墅庭院风_2063986622978420738.json, 图片生成/文生图/动漫_2070124661043716097.json, 图片生成/文生图/动漫女孩_2101663777623207938.json, 图片生成/文生图/动漫美少女_2072470520804761601.json, 图片生成/文生图/卡通3D形象生成器_1916402793215623169.json, 图片生成/文生图/咖啡馆漫画风_2101655459567591426.json, 图片生成/文生图/场景生成_2039074931979325441.json, 图片生成/文生图/基础工作流_1914506513556172801.json, 图片生成/文生图/基础文生图_2013094085589999617.json, 图片生成/文生图/文生图基础款_1927982124413140993.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_5

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/【尺素】RED-Z-IMAGE-AIO文生图_2074013706979209217.json、图片生成/文生图/【遇见AI】SDXL基础文生图工作流_2011360598709243906.json、图片生成/文生图/人物立绘_2039073481756774402.json、图片生成/文生图/元气少女_2044022472999182337.json、图片生成/文生图/冷冬圣诞夜漫画风_2096584608396693506.json…）

- **类型**：Text To Image
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `SetNode` —— 2/15 个有
- `ArgosTranslateTextNode` —— 1/15 个有
- `GetNode` —— 1/15 个有
- `INTConstant` —— 1/15 个有
- `RHHiddenNodes` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 1280 | 15 | 73% |
| 高度 | 1024 | 512 - 1920 | 15 | 63% |
| 采样步数 | 25 | 10 - 50 | 15 | 54% |
| Prompt 约束强度(CFG) | 7.5 | 1 - 8 | 15 | 59% |
| 采样算法 | euler | - | 15 | 67% |
| 调度器 | normal | - | 15 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 1280，15 个样本
- 高度 中位数 1024，观测区间 512 - 1920，15 个样本
- 采样步数 中位数 25，观测区间 10 - 50，15 个样本
- Prompt 约束强度(CFG) 中位数 7.5，观测区间 1 - 8，15 个样本
- 采样算法 最常用 euler，15 个样本，一致性 67%
- 调度器 最常用 normal，15 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
