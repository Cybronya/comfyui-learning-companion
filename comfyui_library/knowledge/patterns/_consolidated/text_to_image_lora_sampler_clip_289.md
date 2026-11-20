---
name: text_to_image_lora_sampler_clip_289
type: Text To Image
frequency: 7
level: weak
coverage: 0.896429
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfySwitchNode, EmptyLatentImage, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ManualSigmas, QwenImage21SageAttentionT8, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux3人像完美一致性图像编辑V1_2111090153166036993.json, 图片生成/图生图/Flux3人像完美一致性图像编辑V1_2114185496237797377.json, 图片生成/图生图/Flux3人像完美一致性图像编辑V1_2115277692634488833.json, 图片生成/文生图/Flux3人像完美一致性-多图图像编辑_2111145894010773506.json, 图片生成/文生图/Flux3人像完美一致性，多图图像编辑反推提示词_2111512061292404738.json, 图片生成/文生图/Qwen Image 2.1 加速PE加in 版，文生图速度翻倍_2110472226297442305.json, 视频生成/图生视频/Qwen_Image_2.1_加速PE加in_版，文生图速度翻倍_2113110553781686274.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_289

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Flux3人像完美一致性图像编辑V1_2111090153166036993.json、图片生成/图生图/Flux3人像完美一致性图像编辑V1_2114185496237797377.json、图片生成/图生图/Flux3人像完美一致性图像编辑V1_2115277692634488833.json、图片生成/文生图/Flux3人像完美一致性-多图图像编辑_2111145894010773506.json、图片生成/文生图/Flux3人像完美一致性，多图图像编辑反推提示词_2111512061292404738.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
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
- `BasicGuider` —— 5/7 个有
- `ConcatTextOfUtils` —— 5/7 个有
- `EmptyFlux2LatentImage` —— 5/7 个有
- `LoraLoaderBypassModelOnly` —— 5/7 个有
- `QwenImage21Cache` —— 5/7 个有
- `ReferenceMultiLatent` —— 5/7 个有
- `easy showAnything` —— 5/7 个有
- `JjkText` —— 3/7 个有
- `solarL_SaveImagesToZip` —— 3/7 个有
- `孤海注释` —— 3/7 个有
- `CFGGuider` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `QwenPERewriteT8` —— 2/7 个有
- `EmptyImage` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 80 - 1024 | 7 | 25% |
| 高度 | 1024 | 80 - 1024 | 7 | 25% |
| 采样步数 | 8 | 4 - 8 | 7 | 69% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 7 | 31% |
| 采样算法 | euler | - | 7 | 57% |
| 调度器 | simple | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 80 - 1024，7 个样本，取值分散，一致性仅 25%
- 高度 中位数 1024，观测区间 80 - 1024，7 个样本，取值分散，一致性仅 25%
- 采样步数 中位数 8，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，7 个样本，取值分散，一致性仅 31%
- 采样算法 最常用 euler，7 个样本，一致性 57%
- 调度器 最常用 simple，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（8/7 个样本）：Steps较低可能导致细节不足
