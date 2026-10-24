---
name: unknown_workflow_lora_sampler_unet_84
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.75075
common_nodes: [CLIPLoader, ConditioningZeroOut, CropWithPadInfo, KSampler, LoraLoaderModelOnly, QwenEditConfigPreparer, QwenEditOutputExtractor, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问edit局部重绘_1999472373009182721.json, 图片生成/图生图/千问→放大25步（模型渲染25步-发布版本v1）_2062006779185291265.json, 图片生成/图生图/换装换脸总丢细节？一键换装+全节点注释，小白也能跑通_2054536498040582146.json, 图片生成/图生图/模特换装_2071437323803389954.json, 图片生成/图生图/电商模特一键换衣工作流_2072610897067073538.json, 图片生成/图生图/超强换装，模特换装蓝菲儿_2058052511046656002.json, 图片生成/图生图/👉千问多人指定自动换装 更好一致性🧁_1991373219519135745.json, 图片生成/图生图/👾超视距AI换装千问版👾26-01-15_2011682224655044609.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_84

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/千问edit局部重绘_1999472373009182721.json、图片生成/图生图/千问→放大25步（模型渲染25步-发布版本v1）_2062006779185291265.json、图片生成/图生图/换装换脸总丢细节？一键换装+全节点注释，小白也能跑通_2054536498040582146.json、图片生成/图生图/模特换装_2071437323803389954.json、图片生成/图生图/电商模特一键换衣工作流_2072610897067073538.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `CropWithPadInfo`
- `KSampler`
- `LoraLoaderModelOnly`
- `QwenEditConfigPreparer`
- `QwenEditOutputExtractor`
- `SaveImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 7/8 个有
- `PrimitiveStringMultiline` —— 6/8 个有
- `Image Comparer (rgthree)` —— 5/8 个有
- `ImageScaleBy` —— 4/8 个有
- `GetNode` —— 3/8 个有
- `QwenEditAdaptiveLongestEdge` —— 3/8 个有
- `Seed (rgthree)` —— 3/8 个有
- `SetNode` —— 3/8 个有
- `Note Plus (mtb)` —— 2/8 个有
- `CR Text` —— 1/8 个有
- `ImageToMask` —— 1/8 个有
- `ImageURLLoader` —— 1/8 个有
- `MaskPreview+` —— 1/8 个有
- `Qwen3VL_Advanced` —— 1/8 个有
- `RH_LLMAPI_NODE` —— 1/8 个有
- `Sa2VANodeTpl` —— 1/8 个有
- `TextInput_` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 25 | 8 | 18% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | beta57 | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 25，8 个样本，取值分散，一致性仅 18%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 beta57，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（7/8 个样本）：Steps较低可能导致细节不足
