---
name: image_to_image_lora_sampler_clip_110
type: Image To Image
frequency: 3
level: strong
coverage: 0.959667
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/小红书卡通人像贴纸（吉卜力风格）_1953749401648943106.json, 图片生成/图生图/新-kontext商业级印花提取工作流V2版本_1956004419567583233.json, 图片生成/图生图/版画艺术生成器_1996222237315309569.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_110

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/小红书卡通人像贴纸（吉卜力风格）_1953749401648943106.json、图片生成/图生图/新-kontext商业级印花提取工作流V2版本_1956004419567583233.json、图片生成/图生图/版画艺术生成器_1996222237315309569.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 2/3 个有
- `BiRefNetRMBG` —— 1/3 个有
- `DF_Image_scale_to_side` —— 1/3 个有
- `GrowMask` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `InvertMask` —— 1/3 个有
- `LayerUtility: ImageBlendAdvance V3` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `ttN concat` —— 1/3 个有
- `ttN text` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 3 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
