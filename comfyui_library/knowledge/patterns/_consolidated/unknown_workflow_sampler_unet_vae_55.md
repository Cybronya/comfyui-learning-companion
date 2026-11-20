---
name: unknown_workflow_sampler_unet_vae_55
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.748133
common_nodes: [CLIPLoader, EmptyLatentImage, KSampler, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Qwen Image 2.1图生图_2101694893407166466.json, 图片生成/图生图/Qwen Image2.1图生图2609_2106041136610635778.json, 图片生成/图生图/Qwen-Image-2.1 文生图增强版_2116117680150376450.json, 图片生成/图生图/image_qwen_image_2_1_ref2i_2102667025813426177.json, 图片生成/图生图/qwen_image_2_1_图像编辑-换背景和姿态_2102207016054906881.json, 图片生成/图生图/qwen_image_2_1_图像编辑-换装_2101845419922903041.json, 图片生成/图生图/qwen_image_2_1_图像编辑-文本换装_2101852516261646337.json, 图片生成/图生图/qwen_image_2_1_图像编辑_2101844068895641601.json, 图片生成/图生图/qwen_image_2_1_手持指定物品_2102203525789995009.json, 图片生成/图生图/qwen_image_2_1_移除背景_2102572577544818689.json, 图片生成/图生图/千问Qwen2.1图像编辑_2101904049938452481.json, 图片生成/文生图/qwen2.1文生图_2104275580962304002.json, 图片生成/文生图/qwen_image_2_1_图像编辑-换背景和姿态_2102217040533745665.json, 图片生成/文生图/千问 qwen image 2.1 单图编辑+全节点注释_2101953275674320897.json, 图片生成/文生图/千问 qwen image 2.1 多图编辑 图片编辑 +全节点注释_2101953245253033985.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_55

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1图生图_2101694893407166466.json、图片生成/图生图/Qwen Image2.1图生图2609_2106041136610635778.json、图片生成/图生图/Qwen-Image-2.1 文生图增强版_2116117680150376450.json、图片生成/图生图/image_qwen_image_2_1_ref2i_2102667025813426177.json、图片生成/图生图/qwen_image_2_1_图像编辑-换背景和姿态_2102207016054906881.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 14/15 个有
- `ResolutionSelector` —— 13/15 个有
- `ComfySwitchNode` —— 11/15 个有
- `QwenImage21Cache` —— 11/15 个有
- `PrimitiveStringMultiline` —— 6/15 个有
- `TextGenerateLTX2Prompt` —— 3/15 个有
- `Anything Everywhere3` —— 2/15 个有
- `CR Prompt Text` —— 2/15 个有
- `CR Text` —— 2/15 个有
- `BatchImagesNode` —— 1/15 个有
- `ImageScaleBy` —— 1/15 个有
- `Text` —— 1/15 个有
- `VAEDecodeTiled` —— 1/15 个有
- `VAEEncodeTiled` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 2048 | 15 | 77% |
| 高度 | 1024 | 1024 - 2048 | 15 | 75% |
| 采样步数 | 25 | 14 - 40 | 15 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | euler | - | 15 | 100% |
| 调度器 | simple | - | 15 | 100% |
| 重绘幅度 | 1 | 0.18 - 1 | 15 | 78% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 2048，15 个样本
- 高度 中位数 1024，观测区间 1024 - 2048，15 个样本
- 采样步数 中位数 25，观测区间 14 - 40，15 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，15 个样本，一致性 100%
- 调度器 最常用 simple，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.18 - 1，15 个样本
