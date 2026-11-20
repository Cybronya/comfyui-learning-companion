---
name: image_to_image_lora_sampler_clip_90
type: Image To Image
frequency: 5
level: strong
coverage: 0.8914
common_nodes: [CLIPTextEncode, ConditioningZeroOut, FluxGuidance, KSampler, LoadImage, NunchakuFluxDiTLoader, NunchakuFluxLoraLoader, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/珠宝首饰电商洗图_改图_改产品颜色_改场景_2001175361377402881.json, 图片生成/文生图/电商产品_换图 换产品颜色或换场景_2001194927230943234.json, 平台全量/【阡陌】Nunchaku Kontext+8步Turbo lora极速秒出图_1964546880803885058.json, 平台全量/【阡陌】Nunchak加速kontext风格转换225种风格随意切换_1950076622268448770.json, 平台全量/调色滤镜-kontext_1959462354905935873.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_90

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/珠宝首饰电商洗图_改图_改产品颜色_改场景_2001175361377402881.json、图片生成/文生图/电商产品_换图 换产品颜色或换场景_2001194927230943234.json、平台全量/【阡陌】Nunchaku Kontext+8步Turbo lora极速秒出图_1964546880803885058.json、平台全量/【阡陌】Nunchak加速kontext风格转换225种风格随意切换_1950076622268448770.json、平台全量/调色滤镜-kontext_1959462354905935873.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `NunchakuFluxLoraLoader`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 4/5 个有
- `NunchakuTextEncoderLoaderV2` —— 4/5 个有
- `Anything Everywhere3` —— 3/5 个有
- `FluxKontextImageScale` —— 3/5 个有
- `ACE_TextTranslate` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `Note Plus (mtb)` —— 2/5 个有
- `Anything Everywhere` —— 1/5 个有
- `DualCLIPLoader` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有
- `easy promptList` —— 1/5 个有
- `easy stylesSelector` —— 1/5 个有
- `easy textSwitch` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 8 - 20 | 5 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 15，观测区间 8 - 20，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
