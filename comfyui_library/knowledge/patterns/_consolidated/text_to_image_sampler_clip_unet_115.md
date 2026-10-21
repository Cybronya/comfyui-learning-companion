---
name: text_to_image_sampler_clip_unet_115
type: Text To Image
frequency: 4
level: moderate
coverage: 0.9625
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, DapaoImageRatioLimitNode, EmptyLatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/文字头像抽卡神器_自动生成_2084090261851955202.json, 图片生成/文生图/风格文字头像自动生成_2080232577151102978.json, 图片生成/文生图/🦁国产之光 Qwen-image2512震撼来袭【随机提示词】_2007451112839843842.json, 图片生成/文生图/🦁国产之光 Qwen-image2512震撼来袭【随机提示词】_2007665464629010433.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_115

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/文字头像抽卡神器_自动生成_2084090261851955202.json、图片生成/文生图/风格文字头像自动生成_2080232577151102978.json、图片生成/文生图/🦁国产之光 Qwen-image2512震撼来袭【随机提示词】_2007451112839843842.json、图片生成/文生图/🦁国产之光 Qwen-image2512震撼来袭【随机提示词】_2007665464629010433.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `DapaoImageRatioLimitNode`
- `EmptyLatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 3/4 个有
- `RH_LLMAPI_NODE` —— 3/4 个有
- `Note Plus (mtb)` —— 2/4 个有
- `DapaoRandomPromptLineCombineNode` —— 1/4 个有
- `DapaoRandomPromptLineExtractNode` —— 1/4 个有
- `easy anythingIndexSwitch` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |
| 采样步数 | 10.5 | 9 - 30 | 4 | 42% |
| Prompt 约束强度(CFG) | 1.3 | 1 - 2.5 | 4 | 62% |
| 采样算法 | dpmpp_2m | - | 4 | 50% |
| 调度器 | karras | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10.5，观测区间 9 - 30，4 个样本，取值分散，一致性仅 42%
- Prompt 约束强度(CFG) 中位数 1.3，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 dpmpp_2m，4 个样本，一致性 50%
- 调度器 最常用 karras，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
