---
name: image_to_image_lora_sampler_clip_211
type: Image To Image
frequency: 2
level: weak
coverage: 0.8525
common_nodes: [Bjornulf_ShowInt, CLIPTextEncode, CR Overlay Text, CR Text, CR Text Concatenate, ConditioningZeroOut, DualCLIPLoader, Float, FluxGuidance, FluxKontextImageScale, ImageCropMerge, ImageScale, ImageScaleBy, Int, KSampler, LayerMask: MaskBoxDetect, LayerUtility: ColorImage V2, LoadImage, LoraLoaderModelOnly, PreviewImage, RH_Translator, ReferenceLatent, SaveImage, SimpleMath+, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/Kontext中英文文海报生（提示词生成背景）_1951584029147648002.json, 平台全量/Kontext中英文海报生成（自定义背景）_1951661459019345921.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_211

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Kontext中英文文海报生（提示词生成背景）_1951584029147648002.json、平台全量/Kontext中英文海报生成（自定义背景）_1951661459019345921.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `Bjornulf_ShowInt`
- `CLIPTextEncode`
- `CR Overlay Text`
- `CR Text`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Float`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageCropMerge`
- `ImageScale`
- `ImageScaleBy`
- `Int`
- `KSampler`
- `LayerMask: MaskBoxDetect`
- `LayerUtility: ColorImage V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RH_Translator`
- `ReferenceLatent`
- `SaveImage`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
