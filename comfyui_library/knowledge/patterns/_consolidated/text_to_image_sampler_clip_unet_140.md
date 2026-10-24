---
name: text_to_image_sampler_clip_unet_140
type: Text To Image
frequency: 4
level: strong
coverage: 0.94575
common_nodes: [CLIPTextEncode, CR Text, ConditioningZeroOut, DeepTranslatorTextNode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, ImageConcanate, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, NunchakuFluxDiTLoader, RH_LLMAPI_NODE, ReferenceLatent, RepeatLatentBatch, SaveImage, Text Concatenate, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Kontext Dev 姿势动作参考生图_1946823970689835009.json, 图片生成/图生图/Kontext主体+姿势动作参考方案_1944075483581648898.json, 图片生成/图生图/电商模特姿势｜动作参考生图_1947995932966170625.json, 图片生成/图生图/🦖KT动作迁移_1952245760781963265.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_140

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Kontext Dev 姿势动作参考生图_1946823970689835009.json、图片生成/图生图/Kontext主体+姿势动作参考方案_1944075483581648898.json、图片生成/图生图/电商模特姿势｜动作参考生图_1947995932966170625.json、图片生成/图生图/🦖KT动作迁移_1952245760781963265.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `DeepTranslatorTextNode`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `ImageConcanate`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `NunchakuFluxDiTLoader`
- `RH_LLMAPI_NODE`
- `ReferenceLatent`
- `RepeatLatentBatch`
- `SaveImage`
- `Text Concatenate`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `easy imageRemBg` —— 3/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 1536 | 1536 - 1536 | 4 | 100% |
| 高度 | 1280 | 1280 - 1280 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 1536，观测区间 1536 - 1536，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，观测区间 1280 - 1280，4 个样本，取值集中（一致性 100%）
