---
name: image_to_image_lora_sampler_unet_282
type: Image To Image
frequency: 2
level: weak
coverage: 0.8665
common_nodes: [CFGNorm, CLIPLoader, CR Overlay Text, CR Text, Compare, ConditioningZeroOut, Fast Groups Bypasser (rgthree), FluxKontextMultiReferenceLatentMethod, GetNode, ImageConcanate, ImageConcatMulti, ImageScaleToTotalPixels, ImpactSwitch, Int, IntToString, InversionDemoLazySwitch, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MergeImageLists, ModelSamplingAuraFlow, Multi Text Merge, ProcessString, QwenMultiangleCameraNode, RHHiddenNodes, RH_LLMAPI_NODE, RunningHub Deepcleaner, SaveImage, SetNode, TextEncodeQwenImageEditPlus, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptLine, easy promptReplace, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/人脸姿势背景+穿搭多角度融合生成_2021142176402513922.json, 平台全量/穿搭大师Pro v5 姿势控制+多角度展示_2013352894757609474.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_282

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/人脸姿势背景+穿搭多角度融合生成_2021142176402513922.json、平台全量/穿搭大师Pro v5 姿势控制+多角度展示_2013352894757609474.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Overlay Text`
- `CR Text`
- `Compare`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `FluxKontextMultiReferenceLatentMethod`
- `GetNode`
- `ImageConcanate`
- `ImageConcatMulti`
- `ImageScaleToTotalPixels`
- `ImpactSwitch`
- `Int`
- `IntToString`
- `InversionDemoLazySwitch`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MergeImageLists`
- `ModelSamplingAuraFlow`
- `Multi Text Merge`
- `ProcessString`
- `QwenMultiangleCameraNode`
- `RHHiddenNodes`
- `RH_LLMAPI_NODE`
- `RunningHub Deepcleaner`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptLine`
- `easy promptReplace`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
