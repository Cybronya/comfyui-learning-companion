---
name: unknown_workflow_lora_sampler_clip_180
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.98
common_nodes: [ArgosTranslateTextNode, BasicGuider, BasicScheduler, CLIPTextEncode, DualCLIPLoader, EG_TC_Node, EmptyLatentImage, Fast Bypasser (rgthree), Florence2ModelLoader, Florence2Run, FluxGuidance, ImageResize+, Int, KSamplerSelect, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModel, LayerUtility: ImageBlendAdvance, LayerUtility: PurgeVRAM, LoadImage, LoraLoader, ModelSamplingFlux, RandomNoise, SamplerCustomAdvanced, SaveImage, TeaCache, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/人物换背景，多角度多姿势不同服装，小红书风格_1986367612152147969.json, 图片生成/图生图/小红书风格-人物换背景，多角度多姿势不同服装_2034538251595292674.json, 图片生成/文生图/人物多角度多姿势场景一致性（一次4张图）_1924977832982999041.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_180

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/人物换背景，多角度多姿势不同服装，小红书风格_1986367612152147969.json、图片生成/图生图/小红书风格-人物换背景，多角度多姿势不同服装_2034538251595292674.json、图片生成/文生图/人物多角度多姿势场景一致性（一次4张图）_1924977832982999041.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `ArgosTranslateTextNode`
- `BasicGuider`
- `BasicScheduler`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EG_TC_Node`
- `EmptyLatentImage`
- `Fast Bypasser (rgthree)`
- `Florence2ModelLoader`
- `Florence2Run`
- `FluxGuidance`
- `ImageResize+`
- `Int`
- `KSamplerSelect`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModel`
- `LayerUtility: ImageBlendAdvance`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoader`
- `ModelSamplingFlux`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TeaCache`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |
| LoRA 模型强度 | 0.5 | 0.5 - 0.5 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.5，观测区间 0.5 - 0.5，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
