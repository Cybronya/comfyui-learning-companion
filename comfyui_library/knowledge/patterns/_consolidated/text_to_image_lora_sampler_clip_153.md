---
name: text_to_image_lora_sampler_clip_153
type: Text To Image
frequency: 6
level: strong
coverage: 0.886
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image 2.1巨物专用支持文生角色参考图生多模式通用，图生图方案_2107199232045314049.json, 图片生成/文生图/Image2.5 Seedance等API接入生图生视频，低成本文生图文生视频方案_2103934036086444034.json, 视频生成/图生视频/qwen-image2.1巨物专用多模式通用｜支持文生图与角色参考图生_2107987558692122626.json, 视频生成/文生视频/Image2.5 Seedance等API接入生图生视频，低成本文生图文生视频方案_2103934036086444034.json, 视频生成/文生视频/Qwen Image 2.1 T2I文生图人像写真级质感 写实人像一步生成_2104696107367489538.json, 视频生成/文生视频/Qwen-Image-2.1_T2I文生图｜人像写真级出图质感｜写实人像一步生成_2104043820429176833.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_153

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen Image 2.1巨物专用支持文生角色参考图生多模式通用，图生图方案_2107199232045314049.json、图片生成/文生图/Image2.5 Seedance等API接入生图生视频，低成本文生图文生视频方案_2103934036086444034.json、视频生成/图生视频/qwen-image2.1巨物专用多模式通用｜支持文生图与角色参考图生_2107987558692122626.json、视频生成/文生视频/Image2.5 Seedance等API接入生图生视频，低成本文生图文生视频方案_2103934036086444034.json、视频生成/文生视频/Qwen Image 2.1 T2I文生图人像写真级质感 写实人像一步生成_2104696107367489538.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 4/6 个有
- `LoadImage` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `PrimitiveStringMultiline` —— 4/6 个有
- `RH_Screenwriter` —— 4/6 个有
- `ResolutionSelector` —— 4/6 个有
- `TextEncodeQwenImage21` —— 4/6 个有
- `WujiUpscaler2` —— 4/6 个有
- `easy showAnything` —— 4/6 个有
- `孤海注释` —— 4/6 个有
- `EmptyImage` —— 3/6 个有
- `ConditioningKrea2Rebalance` —— 2/6 个有
- `Seed (rgthree)` —— 2/6 个有
- `TextGenerate` —— 2/6 个有
- `WujiAPI` —— 2/6 个有
- `WujiClosedSourceGenerator` —— 2/6 个有
- `WujiImagePrompt` —— 2/6 个有
- `easy promptList` —— 2/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（11/6 个样本）：Steps较低可能导致细节不足
