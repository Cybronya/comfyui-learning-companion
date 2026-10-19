---
name: image_to_image_sampler_clip_checkpoint
type: Image To Image
frequency: 4
level: moderate
coverage: 0.9375
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, KSampler, LoadImage, SaveImage, VAEDecode, VAEEncode]
problems: []
missing: []
members: [图片生成/图生图/2021849030879354881.json, 图片生成/文生图/1983414020642381826.json, 图片生成/文生图/1985415351917813761.json, 视频生成/图生视频/2056379103971991553.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_checkpoint

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/2021849030879354881.json、图片生成/文生图/1983414020642381826.json、图片生成/文生图/1985415351917813761.json、视频生成/图生视频/2056379103971991553.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `RH_Captioner` —— 2/4 个有
- `TextCombinerTwo` —— 2/4 个有
- `CR Text` —— 1/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `LoadVideo` —— 1/4 个有
- `LoraLoader` —— 1/4 个有
- `RH_RhartVideoSparkvideo20FastMultimodalVideo` —— 1/4 个有
- `SaveVideo` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.3 | - | 1 | 100% |
| LoRA 文本强度 | 0.3 | - | 1 | 100% |
| 采样步数 | 20 | 20 - 25 | 4 | 90% |
| Prompt 约束强度(CFG) | 8 | 1 - 8 | 4 | 52% |
| 采样算法 | euler_ancestral | - | 4 | 50% |
| 调度器 | normal | - | 4 | 75% |
| 重绘幅度 | 0.43 | 0.36 - 0.87 | 4 | 60% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，4 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 8，4 个样本
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 50%
- 调度器 最常用 normal，4 个样本，一致性 75%
- 重绘幅度 中位数 0.43，观测区间 0.36 - 0.87，4 个样本
