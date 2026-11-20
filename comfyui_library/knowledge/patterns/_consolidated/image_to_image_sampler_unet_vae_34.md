---
name: image_to_image_sampler_unet_vae_34
type: Image To Image
frequency: 6
level: moderate
coverage: 0.655167
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-edit 胸部增强 丰胸神器 1.0_1994406310353510401.json, 图片生成/图生图/Qwen-动漫转写实真人_1987456609242779650.json, 图片生成/图生图/Qwen_Image_Edit 超强编辑 _ 万物可改 _ 开源可部署_1959226946603397122.json, 图片生成/图生图/Qwen图片编辑模型Plus版本_1970454036820488193.json, 图片生成/图生图/qwen_image_edit多图编辑_1970660738824105985.json, 图片生成/文生图/FluxToQwenEdit-NextSceneLora_ 6场景 角色一致性工作流_1979459859504599042.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_34

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen-edit 胸部增强 丰胸神器 1.0_1994406310353510401.json、图片生成/图生图/Qwen-动漫转写实真人_1987456609242779650.json、图片生成/图生图/Qwen_Image_Edit 超强编辑 _ 万物可改 _ 开源可部署_1959226946603397122.json、图片生成/图生图/Qwen图片编辑模型Plus版本_1970454036820488193.json、图片生成/图生图/qwen_image_edit多图编辑_1970660738824105985.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `SetNode` —— 5/6 个有
- `TextEncodeQwenImageEditPlus` —— 5/6 个有
- `TextEncodeQwenImageEdit` —— 4/6 个有
- `ConditioningZeroOut` —— 3/6 个有
- `DWPreprocessor` —— 2/6 个有
- `EmptySD3LatentImage` —— 2/6 个有
- `Image Comparer (rgthree)` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `CLIPTextEncode` —— 1/6 个有
- `DualCLIPLoader` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `Fast Groups Muter (rgthree)` —— 1/6 个有
- `ImageStitch` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `RHHiddenNodes` —— 1/6 个有
- `Text` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 1 - 8 | 6 | 51% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 1 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（10/6 个样本）：Steps较低可能导致细节不足
