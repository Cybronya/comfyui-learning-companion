---
name: image_to_image_lora_sampler_unet_99
type: Image To Image
frequency: 6
level: strong
coverage: 0.819833
common_nodes: [CFGNorm, CLIPLoader, ImageConcanate, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/02-03-02-QwenEdit-多图融合-改动作_1987548649586667522.json, 图片生成/图生图/BFS QwenEdit 2511换头换脸V1_2019439713349804033.json, 图片生成/图生图/BFS QwenEdit 2511换头换脸V1_2020684341747126274.json, 图片生成/图生图/Qwen2511+模特姿势复刻_2003731932687048705.json, 图片生成/图生图/Qwen2511图片编辑(自用版)_2062203408433635330.json, 图片生成/图生图/图片去水印-Qwen-Edit-2511_2077755293496336386.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_99

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/02-03-02-QwenEdit-多图融合-改动作_1987548649586667522.json、图片生成/图生图/BFS QwenEdit 2511换头换脸V1_2019439713349804033.json、图片生成/图生图/BFS QwenEdit 2511换头换脸V1_2020684341747126274.json、图片生成/图生图/Qwen2511+模特姿势复刻_2003731932687048705.json、图片生成/图生图/Qwen2511图片编辑(自用版)_2062203408433635330.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageConcanate`
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
- `FluxKontextMultiReferenceLatentMethod` —— 5/6 个有
- `ImageScaleToTotalPixels` —— 4/6 个有
- `ModelSamplingAuraFlow` —— 4/6 个有
- `CR Prompt Text` —— 3/6 个有
- `CR Text` —— 3/6 个有
- `ConditioningZeroOut` —— 3/6 个有
- `GetNode` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `AIO_Preprocessor` —— 2/6 个有
- `FluxKontextImageScale` —— 2/6 个有
- `Anything Everywhere` —— 1/6 个有
- `Anything Everywhere3` —— 1/6 个有
- `Crop Face` —— 1/6 个有
- `DuckHideNode` —— 1/6 个有
- `Load RetinaFace` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 6 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
