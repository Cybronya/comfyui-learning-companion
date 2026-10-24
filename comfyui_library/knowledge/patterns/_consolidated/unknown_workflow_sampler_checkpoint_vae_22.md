---
name: unknown_workflow_sampler_checkpoint_vae_22
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.6116
common_nodes: [Anything Everywhere3, CheckpointLoaderSimple, DWPreprocessor, EmptyLatentImage, GetNode, ImageScaleToTotalPixels, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, SaveImage, SetNode, Text Multiline, TextEncodeQwenImageEditPlus, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen edit AIO V7 千问图像编辑（适合比较大的变化）_1977316284226523138.json, 图片生成/图生图/Qwen场景一致性 多角度转换_1988519915340611585.json, 图片生成/图生图/千问图像编辑 AIO V7_1984039911756103682.json, 图片生成/图生图/多角度 场景一致性 角度转换+场景定制_2043562427484213249.json, 图片生成/图生图/最强场景一致性 角度转换+场景定制_1990451042057936898.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_22

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen edit AIO V7 千问图像编辑（适合比较大的变化）_1977316284226523138.json、图片生成/图生图/Qwen场景一致性 多角度转换_1988519915340611585.json、图片生成/图生图/千问图像编辑 AIO V7_1984039911756103682.json、图片生成/图生图/多角度 场景一致性 角度转换+场景定制_2043562427484213249.json、图片生成/图生图/最强场景一致性 角度转换+场景定制_1990451042057936898.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：61%

## 共有节点

全部 5 个 workflow 都包含：
- `Anything Everywhere3`
- `CheckpointLoaderSimple`
- `DWPreprocessor`
- `EmptyLatentImage`
- `GetNode`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `Text Multiline`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 4/5 个有
- `QwenImageLatentAspectRatio` —— 4/5 个有
- `TextCombinerTwo` —— 4/5 个有
- `Int` —— 3/5 个有
- `JjkText` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `MuyeTextEditOutput` —— 2/5 个有
- `Note _O` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 768 - 768 | 5 | 100% |
| 高度 | 768 | 768 - 768 | 5 | 100% |
| 采样步数 | 5 | 5 - 5 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | lcm | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，观测区间 768 - 768，5 个样本，取值集中（一致性 100%）
- 高度 中位数 768，观测区间 768 - 768，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 5，观测区间 5 - 5，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 lcm，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
