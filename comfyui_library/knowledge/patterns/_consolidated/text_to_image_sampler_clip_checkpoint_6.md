---
name: text_to_image_sampler_clip_checkpoint_6
type: Text To Image
frequency: 14
level: moderate
coverage: 0.915929
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/【尺素】RED-Z-IMAGE-AIO文生图_2074013706979209217.json, 图片生成/文生图/基础文生图_2013163381582209026.json, 图片生成/文生图/夜色里的新中式建筑_2063975026935820290.json, 图片生成/文生图/宫崎骏风格文生图_2045321433018011649.json, 图片生成/文生图/少女漫特写镜头_2086340546775306242.json, 图片生成/文生图/少年热血漫画风_2099420731863031810.json, 图片生成/文生图/少年热血漫画风_2108742945393434625.json, 图片生成/文生图/少年热血漫画风_2110186250471821314.json, 图片生成/文生图/工作流基础篇-1-基础文生图工作流（SD1.5;SDXL）_2012411587696529410.json, 图片生成/文生图/抖音风视频生成_2039075658810265601.json, 图片生成/文生图/文生图(服装)_2075602877925646338.json, 图片生成/文生图/文生图(服装)_2075854655590064129.json, 图片生成/文生图/文生图(服装)_2076115283038789633.json, 图片生成/文生图/文生图-SDXL_1979279623626330113.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_6

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/【尺素】RED-Z-IMAGE-AIO文生图_2074013706979209217.json、图片生成/文生图/基础文生图_2013163381582209026.json、图片生成/文生图/夜色里的新中式建筑_2063975026935820290.json、图片生成/文生图/宫崎骏风格文生图_2045321433018011649.json、图片生成/文生图/少女漫特写镜头_2086340546775306242.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 1/14 个有
- `GetNode` —— 1/14 个有
- `INTConstant` —— 1/14 个有
- `SetNode` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 1024 | 14 | 77% |
| 高度 | 1024 | 512 - 1904 | 14 | 62% |
| 采样步数 | 27 | 10 - 60 | 14 | 55% |
| Prompt 约束强度(CFG) | 6 | 1 - 8 | 14 | 57% |
| 采样算法 | euler | - | 14 | 71% |
| 调度器 | normal | - | 14 | 64% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 1024，14 个样本
- 高度 中位数 1024，观测区间 512 - 1904，14 个样本
- 采样步数 中位数 27，观测区间 10 - 60，14 个样本
- Prompt 约束强度(CFG) 中位数 6，观测区间 1 - 8，14 个样本
- 采样算法 最常用 euler，14 个样本，一致性 71%
- 调度器 最常用 normal，14 个样本，一致性 64%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
