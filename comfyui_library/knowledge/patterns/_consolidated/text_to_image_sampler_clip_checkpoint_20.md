---
name: text_to_image_sampler_clip_checkpoint_20
type: Text To Image
frequency: 3
level: strong
coverage: 0.868
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, PreviewImage, SaveImage, VAEDecode]
problems: []
missing: [easy positive]
members: [图片生成/文生图/1973294635470729217.json, 图片生成/文生图/20260528_小易第二课_图像放大对比【成功】_2059554361151418370.json, 图片生成/文生图/姿态控制人像生成_1996127763935477761.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_20

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1973294635470729217.json、图片生成/文生图/20260528_小易第二课_图像放大对比【成功】_2059554361151418370.json、图片生成/文生图/姿态控制人像生成_1996127763935477761.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ControlNetApplyAdvanced` —— 2/3 个有
- `ControlNetLoader` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImageUpscaleWithModel` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `UpscaleModelLoader` —— 2/3 个有
- `VAELoader` —— 2/3 个有
- `CLIPSetLastLayer` —— 1/3 个有
- `LoraLoader` —— 1/3 个有
- `easy positive` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 0.6 | - | 1 | 100% |
| LoRA 文本强度 | 0.5 | - | 1 | 100% |
| 宽度 | 1024 | 720 - 1024 | 3 | 84% |
| 高度 | 1024 | 768 - 1080 | 3 | 86% |
| 采样步数 | 30 | 20 - 30 | 3 | 82% |
| Prompt 约束强度(CFG) | 7 | 5 - 8 | 3 | 81% |
| 采样算法 | euler | - | 3 | 33% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 720 - 1024，3 个样本，取值集中（一致性 84%）
- 高度 中位数 1024，观测区间 768 - 1080，3 个样本，取值集中（一致性 86%）
- 采样步数 中位数 30，观测区间 20 - 30，3 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 5 - 8，3 个样本，取值集中（一致性 81%）
- 采样算法 最常用 euler，3 个样本，一致性 33%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：easy positive
