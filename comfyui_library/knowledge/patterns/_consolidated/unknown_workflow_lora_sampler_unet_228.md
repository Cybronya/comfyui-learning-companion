---
name: unknown_workflow_lora_sampler_unet_228
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8695
common_nodes: [CFGNorm, CLIPLoader, CR Text, ConditioningZeroOut, Image Comparer (rgthree), JWStringConcat, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, QwenEditConfigPreparer, SaveImage, Seed (rgthree), TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/灯光角度编辑+qwen_edit_2509+_2074078675762503681.json, 平台全量/人物多视图+单独生成+Qwen_image_edit_2509_2074060067506311170.json, 平台全量/人物姿势迁移+2.0+Qwen_image_edit_2509_2074071010852298753.json, 平台全量/镜头角度和光照角度联合编辑+Qwen_image_edit_2509_2074078718523432962.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_228

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/灯光角度编辑+qwen_edit_2509+_2074078675762503681.json、平台全量/人物多视图+单独生成+Qwen_image_edit_2509_2074060067506311170.json、平台全量/人物姿势迁移+2.0+Qwen_image_edit_2509_2074071010852298753.json、平台全量/镜头角度和光照角度联合编辑+Qwen_image_edit_2509_2074078718523432962.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `JWStringConcat`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `QwenEditConfigPreparer`
- `SaveImage`
- `Seed (rgthree)`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `SimpleMath+` —— 3/4 个有
- `easy getNode` —— 3/4 个有
- `easy setNode` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `easy textIndexSwitch` —— 3/4 个有
- `Int` —— 2/4 个有
- `CR Text Concatenate` —— 1/4 个有
- `DWPreprocessor` —— 1/4 个有
- `LayerUtility: ImageReel` —— 1/4 个有
- `LayerUtility: ImageReelComposit` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `easy imageIndexSwitch` —— 1/4 个有
- `easy int` —— 1/4 个有
- `easy textSwitch` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（7/4 个样本）：Steps较低可能导致细节不足
