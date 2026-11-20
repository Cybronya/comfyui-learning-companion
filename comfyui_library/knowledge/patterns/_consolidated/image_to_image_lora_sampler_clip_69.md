---
name: image_to_image_lora_sampler_clip_69
type: Image To Image
frequency: 6
level: strong
coverage: 0.938333
common_nodes: [CLIPTextEncode, FluxGuidance, ImpactInt, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/全能产品精修（金属 首饰 服装鞋包 美妆）_2000775126763307010.json, 平台全量/劈腿_1996213553151483906.json, 平台全量/商业级人像精修，增加皮肤质感_2116013929829851138.json, 平台全量/展示胸_1996213773113376769.json, 平台全量/翘腿_1996214739845922818.json, 平台全量/翘臀_1996216062301577217.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_69

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/全能产品精修（金属 首饰 服装鞋包 美妆）_2000775126763307010.json、平台全量/劈腿_1996213553151483906.json、平台全量/商业级人像精修，增加皮肤质感_2116013929829851138.json、平台全量/展示胸_1996213773113376769.json、平台全量/翘腿_1996214739845922818.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `FluxGuidance`
- `ImpactInt`
- `KSampler`
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
- `DualCLIPLoader` —— 5/6 个有
- `Fast Groups Bypasser (rgthree)` —— 5/6 个有
- `Text _O` —— 5/6 个有
- `easy cleanGpuUsed` —— 5/6 个有
- `Label (rgthree)` —— 4/6 个有
- `LayerUtility: PurgeVRAM V2` —— 4/6 个有
- `ConditioningZeroOut` —— 2/6 个有
- `Float` —— 2/6 个有
- `Image Comparer (rgthree)` —— 2/6 个有
- `easy promptConcat` —— 2/6 个有
- `CLIPLoader` —— 1/6 个有
- `EmptyFlux2LatentImage` —— 1/6 个有
- `Image Filter Adjustments` —— 1/6 个有
- `ImpactSwitch` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `LayerColor: Brightness & Contrast` —— 1/6 个有
- `LayerColor: ColorTemperature` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 6 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，6 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
