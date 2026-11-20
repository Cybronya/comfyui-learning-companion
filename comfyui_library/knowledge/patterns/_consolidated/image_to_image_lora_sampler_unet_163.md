---
name: image_to_image_lora_sampler_unet_163
type: Image To Image
frequency: 4
level: moderate
coverage: 0.90675
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/二哥玩AI-电商图生多图-一天1000张电商模特图_2061364098285268993.json, 图片生成/图生图/实物电商自动角度（10图版）_2040671158126780417.json, 图片生成/图生图/提取电商图封面模板_2034665275026579457.json, 图片生成/文生图/qwen_image_edit_2511连续分镜生产_2007869415899013122.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_163

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/二哥玩AI-电商图生多图-一天1000张电商模特图_2061364098285268993.json、图片生成/图生图/实物电商自动角度（10图版）_2040671158126780417.json、图片生成/图生图/提取电商图封面模板_2034665275026579457.json、图片生成/文生图/qwen_image_edit_2511连续分镜生产_2007869415899013122.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
- `ImageScaleToTotalPixels`
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
- `PreviewImage` —— 3/4 个有
- `easy promptLine` —— 3/4 个有
- `EmptyLatentImage` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `VAEDecodeTiled` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `EmptySD3LatentImage` —— 1/4 个有
- `JoinStrings` —— 1/4 个有
- `Qwen3_VQA` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1596 | - | 2 | 50% |
| 高度 | 1060 | - | 2 | 75% |
| 采样步数 | 6 | 4 - 8 | 4 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1596，样本不足，未给区间，2 个样本
- 高度 中位数 1060，样本不足，未给区间，2 个样本
- 采样步数 中位数 6，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
