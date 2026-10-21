---
name: text_to_image_upscale_lora_sampler_27
type: Text To Image
frequency: 4
level: strong
coverage: 0.87575
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderModelOnly, RH_Screenwriter, SaveImage, UNETLoader, VAEDecode, VAELoader, WujiUpscaler2, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1巨物专用支持文生角色参考图生多模式通用，图生图方案_2107199232045314049.json, 图片生成/文生图/Image2.5 Seedance等API接入生图生视频，低成本文生图文生视频方案_2103934036086444034.json, 视频生成/图生视频/qwen-image2.1巨物专用多模式通用｜支持文生图与角色参考图生_2107987558692122626.json, 视频生成/文生视频/Image2.5 Seedance等API接入生图生视频，低成本文生图文生视频方案_2103934036086444034.json]
source: knowledge_consolidation
---

# text_to_image_upscale_lora_sampler_27

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1巨物专用支持文生角色参考图生多模式通用，图生图方案_2107199232045314049.json、图片生成/文生图/Image2.5 Seedance等API接入生图生视频，低成本文生图文生视频方案_2103934036086444034.json、视频生成/图生视频/qwen-image2.1巨物专用多模式通用｜支持文生图与角色参考图生_2107987558692122626.json、视频生成/文生视频/Image2.5 Seedance等API接入生图生视频，低成本文生图文生视频方案_2103934036086444034.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RH_Screenwriter`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WujiUpscaler2`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 3/4 个有
- `ConditioningKrea2Rebalance` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `ResolutionSelector` —— 2/4 个有
- `TextEncodeQwenImage21` —— 2/4 个有
- `WujiAPI` —— 2/4 个有
- `WujiClosedSourceGenerator` —— 2/4 个有
- `WujiImagePrompt` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `EmptyImage` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（8/4 个样本）：Steps较低可能导致细节不足
