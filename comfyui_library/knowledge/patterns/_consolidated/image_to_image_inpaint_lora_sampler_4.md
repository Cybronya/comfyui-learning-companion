---
name: image_to_image_inpaint_lora_sampler_4
type: Image To Image
frequency: 5
level: moderate
coverage: 0.7612
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, DualCLIPLoader, Fast Groups Bypasser (rgthree), FluxGuidance, Image Comparer (rgthree), ImageCrop, InpaintModelConditioning, Int, KSampler, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, ReferenceLatent, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageColorMatch, easy makeImageForICLora]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/ACE+F.2_万物迁移_写实人物_动漫角色_物品迁移进新图_2097165329062514690.json, 图片生成/图生图/ACE+F.2_万物迁移_写实人物_动漫角色_物品迁移进新图_2097504995510935553.json, 图片生成/图生图/FLUX 1.0 + Redux +（ACE进阶）局部修改（换衣）2套工作流合集_2045756197218816002.json, 图片生成/图生图/FLUX 1.0 + Redux +（ACE进阶）局部修改（换衣）2套工作流合集_2055025391521288193.json, 平台全量/ACE+F.2 万物迁移 （写实人物 _ 动漫角色 _ 物品）迁移进新图_2049046900711628802.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_lora_sampler_4

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/ACE+F.2_万物迁移_写实人物_动漫角色_物品迁移进新图_2097165329062514690.json、图片生成/图生图/ACE+F.2_万物迁移_写实人物_动漫角色_物品迁移进新图_2097504995510935553.json、图片生成/图生图/FLUX 1.0 + Redux +（ACE进阶）局部修改（换衣）2套工作流合集_2045756197218816002.json、图片生成/图生图/FLUX 1.0 + Redux +（ACE进阶）局部修改（换衣）2套工作流合集_2055025391521288193.json、平台全量/ACE+F.2 万物迁移 （写实人物 _ 动漫角色 _ 物品）迁移进新图_2049046900711628802.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 5 个 workflow 都包含：
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
- `Any Switch (rgthree)` —— 3/5 个有
- `FastCanvas` —— 3/5 个有
- `FastCanvasTool` —— 3/5 个有
- `RHHiddenNodes` —— 3/5 个有
- `RMBG` —— 3/5 个有
- `ShowText|pysssss` —— 3/5 个有
- `easy imageConcat` —— 3/5 个有
- `DifferentialDiffusion` —— 2/5 个有
- `DownloadAndLoadFlorence2Model` —— 2/5 个有
- `EG_ZZ_MH` —— 2/5 个有
- `Florence2Run` —— 2/5 个有
- `ImageToMask` —— 2/5 个有
- `InpaintCrop` —— 2/5 个有
- `InpaintExtendOutpaint` —— 2/5 个有
- `InpaintResize` —— 2/5 个有
- `InpaintStitch` —— 2/5 个有
- `LayerMask: SegmentAnythingUltra V2` —— 2/5 个有
- `MaskToImage` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 5 - 20 | 5 | 48% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | sgm_uniform | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 5 - 20，5 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
