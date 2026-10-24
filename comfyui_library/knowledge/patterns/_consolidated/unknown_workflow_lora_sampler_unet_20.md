---
name: unknown_workflow_lora_sampler_unet_20
type: Unknown Workflow
frequency: 19
level: strong
coverage: 0.722789
common_nodes: [CLIPLoader, EmptySD3LatentImage, GetNode, ImageResizeKJv2, KSampler, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, PrimitiveInt, SaveImage, SetNode, Text Multiline, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen 自动换装 效果炸裂 Qwen Edit Plus_1993935360845692930.json, 图片生成/图生图/Qwen自动换装=Qwen Edit Plus=艾橘溪_1971919377803243522.json, 图片生成/图生图/Qwen自动换装=Qwen Edit Plus_2049691407861944322.json, 图片生成/图生图/Qwen自动换装=Qwen Edit Plus_2050774538560000001.json, 图片生成/图生图/Qwen自动换装=Qwen Edit Plus。Nice!快来实现你的服装自由~_2019614697393229825.json, 图片生成/图生图/Qwen自动换装=Qwen+Edit+Plus_2016404512042393601.json, 图片生成/图生图/Qwen自动换装=Qwen+Edit+Plus_2043573551764082689.json, 图片生成/图生图/Qwen自动换装=Qwen+Edit_2037913702409707521.json, 图片生成/图生图/一键超丝滑人物换装_2018251027530649601.json, 图片生成/图生图/人物变装_2001536253583605761.json, 图片生成/图生图/人物换装V2_1998660901823766529.json, 图片生成/图生图/双图合成 Qwen Edit Plus=艾橘溪_1972242738039156738.json, 图片生成/图生图/双图合成 Qwen Edit Plus_2079453732571541505.json, 图片生成/图生图/超丝滑一键人物换装_2044658402135117826.json, 图片生成/图生图/超丝滑一键人物换装_2057004893273157633.json, 图片生成/图生图/超丝滑一键人物换装_2063903458717159425.json, 图片生成/图生图/超丝滑一键人物换装_2066404608926371842.json, 图片生成/文生图/Qwen Edit Plus 2image_2005489054781243393.json, 视频生成/图生视频/图生图  简单易操作  Qwen自动换装=Qwen Edit Plus_2029100909296361474.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_20

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/Qwen 自动换装 效果炸裂 Qwen Edit Plus_1993935360845692930.json、图片生成/图生图/Qwen自动换装=Qwen Edit Plus=艾橘溪_1971919377803243522.json、图片生成/图生图/Qwen自动换装=Qwen Edit Plus_2049691407861944322.json、图片生成/图生图/Qwen自动换装=Qwen Edit Plus_2050774538560000001.json、图片生成/图生图/Qwen自动换装=Qwen Edit Plus。Nice!快来实现你的服装自由~_2019614697393229825.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `EmptySD3LatentImage`
- `GetNode`
- `ImageResizeKJv2`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveInt`
- `SaveImage`
- `SetNode`
- `Text Multiline`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `VAELoader` —— 17/19 个有
- `ConditioningZeroOut` —— 16/19 个有
- `ImageConcatMulti` —— 16/19 个有
- `ImageStitch` —— 16/19 个有
- `CFGNorm` —— 3/19 个有
- `ModelSamplingAuraFlow` —— 3/19 个有
- `TextEncodeQwenImageEdit` —— 3/19 个有
- `CheckpointLoaderSimple` —— 2/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 19 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 19 | 100% |
| 采样算法 | euler | - | 19 | 100% |
| 调度器 | simple | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，19 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，19 个样本，一致性 100%
- 调度器 最常用 simple，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 高发问题（19/19 个样本）：Steps较低可能导致细节不足
