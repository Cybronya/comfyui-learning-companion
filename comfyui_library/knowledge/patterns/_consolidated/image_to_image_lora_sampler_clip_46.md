---
name: image_to_image_lora_sampler_clip_46
type: Image To Image
frequency: 6
level: moderate
coverage: 0.7465
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CR Prompt Text, GetNode, ImageScaleToTotalPixels, JWStringConcat, KSampler, LoadImage, LoraLoaderModelOnly, MemoryCleaner, ModelSamplingAuraFlow, Qwen3_VQA, SaveImage, SetNode, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy int, easy showAnything, 图像缩放V2_孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-史上最强动漫转写实真人（Z-image重绘CFG1.6）_2002567462472302594.json, 图片生成/图生图/Qwen-史上最强动漫转真人（Z-image_FlowMatch重绘）_2002654471387770881.json, 图片生成/图生图/【推荐】Qwen+Z-image+FlowMat强动漫转真人_2008549846252261378.json, 图片生成/图生图/【推荐】动漫转写实真人（Z-image重绘CFG1.6）_2008549814203588610.json, 图片生成/图生图/动漫转写实真人-Z-image重绘_2002960576038989826.json, 图片生成/图生图/动漫转真人_2004780912804069377.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_46

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen-史上最强动漫转写实真人（Z-image重绘CFG1.6）_2002567462472302594.json、图片生成/图生图/Qwen-史上最强动漫转真人（Z-image_FlowMatch重绘）_2002654471387770881.json、图片生成/图生图/【推荐】Qwen+Z-image+FlowMat强动漫转真人_2008549846252261378.json、图片生成/图生图/【推荐】动漫转写实真人（Z-image重绘CFG1.6）_2008549814203588610.json、图片生成/图生图/动漫转写实真人-Z-image重绘_2002960576038989826.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `GetNode`
- `ImageScaleToTotalPixels`
- `JWStringConcat`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MemoryCleaner`
- `ModelSamplingAuraFlow`
- `Qwen3_VQA`
- `SaveImage`
- `SetNode`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy int`
- `easy showAnything`
- `图像缩放V2_孤海`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 5/6 个有
- `FlowMatchEulerDiscreteScheduler (Custom)` —— 5/6 个有
- `KSamplerSelect` —— 5/6 个有
- `LazyCache` —— 5/6 个有
- `RandomNoise` —— 5/6 个有
- `SamplerCustomAdvanced` —— 5/6 个有
- `SplitSigmasDenoise` —— 5/6 个有
- `Fast Groups Muter (rgthree)` —— 4/6 个有
- `ConditioningZeroOut` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 10 | 6 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.6 | 6 | 80% |
| 采样算法 | res_2m | - | 6 | 83% |
| 调度器 | sgm_uniform | - | 6 | 83% |
| 重绘幅度 | 1 | 0.4 - 1 | 6 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 10，6 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.6，6 个样本
- 采样算法 最常用 res_2m，6 个样本，一致性 83%
- 调度器 最常用 sgm_uniform，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，6 个样本
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
