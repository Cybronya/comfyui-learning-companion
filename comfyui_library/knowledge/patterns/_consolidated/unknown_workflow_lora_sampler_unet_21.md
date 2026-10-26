---
name: unknown_workflow_lora_sampler_unet_21
type: Unknown Workflow
frequency: 19
level: moderate
coverage: 0.837158
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/AI生成你的前世今生_2041434675314429954.json, 图片生成/图生图/AI生成你的前世今生_2087720266213449729.json, 图片生成/图生图/FireRed Image Edit一键换装_+换衣电商服装系列_2061592741133508609.json, 图片生成/图生图/FireRed-Edit 最强开源模型_2026883018471772161.json, 图片生成/图生图/FireRed-Image-Edit  人物换装换衣_2079505468896141314.json, 图片生成/图生图/FireRed-Image-Edit 1.1图片编辑模型，最多三图_2026952933660696578.json, 图片生成/图生图/FireRed-Image-Edit 1.1多图片编辑模型_2029858512251133954.json, 图片生成/图生图/FireRed-Image-Edit 小红书  一键换衣_2041757058877366274.json, 图片生成/图生图/FireRed-Image-Edit 小红书 换衣服 一键换衣_2035953103727501314.json, 图片生成/图生图/FireRed-Image-Edit 小红书 换衣服 一键换衣_2039363350714392578.json, 图片生成/图生图/FireRed-Image-Edit 小红书一键换衣_2038123021789044738.json, 图片生成/图生图/FireRed-Image-Edit一键换装  电商服装快速换装换衣_2059284766104580098.json, 图片生成/图生图/FireRed-Image-Edit合集_2030966569660063746.json, 图片生成/图生图/FireRed-Image-Edit换装 换衣  电商服装展示 小红书  快速变装_2074472541913174018.json, 图片生成/图生图/qwen+image+2511单图编辑工作流x_2016850738546221057.json, 图片生成/图生图/千问Edit2511图像编辑-单图_2003625082419355650.json, 图片生成/图生图/千问Edit2511配合lora-单图-马克笔效果图转换手绘_2016700485247438849.json, 图片生成/图生图/最新千问Qwen-Edit2511多图编辑_2003688693493841921.json, 视频生成/图生视频/最新千问Qwen-Edit2511单图编辑_2003688668789391361.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_21

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/AI生成你的前世今生_2041434675314429954.json、图片生成/图生图/AI生成你的前世今生_2087720266213449729.json、图片生成/图生图/FireRed Image Edit一键换装_+换衣电商服装系列_2061592741133508609.json、图片生成/图生图/FireRed-Edit 最强开源模型_2026883018471772161.json、图片生成/图生图/FireRed-Image-Edit  人物换装换衣_2079505468896141314.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 16/19 个有
- `Image Comparer (rgthree)` —— 14/19 个有
- `FluxKontextImageScale` —— 7/19 个有
- `EmptyLatentImage` —— 6/19 个有
- `Text Multiline` —— 5/19 个有
- `ImpactSwitch` —— 4/19 个有
- `Anything Everywhere3` —— 3/19 个有
- `Fast Groups Bypasser (rgthree)` —— 3/19 个有
- `FluxResolutionNode` —— 3/19 个有
- `RH_LLMAPI_NODE` —— 3/19 个有
- `easy showAnything` —— 3/19 个有
- `Text` —— 2/19 个有
- `easy promptLine` —— 2/19 个有
- `AIO_Preprocessor` —— 1/19 个有
- `Int` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 15 | 19 | 46% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 19 | 100% |
| 采样算法 | euler | - | 19 | 100% |
| 调度器 | simple | - | 19 | 63% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |
| 宽度 | 896 | 512 - 1504 | 6 | 54% |
| 高度 | 756 | 512 - 1280 | 6 | 59% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 15，19 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，19 个样本，一致性 100%
- 调度器 最常用 simple，19 个样本，一致性 63%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 宽度 中位数 896，观测区间 512 - 1504，6 个样本
- 高度 中位数 756，观测区间 512 - 1280，6 个样本
- 高发问题（20/19 个样本）：Steps较低可能导致细节不足
