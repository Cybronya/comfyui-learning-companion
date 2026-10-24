---
name: text_to_image_sampler_clip_checkpoint_14
type: Text To Image
frequency: 6
level: moderate
coverage: 1
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/Z-image-AIO文生图_1999088870409072641.json, 图片生成/文生图/chai·文生图工作流_1904438332934520833.json, 图片生成/文生图/clip简易图片_2108889381011550210.json, 图片生成/文生图/controlnet文生图SD_2096536231768317953.json, 图片生成/文生图/flux和XL基础文生图_1940024417504366593.json, 图片生成/文生图/flux和XL基础文生图配合基础课教学08节_1932244857421819905.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_14

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/Z-image-AIO文生图_1999088870409072641.json、图片生成/文生图/chai·文生图工作流_1904438332934520833.json、图片生成/文生图/clip简易图片_2108889381011550210.json、图片生成/文生图/controlnet文生图SD_2096536231768317953.json、图片生成/文生图/flux和XL基础文生图_1940024417504366593.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/6 个有
- `BNK_CLIPTextEncodeAdvanced` —— 2/6 个有
- `KSampler //Inspire` —— 2/6 个有
- `TT_img_enc` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 20 | 6 | 80% |
| Prompt 约束强度(CFG) | 4.265 | 1 - 8 | 6 | 23% |
| 采样算法 | euler | - | 6 | 67% |
| 调度器 | simple | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 832 | 512 - 1024 | 6 | 80% |
| 高度 | 1536 | 512 - 1680 | 6 | 71% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 4.265，观测区间 1 - 8，6 个样本，取值分散，一致性仅 23%
- 采样算法 最常用 euler，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 832，观测区间 512 - 1024，6 个样本
- 高度 中位数 1536，观测区间 512 - 1680，6 个样本
