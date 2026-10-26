---
name: image_to_image_sampler_vae_16
type: Image To Image
frequency: 9
level: moderate
coverage: 0.931778
common_nodes: [KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen controlnet控制工作流_1961414118060265474.json, 图片生成/图生图/Qwen 毛坯出效果图工作流_1966836671448748033.json, 图片生成/图生图/Qwen-Edit-2511-换脸工作流_2004526917825032193.json, 图片生成/图生图/Qwen-edit-2511-动作迁移_2007272237237276674.json, 图片生成/图生图/nunchaku qwen加速姿态迁移_1969261471488241666.json, 图片生成/图生图/nunchaku双截棍加速 qwen-image-edit 千问姿态迁移工作流_1970131353419345921.json, 图片生成/图生图/人物姿态迁移qwen版 单人使用版_1970816529736605698.json, 图片生成/图生图/生图-图改变姿态-qwen-edit-2511-8步_2008026677938495490.json, 图片生成/图生图/生图-图改变姿态深度等Control控制-kontext_1973349883140812801.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_16

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen controlnet控制工作流_1961414118060265474.json、图片生成/图生图/Qwen 毛坯出效果图工作流_1966836671448748033.json、图片生成/图生图/Qwen-Edit-2511-换脸工作流_2004526917825032193.json、图片生成/图生图/Qwen-edit-2511-动作迁移_2007272237237276674.json、图片生成/图生图/nunchaku qwen加速姿态迁移_1969261471488241666.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 9 个 workflow 都包含：
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 8/9 个有
- `ModelSamplingAuraFlow` —— 8/9 个有
- `ControlNetApplyAdvanced` —— 7/9 个有
- `ControlNetLoader` —— 7/9 个有
- `UNETLoader` —— 7/9 个有
- `CLIPTextEncode` —— 6/9 个有
- `LoraLoaderModelOnly` —— 6/9 个有
- `PreviewImage` —— 6/9 个有
- `DWPreprocessor` —— 5/9 个有
- `CFGNorm` —— 4/9 个有
- `ConditioningZeroOut` —— 4/9 个有
- `SetUnionControlNetType` —— 4/9 个有
- `AIO_Preprocessor` —— 3/9 个有
- `TextEncodeQwenImageEdit` —— 3/9 个有
- `TextEncodeQwenImageEditPlus` —— 3/9 个有
- `GetImageSizeAndCount` —— 2/9 个有
- `ImageResizeKJ` —— 2/9 个有
- `NunchakuQwenImageDiTLoader` —— 2/9 个有
- `easy imageConcat` —— 2/9 个有
- `easy int` —— 2/9 个有
- `easy seed` —— 2/9 个有
- `DualCLIPLoader` —— 1/9 个有
- `FluxGuidance` —— 1/9 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/9 个有
- `ImageConcatMulti` —— 1/9 个有
- `ReferenceLatent` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 6 - 20 | 9 | 54% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| ControlNet 权重 | 1 | 0.75 - 2 | 7 | 63% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 6 - 20，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 1，观测区间 0.75 - 2，7 个样本
- 高发问题（7/9 个样本）：Steps较低可能导致细节不足
