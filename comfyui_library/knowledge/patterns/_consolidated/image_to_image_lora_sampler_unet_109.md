---
name: image_to_image_lora_sampler_unet_109
type: Image To Image
frequency: 6
level: strong
coverage: 0.964
common_nodes: [CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/【Qwen Edit 2511】多姿势多角度套图生成-场景人物一致性（真人略油）_2004162954566246402.json, 图片生成/图生图/一键生成15副姿势图动漫，真人_1990075137741516801.json, 图片生成/图生图/一键生成人物不同姿态_1987670680714022914.json, 图片生成/图生图/一键生成人物穿搭_1991670602532659201.json, 图片生成/图生图/人物一致性-多表情_2012765224817922050.json, 图片生成/图生图/人物生成换装工作流_2065382569604116482.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_109

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/【Qwen Edit 2511】多姿势多角度套图生成-场景人物一致性（真人略油）_2004162954566246402.json、图片生成/图生图/一键生成15副姿势图动漫，真人_1990075137741516801.json、图片生成/图生图/一键生成人物不同姿态_1987670680714022914.json、图片生成/图生图/一键生成人物穿搭_1991670602532659201.json、图片生成/图生图/人物一致性-多表情_2012765224817922050.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `ImageScaleToTotalPixels`
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
- `CFGNorm` —— 4/6 个有
- `ModelSamplingAuraFlow` —— 4/6 个有
- `RHHiddenNodes` —— 4/6 个有
- `ConditioningZeroOut` —— 3/6 个有
- `EmptySD3LatentImage` —— 3/6 个有
- `PrimitiveStringMultiline` —— 3/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `CLIPTextEncode` —— 1/6 个有
- `CompressImages` —— 1/6 个有
- `DeepTranslatorTextNode` —— 1/6 个有
- `EmptyHunyuanLatentVideo` —— 1/6 个有
- `Int` —— 1/6 个有
- `PreviewImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 6 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 67% |
| 调度器 | simple | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（7/6 个样本）：Steps较低可能导致细节不足
