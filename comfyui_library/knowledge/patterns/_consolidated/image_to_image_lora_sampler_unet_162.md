---
name: image_to_image_lora_sampler_unet_162
type: Image To Image
frequency: 4
level: strong
coverage: 0.963
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen2511 遮罩移除物体_2032635446202732546.json, 图片生成/图生图/去除水印：图片由AI生成_2078390052329189378.json, 图片生成/图生图/图像编辑 _ Qwen-Edit_2511_1948316912116740098.json, 图片生成/图生图/角色一致性_1916660896893177858.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_162

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/qwen2511 遮罩移除物体_2032635446202732546.json、图片生成/图生图/去除水印：图片由AI生成_2078390052329189378.json、图片生成/图生图/图像编辑 _ Qwen-Edit_2511_1948316912116740098.json、图片生成/图生图/角色一致性_1916660896893177858.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
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
- `TextEncodeQwenImageEditPlus` —— 3/4 个有
- `ConstrainImage|pysssss` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `Anything Everywhere` —— 1/4 个有
- `Anything Everywhere3` —— 1/4 个有
- `DrawMaskOnImage` —— 1/4 个有
- `LayerMask: MaskPreview` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `MaskBlur+` —— 1/4 个有
- `MaskFillHoles` —— 1/4 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 4 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（17/4 个样本）：Steps较低可能导致细节不足
