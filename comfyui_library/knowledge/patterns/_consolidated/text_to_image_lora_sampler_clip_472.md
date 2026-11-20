---
name: text_to_image_lora_sampler_clip_472
type: Text To Image
frequency: 4
level: strong
coverage: 0.9455
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea_2_Turbo高美学文生图｜出图质感直接拉满_2098986502435991553.json, 图片生成/文生图/Krea_2_Turbo高美学文生图｜出图质感直接拉满_2099662369931751426.json, 图片生成/文生图/qwen-image-2.1文生图基础款｜参数清爽开箱即用｜日常出图够用了_2102320781945561089.json, 视频生成/文生视频/Qwen_image_2.1文生图美少女特调｜写实风格出图细腻｜二次元真人两相宜_2104048080306917377.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_472

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Krea_2_Turbo高美学文生图｜出图质感直接拉满_2098986502435991553.json、图片生成/文生图/Krea_2_Turbo高美学文生图｜出图质感直接拉满_2099662369931751426.json、图片生成/文生图/qwen-image-2.1文生图基础款｜参数清爽开箱即用｜日常出图够用了_2102320781945561089.json、视频生成/文生视频/Qwen_image_2.1文生图美少女特调｜写实风格出图细腻｜二次元真人两相宜_2104048080306917377.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `ModelSamplingAuraFlow` —— 2/4 个有
- `PathchSageAttentionKJ` —— 2/4 个有
- `SaveImageAdvanced` —— 2/4 个有
- `TextEncodeQwenImage21` —— 2/4 个有
- `easy loraStack` —— 2/4 个有
- `easy loraStackApply` —— 2/4 个有
- `ResolutionSelector` —— 1/4 个有
- `TextGenerateLTX2Prompt` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
