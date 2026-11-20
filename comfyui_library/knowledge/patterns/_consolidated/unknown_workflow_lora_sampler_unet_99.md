---
name: unknown_workflow_lora_sampler_unet_99
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.84375
common_nodes: [CLIPLoader, CR Text, GetImageSize+, Image Comparer (rgthree), ImageLoader, JoinStrings, KSampler, LoraLoaderModelOnly, PainterFluxImageEdit, RMBG, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/(换背景)Klein 电商产品换背景_2101441007203217409.json, 图片生成/图生图/F.2 Klein 9B电商产品换背景_2061791311056953345.json, 图片生成/图生图/F.2klein 9b白底转家具背景美式现代经典风格_2059573998828216322.json, 图片生成/图生图/LLM参考反推(产品换背景)Klein 电商产品换背景_2101449962088390658.json, 图片生成/图生图/klein9b白底转家具现代美式经典风格支持2048px_2061278579966697474.json, 图片生成/文生图/Klein 电商产品换背景_2054585633120759809.json, 平台全量/产品换场景 电商产品换背景 Flux-2-klein-9B_2063808193297469441.json, 平台全量/产品白底图生成背景 Flux2Klein 产品换背景  商业级场景生成_2046405589181403138.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_99

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/(换背景)Klein 电商产品换背景_2101441007203217409.json、图片生成/图生图/F.2 Klein 9B电商产品换背景_2061791311056953345.json、图片生成/图生图/F.2klein 9b白底转家具背景美式现代经典风格_2059573998828216322.json、图片生成/图生图/LLM参考反推(产品换背景)Klein 电商产品换背景_2101449962088390658.json、图片生成/图生图/klein9b白底转家具现代美式经典风格支持2048px_2061278579966697474.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CR Text`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageLoader`
- `JoinStrings`
- `KSampler`
- `LoraLoaderModelOnly`
- `PainterFluxImageEdit`
- `RMBG`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/8 个有
- `PreviewImage` —— 6/8 个有
- `AILab_QwenVL` —— 5/8 个有
- `Fast Groups Bypasser (rgthree)` —— 5/8 个有
- `AILab_ColorInput` —— 4/8 个有
- `INTConstant` —— 4/8 个有
- `AILab_LoadImage` —— 2/8 个有
- `ConstrainImage|pysssss` —— 2/8 个有
- `DownloadAndLoadQwen2_5_VLModel` —— 2/8 个有
- `Flux2KleinColorAnchor` —— 2/8 个有
- `Qwen2_5_VL_Run` —— 2/8 个有
- `ReferenceLatent` —— 2/8 个有
- `easy imageDetailTransfer` —— 2/8 个有
- `Int` —— 1/8 个有
- `RHLLMChatNode` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 8 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（13/8 个样本）：Steps较低可能导致细节不足
