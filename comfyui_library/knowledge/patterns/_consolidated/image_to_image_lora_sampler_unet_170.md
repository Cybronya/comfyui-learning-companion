---
name: image_to_image_lora_sampler_unet_170
type: Image To Image
frequency: 4
level: moderate
coverage: 0.883
common_nodes: [CLIPLoader, Int, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/超级分镜2511_2004558868975939585.json, 图片生成/图生图/超级分镜动漫版_2016459672915550209.json, 图片生成/文生图/视频生成-生成分镜图片_2012090015605596162.json, 图片生成/文生图/视频生成-生成分镜图片多角色_2098296059050160129.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_170

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/超级分镜2511_2004558868975939585.json、图片生成/图生图/超级分镜动漫版_2016459672915550209.json、图片生成/文生图/视频生成-生成分镜图片_2012090015605596162.json、图片生成/文生图/视频生成-生成分镜图片多角色_2098296059050160129.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `Int`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 2/4 个有
- `CFGNorm` —— 2/4 个有
- `CR Prompt Text` —— 2/4 个有
- `Fast Groups Muter (rgthree)` —— 2/4 个有
- `JWStringConcat` —— 2/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `ModelSamplingAuraFlow` —— 2/4 个有
- `Qwen3_VQA` —— 2/4 个有
- `Text Multiline` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 12 | 4 | 50% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler_ancestral | - | 4 | 50% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 12，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 50%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（2/4 个样本）：Steps较低可能导致细节不足
