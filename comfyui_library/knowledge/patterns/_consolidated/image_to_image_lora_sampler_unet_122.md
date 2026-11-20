---
name: image_to_image_lora_sampler_unet_122
type: Image To Image
frequency: 6
level: strong
coverage: 0.9825
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/12.人物动作替换_2050783766943158274.json, 图片生成/图生图/2.佩戴首饰_2050622012984438785.json, 图片生成/图生图/2026贺喜新春-四宫格Qwen-Edit-2511 新年海报_2012900372683165697.json, 图片生成/图生图/2026贺喜新春-四宫格新年海报_2019610385413840897.json, 图片生成/图生图/👾怪獸-QWEN2511-EDIT-动漫转真人👾_2014656818890416130.json, 平台全量/qwen自动生成国风新年海报_2014160962579865602.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_122

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/12.人物动作替换_2050783766943158274.json、图片生成/图生图/2.佩戴首饰_2050622012984438785.json、图片生成/图生图/2026贺喜新春-四宫格Qwen-Edit-2511 新年海报_2012900372683165697.json、图片生成/图生图/2026贺喜新春-四宫格新年海报_2019610385413840897.json、图片生成/图生图/👾怪獸-QWEN2511-EDIT-动漫转真人👾_2014656818890416130.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SeedVR2LoadDiTModel` —— 5/6 个有
- `SeedVR2LoadVAEModel` —— 5/6 个有
- `SeedVR2VideoUpscaler` —— 5/6 个有
- `ConditioningZeroOut` —— 4/6 个有
- `ImageScaleToTotalPixels` —— 4/6 个有
- `easy cleanGpuUsed` —— 4/6 个有
- `EmptySD3LatentImage` —— 3/6 个有
- `ReferenceLatent` —— 3/6 个有
- `easy promptList` —— 3/6 个有
- `CR Text` —— 2/6 个有
- `ImageScaleToMaxDimension` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `MuyeTextEditOutput` —— 1/6 个有
- `RH_LLMAPI_Pro_Node` —— 1/6 个有
- `RunningHub Deepcleaner` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `TextConcatenate` —— 1/6 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/6 个有
- `easy clearCacheAll` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 10 | 6 | 62% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 50% |
| 调度器 | beta57 | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 10，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 50%
- 调度器 最常用 beta57，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
