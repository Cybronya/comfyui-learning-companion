---
name: image_to_image_lora_sampler_clip_70
type: Image To Image
frequency: 6
level: strong
coverage: 0.867333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Image Comparer (rgthree), JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/服装精修抠图 Flux2 klein 9b 拍照图片去背景 去褶皱3D展示 生成白底图_2036320212814925826.json, 平台全量/珠宝精修_2072676815323357186.json, 平台全量/精修首饰_珠宝 万能产品修图 Flux-2-Klein-9B 抠图png透明图 五金数码珠宝箱包 产_2037455919994376193.json, 平台全量/静物鞋子修饰_2061265139613134849.json, 平台全量/首饰草图转换V1.0_2117909332481368065.json, 数字人/数字人/空白工作流_2088544556475305986.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_70

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/服装精修抠图 Flux2 klein 9b 拍照图片去背景 去褶皱3D展示 生成白底图_2036320212814925826.json、平台全量/珠宝精修_2072676815323357186.json、平台全量/精修首饰_珠宝 万能产品修图 Flux-2-Klein-9B 抠图png透明图 五金数码珠宝箱包 产_2037455919994376193.json、平台全量/静物鞋子修饰_2061265139613134849.json、平台全量/首饰草图转换V1.0_2117909332481368065.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Image Comparer (rgthree)`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/6 个有
- `FluxGuidance` —— 5/6 个有
- `ImpactInt` —— 5/6 个有
- `SaveImage` —— 5/6 个有
- `easy promptConcat` —— 5/6 个有
- `Float` —— 4/6 个有
- `GrowMask` —— 3/6 个有
- `InvertMask` —— 3/6 个有
- `JoinImageWithAlpha` —— 3/6 个有
- `LayerMask: BiRefNetUltraV2` —— 3/6 个有
- `LayerMask: LoadBiRefNetModelV2` —— 3/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `SaveImagePlus` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 5 | 6 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 5，6 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（7/6 个样本）：Steps较低可能导致细节不足
