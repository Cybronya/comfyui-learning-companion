---
name: text_to_image_sampler_clip_unet_90
type: Text To Image
frequency: 8
level: strong
coverage: 0.973
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/z-image随机Prompt.一键生成一组写真_2004923441016958978.json, 图片生成/文生图/文生图-角色生成_2058015180101083138.json, 图片生成/文生图/画安-Z-Image基本文生图_2080862730688491521.json, 图片生成/文生图/造相 Z-image 文生图_2073282210454659074.json, 图片生成/文生图/造相-Z-Image-Turo 文生图官方版_1993841938419957762.json, 图片生成/文生图/阿墨AIGC-Z-image-文生图基础工作流_2025764477991391233.json, 图片生成/文生图/麦穗AI-Z-image-文生图基础工作流_2066558941785579521.json, 视频生成/文生视频/高清超真实Z-image文生图_1999125125809176577.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_90

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/z-image随机Prompt.一键生成一组写真_2004923441016958978.json、图片生成/文生图/文生图-角色生成_2058015180101083138.json、图片生成/文生图/画安-Z-Image基本文生图_2080862730688491521.json、图片生成/文生图/造相 Z-image 文生图_2073282210454659074.json、图片生成/文生图/造相-Z-Image-Turo 文生图官方版_1993841938419957762.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 7/8 个有
- `ModelSamplingAuraFlow` —— 5/8 个有
- `DPRandomGenerator` —— 1/8 个有
- `easy batchAnything` —— 1/8 个有
- `easy forLoopEnd` —— 1/8 个有
- `easy forLoopStart` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 864 - 1920 | 8 | 69% |
| 高度 | 1536 | 1024 - 1920 | 8 | 77% |
| 采样步数 | 9 | 8 - 10 | 8 | 93% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 864 - 1920，8 个样本
- 高度 中位数 1536，观测区间 1024 - 1920，8 个样本
- 采样步数 中位数 9，观测区间 8 - 10，8 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（5/8 个样本）：Steps较低可能导致细节不足
