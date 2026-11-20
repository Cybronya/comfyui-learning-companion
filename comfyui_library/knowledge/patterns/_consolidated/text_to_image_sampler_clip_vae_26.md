---
name: text_to_image_sampler_clip_vae_26
type: Text To Image
frequency: 4
level: strong
coverage: 0.9345
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/ZIMAGE-反推生图操作台_2092149423693455361.json, 图片生成/图生图/LH-DMT版本-2.生图片类-031.Z-image文生图 + 图像重绘_2016507574392197121.json, 图片生成/图生图/Z-Image去网红感+QWEN自动反推提示词真实图生文生图_2012370345021415426.json, 数字人/数字人/ZIMAGE-杰洛特图片反推生图_2044352477067218946.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_26

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/反推提示词/ZIMAGE-反推生图操作台_2092149423693455361.json、图片生成/图生图/LH-DMT版本-2.生图片类-031.Z-image文生图 + 图像重绘_2016507574392197121.json、图片生成/图生图/Z-Image去网红感+QWEN自动反推提示词真实图生文生图_2012370345021415426.json、数字人/数字人/ZIMAGE-杰洛特图片反推生图_2044352477067218946.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 3/4 个有
- `Qwen3VL_Advanced` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `Fast Groups Muter (rgthree)` —— 2/4 个有
- `JjkShowText` —— 2/4 个有
- `图像缩放V2_孤海` —— 2/4 个有
- `CheckpointLoaderSimple` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有
- `VAEEncode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1148 | 720 - 1216 | 4 | 81% |
| 高度 | 2040 | 1280 - 2160 | 4 | 81% |
| 采样步数 | 9 | 8 - 10 | 4 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | res_2s | - | 4 | 50% |
| 调度器 | bong_tangent | - | 4 | 50% |
| 重绘幅度 | 1 | 0.7 - 1 | 4 | 86% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1148，观测区间 720 - 1216，4 个样本，取值集中（一致性 81%）
- 高度 中位数 2040，观测区间 1280 - 2160，4 个样本，取值集中（一致性 81%）
- 采样步数 中位数 9，观测区间 8 - 10，4 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2s，4 个样本，一致性 50%
- 调度器 最常用 bong_tangent，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.7 - 1，4 个样本，取值集中（一致性 86%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
