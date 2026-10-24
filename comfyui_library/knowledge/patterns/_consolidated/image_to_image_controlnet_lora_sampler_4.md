---
name: image_to_image_controlnet_lora_sampler_4
type: Image To Image
frequency: 3
level: strong
coverage: 0.863
common_nodes: [AIO_Preprocessor, AutoCropFaces, CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, DapaoImageAspectRatioResizeNode, Fast Bypasser (rgthree), GrowMaskWithBlur, Image Comparer (rgthree), ImageConcanate, Int, JoinStrings, KSampler, LayerMask: PersonMaskUltra V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskToImage, ModelPatchLoader, Mute / Bypass Repeater (rgthree), PainterFluxImageEdit, PreviewImage, PrimitiveFloat, Qwen3_VQA, QwenImageDiffsynthControlnet, SaveImage, ShowText|pysssss, SolidMask, TextInput_, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy clearCacheAll, easy ifElse, easy imageRemBg, easy isMaskEmpty, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/F.2klein服装模特换脸面部光影完美融合_2058043031294668802.json, 图片生成/图生图/flux2klein服装模特换脸面部光影完美融合_2048770691331268610.json, 图片生成/图生图/flux2klein服装模特换脸面部光影完美融合_2051192977095180290.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_lora_sampler_4

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/F.2klein服装模特换脸面部光影完美融合_2058043031294668802.json、图片生成/图生图/flux2klein服装模特换脸面部光影完美融合_2048770691331268610.json、图片生成/图生图/flux2klein服装模特换脸面部光影完美融合_2051192977095180290.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `AutoCropFaces`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `DapaoImageAspectRatioResizeNode`
- `Fast Bypasser (rgthree)`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `Int`
- `JoinStrings`
- `KSampler`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `ModelPatchLoader`
- `Mute / Bypass Repeater (rgthree)`
- `PainterFluxImageEdit`
- `PreviewImage`
- `PrimitiveFloat`
- `Qwen3_VQA`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `ShowText|pysssss`
- `SolidMask`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy clearCacheAll`
- `easy ifElse`
- `easy imageRemBg`
- `easy isMaskEmpty`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 5 - 5 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | dpmpp_2m_sde | - | 3 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 5 - 5，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde，3 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
