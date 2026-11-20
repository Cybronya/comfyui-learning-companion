---
name: image_to_image_lora_sampler_unet_68
type: Image To Image
frequency: 8
level: strong
coverage: 0.975625
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/12.人物动作替换_2050783766943158274.json, 图片生成/图生图/2.佩戴首饰_2050622012984438785.json, 图片生成/图生图/2026贺喜新春-四宫格Qwen-Edit-2511 新年海报_2012900372683165697.json, 图片生成/图生图/2026贺喜新春-四宫格新年海报_2019610385413840897.json, 图片生成/图生图/双图编辑-图片人物替换-AIGC大赏-修改_2090115164480827393.json, 图片生成/图生图/双图编辑-图片人物替换-AIGC大赏_2043255864382988289.json, 图片生成/图生图/提示词替换人物_2111667142767763458.json, 图片生成/图生图/👾怪獸-QWEN2511-EDIT-动漫转真人👾_2014656818890416130.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_68

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/12.人物动作替换_2050783766943158274.json、图片生成/图生图/2.佩戴首饰_2050622012984438785.json、图片生成/图生图/2026贺喜新春-四宫格Qwen-Edit-2511 新年海报_2012900372683165697.json、图片生成/图生图/2026贺喜新春-四宫格新年海报_2019610385413840897.json、图片生成/图生图/双图编辑-图片人物替换-AIGC大赏-修改_2090115164480827393.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SeedVR2LoadDiTModel` —— 7/8 个有
- `SeedVR2LoadVAEModel` —— 7/8 个有
- `SeedVR2VideoUpscaler` —— 7/8 个有
- `ImageScaleToTotalPixels` —— 6/8 个有
- `SaveImage` —— 6/8 个有
- `CR Text` —— 5/8 个有
- `CompressImages` —— 3/8 个有
- `ConditioningZeroOut` —— 3/8 个有
- `ImageConcanate` —— 3/8 个有
- `easy cleanGpuUsed` —— 3/8 个有
- `easy promptList` —— 3/8 个有
- `EmptySD3LatentImage` —— 2/8 个有
- `ImageScaleToMaxDimension` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `ReferenceLatent` —— 2/8 个有
- `MuyeTextEditOutput` —— 1/8 个有
- `RunningHub Deepcleaner` —— 1/8 个有
- `TextConcatenate` —— 1/8 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/8 个有
- `easy clearCacheAll` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 8 | 59% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 75% |
| 调度器 | simple | - | 8 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 75%
- 调度器 最常用 simple，8 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（7/8 个样本）：Steps较低可能导致细节不足
