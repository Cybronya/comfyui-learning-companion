---
name: image_to_image_controlnet_lora_sampler_5
type: Image To Image
frequency: 3
level: strong
coverage: 0.737667
common_nodes: [AIO_Preprocessor, BasicGuider, BasicScheduler, CLIPTextEncode, CLIPTextEncodeFlux, CR Latent Batch Size, CR Text, CR Text Concatenate, ConditioningZeroOut, ControlNetApplySD3, ControlNetLoaderAdvanced, DualCLIPLoader, Fast Groups Bypasser (rgthree), FluxGuidance, Image Comparer (rgthree), ImpactSwitch, Int, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoader, PreviewImage, RH_Translator, RandomNoise, SamplerCustomAdvanced, SaveImage, SetUnionControlNetType, ShowText|pysssss, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy float]
problems: []
missing: []
members: [图片生成/图生图/FLUX krea 图生图工作流｜ControlNet_1953392904431697922.json, 图片生成/图生图/FLUX 图生图 + 反推提示词 + ControlNet_1942957881928925186.json, 图片生成/图生图/Flux Krea 图生图+自动提示词+润色+ControlNet_1951125854850064386.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_lora_sampler_5

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/FLUX krea 图生图工作流｜ControlNet_1953392904431697922.json、图片生成/图生图/FLUX 图生图 + 反推提示词 + ControlNet_1942957881928925186.json、图片生成/图生图/Flux Krea 图生图+自动提示词+润色+ControlNet_1951125854850064386.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `CR Latent Batch Size`
- `CR Text`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `ControlNetApplySD3`
- `ControlNetLoaderAdvanced`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImpactSwitch`
- `Int`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `RH_Translator`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetUnionControlNetType`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy float`

**可变部分**（部分 workflow 才有）：
- `PrimitiveBoolean` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `RH_Prompter` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `easy ifElse` —— 2/3 个有
- `Joy_caption_two` —— 1/3 个有
- `Joy_caption_two_load` —— 1/3 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/3 个有
- `TextInput_` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.2 | 0.2 - 0.2 | 3 | 100% |
| LoRA 文本强度 | 0.2 | 0.2 - 0.2 | 3 | 100% |
| ControlNet 权重 | 0.5 | 0.5 - 0.5 | 3 | 100% |
| 采样步数 | 30 | 20 - 30 | 3 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 0.55 | 0.55 - 0.55 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.2，观测区间 0.2 - 0.2，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.2，观测区间 0.2 - 0.2，3 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.5，观测区间 0.5 - 0.5，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 30，观测区间 20 - 30，3 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 0.55，观测区间 0.55 - 0.55，3 个样本，取值集中（一致性 100%）
