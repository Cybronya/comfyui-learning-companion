---
name: image_to_image_sampler_unet_vae_43
type: Image To Image
frequency: 4
level: moderate
coverage: 0.89375
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问Qwen Edit 2511任意切换视觉_2010756226547716098.json, 图片生成/图生图/千问编辑模型Plus双图_1970426505799081986.json, 图片生成/图生图/可视化摄像机角度调节_2039583466450325506.json, 图片生成/图生图/图生图 _ 场景角度切换_1996085406431166466.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_43

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/千问Qwen Edit 2511任意切换视觉_2010756226547716098.json、图片生成/图生图/千问编辑模型Plus双图_1970426505799081986.json、图片生成/图生图/可视化摄像机角度调节_2039583466450325506.json、图片生成/图生图/图生图 _ 场景角度切换_1996085406431166466.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `PreviewImage` —— 2/4 个有
- `QwenMultiangleCameraNode` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `ImpactSwitch` —— 1/4 个有
- `PIP_图像联结` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `Qwen3_VQA_Plus` —— 1/4 个有
- `Text` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 4 | 40% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 4 | 53% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，4 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
