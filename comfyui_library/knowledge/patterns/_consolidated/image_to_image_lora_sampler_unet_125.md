---
name: image_to_image_lora_sampler_unet_125
type: Image To Image
frequency: 6
level: strong
coverage: 0.9375
common_nodes: [CFGNorm, CLIPLoader, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FireRed 转写实 带剪裁和标准化处理v2_2031261630184562689.json, 图片生成/图生图/FireRed 转写实_2030669437854027777.json, 图片生成/图生图/FireRed-Image-edit1.1单图_双图_三图编辑_2029806395092115457.json, 图片生成/图生图/FireRed-Image-edit1.1单图_双图_三图编辑_2030064414078017537.json, 图片生成/图生图/KINWING_白底图背景替换_Qwen edit_2046550050255413249.json, 图片生成/文生图/2030095760506753026.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_125

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/FireRed 转写实 带剪裁和标准化处理v2_2031261630184562689.json、图片生成/图生图/FireRed 转写实_2030669437854027777.json、图片生成/图生图/FireRed-Image-edit1.1单图_双图_三图编辑_2029806395092115457.json、图片生成/图生图/FireRed-Image-edit1.1单图_双图_三图编辑_2030064414078017537.json、图片生成/图生图/KINWING_白底图背景替换_Qwen edit_2046550050255413249.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextImageScale`
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
- `Image Comparer (rgthree)` —— 5/6 个有
- `CR Prompt Text` —— 4/6 个有
- `EmptyLatentImage` —— 3/6 个有
- `Anything Everywhere3` —— 2/6 个有
- `easy positive` —— 2/6 个有
- `AddLabel` —— 1/6 个有
- `ConditioningZeroOut` —— 1/6 个有
- `Fast Bypasser (rgthree)` —— 1/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `InpaintCropImproved` —— 1/6 个有
- `RunningHub Deepcleaner` —— 1/6 个有
- `easy imageConcat` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 6 | 55% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1920 | 1920 - 1920 | 3 | 100% |
| 高度 | 1080 | 1080 - 1080 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1920，观测区间 1920 - 1920，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1080，观测区间 1080 - 1080，3 个样本，取值集中（一致性 100%）
- 高发问题（11/6 个样本）：Steps较低可能导致细节不足
