---
name: image_to_image_lora_sampler_unet_85
type: Image To Image
frequency: 7
level: strong
coverage: 0.753143
common_nodes: [CLIPLoader, ConditioningZeroOut, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux-klein 9b 加速版三合一人物证件照工作流 V1.0_2038078453303484418.json, 图片生成/图生图/Meitu   Qwen2509 更好的一致性_1981217441818771457.json, 图片生成/图生图/Qwen-Image海报生成工作流_1982450271907389441.json, 图片生成/图生图/Qwen2509 Meitu版 一致性更好_1982409209759309825.json, 图片生成/图生图/Qwen2509_2002940398152609794.json, 图片生成/图生图/flux-klein 9b 人物证件照双方案生成 更新2026.3.22_2033449471559868418.json, 图片生成/文生图/Qwen--海报设计_1965378348828475394.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_85

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Flux-klein 9b 加速版三合一人物证件照工作流 V1.0_2038078453303484418.json、图片生成/图生图/Meitu   Qwen2509 更好的一致性_1981217441818771457.json、图片生成/图生图/Qwen-Image海报生成工作流_1982450271907389441.json、图片生成/图生图/Qwen2509 Meitu版 一致性更好_1982409209759309825.json、图片生成/图生图/Qwen2509_2002940398152609794.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 5/7 个有
- `MuyeTextEditOutput` —— 5/7 个有
- `TextEncodeQwenImageEdit` —— 5/7 个有
- `CLIPTextEncode` —— 4/7 个有
- `PreviewImage` —— 4/7 个有
- `EmptyFlux2LatentImage` —— 2/7 个有
- `EmptySD3LatentImage` —— 2/7 个有
- `Int` —— 2/7 个有
- `LayerUtility: PurgeVRAM` —— 2/7 个有
- `ReferenceLatent` —— 2/7 个有
- `easy cleanGpuUsed` —— 2/7 个有
- `easy imageInsetCrop` —— 2/7 个有
- `CR Draw Shape` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `NineGridMosaicNode` —— 1/7 个有
- `RH_Nano_Banana_Image2Image` —— 1/7 个有
- `SeargePromptCombiner` —— 1/7 个有
- `SeargePromptText` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 0.25 - 1 | 7 | 57% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 0.25 - 1，7 个样本
- 高发问题（12/7 个样本）：Steps较低可能导致细节不足
