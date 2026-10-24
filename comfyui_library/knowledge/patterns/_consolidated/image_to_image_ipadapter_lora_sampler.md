---
name: image_to_image_ipadapter_lora_sampler
type: Image To Image
frequency: 4
level: strong
coverage: 0.975
common_nodes: [BiRefNet_Hugo, BrushNet, BrushNetLoader, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, DetailTransfer, DualCLIPLoader, FluxGuidance, GrowMask, ImageCompositeMasked, ImitationHueNode, InvertMask, JanusImageUnderstanding, JanusModelLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, SaveImage, StringFunction|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy ipadapterApplyADV]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/众馨电商换背景_1985911393323032577.json, 图片生成/图生图/参考背景出电商产品背景_1902407265251667970.json, 图片生成/图生图/参考背景出电商产品背景_2013529138140815362.json, 图片生成/图生图/参考背景出电商产品背景_2013847774223142913.json]
source: knowledge_consolidation
---

# image_to_image_ipadapter_lora_sampler

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/众馨电商换背景_1985911393323032577.json、图片生成/图生图/参考背景出电商产品背景_1902407265251667970.json、图片生成/图生图/参考背景出电商产品背景_2013529138140815362.json、图片生成/图生图/参考背景出电商产品背景_2013847774223142913.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 4 个 workflow 都包含：
- `BiRefNet_Hugo`
- `BrushNet`
- `BrushNetLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `DetailTransfer`
- `DualCLIPLoader`
- `FluxGuidance`
- `GrowMask`
- `ImageCompositeMasked`
- `ImitationHueNode`
- `InvertMask`
- `JanusImageUnderstanding`
- `JanusModelLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy ipadapterApplyADV`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
