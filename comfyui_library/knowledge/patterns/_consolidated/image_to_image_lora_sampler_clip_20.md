---
name: image_to_image_lora_sampler_clip_20
type: Image To Image
frequency: 10
level: strong
coverage: 0.8119
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, JjkText, KSampler, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/ComfyUI产品精修｜Flux.2 Klein去背景透明输出，全节点注释_2061069418087669761.json, 图片生成/图生图/Flux2 Klein 最强服装精修｜去褶皱｜版型整理｜3D立体质感_2112752360589193218.json, 图片生成/图生图/Klein——商业级首饰精修_2101443408731660290.json, 图片生成/图生图/产品高清放大精修_2074324801182855169.json, 图片生成/图生图/服装精修抠图 拍照图片去背景去褶皱3D展示生成白底图_2065051102151798785.json, 图片生成/图生图/珍珠饰品精修_2107821425888415745.json, 图片生成/图生图/珠宝玉石精修_2093656443189813250.json, 图片生成/图生图/精修Klein首饰_珠宝_2037102554424807425.json, 图片生成/图生图/精修首饰_珠宝_2037125851174670337.json, 图片生成/图生图/鞋子抠图-多视角生图-提取卖点全流程_2078423830032371714.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_20

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/ComfyUI产品精修｜Flux.2 Klein去背景透明输出，全节点注释_2061069418087669761.json、图片生成/图生图/Flux2 Klein 最强服装精修｜去褶皱｜版型整理｜3D立体质感_2112752360589193218.json、图片生成/图生图/Klein——商业级首饰精修_2101443408731660290.json、图片生成/图生图/产品高清放大精修_2074324801182855169.json、图片生成/图生图/服装精修抠图 拍照图片去背景去褶皱3D展示生成白底图_2065051102151798785.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `JjkText`
- `KSampler`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 9/10 个有
- `Float` —— 9/10 个有
- `FluxGuidance` —— 9/10 个有
- `GrowMask` —— 9/10 个有
- `InvertMask` —— 9/10 个有
- `JoinImageWithAlpha` —— 9/10 个有
- `Image Comparer (rgthree)` —— 8/10 个有
- `ImpactInt` —— 8/10 个有
- `easy promptConcat` —— 8/10 个有
- `PreviewImage` —— 2/10 个有
- `BRIA_RMBG_ModelLoader_Zho` —— 1/10 个有
- `BRIA_RMBG_Zho` —— 1/10 个有
- `CR Text` —— 1/10 个有
- `GetImageSize` —— 1/10 个有
- `GetNode` —— 1/10 个有
- `HfImageToRGB` —— 1/10 个有
- `ImageScale` —— 1/10 个有
- `NegiTools_CompositeImages` —— 1/10 个有
- `ReinhardColorTransfer` —— 1/10 个有
- `SaveImageAdvanced` —— 1/10 个有
- `SetNode` —— 1/10 个有
- `SolidColor` —— 1/10 个有
- `TT_img_enc` —— 1/10 个有
- `preview_mask` —— 1/10 个有
- `孤海注释` —— 1/10 个有
- `忽略多组孤海` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
