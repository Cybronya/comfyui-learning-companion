---
name: text_to_image_lora_sampler_clip_708
type: Text To Image
frequency: 2
level: weak
coverage: 0.917
common_nodes: [AddLabel, Anything Everywhere3, CLIPTextEncode, CR Image Grid Panel, CR Text Concatenate, CR Text List To String, DualCLIPLoader, EmptyLatentImage, Fast Bypasser (rgthree), FluxGuidance, ImageListToBatch+, ImageListToImageBatch, KSampler, LayerUtility: If , Lora Loader, Primitive integer [Crystools], RH_Translator, SaveImage, SomethingToString, UNETLoader, VAEDecode, VAELoader, easy anythingIndexSwitch, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy isNone, easy rangeFloat, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/flux_多lora权重测试(for循环)_2012350655842750465.json, 平台全量/多lora不同权重测试(for循环)_2025823336172888065.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_708

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/flux_多lora权重测试(for循环)_2012350655842750465.json、平台全量/多lora不同权重测试(for循环)_2025823336172888065.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `AddLabel`
- `Anything Everywhere3`
- `CLIPTextEncode`
- `CR Image Grid Panel`
- `CR Text Concatenate`
- `CR Text List To String`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `Fast Bypasser (rgthree)`
- `FluxGuidance`
- `ImageListToBatch+`
- `ImageListToImageBatch`
- `KSampler`
- `LayerUtility: If `
- `Lora Loader`
- `Primitive integer [Crystools]`
- `RH_Translator`
- `SaveImage`
- `SomethingToString`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy batchAnything`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy isNone`
- `easy rangeFloat`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 504 | - | 2 | 100% |
| 高度 | 504 | - | 2 | 100% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 504，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 504，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
