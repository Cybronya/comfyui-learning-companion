---
name: image_to_image_lora_sampler_unet_168
type: Image To Image
frequency: 3
level: strong
coverage: 0.824333
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit image百搭秀——人物换装 终极姿势控制_1995873371814518785.json, 图片生成/图生图/Qwen Edit 一致性多角度分镜编辑手动提示词-镜头转换lora_2003466889487630337.json, 图片生成/图生图/Qwen Edit 一致性多角度编辑V1（提示词手写版-多图）_1987563699441479682.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_168

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen Edit image百搭秀——人物换装 终极姿势控制_1995873371814518785.json、图片生成/图生图/Qwen Edit 一致性多角度分镜编辑手动提示词-镜头转换lora_2003466889487630337.json、图片生成/图生图/Qwen Edit 一致性多角度编辑V1（提示词手写版-多图）_1987563699441479682.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `JDCN_StringToList` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `easy imageSize` —— 2/3 个有
- `DWPreprocessor` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImpactSwitch` —— 1/3 个有
- `Qwen3VL_Advanced` —— 1/3 个有
- `Text Concatenate` —— 1/3 个有
- `TextInput_` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 3 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
