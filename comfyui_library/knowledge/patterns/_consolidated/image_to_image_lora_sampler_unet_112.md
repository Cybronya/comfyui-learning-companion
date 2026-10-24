---
name: image_to_image_lora_sampler_unet_112
type: Image To Image
frequency: 6
level: moderate
coverage: 0.937
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/删除人物保留衣服_2006911696627048449.json, 图片生成/图生图/千问图片编辑工作流_1986050948818751490.json, 图片生成/图生图/单图多角度_2073899870544551938.json, 图片生成/图生图/废片光影重构影楼艺术照_2036626776293646338.json, 图片生成/图生图/扩图 - Qwen-Image-Edit-2511_2039543264075849730.json, 图片生成/图生图/扩图，上下左右自定义尺寸，超快_2018966865443295233.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_112

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/删除人物保留衣服_2006911696627048449.json、图片生成/图生图/千问图片编辑工作流_1986050948818751490.json、图片生成/图生图/单图多角度_2073899870544551938.json、图片生成/图生图/废片光影重构影楼艺术照_2036626776293646338.json、图片生成/图生图/扩图 - Qwen-Image-Edit-2511_2039543264075849730.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 5/6 个有
- `ModelSamplingAuraFlow` —— 5/6 个有
- `ReferenceLatent` —— 5/6 个有
- `Image Comparer (rgthree)` —— 4/6 个有
- `ConstrainImage|pysssss` —— 3/6 个有
- `FluxKontextImageScale` —— 3/6 个有
- `ImagePadKJ` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `GenerateNoise` —— 1/6 个有
- `GetImageSize` —— 1/6 个有
- `LGNoiseInjectionLatent` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `QwenMultiangleCameraNode` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 6 | 36% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 67% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，6 个样本，取值分散，一致性仅 36%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（4/6 个样本）：Steps较低可能导致细节不足
