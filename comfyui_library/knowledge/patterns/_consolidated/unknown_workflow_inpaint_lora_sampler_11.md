---
name: unknown_workflow_inpaint_lora_sampler_11
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.85675
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), InpaintCrop, InpaintModelConditioning, InpaintStitch, KSampler, LayerMask: MaskStroke, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy imageInsetCrop]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/ACE万物迁移_1988895003441238017.json, 图片生成/图生图/FLUX 万物迁移工作流_2091471917231460354.json, 图片生成/图生图/FLUX、ACE++产品迁移、万物迁移_1937927899880013825.json, 图片生成/图生图/Flux_产品迁移_sdz_1935332432474198018.json, 图片生成/图生图/石头_1955118653920481281.json, 图片生成/图生图/细小产品迁移工作流_2036107912103333890.json, 平台全量/ACE万物迁移工作流_1917951994667925506.json, 平台全量/ACE万物迁移工作流【AI小王子】_1915612316203679745.json, 平台全量/ACE万物迁移工作流（学习版）_1975178341751894017.json, 平台全量/Redex+ACE++万物产品迁移+融合光影工作流_1892831806801010690.json, 平台全量/万物迁移 电商神器 大物件 首饰 清晰 无黑边 fill+redux_1953758894973702146.json, 平台全量/吉驰万物迁移_1955925531768356865.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_11

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/ACE万物迁移_1988895003441238017.json、图片生成/图生图/FLUX 万物迁移工作流_2091471917231460354.json、图片生成/图生图/FLUX、ACE++产品迁移、万物迁移_1937927899880013825.json、图片生成/图生图/Flux_产品迁移_sdz_1935332432474198018.json、图片生成/图生图/石头_1955118653920481281.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `KSampler`
- `LayerMask: MaskStroke`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageInsetCrop`

**可变部分**（部分 workflow 才有）：
- `GetImageSize+` —— 11/12 个有
- `GrowMaskWithBlur` —— 11/12 个有
- `ImageCompositeMasked` —— 11/12 个有
- `ImageScale` —— 11/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/12 个有
- `Mask Fill Holes` —— 11/12 个有
- `easy makeImageForICLora` —— 11/12 个有
- `ImageAndMaskPreview` —— 9/12 个有
- `LayerMask: LoadFlorence2Model` —— 8/12 个有
- `LayerUtility: Florence2Image2Prompt` —— 8/12 个有
- `InpaintResize` —— 2/12 个有
- `Fast Groups Bypasser (rgthree)` —— 1/12 个有
- `GetImageSize` —— 1/12 个有
- `ImageResize+` —— 1/12 个有
- `ImageToMask` —— 1/12 个有
- `LayerMask: MaskPreview` —— 1/12 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/12 个有
- `LayerUtility: ColorImage` —— 1/12 个有
- `MaskPreview+` —— 1/12 个有
- `MaskToImage` —— 1/12 个有
- `TextInput_` —— 1/12 个有
- `easy getNode` —— 1/12 个有
- `easy imageConcat` —— 1/12 个有
- `easy setNode` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 12 | 58% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | beta | - | 12 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（17/12 个样本）：Steps较低可能导致细节不足
