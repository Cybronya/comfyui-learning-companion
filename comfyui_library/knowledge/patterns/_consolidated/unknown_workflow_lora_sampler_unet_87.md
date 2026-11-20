---
name: unknown_workflow_lora_sampler_unet_87
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.801125
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Cherish the bond 矢量宠物定制_2002935381395927041.json, 图片生成/图生图/QWen-Edit-2509-一致性增强版-换衣_1970021369595502593.json, 图片生成/图生图/Qwen Image Edit2509-单图融合编辑工作流_1987877193000882178.json, 图片生成/图生图/Qwen Image Edit2509-多图融合编辑工作流_1987853484341006338.json, 图片生成/图生图/Qwen-Edit-2509 Consistance Edit（图像一致性） workflow v4.0_1989864091101614081.json, 图片生成/图生图/Qwen-Edit一键生成字体海报_2003726936436318209.json, 图片生成/图生图/Qwen-创意涂鸦海报_2041395180921692161.json, 图片生成/图生图/图生图-产品创意海报_2040662642892742657.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_87

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Cherish the bond 矢量宠物定制_2002935381395927041.json、图片生成/图生图/QWen-Edit-2509-一致性增强版-换衣_1970021369595502593.json、图片生成/图生图/Qwen Image Edit2509-单图融合编辑工作流_1987877193000882178.json、图片生成/图生图/Qwen Image Edit2509-多图融合编辑工作流_1987853484341006338.json、图片生成/图生图/Qwen-Edit-2509 Consistance Edit（图像一致性） workflow v4.0_1989864091101614081.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 7/8 个有
- `seed _O` —— 5/8 个有
- `Text _O` —— 4/8 个有
- `easy showAnything` —— 3/8 个有
- `Fast Groups Muter (rgthree)` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `Seed (rgthree)` —— 2/8 个有
- `TextCombinerTwo` —— 2/8 个有
- `TextInput_` —— 2/8 个有
- `EmptyLatentImage` —— 1/8 个有
- `ImageConcatMulti` —— 1/8 个有
- `PDIMAGE_LongerSize` —— 1/8 个有
- `easy imageConcat` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 50% |
| 调度器 | simple | - | 8 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 768 | - | 1 | 100% |
| 高度 | 1024 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 50%
- 调度器 最常用 simple，8 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
