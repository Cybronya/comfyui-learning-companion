---
name: text_to_image_sampler_clip_checkpoint_18
type: Text To Image
frequency: 4
level: moderate
coverage: 0.97225
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/Z-image-AIO文生图_1999088870409072641.json, 图片生成/文生图/controlnet文生图SD_2096536231768317953.json, 图片生成/文生图/generate_image_2069748514313293826.json, 图片生成/文生图/▶▷Krea2-高清生图AIO_2077747265082585089.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_18

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Z-image-AIO文生图_1999088870409072641.json、图片生成/文生图/controlnet文生图SD_2096536231768317953.json、图片生成/文生图/generate_image_2069748514313293826.json、图片生成/文生图/▶▷Krea2-高清生图AIO_2077747265082585089.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `TT_img_enc` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 10 - 20 | 4 | 67% |
| Prompt 约束强度(CFG) | 4 | 1 - 7.53 | 4 | 24% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1012 | 768 - 1024 | 4 | 89% |
| 高度 | 1408 | 1024 - 1680 | 4 | 82% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 15，观测区间 10 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 7.53，4 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1012，观测区间 768 - 1024，4 个样本，取值集中（一致性 89%）
- 高度 中位数 1408，观测区间 1024 - 1680，4 个样本，取值集中（一致性 82%）
