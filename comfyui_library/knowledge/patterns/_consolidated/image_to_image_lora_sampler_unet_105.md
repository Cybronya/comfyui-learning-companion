---
name: image_to_image_lora_sampler_unet_105
type: Image To Image
frequency: 6
level: moderate
coverage: 0.9085
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen controlnet控制工作流_1961414118060265474.json, 图片生成/图生图/Qwen 毛坯出效果图工作流_1966836671448748033.json, 图片生成/图生图/Qwen-Image-2512图生图_1953010725393526786.json, 图片生成/图生图/Qwen-edit-Controlnet控制工作流_1961761519048572929.json, 图片生成/文生图/Qwen Image Edit 千问模型-CN图像编辑 @橘子_SJRJT_1963114897561333762.json, 图片生成/文生图/Qwen 文生图+CN控制 @橘子_SJRJT_1962818248989360130.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_105

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen controlnet控制工作流_1961414118060265474.json、图片生成/图生图/Qwen 毛坯出效果图工作流_1966836671448748033.json、图片生成/图生图/Qwen-Image-2512图生图_1953010725393526786.json、图片生成/图生图/Qwen-edit-Controlnet控制工作流_1961761519048572929.json、图片生成/文生图/Qwen Image Edit 千问模型-CN图像编辑 @橘子_SJRJT_1963114897561333762.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
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
- `AIO_Preprocessor` —— 5/6 个有
- `ControlNetLoader` —— 5/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `SetUnionControlNetType` —— 5/6 个有
- `CFGNorm` —— 4/6 个有
- `CLIPTextEncode` —— 3/6 个有
- `ControlNetApplySD3` —— 3/6 个有
- `EmptyLatentImage` —— 3/6 个有
- `ImageScaleToTotalPixels` —— 3/6 个有
- `OpenposePreprocessor` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `TextEncodeQwenImageEdit` —— 3/6 个有
- `ControlNetApplyAdvanced` —— 2/6 个有
- `FluxKontextImageScale` —— 1/6 个有
- `scale` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 6 | 59% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | beta | - | 6 | 50% |
| 重绘幅度 | 1 | 0.5 - 1 | 6 | 80% |
| ControlNet 权重 | 1.2 | 0.75 - 1.8 | 5 | 64% |
| 宽度 | 1280 | 1280 - 1280 | 3 | 100% |
| 高度 | 720 | 720 - 720 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，6 个样本
- ControlNet 权重 中位数 1.2，观测区间 0.75 - 1.8，5 个样本
- 宽度 中位数 1280，观测区间 1280 - 1280，3 个样本，取值集中（一致性 100%）
- 高度 中位数 720，观测区间 720 - 720，3 个样本，取值集中（一致性 100%）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
