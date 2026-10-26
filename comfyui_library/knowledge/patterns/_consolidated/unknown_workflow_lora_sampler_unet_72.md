---
name: unknown_workflow_lora_sampler_unet_72
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.894556
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-Edit 2509写真套图，完美一致性_1988103540386209794.json, 图片生成/图生图/Qwen-image-Edit换背景海滩落日_1958042147771527170.json, 图片生成/图生图/Qwen-image-edit-2509版 解决千问编辑图片位移的问题_1978471174646730754.json, 图片生成/图生图/Qwen2509写真套图，完美一致性_1995445440655110145.json, 图片生成/图生图/Qwen_image_edit_图像编辑_1958378093205471233.json, 图片生成/图生图/商用级PS+QwenEdit2509电商产品图_2043845775716786177.json, 图片生成/图生图/超强写真套图_1995145813921869825.json, 图片生成/图生图/👾怪獸-IP打造神器-固定人物多场景照片👾_1992556792353976322.json, 图片生成/图生图/👾怪獸-圣诞节写真特级👾_1996148103365476354.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_72

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Edit 2509写真套图，完美一致性_1988103540386209794.json、图片生成/图生图/Qwen-image-Edit换背景海滩落日_1958042147771527170.json、图片生成/图生图/Qwen-image-edit-2509版 解决千问编辑图片位移的问题_1978471174646730754.json、图片生成/图生图/Qwen2509写真套图，完美一致性_1995445440655110145.json、图片生成/图生图/Qwen_image_edit_图像编辑_1958378093205471233.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 8/9 个有
- `TextEncodeQwenImageEdit` —— 7/9 个有
- `RHHiddenNodes` —— 6/9 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 6/9 个有
- `ConditioningZeroOut` —— 4/9 个有
- `EmptySD3LatentImage` —— 4/9 个有
- `PreviewImage` —— 4/9 个有
- `Image Comparer (rgthree)` —— 3/9 个有
- `CFGNorm` —— 2/9 个有
- `JjkText` —— 2/9 个有
- `PrimitiveStringMultiline` —— 2/9 个有
- `Anything Everywhere` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 9 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | er_sde | - | 9 | 67% |
| 调度器 | beta57 | - | 9 | 44% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，9 个样本，一致性 67%
- 调度器 最常用 beta57，9 个样本，一致性 44%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
