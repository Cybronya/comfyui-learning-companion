---
name: text_to_image_controlnet_lora_sampler_16
type: Text To Image
frequency: 3
level: moderate
coverage: 0.893333
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApply, DiffControlNetLoader, EmptyLatentImage, KSampler, LoadImage, LoraLoader, PreviewImage, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图标毛绒质感转换模型_1915368356155953154.json, 图片生成/图生图/毛绒logo_1914950742438834178.json, 图片生成/文生图/输出三种风格图片_1998184803860144130.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_lora_sampler_16

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/图标毛绒质感转换模型_1915368356155953154.json、图片生成/图生图/毛绒logo_1914950742438834178.json、图片生成/文生图/输出三种风格图片_1998184803860144130.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApply`
- `DiffControlNetLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `CannyEdgePreprocessor` —— 2/3 个有
- `Image Filter Adjustments` —— 2/3 个有
- `ImageResize+` —— 2/3 个有
- `AIO_Preprocessor` —— 1/3 个有
- `ImageScaleBy` —— 1/3 个有
- `Primitive string multiline [Crystools]` —— 1/3 个有
- `VAELoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 9 - 20 | 3 | 68% |
| Prompt 约束强度(CFG) | 7 | 1.7 - 7 | 3 | 52% |
| 采样算法 | dpmpp_2m | - | 3 | 67% |
| 调度器 | karras | - | 3 | 67% |
| 重绘幅度 | 1 | 0.5 - 1 | 3 | 72% |
| ControlNet 权重 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 0.5 | 0.5 - 0.7 | 3 | 83% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 768 | 768 - 768 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 9 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 7，观测区间 1.7 - 7，3 个样本
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 67%
- 调度器 最常用 karras，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，3 个样本
- ControlNet 权重 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.5，观测区间 0.5 - 0.7，3 个样本，取值集中（一致性 83%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 768，观测区间 768 - 768，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
