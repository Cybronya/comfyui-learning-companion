---
name: text_to_image_sampler_clip_unet_139
type: Text To Image
frequency: 5
level: strong
coverage: 0.9444
common_nodes: [CLIPTextEncode, CR Text, ConditioningZeroOut, DeepTranslatorTextNode, DualCLIPLoader, EmptyLatentImage, FluxGuidance, ImageConcanate, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, NunchakuFluxDiTLoader, RH_LLMAPI_NODE, ReferenceLatent, RepeatLatentBatch, SaveImage, Text Concatenate, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Kontext Dev 姿势动作参考生图_1946823970689835009.json, 图片生成/图生图/Kontext主体+姿势动作参考方案_1944075483581648898.json, 图片生成/图生图/电商模特姿势｜动作参考生图_1947995932966170625.json, 图片生成/图生图/🦖KT动作迁移_1952245760781963265.json, 平台全量/动漫图片人物按照参考姿势变换（保持一致性）_1944548959790485505.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_139

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Kontext Dev 姿势动作参考生图_1946823970689835009.json、图片生成/图生图/Kontext主体+姿势动作参考方案_1944075483581648898.json、图片生成/图生图/电商模特姿势｜动作参考生图_1947995932966170625.json、图片生成/图生图/🦖KT动作迁移_1952245760781963265.json、平台全量/动漫图片人物按照参考姿势变换（保持一致性）_1944548959790485505.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
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
- `AIO_Preprocessor` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `easy imageRemBg` —— 4/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1536 | 1536 - 1536 | 5 | 100% |
| 高度 | 1280 | 1280 - 1280 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1536，观测区间 1536 - 1536，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1280，观测区间 1280 - 1280，5 个样本，取值集中（一致性 100%）
