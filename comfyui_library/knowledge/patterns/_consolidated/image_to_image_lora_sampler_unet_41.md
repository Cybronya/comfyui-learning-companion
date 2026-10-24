---
name: image_to_image_lora_sampler_unet_41
type: Image To Image
frequency: 12
level: strong
coverage: 0.807667
common_nodes: [CFGNorm, CLIPLoader, GetImageSize, Image Blank, ImageConcanate, ImageScaleToTotalPixels, Int, KSampler, LayerMask: SegformerB2ClothesUltra, LayerUtility: ImageBlendAdvance V3, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptConcat]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit 千问百搭秀  角色一致性 姿势控制 图生图_1976831964563095553.json, 图片生成/图生图/Qwen eidt 2509 指定面貌 服装 姿势_1980567131815329793.json, 图片生成/图生图/全能图片V1 平替丨服装百搭秀+姿势控制+OOTD！！_1981181173760163841.json, 图片生成/图生图/千问百搭秀  完美平替全能图片V1_1972839275874177026.json, 图片生成/图生图/千问百搭秀  完美平替全能图片V1_2007449812660129794.json, 图片生成/图生图/千问自动穿戴_1967577548517437441.json, 图片生成/图生图/图片-千问完美平替全能图片V1_1963420621466218497.json, 图片生成/图生图/图片-千问百搭秀 v2 姿势控制_1976630272911347714.json, 图片生成/图生图/欧美杂志换装_1963077824921972737.json, 图片生成/图生图/百搭秀 完美平替全能图片V1_1971504458314235906.json, 图片生成/图生图/穿比基尼_1970012267393806338.json, 图片生成/文生图/电商衣服配饰百搭秀---OOTD9---完美平替全能图片V1_2024459821239508993.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_41

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Qwen Edit 千问百搭秀  角色一致性 姿势控制 图生图_1976831964563095553.json、图片生成/图生图/Qwen eidt 2509 指定面貌 服装 姿势_1980567131815329793.json、图片生成/图生图/全能图片V1 平替丨服装百搭秀+姿势控制+OOTD！！_1981181173760163841.json、图片生成/图生图/千问百搭秀  完美平替全能图片V1_1972839275874177026.json、图片生成/图生图/千问百搭秀  完美平替全能图片V1_2007449812660129794.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `GetImageSize`
- `Image Blank`
- `ImageConcanate`
- `ImageScaleToTotalPixels`
- `Int`
- `KSampler`
- `LayerMask: SegformerB2ClothesUltra`
- `LayerUtility: ImageBlendAdvance V3`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptConcat`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 10/12 个有
- `EmptyLatentImage` —— 8/12 个有
- `GetNode` —— 8/12 个有
- `ImpactSwitch` —— 8/12 个有
- `PreviewImage` —— 8/12 个有
- `SetNode` —— 8/12 个有
- `TextEncodeQwenImageEdit` —— 8/12 个有
- `Compare` —— 4/12 个有
- `InversionDemoLazySwitch` —— 4/12 个有
- `RHHiddenNodes` —— 4/12 个有
- `LayerUtility: ImageReel` —— 3/12 个有
- `LayerUtility: ImageReelComposit` —— 3/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 12 | 12 | 87% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 1152 | 1152 - 1152 | 8 | 100% |
| 高度 | 1536 | 1536 - 1536 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 12，12 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 1152，观测区间 1152 - 1152，8 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，8 个样本，取值集中（一致性 100%）
- 高发问题（11/12 个样本）：Steps较低可能导致细节不足
