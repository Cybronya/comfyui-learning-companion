---
name: unknown_workflow_lora_sampler_unet_114
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.868286
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-Edit 2509写真套图，完美一致性_1988103540386209794.json, 图片生成/图生图/Qwen-image-Edit换背景海滩落日_1958042147771527170.json, 图片生成/图生图/Qwen-image-edit-2509版 解决千问编辑图片位移的问题_1978471174646730754.json, 图片生成/图生图/Qwen2509写真套图，完美一致性_1995445440655110145.json, 图片生成/图生图/Qwen_image_edit_图像编辑_1958378093205471233.json, 图片生成/图生图/单图套装 _ 更换服装-qwen_image_edit_2511_2099760789157670914.json, 图片生成/图生图/小红书FireRed-Image-edit1.1双图编辑(换装)_2032084048595656705.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_114

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Edit 2509写真套图，完美一致性_1988103540386209794.json、图片生成/图生图/Qwen-image-Edit换背景海滩落日_1958042147771527170.json、图片生成/图生图/Qwen-image-edit-2509版 解决千问编辑图片位移的问题_1978471174646730754.json、图片生成/图生图/Qwen2509写真套图，完美一致性_1995445440655110145.json、图片生成/图生图/Qwen_image_edit_图像编辑_1958378093205471233.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 6/7 个有
- `ConditioningZeroOut` —— 4/7 个有
- `Image Comparer (rgthree)` —— 4/7 个有
- `PreviewImage` —— 4/7 个有
- `TextEncodeQwenImageEdit` —— 4/7 个有
- `CFGNorm` —— 3/7 个有
- `JjkText` —— 3/7 个有
- `RHHiddenNodes` —— 3/7 个有
- `EmptySD3LatentImage` —— 2/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 2/7 个有
- `TextEncodeQwenImageEditPlusPro_lrzjason` —— 2/7 个有
- `Anything Everywhere` —— 1/7 个有
- `FluxKontextImageScale` —— 1/7 个有
- `ImageConcanate` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 7 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 57% |
| 调度器 | beta57 | - | 7 | 43% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 57%
- 调度器 最常用 beta57，7 个样本，一致性 43%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
