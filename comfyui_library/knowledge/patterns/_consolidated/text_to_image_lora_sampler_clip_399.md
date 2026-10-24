---
name: text_to_image_lora_sampler_clip_399
type: Text To Image
frequency: 4
level: weak
coverage: 0.89675
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfySwitchNode, EmptyLatentImage, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ManualSigmas, QwenImage21SageAttentionT8, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux3人像完美一致性图像编辑V1_2111090153166036993.json, 图片生成/文生图/Flux3人像完美一致性-多图图像编辑_2111145894010773506.json, 图片生成/文生图/Flux3人像完美一致性，多图图像编辑反推提示词_2111512061292404738.json, 图片生成/文生图/Qwen Image 2.1 加速PE加in 版，文生图速度翻倍_2110472226297442305.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_399

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux3人像完美一致性图像编辑V1_2111090153166036993.json、图片生成/文生图/Flux3人像完美一致性-多图图像编辑_2111145894010773506.json、图片生成/文生图/Flux3人像完美一致性，多图图像编辑反推提示词_2111512061292404738.json、图片生成/文生图/Qwen Image 2.1 加速PE加in 版，文生图速度翻倍_2110472226297442305.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ComfySwitchNode`
- `EmptyLatentImage`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `QwenImage21SageAttentionT8`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 3/4 个有
- `ConcatTextOfUtils` —— 3/4 个有
- `EmptyFlux2LatentImage` —— 3/4 个有
- `LoraLoaderBypassModelOnly` —— 3/4 个有
- `QwenImage21Cache` —— 3/4 个有
- `ReferenceMultiLatent` —— 3/4 个有
- `孤海注释` —— 3/4 个有
- `JjkText` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `solarL_SaveImagesToZip` —— 2/4 个有
- `CFGGuider` —— 1/4 个有
- `QwenPERewriteT8` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 552 | 80 - 1024 | 4 | 14% |
| 高度 | 552 | 80 - 1024 | 4 | 14% |
| 采样步数 | 6 | 4 - 8 | 4 | 67% |
| Prompt 约束强度(CFG) | 2.75 | 1 - 4.5 | 4 | 36% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 552，观测区间 80 - 1024，4 个样本，取值分散，一致性仅 14%
- 高度 中位数 552，观测区间 80 - 1024，4 个样本，取值分散，一致性仅 14%
- 采样步数 中位数 6，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 2.75，观测区间 1 - 4.5，4 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
