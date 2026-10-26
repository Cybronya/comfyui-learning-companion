---
name: text_to_image_sampler_clip_checkpoint_22
type: Text To Image
frequency: 3
level: strong
coverage: 1
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/Z-image-AIO文生图_1999088870409072641.json, 图片生成/文生图/flux和XL基础文生图_1940024417504366593.json, 图片生成/文生图/flux和XL基础文生图配合基础课教学08节_1932244857421819905.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_22

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-image-AIO文生图_1999088870409072641.json、图片生成/文生图/flux和XL基础文生图_1940024417504366593.json、图片生成/文生图/flux和XL基础文生图配合基础课教学08节_1932244857421819905.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `BNK_CLIPTextEncodeAdvanced` —— 2/3 个有
- `KSampler //Inspire` —— 2/3 个有
- `TT_img_enc` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 20 | 3 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 832 | 832 - 1024 | 3 | 90% |
| 高度 | 1536 | 1536 - 1680 | 3 | 96% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 832，观测区间 832 - 1024，3 个样本，取值集中（一致性 90%）
- 高度 中位数 1536，观测区间 1536 - 1680，3 个样本，取值集中（一致性 96%）
