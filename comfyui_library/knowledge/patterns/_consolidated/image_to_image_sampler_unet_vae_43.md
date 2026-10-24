---
name: image_to_image_sampler_unet_vae_43
type: Image To Image
frequency: 6
level: moderate
coverage: 0.933167
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/服装_床品_地毯花纹一键提取_2082687997262262274.json, 图片生成/图生图/电商模特三视图_qwen_image_edit_2509_Jefsky_1976877911221456897.json, 图片生成/图生图/空气手势_1981375615989358593.json, 图片生成/图生图/空白工作流_2042557859346522114.json, 图片生成/图生图/精修_产品直出电商摄影图_美工必备_2015801568494358530.json, 图片生成/图生图/精修白底不求人-手机随手拍高质量电商主图，扣图去背景_1993571394655109121.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_43

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/服装_床品_地毯花纹一键提取_2082687997262262274.json、图片生成/图生图/电商模特三视图_qwen_image_edit_2509_Jefsky_1976877911221456897.json、图片生成/图生图/空气手势_1981375615989358593.json、图片生成/图生图/空白工作流_2042557859346522114.json、图片生成/图生图/精修_产品直出电商摄影图_美工必备_2015801568494358530.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `EmptySD3LatentImage` —— 4/6 个有
- `TextEncodeQwenImageEdit` —— 3/6 个有
- `TextEncodeQwenImageEditPlus` —— 3/6 个有
- `CLIPTextEncode` —— 2/6 个有
- `CR Text` —— 2/6 个有
- `ConditioningZeroOut` —— 2/6 个有
- `DualCLIPLoader` —— 2/6 个有
- `FluxGuidance` —— 2/6 个有
- `GetImageSize+` —— 2/6 个有
- `Image Comparer (rgthree)` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `ReferenceLatent` —— 2/6 个有
- `TextInput_` —— 2/6 个有
- `LayerMask: BiRefNetUltraV2` —— 1/6 个有
- `LayerMask: LoadBiRefNetModel` —— 1/6 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/6 个有
- `LoraLoader` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| 采样步数 | 8 | 4 - 20 | 6 | 49% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，6 个样本，取值分散，一致性仅 49%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（8/6 个样本）：Steps较低可能导致细节不足
