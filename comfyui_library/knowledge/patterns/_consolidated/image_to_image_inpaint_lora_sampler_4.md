---
name: image_to_image_inpaint_lora_sampler_4
type: Image To Image
frequency: 4
level: moderate
coverage: 0.766
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, DualCLIPLoader, Fast Groups Bypasser (rgthree), FluxGuidance, Image Comparer (rgthree), ImageCrop, InpaintModelConditioning, Int, KSampler, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, ReferenceLatent, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageColorMatch, easy makeImageForICLora]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/ACE+F.2_万物迁移_写实人物_动漫角色_物品迁移进新图_2097165329062514690.json, 图片生成/图生图/ACE+F.2_万物迁移_写实人物_动漫角色_物品迁移进新图_2097504995510935553.json, 图片生成/图生图/FLUX 1.0 + Redux +（ACE进阶）局部修改（换衣）2套工作流合集_2045756197218816002.json, 图片生成/图生图/FLUX 1.0 + Redux +（ACE进阶）局部修改（换衣）2套工作流合集_2055025391521288193.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_lora_sampler_4

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/ACE+F.2_万物迁移_写实人物_动漫角色_物品迁移进新图_2097165329062514690.json、图片生成/图生图/ACE+F.2_万物迁移_写实人物_动漫角色_物品迁移进新图_2097504995510935553.json、图片生成/图生图/FLUX 1.0 + Redux +（ACE进阶）局部修改（换衣）2套工作流合集_2045756197218816002.json、图片生成/图生图/FLUX 1.0 + Redux +（ACE进阶）局部修改（换衣）2套工作流合集_2055025391521288193.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageCrop`
- `InpaintModelConditioning`
- `Int`
- `KSampler`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageColorMatch`
- `easy makeImageForICLora`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 2/4 个有
- `DifferentialDiffusion` —— 2/4 个有
- `DownloadAndLoadFlorence2Model` —— 2/4 个有
- `EG_ZZ_MH` —— 2/4 个有
- `FastCanvas` —— 2/4 个有
- `FastCanvasTool` —— 2/4 个有
- `Florence2Run` —— 2/4 个有
- `ImageToMask` —— 2/4 个有
- `InpaintCrop` —— 2/4 个有
- `InpaintExtendOutpaint` —— 2/4 个有
- `InpaintResize` —— 2/4 个有
- `InpaintStitch` —— 2/4 个有
- `LayerMask: SegmentAnythingUltra V2` —— 2/4 个有
- `MaskToImage` —— 2/4 个有
- `RHHiddenNodes` —— 2/4 个有
- `RMBG` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `easy imageConcat` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12.5 | 5 - 20 | 4 | 40% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | sgm_uniform | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12.5，观测区间 5 - 20，4 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
