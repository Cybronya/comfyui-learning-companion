---
name: unknown_workflow_lora_sampler_unet_52
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.845667
common_nodes: [CLIPLoader, CR Text, GetImageSize+, Image Comparer (rgthree), ImageLoader, JoinStrings, KSampler, LoraLoaderModelOnly, PainterFluxImageEdit, PreviewImage, RMBG, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Klein 电商产品换背景_2054585633120759809.json, 图片生成/文生图/Klein-9B 电商产品换背景(零偏移)_2049738363753779201.json, 图片生成/文生图/klein9b白底转家具现代美式经典风格支持2048px_2055481736271802370.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_52

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Klein 电商产品换背景_2054585633120759809.json、图片生成/文生图/Klein-9B 电商产品换背景(零偏移)_2049738363753779201.json、图片生成/文生图/klein9b白底转家具现代美式经典风格支持2048px_2055481736271802370.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageLoader`
- `JoinStrings`
- `KSampler`
- `LoraLoaderModelOnly`
- `PainterFluxImageEdit`
- `PreviewImage`
- `RMBG`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_ColorInput` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `easy imageDetailTransfer` —— 2/3 个有
- `AILab_QwenVL` —— 1/3 个有
- `ConstrainImage|pysssss` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Flux2KleinColorAnchor` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `ImagePadForOutpaint` —— 1/3 个有
- `Int` —— 1/3 个有
- `ReferenceLatent` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（4/3 个样本）：Steps较低可能导致细节不足
