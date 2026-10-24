---
name: image_to_image_sampler_clip_unet_125
type: Image To Image
frequency: 4
level: strong
coverage: 0.88375
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FastCanvas, FastCanvasTool, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/换头kontext1_1957067763853266946.json, 图片生成/图生图/最简单的万物迁移工作流_1993107473835950081.json, 图片生成/图生图/电商产品换背景_1977564005516627970.json, 图片生成/图生图/电商商品演示_Kontext-DEV稳定双图编辑_1940684028246732802.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_125

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/换头kontext1_1957067763853266946.json、图片生成/图生图/最简单的万物迁移工作流_1993107473835950081.json、图片生成/图生图/电商产品换背景_1977564005516627970.json、图片生成/图生图/电商商品演示_Kontext-DEV稳定双图编辑_1940684028246732802.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FastCanvas`
- `FastCanvasTool`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 3/4 个有
- `RepeatLatentBatch` —— 3/4 个有
- `ImageScaleDownToSize` —— 2/4 个有
- `ImageStitch` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `easy imageRemBg` —— 2/4 个有
- `BiRefNetRMBG` —— 1/4 个有
- `DeepTranslatorTextNode` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `LayerMask: RmBgUltra V2` —— 1/4 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/4 个有
- `LayerUtility: CropByMask V2` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy clearCacheAll` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
