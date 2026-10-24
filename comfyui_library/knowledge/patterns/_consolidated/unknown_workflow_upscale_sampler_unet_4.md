---
name: unknown_workflow_upscale_sampler_unet_4
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.8415
common_nodes: [CLIPLoader, EmptyLatentImage, Fast Groups Muter (rgthree), KSampler, LoadImage, PreviewAny, PrimitiveStringMultiline, RH_LLMAPI_NODE, RH_RhartImageG2ImageToImage, SaveImage, UNETLoader, VAEDecode, VAELoader, WujiCleaner, WujiUpscaler, easy promptConcat]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Eidt-2511、image2二合一，多参海报生成器（文生、多图生均可）_2089233347670265858.json, 图片生成/图生图/Qwen-Eidt-2511、image2二合一，多参海报生成器（文生、多图生均可）_2091914339182800897.json, 图片生成/图生图/Qwen-image2.1、image2.5二合一，多参海报生成器文生、多图生均可_2110647588159578114.json, 图片生成/图生图/Qwen-image2.1、image2.5二合一，多参海报生成器文生、多图生均可_2111277034977710081.json, 图片生成/图生图/Qwen-image2.1、image2.5二合一，多参海报生成器（文生、多图生均可）_2107851850220400642.json, 图片生成/图生图/单图多参图片编辑（Qwen-Eidt-2511、image2二合一）_2092065502762979329.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_unet_4

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen-Eidt-2511、image2二合一，多参海报生成器（文生、多图生均可）_2089233347670265858.json、图片生成/图生图/Qwen-Eidt-2511、image2二合一，多参海报生成器（文生、多图生均可）_2091914339182800897.json、图片生成/图生图/Qwen-image2.1、image2.5二合一，多参海报生成器文生、多图生均可_2110647588159578114.json、图片生成/图生图/Qwen-image2.1、image2.5二合一，多参海报生成器文生、多图生均可_2111277034977710081.json、图片生成/图生图/Qwen-image2.1、image2.5二合一，多参海报生成器（文生、多图生均可）_2107851850220400642.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `Fast Groups Muter (rgthree)`
- `KSampler`
- `LoadImage`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_NODE`
- `RH_RhartImageG2ImageToImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WujiCleaner`
- `WujiUpscaler`
- `easy promptConcat`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 3/6 个有
- `ConditioningZeroOut` —— 3/6 个有
- `FluxKontextMultiReferenceLatentMethod` —— 3/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `PresetTextSelector` —— 3/6 个有
- `TextEncodeQwenImage21` —— 3/6 个有
- `TextEncodeQwenImageEditPlus` —— 3/6 个有
- `WujiPromptEditor` —— 3/6 个有
- `WujiStyleSelector` —— 3/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1260 | 720 - 1560 | 6 | 67% |
| 高度 | 1092 | 904 - 1280 | 6 | 83% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1260，观测区间 720 - 1560，6 个样本
- 高度 中位数 1092，观测区间 904 - 1280，6 个样本，取值集中（一致性 83%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
