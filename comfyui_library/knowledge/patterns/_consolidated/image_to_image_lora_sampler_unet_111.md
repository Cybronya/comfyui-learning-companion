---
name: image_to_image_lora_sampler_unet_111
type: Image To Image
frequency: 6
level: moderate
coverage: 0.932833
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptLine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/二哥玩AI-电商图生多图-一天1000张电商模特图_2061364098285268993.json, 图片生成/图生图/实物电商自动角度（10图版）_2040671158126780417.json, 图片生成/图生图/按数量自动分镜V2-适合补充机位_2023385298331242497.json, 图片生成/图生图/自动分镜V3-适合短视频分镜_2023356108282273793.json, 图片生成/图生图/自动按照场景生成九张分镜图人物一致性_2039897985915555841.json, 图片生成/文生图/qwen_image_edit_2511连续分镜生产_2007869415899013122.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_111

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/二哥玩AI-电商图生多图-一天1000张电商模特图_2061364098285268993.json、图片生成/图生图/实物电商自动角度（10图版）_2040671158126780417.json、图片生成/图生图/按数量自动分镜V2-适合补充机位_2023385298331242497.json、图片生成/图生图/自动分镜V3-适合短视频分镜_2023356108282273793.json、图片生成/图生图/自动按照场景生成九张分镜图人物一致性_2039897985915555841.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
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
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `easy showAnything` —— 4/6 个有
- `RH_LLMAPI_NODE` —— 3/6 个有
- `Text` —— 3/6 个有
- `EmptyLatentImage` —— 2/6 个有
- `Image Comparer (rgthree)` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `VAEDecodeTiled` —— 2/6 个有
- `CR Prompt Text` —— 1/6 个有
- `EmptySD3LatentImage` —— 1/6 个有
- `JoinStrings` —— 1/6 个有
- `Qwen3_VQA` —— 1/6 个有
- `Text Multiline` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1596 | - | 2 | 50% |
| 高度 | 1060 | - | 2 | 75% |
| 采样步数 | 8 | 4 - 8 | 6 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1596，样本不足，未给区间，2 个样本
- 高度 中位数 1060，样本不足，未给区间，2 个样本
- 采样步数 中位数 8，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
