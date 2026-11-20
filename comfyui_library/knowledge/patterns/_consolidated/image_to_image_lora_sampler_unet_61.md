---
name: image_to_image_lora_sampler_unet_61
type: Image To Image
frequency: 9
level: moderate
coverage: 0.911333
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FireRed Image Edit 1.0 图像编辑+Zimage高清RH在线工作流_2025965892865105922.json, 图片生成/图生图/FireRed-Image-Edit工作流_2026563265744080898.json, 图片生成/图生图/QWEN-最新编辑模型_2003645392963158018.json, 图片生成/图生图/QWEN2511+重打光l(Relight)ora强化版_2014561496826646530.json, 图片生成/图生图/Qwen 2511 多角度 + Z-Image-Turbo_2010904385815056386.json, 图片生成/图生图/Qwen 一键多角度相机 多角度照明工作流 V1.0_2011096627490070530.json, 图片生成/图生图/Qwen 多角度相机 多角度照明_2012894465811288065.json, 图片生成/图生图/Qwen-Edit2511人物多角度生成_2009909041430011905.json, 图片生成/文生图/Z-Image-Turbo 多角度学习_2039927595122298882.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_61

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/FireRed Image Edit 1.0 图像编辑+Zimage高清RH在线工作流_2025965892865105922.json、图片生成/图生图/FireRed-Image-Edit工作流_2026563265744080898.json、图片生成/图生图/QWEN-最新编辑模型_2003645392963158018.json、图片生成/图生图/QWEN2511+重打光l(Relight)ora强化版_2014561496826646530.json、图片生成/图生图/Qwen 2511 多角度 + Z-Image-Turbo_2010904385815056386.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
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
- `EmptySD3LatentImage` —— 6/9 个有
- `easy showAnything` —— 6/9 个有
- `ImageScaleToTotalPixels` —— 5/9 个有
- `QwenMultiangleCameraNode` —— 5/9 个有
- `easy promptList` —— 5/9 个有
- `CLIPTextEncode` —— 3/9 个有
- `ConditioningZeroOut` —— 3/9 个有
- `PreviewImage` —— 3/9 个有
- `QwenMultiangleLightningNode` —— 3/9 个有
- `CR Text Concatenate` —— 2/9 个有
- `LayerUtility: PurgeVRAM` —— 2/9 个有
- `AddLabel` —— 1/9 个有
- `GetImageSizeAndCount` —— 1/9 个有
- `ImageScaleBy` —— 1/9 个有
- `Seed (rgthree)` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 12 | 9 | 53% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 67% |
| 调度器 | simple | - | 9 | 67% |
| 重绘幅度 | 1 | 0.4 - 1 | 9 | 71% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 12，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 67%
- 调度器 最常用 simple，9 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，9 个样本
- 高发问题（11/9 个样本）：Steps较低可能导致细节不足
