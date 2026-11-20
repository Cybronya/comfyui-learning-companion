---
name: unknown_workflow_lora_sampler_unet_152
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.933
common_nodes: [CLIPLoader, ConditioningZeroOut, FaceAnalysisModels, FaceBoundingBox, Image Comparer (rgthree), ImageCompositeMasked, KSampler, LayerUtility: BooleanOperatorV2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleRestore V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, Preview from image [Crystools], QwenEditTextEncode_EditUtils, SaveImage, Switch string [Crystools], TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UNETLoader, VAEDecode, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch, easy imageSize, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/(无损画质)商业级面部磨皮（超好用）_2036328516828012545.json, 图片生成/图生图/豹豹喵呜制作：商业级面部磨皮工作流_2034284216367718401.json, 平台全量/小红书 _ FireRed _ 素颜美妆_1890326859761197058.json, 平台全量/换头换脸 FireRed 皮肤增加细节 去除AI模糊塑料感小红书  更好一致性 高清修复细节_2045664855700545537.json, 平台全量/换头换脸 皮肤增加细节 去除AI模糊塑料感小红书 FireRed 更好一致性 高清修复细节_2035874556384124929.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_152

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/(无损画质)商业级面部磨皮（超好用）_2036328516828012545.json、图片生成/图生图/豹豹喵呜制作：商业级面部磨皮工作流_2034284216367718401.json、平台全量/小红书 _ FireRed _ 素颜美妆_1890326859761197058.json、平台全量/换头换脸 FireRed 皮肤增加细节 去除AI模糊塑料感小红书  更好一致性 高清修复细节_2045664855700545537.json、平台全量/换头换脸 皮肤增加细节 去除AI模糊塑料感小红书 FireRed 更好一致性 高清修复细节_2035874556384124929.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `Image Comparer (rgthree)`
- `ImageCompositeMasked`
- `KSampler`
- `LayerUtility: BooleanOperatorV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleRestore V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `Preview from image [Crystools]`
- `QwenEditTextEncode_EditUtils`
- `SaveImage`
- `Switch string [Crystools]`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy imageSize`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 5 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 0.75 - 1 | 5 | 86% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.75 - 1，5 个样本，取值集中（一致性 86%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
