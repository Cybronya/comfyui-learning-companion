---
name: unknown_workflow_sampler_vae_11
type: Unknown Workflow
frequency: 22
level: moderate
coverage: 0.828091
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, PreviewImage, RH_LLMAPI_NODE, SaveImage, Text Multiline, TextEncodeQwenImageEditPlusAdvance_lrzjason, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Nunchaku-千问Edit2509图像编辑-单图_1971195509471952898.json, 图片生成/图生图/Nunchaku-千问Edit2509图像编辑-多图融合_1971196973699284993.json, 图片生成/图生图/Qwen Image Edit 2511-单图编辑-提示词优化_2003833825832648705.json, 图片生成/图生图/Qwen Image Edit 2511-多图编辑-提示词优化_2003830071397892098.json, 图片生成/图生图/Qwen_image_Edit_2511千问图片编辑-单图_2003744147611762690.json, 图片生成/图生图/【Supermate】千问Edit2511图像编辑-脸部融合_2003714145767833601.json, 图片生成/图生图/千问Edit2509-单图-效果图转换手绘_1974725230688120833.json, 图片生成/图生图/千问Edit2509图像编辑-单图_1970831316243648513.json, 图片生成/图生图/千问Edit2509图像编辑-多图融合_1970858618352504834.json, 图片生成/图生图/千问Edit2509配合lora-单图-效果图转换手绘_1981990651577409537.json, 图片生成/图生图/千问Edit2511图像编辑-单图_2003636801959043074.json, 图片生成/图生图/千问Edit2511图像编辑-单图_2071099776166350849.json, 图片生成/图生图/千问Edit2511图像编辑-单图_2071102894794960897.json, 图片生成/图生图/千问Edit2511图像编辑-多图融合_2003558265445335041.json, 图片生成/图生图/千问Edit2511图像编辑-多图融合_2003625306432913410.json, 图片生成/图生图/千问Edit2511图像编辑-多图融合_2003650176382345217.json, 图片生成/图生图/千问Edit2511图像编辑-多图融合_2065079427427557377.json, 图片生成/图生图/千问Edit2511图像编辑-多图融合_2065096059185098753.json, 图片生成/图生图/千问Edit2511图像编辑-多图融合_2065416364688502786.json, 图片生成/图生图/千问Edit2511图像编辑_2003705719016833025.json, 图片生成/图生图/千问Edit2511多图编辑_2003716186049290242.json, 图片生成/图生图/老照片修复·超强悍_2010981023328243714.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_11

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/图生图/Nunchaku-千问Edit2509图像编辑-单图_1971195509471952898.json、图片生成/图生图/Nunchaku-千问Edit2509图像编辑-多图融合_1971196973699284993.json、图片生成/图生图/Qwen Image Edit 2511-单图编辑-提示词优化_2003833825832648705.json、图片生成/图生图/Qwen Image Edit 2511-多图编辑-提示词优化_2003830071397892098.json、图片生成/图生图/Qwen_image_Edit_2511千问图片编辑-单图_2003744147611762690.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 22 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `RH_LLMAPI_NODE`
- `SaveImage`
- `Text Multiline`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyLatentImage` —— 21/22 个有
- `UNETLoader` —— 21/22 个有
- `FluxKontextImageScale` —— 20/22 个有
- `LoraLoaderModelOnly` —— 20/22 个有
- `easy showAnything` —— 20/22 个有
- `FluxResolutionNode` —— 19/22 个有
- `LayerUtility: ImageReel` —— 12/22 个有
- `LayerUtility: ImageReelComposit` —— 12/22 个有
- `ImageConcanate` —— 11/22 个有
- `ImpactSwitch` —— 10/22 个有
- `Image Comparer (rgthree)` —— 3/22 个有
- `AIO_Preprocessor` —— 2/22 个有
- `AddLabel` —— 2/22 个有
- `GetNode` —— 2/22 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/22 个有
- `LayerUtility: PurgeVRAM V2` —— 2/22 个有
- `NunchakuQwenImageDiTLoader` —— 2/22 个有
- `PrimitiveInt` —— 2/22 个有
- `SetNode` —— 2/22 个有
- `ShowText|pysssss` —— 2/22 个有
- `Int` —— 1/22 个有
- `OpenposePreprocessor` —— 1/22 个有
- `TextInputBasic` —— 1/22 个有
- `easy promptLine` —— 1/22 个有
- `workflow>面部修复` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 22 | 62% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 22 | 62% |
| 采样算法 | euler | - | 22 | 95% |
| 调度器 | simple | - | 22 | 59% |
| 重绘幅度 | 1 | 1 - 1 | 22 | 100% |
| 宽度 | 512 | 512 - 512 | 21 | 100% |
| 高度 | 512 | 512 - 512 | 21 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，22 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，22 个样本
- 采样算法 最常用 euler，22 个样本，一致性 95%
- 调度器 最常用 simple，22 个样本，一致性 59%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，21 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，21 个样本，取值集中（一致性 100%）
- 高发问题（20/22 个样本）：Steps较低可能导致细节不足
