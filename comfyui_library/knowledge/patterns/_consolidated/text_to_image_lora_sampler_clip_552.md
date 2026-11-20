---
name: text_to_image_lora_sampler_clip_552
type: Text To Image
frequency: 3
level: strong
coverage: 0.875
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, ImpactSwitch, Int, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, PathchSageAttentionKJ, RH_LLMAPI_NODE, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 修仙短剧人物一致性增强_1965625145698209793.json, 图片生成/文生图/Qwen Image 文生图_1988803647096098817.json, 图片生成/文生图/漫剧人设场景图生成（千问）_2008447165357629441.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_552

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Qwen Image 修仙短剧人物一致性增强_1965625145698209793.json、图片生成/文生图/Qwen Image 文生图_1988803647096098817.json、图片生成/文生图/漫剧人设场景图生成（千问）_2008447165357629441.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `ImpactSwitch`
- `Int`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
- `RH_LLMAPI_NODE`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 2/3 个有
- `SaveImage` —— 2/3 个有
- `SaveImagePlus` —— 2/3 个有
- `ShowText` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `SeedVR2LoadDiTModel` —— 1/3 个有
- `SeedVR2LoadVAEModel` —— 1/3 个有
- `SeedVR2VideoUpscaler` —— 1/3 个有
- `easy showAnything` —— 1/3 个有
- `ttN concat` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
