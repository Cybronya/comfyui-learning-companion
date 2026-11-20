---
name: text_to_image_sampler_clip_checkpoint_16
type: Text To Image
frequency: 5
level: weak
coverage: 0.8546
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/文生图第4课：SDXL Refiner 精修，comfyui从入门到躺平系列教程_1979416721058598913.json, 图片生成/文生图/文生图（SD1.5;SDXL）_2064679284408672257.json, 图片生成/文生图/新手工作流_2042208507885260802.json, 图片生成/文生图/森林岛大冒险1.0_1993881356163809282.json, 图片生成/文生图/艺术品高清图-鼻烟壶_1778063085018353666.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_16

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/文生图第4课：SDXL Refiner 精修，comfyui从入门到躺平系列教程_1979416721058598913.json、图片生成/文生图/文生图（SD1.5;SDXL）_2064679284408672257.json、图片生成/文生图/新手工作流_2042208507885260802.json、图片生成/文生图/森林岛大冒险1.0_1993881356163809282.json、图片生成/文生图/艺术品高清图-鼻烟壶_1778063085018353666.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/5 个有
- `VAEEncode` —— 3/5 个有
- `LoraLoader` —— 2/5 个有
- `LatentUpscaleBy` —— 1/5 个有
- `RMBG` —— 1/5 个有
- `Text Multiline` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1024 | 5 | 89% |
| 高度 | 1024 | 1024 - 1280 | 5 | 90% |
| 采样步数 | 20 | 5 - 230 | 5 | 0% |
| Prompt 约束强度(CFG) | 5 | 2 - 8 | 5 | 60% |
| 采样算法 | euler | - | 5 | 40% |
| 调度器 | karras | - | 5 | 60% |
| 重绘幅度 | 1 | 0.25 - 1 | 5 | 59% |
| LoRA 模型强度 | 0.725 | - | 2 | 69% |
| LoRA 文本强度 | 0.65 | - | 2 | 46% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1024，5 个样本，取值集中（一致性 89%）
- 高度 中位数 1024，观测区间 1024 - 1280，5 个样本，取值集中（一致性 90%）
- 采样步数 中位数 20，观测区间 5 - 230，5 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 5，观测区间 2 - 8，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 40%
- 调度器 最常用 karras，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 0.25 - 1，5 个样本
- LoRA 模型强度 中位数 0.725，样本不足，未给区间，2 个样本
- LoRA 文本强度 中位数 0.65，样本不足，未给区间，2 个样本，取值分散，一致性仅 46%
- 风险：采样步数 观测到 230，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
