---
name: text_to_image_sampler_clip_unet_204
type: Text To Image
frequency: 3
level: strong
coverage: 0.872333
common_nodes: [CLIPLoader, CLIPTextEncode, CR SDXL Aspect Ratio, CR Text Replace, EmptyLatentImage, GetRandomIntegerInRange, ImageToMask, ImpactStringSelector, ImpactSwitch, KSampler, LayerUtility: ColorImage V2, LayerUtility: ImageCombineAlpha, LoadImage, ModelSamplingAuraFlow, RH_Captioner, SaveImage, Textbox, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/Qwen-lmage  创意书法字体_1953685065354149889.json, 平台全量/书法仿画工作流带抠图_2041862899005657090.json, 平台全量/创意书法字体（19种字体选择）_2011813714952986625.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_204

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen-lmage  创意书法字体_1953685065354149889.json、平台全量/书法仿画工作流带抠图_2041862899005657090.json、平台全量/创意书法字体（19种字体选择）_2011813714952986625.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR SDXL Aspect Ratio`
- `CR Text Replace`
- `EmptyLatentImage`
- `GetRandomIntegerInRange`
- `ImageToMask`
- `ImpactStringSelector`
- `ImpactSwitch`
- `KSampler`
- `LayerUtility: ColorImage V2`
- `LayerUtility: ImageCombineAlpha`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `RH_Captioner`
- `SaveImage`
- `Textbox`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 2.5 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 2.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
