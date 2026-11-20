---
name: unknown_workflow_lora_sampler_clip_180
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.5595
common_nodes: [Any Switch (rgthree), BasicGuider, BasicScheduler, CLIPTextEncode, DepthAnythingPreprocessor, DisableNoise, DualCLIPLoader, EmptyLatentImage, FluxGuidance, GetNode, Int, KSamplerSelect, LayerFilter: Film, LoraLoaderModelOnly, ModelSamplingFlux, PreviewImage, RandomNoise, SamplerCustomAdvanced, SaveImage, Seed Everywhere, SetNode, SplitSigmasDenoise, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/「最强网感」小红书质感_1882289781651406850.json, 平台全量/Flux 美腿生成器_1840130787860774913.json, 平台全量/【企鹅AI】Flux girl 网红生成器V1（极致真实感）_1838164226585116674.json, 平台全量/【企鹅AI】FluxGirl生成器 RoseOnly_1839220520809332737.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_180

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/「最强网感」小红书质感_1882289781651406850.json、平台全量/Flux 美腿生成器_1840130787860774913.json、平台全量/【企鹅AI】Flux girl 网红生成器V1（极致真实感）_1838164226585116674.json、平台全量/【企鹅AI】FluxGirl生成器 RoseOnly_1839220520809332737.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：56%

## 共有节点

全部 4 个 workflow 都包含：
- `Any Switch (rgthree)`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DepthAnythingPreprocessor`
- `DisableNoise`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `GetNode`
- `Int`
- `KSamplerSelect`
- `LayerFilter: Film`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `PreviewImage`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed Everywhere`
- `SetNode`
- `SplitSigmasDenoise`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text Input Switch (4 way)` —— 3/4 个有
- `Random Number` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `String` —— 3/4 个有
- `StringFunction|pysssss` —— 3/4 个有
- `DeepTranslatorTextNode` —— 2/4 个有
- `ImageResize+` —— 2/4 个有
- `Joy_caption` —— 2/4 个有
- `Joy_caption_load` —— 2/4 个有
- `LayerUtility: TextBox` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `TextWildcardList_AS` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `DisplayText` —— 1/4 个有
- `RH_Prompter` —— 1/4 个有
- `easy promptConcat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
