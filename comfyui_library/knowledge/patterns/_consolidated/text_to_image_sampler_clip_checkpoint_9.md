---
name: text_to_image_sampler_clip_checkpoint_9
type: Text To Image
frequency: 7
level: moderate
coverage: 0.971429
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/中西合璧古典美人一键生成_1889372369155448834.json, 图片生成/文生图/少年热血漫画风_2099420731863031810.json, 图片生成/文生图/文生图基础款1_1851544019800313857.json, 图片生成/文生图/文生图基础款_1818200162132209665.json, 图片生成/文生图/文生图基础款_1830501484281688065.json, 图片生成/文生图/文生图基础款_1851451030012841985.json, 图片生成/文生图/文生图宠物_1778280371394240514.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_9

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/中西合璧古典美人一键生成_1889372369155448834.json、图片生成/文生图/少年热血漫画风_2099420731863031810.json、图片生成/文生图/文生图基础款1_1851544019800313857.json、图片生成/文生图/文生图基础款_1818200162132209665.json、图片生成/文生图/文生图基础款_1830501484281688065.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CLIPSetLastLayer` —— 1/7 个有
- `JjkText` —— 1/7 个有
- `JoinStrings` —— 1/7 个有
- `VAELoader` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 768 | 7 | 88% |
| 高度 | 1024 | 512 - 1024 | 7 | 81% |
| 采样步数 | 20 | 20 - 50 | 7 | 59% |
| Prompt 约束强度(CFG) | 8 | 3.5 - 8 | 7 | 76% |
| 采样算法 | dpmpp_2m_sde | - | 7 | 57% |
| 调度器 | karras | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 768，7 个样本，取值集中（一致性 88%）
- 高度 中位数 1024，观测区间 512 - 1024，7 个样本，取值集中（一致性 81%）
- 采样步数 中位数 20，观测区间 20 - 50，7 个样本
- Prompt 约束强度(CFG) 中位数 8，观测区间 3.5 - 8，7 个样本
- 采样算法 最常用 dpmpp_2m_sde，7 个样本，一致性 57%
- 调度器 最常用 karras，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
