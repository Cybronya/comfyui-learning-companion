---
name: text_to_image_sampler_clip_checkpoint_10
type: Text To Image
frequency: 8
level: weak
coverage: 0.877875
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/文生图工作流_2090257194913718274.json, 图片生成/文生图/文生图工作流搭建_2007747002171400193.json, 图片生成/文生图/文生图最简版_1990400035454148610.json, 图片生成/文生图/文生图第4课：SDXL Refiner 精修，comfyui从入门到躺平系列教程_1979416721058598913.json, 图片生成/文生图/文生图（SD1.5;SDXL）_2064679284408672257.json, 图片生成/文生图/新手工作流_2042208507885260802.json, 图片生成/文生图/森林岛大冒险1.0_1993881356163809282.json, 图片生成/文生图/艺术品高清图-鼻烟壶_1778063085018353666.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_checkpoint_10

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/文生图工作流_2090257194913718274.json、图片生成/文生图/文生图工作流搭建_2007747002171400193.json、图片生成/文生图/文生图最简版_1990400035454148610.json、图片生成/文生图/文生图第4课：SDXL Refiner 精修，comfyui从入门到躺平系列教程_1979416721058598913.json、图片生成/文生图/文生图（SD1.5;SDXL）_2064679284408672257.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 6/8 个有
- `LoraLoader` —— 3/8 个有
- `VAEEncode` —— 3/8 个有
- `LatentUpscaleBy` —— 1/8 个有
- `RMBG` —— 1/8 个有
- `Text Multiline` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 5 - 230 | 8 | 0% |
| Prompt 约束强度(CFG) | 6.5 | 2 - 8 | 8 | 64% |
| 采样算法 | euler | - | 8 | 50% |
| 调度器 | karras | - | 8 | 50% |
| 重绘幅度 | 1 | 0.25 - 1 | 8 | 68% |
| 宽度 | 896 | 512 - 1024 | 8 | 70% |
| 高度 | 1024 | 512 - 1280 | 8 | 67% |
| LoRA 模型强度 | 0.95 | 0.5 - 1 | 3 | 72% |
| LoRA 文本强度 | 1 | 0.3 - 1 | 3 | 57% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 5 - 230，8 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 6.5，观测区间 2 - 8，8 个样本
- 采样算法 最常用 euler，8 个样本，一致性 50%
- 调度器 最常用 karras，8 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.25 - 1，8 个样本
- 宽度 中位数 896，观测区间 512 - 1024，8 个样本
- 高度 中位数 1024，观测区间 512 - 1280，8 个样本
- LoRA 模型强度 中位数 0.95，观测区间 0.5 - 1，3 个样本
- LoRA 文本强度 中位数 1，观测区间 0.3 - 1，3 个样本
- 风险：采样步数 观测到 230，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
