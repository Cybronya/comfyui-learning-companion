---
name: unknown_workflow_lora_sampler_unet_44
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.904231
common_nodes: [CLIPLoader, GetImageSize+, Image Comparer (rgthree), KSampler, LoraLoaderModelOnly, PainterFluxImageEdit, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX.2 Klein9B电商产品换背景_2058110770403176449.json, 图片生成/图生图/FLUX.2+Klein9B单图_2105504127831855106.json, 图片生成/图生图/FLUX.2+Klein9B单图_2105650210314743809.json, 图片生成/图生图/FLUX2_Klein去除ai感_2035190919212834818.json, 图片生成/图生图/Klein_4步自适应光照溶图打光_2087360495371251714.json, 图片生成/图生图/Klein_万能产品改色支持色值改色_2087362725247803393.json, 图片生成/图生图/Klein_产品换背景_2087364324204564481.json, 图片生成/图生图/最新产品换背景-Klein_2063910955804880897.json, 图片生成/图生图/白底产品换背景(零偏移)——Klein-9B_2071872504309837826.json, 图片生成/图生图/蒜香卡普klein9b白底转家具现代美式经典风格支持2048px_2050820159954272257.json, 图片生成/文生图/Klein-9B 电商产品换背景(零偏移)_2049738363753779201.json, 图片生成/文生图/klein9b白底转家具现代美式经典风格支持2048px_2055481736271802370.json, 平台全量/Klein_产品换背景_2019580260903292929.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_44

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/FLUX.2 Klein9B电商产品换背景_2058110770403176449.json、图片生成/图生图/FLUX.2+Klein9B单图_2105504127831855106.json、图片生成/图生图/FLUX.2+Klein9B单图_2105650210314743809.json、图片生成/图生图/FLUX2_Klein去除ai感_2035190919212834818.json、图片生成/图生图/Klein_4步自适应光照溶图打光_2087360495371251714.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoraLoaderModelOnly`
- `PainterFluxImageEdit`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 12/13 个有
- `ConstrainImage|pysssss` —— 12/13 个有
- `ImageLoader` —— 12/13 个有
- `JoinStrings` —— 11/13 个有
- `AILab_ColorInput` —— 10/13 个有
- `RMBG` —— 10/13 个有
- `ShowText|pysssss` —— 6/13 个有
- `PreviewImage` —— 4/13 个有
- `easy imageDetailTransfer` —— 4/13 个有
- `ImagePadForOutpaint` —— 3/13 个有
- `LoadImage` —— 3/13 个有
- `AILab_QwenVL` —— 2/13 个有
- `Fast Groups Bypasser (rgthree)` —— 2/13 个有
- `Flux2KleinColorAnchor` —— 2/13 个有
- `Int` —— 2/13 个有
- `ReferenceLatent` —— 2/13 个有
- `ImageStitch` —— 1/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 13 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.1 | 13 | 97% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 85% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.1，13 个样本，取值集中（一致性 97%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 85%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（17/13 个样本）：Steps较低可能导致细节不足
