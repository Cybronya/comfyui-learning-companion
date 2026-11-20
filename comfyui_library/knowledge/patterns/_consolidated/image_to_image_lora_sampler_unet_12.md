---
name: image_to_image_lora_sampler_unet_12
type: Image To Image
frequency: 24
level: strong
coverage: 0.833833
common_nodes: [CFGNorm, CLIPLoader, GetImageSize, Image Blank, ImageConcanate, ImageScaleToTotalPixels, Int, KSampler, LayerMask: SegformerB2ClothesUltra, LayerUtility: ImageBlendAdvance V3, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptConcat]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit 千问百搭秀  角色一致性 姿势控制 图生图_1976831964563095553.json, 图片生成/图生图/Qwen eidt 2509 指定面貌 服装 姿势_1980567131815329793.json, 图片生成/图生图/全能图片V1 平替丨服装百搭秀+姿势控制+OOTD！！_1981181173760163841.json, 图片生成/图生图/千问百搭秀  完美平替全能图片V1_1972839275874177026.json, 图片生成/图生图/千问百搭秀  完美平替全能图片V1_2007449812660129794.json, 图片生成/图生图/千问自动穿戴_1967577548517437441.json, 图片生成/图生图/图片-千问完美平替全能图片V1_1963420621466218497.json, 图片生成/图生图/图片-千问百搭秀 v2 姿势控制_1976630272911347714.json, 图片生成/图生图/欧美杂志换装_1963077824921972737.json, 图片生成/图生图/百搭秀 完美平替全能图片V1_1971504458314235906.json, 图片生成/图生图/穿比基尼_1970012267393806338.json, 图片生成/文生图/电商衣服配饰百搭秀---OOTD9---完美平替全能图片V1_2024459821239508993.json, 平台全量/【QWEN EDIT OOTD PLUS服装穿搭人物一致换装 套图 服装迁移 完美换装 穿搭 套图_1971388044123258882.json, 平台全量/【精准换装】Qwen image 千问写实摄影时装秀 杂志封面 人物一致换装 完美平替全能图片V1_1962350357240287234.json, 平台全量/【超强一致性】千问百搭秀 Qwen edit 编辑&多图融合  换装换脸 替换背景 物品迁移 电商产_1983042419744735233.json, 平台全量/【超强一致性】千问百搭秀 Qwen edit 编辑&多图融合  换装换脸 替换背景 物品迁移 电商产_1985207658493919234.json, 平台全量/【超强一致性】千问百搭秀 Qwen edit 编辑&多图融合  换装换脸 替换背景 物品迁移 电商产_1986321991152140290.json, 平台全量/人物换装 终极姿势控制 Qwen edit image 人物百搭秀Pro  平替全能图片V1 Pro_1993498513199874050.json, 平台全量/千问最新换装指定动作+人脸控制电商套图一气呵成完美平台 全能图片V1_1983211639212285954.json, 平台全量/千问最新换装指定动作+人脸控制电商套图完美生成_1983215200193159169.json, 平台全量/千问服装穿搭换装 姿势控制 OOTD 完美平替全能图片V1_1983205975257718785.json, 平台全量/千问百搭秀  OOTD  完美平替全能图片V1_1961554377045688321.json, 平台全量/千问百搭秀 v2 姿势控制 OOTD 完美平替全能图片V1_1964901394643865602.json, 平台全量/千问百搭秀 v2_1965755903700041730.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_12

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/图生图/Qwen Edit 千问百搭秀  角色一致性 姿势控制 图生图_1976831964563095553.json、图片生成/图生图/Qwen eidt 2509 指定面貌 服装 姿势_1980567131815329793.json、图片生成/图生图/全能图片V1 平替丨服装百搭秀+姿势控制+OOTD！！_1981181173760163841.json、图片生成/图生图/千问百搭秀  完美平替全能图片V1_1972839275874177026.json、图片生成/图生图/千问百搭秀  完美平替全能图片V1_2007449812660129794.json…）

- **类型**：Image To Image
- **样本数**：24
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 24 个 workflow 都包含：
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
- `Fast Groups Bypasser (rgthree)` —— 21/24 个有
- `Compare` —— 13/24 个有
- `InversionDemoLazySwitch` —— 13/24 个有
- `RHHiddenNodes` —— 12/24 个有
- `TextEncodeQwenImageEdit` —— 12/24 个有
- `EmptyLatentImage` —— 11/24 个有
- `GetNode` —— 11/24 个有
- `ImpactSwitch` —— 11/24 个有
- `LayerUtility: ImageReel` —— 11/24 个有
- `LayerUtility: ImageReelComposit` —— 11/24 个有
- `PreviewImage` —— 11/24 个有
- `SetNode` —— 11/24 个有
- `Anything Everywhere3` —— 1/24 个有
- `ControlNetApplyAdvanced` —— 1/24 个有
- `ControlNetLoader` —— 1/24 个有
- `DWPreprocessor` —— 1/24 个有
- `SetUnionControlNetType` —— 1/24 个有
- `easy cleanGpuUsed` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 12 | 24 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 24 | 100% |
| 采样算法 | euler | - | 24 | 100% |
| 调度器 | simple | - | 24 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 24 | 100% |
| 宽度 | 1152 | 1152 - 1152 | 11 | 100% |
| 高度 | 1536 | 1536 - 1536 | 11 | 100% |
| ControlNet 权重 | 1.8 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/24 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 12，24 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，24 个样本，一致性 100%
- 调度器 最常用 simple，24 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 宽度 中位数 1152，观测区间 1152 - 1152，11 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，11 个样本，取值集中（一致性 100%）
- 高发问题（23/24 个样本）：Steps较低可能导致细节不足
