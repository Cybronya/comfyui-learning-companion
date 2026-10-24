---
name: image_to_image_lora_sampler_clip_7
type: Image To Image
frequency: 19
level: moderate
coverage: 0.941263
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/产品换背景-klein_2042792273842282498.json, 图片生成/图生图/图生图-百度-ERNIE-Image_2044557979541835777.json, 图片生成/图生图/平铺图转立体图 3D立体图_2086699823432028162.json, 图片生成/图生图/挂拍_平铺图生成立体图 隐形模特 电商服饰展示 服饰提取 3D立体图_2064913964567457794.json, 图片生成/图生图/挂拍_平铺图转立体图 隐形模特 电商服饰展示 服饰提取 3D立体图_2041123739076665345.json, 图片生成/图生图/挂拍_平铺图转立体图 隐形模特 电商服饰展示 服饰提取 3D立体图_2057332722913333250.json, 图片生成/图生图/挂拍_平铺图转立体图 隐形模特 电商服饰展示 服饰提取 3D立体图_2064652694303887361.json, 图片生成/图生图/挂拍_平铺图转立体图 隐形模特 电商服饰展示 服饰提取 3D立体图_2074044441094082561.json, 图片生成/图生图/挂拍_平铺图转立体图+隐形模特+电商服饰展示+服饰提取+3D立体图_2073971346475933697.json, 图片生成/图生图/挂拍_平铺图转立体图_隐形模特_电商服饰展示_服饰提取_3D立体图_2062419055998496770.json, 图片生成/图生图/挂拍_平铺图转立体图_隐形模特_电商服饰展示_服饰提取_3D立体图_2092893109830115330.json, 图片生成/图生图/挂拍_平铺图转立体图_隐形模特_电商服饰展示_服饰提取_3D立体图_2093501578065043458.json, 图片生成/图生图/服装展示  电商服装  平铺转立体图_2070218753207529474.json, 图片生成/图生图/服装展示  电商服装  平铺转立体图_2070576319703896065.json, 图片生成/图生图/服装平铺图转立体图，服饰提取3D立体图_2057289672996507650.json, 图片生成/图生图/服装平面图提取生成电商白底图立体图_2065861601772789762.json, 图片生成/图生图/电商服饰展示 服饰提取 平铺图转立体图 3D立体化隐形模特_2079807412177031169.json, 图片生成/图生图/电商服饰提取 3D立体图 挂拍_平铺图转立体图_2054016935746121729.json, 图片生成/图生图/粉嫩皮肤 Klein 9B_2044917625544773634.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_7

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/产品换背景-klein_2042792273842282498.json、图片生成/图生图/图生图-百度-ERNIE-Image_2044557979541835777.json、图片生成/图生图/平铺图转立体图 3D立体图_2086699823432028162.json、图片生成/图生图/挂拍_平铺图生成立体图 隐形模特 电商服饰展示 服饰提取 3D立体图_2064913964567457794.json、图片生成/图生图/挂拍_平铺图转立体图 隐形模特 电商服饰展示 服饰提取 3D立体图_2041123739076665345.json…）

- **类型**：Image To Image
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 18/19 个有
- `ReferenceLatent` —— 18/19 个有
- `EmptyFlux2LatentImage` —— 16/19 个有
- `LayerUtility: FluxKontextImageScale` —— 16/19 个有
- `easy imageSize` —— 14/19 个有
- `scale` —— 3/19 个有
- `AdaptiveLongestEdge_EditUtils` —— 2/19 个有
- `Flux2KleinConfigPreparer_EditUtils` —— 2/19 个有
- `Flux2KleinModelConfig_EditUtils` —— 2/19 个有
- `GetImageSize` —— 2/19 个有
- `EditTextEncode_EditUtils` —— 1/19 个有
- `KSamplerAdvanced` —— 1/19 个有
- `ModelSamplingAuraFlow` —— 1/19 个有
- `PrimitiveStringMultiline` —— 1/19 个有
- `TT_img_enc` —— 1/19 个有
- `easy clearCacheAll` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 2 - 20 | 19 | 35% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 19 | 69% |
| 采样算法 | euler | - | 19 | 100% |
| 调度器 | simple | - | 19 | 95% |
| 重绘幅度 | 1 | 0.5 - 1 | 19 | 89% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 18/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 2 - 20，19 个样本，取值分散，一致性仅 35%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，19 个样本
- 采样算法 最常用 euler，19 个样本，一致性 100%
- 调度器 最常用 simple，19 个样本，一致性 95%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，19 个样本，取值集中（一致性 89%）
- 高发问题（18/19 个样本）：Steps较低可能导致细节不足
