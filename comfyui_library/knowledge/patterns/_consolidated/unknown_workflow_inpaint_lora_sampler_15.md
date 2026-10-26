---
name: unknown_workflow_inpaint_lora_sampler_15
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.861167
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), InpaintCrop, InpaintModelConditioning, InpaintStitch, KSampler, LayerMask: MaskStroke, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy imageInsetCrop]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/ACE万物迁移_1988895003441238017.json, 图片生成/图生图/FLUX 万物迁移工作流_2091471917231460354.json, 图片生成/图生图/FLUX、ACE++产品迁移、万物迁移_1937927899880013825.json, 图片生成/图生图/Flux_产品迁移_sdz_1935332432474198018.json, 图片生成/图生图/石头_1955118653920481281.json, 图片生成/图生图/细小产品迁移工作流_2036107912103333890.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_15

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/ACE万物迁移_1988895003441238017.json、图片生成/图生图/FLUX 万物迁移工作流_2091471917231460354.json、图片生成/图生图/FLUX、ACE++产品迁移、万物迁移_1937927899880013825.json、图片生成/图生图/Flux_产品迁移_sdz_1935332432474198018.json、图片生成/图生图/石头_1955118653920481281.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
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
- `GetImageSize+` —— 5/6 个有
- `GrowMaskWithBlur` —— 5/6 个有
- `ImageCompositeMasked` —— 5/6 个有
- `ImageScale` —— 5/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `Mask Fill Holes` —— 5/6 个有
- `easy makeImageForICLora` —— 5/6 个有
- `ImageAndMaskPreview` —— 4/6 个有
- `LayerMask: LoadFlorence2Model` —— 3/6 个有
- `LayerUtility: Florence2Image2Prompt` —— 3/6 个有
- `InpaintResize` —— 2/6 个有
- `GetImageSize` —— 1/6 个有
- `ImageResize+` —— 1/6 个有
- `ImageToMask` —— 1/6 个有
- `LayerMask: MaskPreview` —— 1/6 个有
- `LayerUtility: ColorImage` —— 1/6 个有
- `MaskToImage` —— 1/6 个有
- `easy imageConcat` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 6 | 59% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | beta | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（8/6 个样本）：Steps较低可能导致细节不足
