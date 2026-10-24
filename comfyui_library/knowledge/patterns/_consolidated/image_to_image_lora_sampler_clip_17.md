---
name: image_to_image_lora_sampler_clip_17
type: Image To Image
frequency: 12
level: strong
coverage: 0.88725
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/完美丰胸一键运行_1981197400008196098.json, 图片生成/图生图/精修  产品精修  高清放大  高清修复_2067117890985349122.json, 图片生成/图生图/精修  产品精修  高清放大  高清修复_2067171835975913473.json, 图片生成/图生图/精修  产品精修  高清放大  高清修复_2067179157712359425.json, 图片生成/图生图/精修  产品精修  高清放大  高清修复_2067208635549310978.json, 图片生成/图生图/精修  产品精修  高清放大  高清修复_2067220096564682753.json, 图片生成/图生图/精修  产品精修  高清放大  高清修复_2067291955792539649.json, 图片生成/图生图/精修-3C电器类-kontxet_1959112427612876802.json, 图片生成/图生图/精修-人像类-kontxet_1959172035203248129.json, 图片生成/图生图/精修-美妆类-kontxet_1959132660998287362.json, 图片生成/图生图/精修-饰品类-kontxet_1959157765254098946.json, 图片生成/图生图/老照片修复去划痕上色工作流_1984951466794303490.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_17

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/完美丰胸一键运行_1981197400008196098.json、图片生成/图生图/精修  产品精修  高清放大  高清修复_2067117890985349122.json、图片生成/图生图/精修  产品精修  高清放大  高清修复_2067171835975913473.json、图片生成/图生图/精修  产品精修  高清放大  高清修复_2067179157712359425.json、图片生成/图生图/精修  产品精修  高清放大  高清修复_2067208635549310978.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/12 个有
- `PreviewImage` —— 10/12 个有
- `UNETLoader` —— 10/12 个有
- `DetailTransfer` —— 4/12 个有
- `UnetLoaderGGUF` —— 2/12 个有
- `easy cleanGpuUsed` —— 2/12 个有
- `CR Simple Image Compare` —— 1/12 个有
- `FluxKontextImageScale` —— 1/12 个有
- `ImageScaleToTotalPixels` —— 1/12 个有
- `Primitive string multiline [Crystools]` —— 1/12 个有
- `TeaCache` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 30 | 12 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 0.9 - 1 | 12 | 97% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 30，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.9 - 1，12 个样本，取值集中（一致性 97%）
