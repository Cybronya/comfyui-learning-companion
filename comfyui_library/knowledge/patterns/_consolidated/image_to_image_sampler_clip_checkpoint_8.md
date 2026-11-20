---
name: image_to_image_sampler_clip_checkpoint_8
type: Image To Image
frequency: 4
level: moderate
coverage: 1
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/SD1.5+智能锐化 1.0_2098204817767362561.json, 图片生成/图生图/SD3图生图动漫风格_1934135456093097986.json, 图片生成/图生图/一键转绘梦境动漫风格女生_1925326586818572290.json, 图片生成/图生图/图生图SDXL写实摄影_1933376541835309057.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_checkpoint_8

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/SD1.5+智能锐化 1.0_2098204817767362561.json、图片生成/图生图/SD3图生图动漫风格_1934135456093097986.json、图片生成/图生图/一键转绘梦境动漫风格女生_1925326586818572290.json、图片生成/图生图/图生图SDXL写实摄影_1933376541835309057.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `WD14Tagger|pysssss` —— 2/4 个有
- `Image Compare (mtb)` —— 1/4 个有
- `ImageSmartSharpen+` —— 1/4 个有
- `ModelSamplingSD3` —— 1/4 个有
- `TripleCLIPLoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 21 | 20 - 30 | 4 | 82% |
| Prompt 约束强度(CFG) | 7.5 | 4 - 8 | 4 | 76% |
| 采样算法 | euler_ancestral | - | 4 | 50% |
| 调度器 | simple | - | 4 | 25% |
| 重绘幅度 | 0.45 | 0.1 - 0.8 | 4 | 40% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 21，观测区间 20 - 30，4 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 7.5，观测区间 4 - 8，4 个样本
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 25%
- 重绘幅度 中位数 0.45，观测区间 0.1 - 0.8，4 个样本，取值分散，一致性仅 40%
