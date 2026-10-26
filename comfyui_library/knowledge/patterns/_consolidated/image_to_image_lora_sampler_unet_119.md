---
name: image_to_image_lora_sampler_unet_119
type: Image To Image
frequency: 5
level: moderate
coverage: 0.8458
common_nodes: [CFGNorm, CLIPLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/37.tonnie-Qwen image扩图和重绘（效果不好）_2003855307208073217.json, 图片生成/图生图/51.tonnie-Qwen Edit 下一个镜头（效果不好）_2007931488599281666.json, 图片生成/图生图/72.tonnie-2512局部重绘_2010727383120220161.json, 图片生成/图生图/Qwen-image-2512局部重绘（邪修玩法须要抽卡）_2006558396165660674.json, 图片生成/图生图/万象Qwen 局部重绘＋无限扩图_1967901045248655362.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_119

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/37.tonnie-Qwen image扩图和重绘（效果不好）_2003855307208073217.json、图片生成/图生图/51.tonnie-Qwen Edit 下一个镜头（效果不好）_2007931488599281666.json、图片生成/图生图/72.tonnie-2512局部重绘_2010727383120220161.json、图片生成/图生图/Qwen-image-2512局部重绘（邪修玩法须要抽卡）_2006558396165660674.json、图片生成/图生图/万象Qwen 局部重绘＋无限扩图_1967901045248655362.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 4/5 个有
- `ControlNetInpaintingAliMamaApply` —— 4/5 个有
- `ControlNetLoader` —— 4/5 个有
- `Mask Fill Holes` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `DifferentialDiffusion` —— 2/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `ImagePadForOutpaint` —— 2/5 个有
- `MaskBlur+` —— 2/5 个有
- `SetLatentNoiseMask` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `MaskFillHoles` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 1/5 个有
- `easy promptLine` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 5 - 10 | 5 | 71% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | beta | - | 5 | 80% |
| 重绘幅度 | 1 | 0.1 - 1 | 5 | 56% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 5 - 10，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 0.1 - 1，5 个样本
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
