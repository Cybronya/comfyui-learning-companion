---
name: text_to_image_sampler_clip_unet_152
type: Text To Image
frequency: 4
level: moderate
coverage: 0.74925
common_nodes: [CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, JanusImageUnderstanding, JanusModelLoader, KSampler, LayerUtility: PurgeVRAM, LoadImage, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/DeepseekR1+Janus-Pro模型工作流-StarAI_1891457968028917761.json, 图片生成/反推提示词/deepseek-JanusPro图片反推-FLUX图生图+LORA_1892560824442261506.json, 图片生成/文生图/Flux-文生图-图生图-加速版_2009553183344959489.json, 图片生成/文生图/Qwen-Image-Edit-文生图-图生图-加速版_2007390911692541953.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_152

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/反推提示词/DeepseekR1+Janus-Pro模型工作流-StarAI_1891457968028917761.json、图片生成/反推提示词/deepseek-JanusPro图片反推-FLUX图生图+LORA_1892560824442261506.json、图片生成/文生图/Flux-文生图-图生图-加速版_2009553183344959489.json、图片生成/文生图/Qwen-Image-Edit-文生图-图生图-加速版_2007390911692541953.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `JanusImageUnderstanding`
- `JanusModelLoader`
- `KSampler`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `ArgosTranslateTextNode` —— 2/4 个有
- `CR Text` —— 2/4 个有
- `ConstrainImage|pysssss` —— 2/4 个有
- `DifferentialDiffusion` —— 2/4 个有
- `Image Compare (mtb)` —— 2/4 个有
- `VAEEncode` —— 2/4 个有
- `CLIPLoader` —— 1/4 个有
- `LmcqDeepGen` —— 1/4 个有
- `LmcqDeepLoader` —— 1/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有
- `Note Plus (mtb)` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy clearCacheAll` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 808 | 512 - 1104 | 4 | 63% |
| 高度 | 1120 | 768 - 1472 | 4 | 69% |
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1.75 | 1 - 2.5 | 4 | 57% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 100% |
| 重绘幅度 | 0.8 | 0.6 - 1 | 4 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 808，观测区间 512 - 1104，4 个样本
- 高度 中位数 1120，观测区间 768 - 1472，4 个样本
- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.75，观测区间 1 - 2.5，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 100%
- 重绘幅度 中位数 0.8，观测区间 0.6 - 1，4 个样本
