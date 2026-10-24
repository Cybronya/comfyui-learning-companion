---
name: unknown_workflow_lora_sampler_unet_51
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8235
common_nodes: [AutoCropFaces, CLIPLoader, EmptyLatentImage, Image Paste Crop, ImageAndMaskPreview, ImageResizeKJv2, KSampler, LayerMask: SegformerB2ClothesUltra, LayerUtility: ImageRemoveAlpha, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QwenEdit2511最强换脸_换头工作流 融合性超好_2003147842309038081.json, 图片生成/图生图/edit换脸_2110686259562762241.json, 图片生成/图生图/qwen_edit_2509_一键换头工作流_2015385940776194050.json, 图片生成/图生图/换头QwenEdit超强一致性_2039727354066509825.json, 图片生成/图生图/换头，换状， 绝对的一致性_2010542559831007234.json, 图片生成/图生图/最强换头术=QwenEdi_1997203172911419394.json, 图片生成/图生图/最强换头术=QwenEdit2511换脸=B站艾橘溪_1990343142316625921.json, 图片生成/图生图/短剧换头换脸Qwenedit2511_2018615350392262657.json, 图片生成/图生图/超强换头术 人物写实换脸  极速版_2089907924406726658.json, 图片生成/文生图/图一头换到图二上+换头+换脸+全节点注释_2056949319693070338.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_51

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/QwenEdit2511最强换脸_换头工作流 融合性超好_2003147842309038081.json、图片生成/图生图/edit换脸_2110686259562762241.json、图片生成/图生图/qwen_edit_2509_一键换头工作流_2015385940776194050.json、图片生成/图生图/换头QwenEdit超强一致性_2039727354066509825.json、图片生成/图生图/换头，换状， 绝对的一致性_2010542559831007234.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 10 个 workflow 都包含：
- `AutoCropFaces`
- `CLIPLoader`
- `EmptyLatentImage`
- `Image Paste Crop`
- `ImageAndMaskPreview`
- `ImageResizeKJv2`
- `KSampler`
- `LayerMask: SegformerB2ClothesUltra`
- `LayerUtility: ImageRemoveAlpha`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 7/10 个有
- `ImageConcanate` —— 7/10 个有
- `LayerUtility: PurgeVRAM` —— 7/10 个有
- `PrimitiveInt` —— 7/10 个有
- `SetNode` —— 7/10 个有
- `PreviewImage` —— 4/10 个有
- `CFGNorm` —— 3/10 个有
- `ConditioningZeroOut` —— 3/10 个有
- `Get Image Size` —— 3/10 个有
- `ImageScale` —— 3/10 个有
- `CR Text` —— 2/10 个有
- `ImpactInt` —— 2/10 个有
- `FaceAlign` —— 1/10 个有
- `FaceAnalysisModels` —— 1/10 个有
- `RHHiddenNodes` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 512 - 720 | 10 | 86% |
| 高度 | 1280 | 512 - 1280 | 10 | 66% |
| 采样步数 | 4 | 4 - 8 | 10 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 720，观测区间 512 - 720，10 个样本，取值集中（一致性 86%）
- 高度 中位数 1280，观测区间 512 - 1280，10 个样本
- 采样步数 中位数 4，观测区间 4 - 8，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
