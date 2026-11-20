---
name: unknown_workflow_sampler_clip_unet_463
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.857667
common_nodes: [BasicGuider, BasicScheduler, CLIPTextEncode, CR Text, DualCLIPLoader, FluxGuidance, KSamplerSelect, LoadImage, ModelSamplingFlux, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/kontext Dev电商产品图生成-产品替换-产品修改等_1939291635899408386.json, 平台全量/一句话改变人物方向 自动润色版_1950038405256273922.json, 平台全量/🥎Kontext 老照片一键修复+上色🤹_1950027254594232322.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_463

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/kontext Dev电商产品图生成-产品替换-产品修改等_1939291635899408386.json、平台全量/一句话改变人物方向 自动润色版_1950038405256273922.json、平台全量/🥎Kontext 老照片一键修复+上色🤹_1950027254594232322.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CR Text`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingFlux`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 2/3 个有
- `EmptySD3LatentImage` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `FluxKontextImageScale` —— 2/3 个有
- `GetImageSize+` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `RH_LLMAPI_NODE` —— 2/3 个有
- `EmptyLatentImage` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `JoinStrings` —— 1/3 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/3 个有
- `LayerUtility: ColorPicker` —— 1/3 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1280 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
