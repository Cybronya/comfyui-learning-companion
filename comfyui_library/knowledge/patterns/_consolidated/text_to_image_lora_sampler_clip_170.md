---
name: text_to_image_lora_sampler_clip_170
type: Text To Image
frequency: 7
level: strong
coverage: 0.908
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea_2_Turbo高美学文生图｜出图质感直接拉满_2098928781699407874.json, 图片生成/文生图/Krea_2_Turbo高美学文生图｜出图质感直接拉满_2098986502435991553.json, 图片生成/文生图/Krea_2_Turbo高美学文生图｜出图质感直接拉满_2099662369931751426.json, 图片生成/文生图/Qwen2.1文生图写实风格 照片级质感画面直出_2105475614315737089.json, 图片生成/文生图/Qwen朋友圈海报设计V1.0文生图工具_2100273790323351553.json, 图片生成/文生图/Qwen朋友圈海报设计文生图处理生成工作流_2101019397950361601.json, 图片生成/文生图/小腰精体态曲线塑造 文生图一键生成完美身材比例_2104343399116664834.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_170

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Krea_2_Turbo高美学文生图｜出图质感直接拉满_2098928781699407874.json、图片生成/文生图/Krea_2_Turbo高美学文生图｜出图质感直接拉满_2098986502435991553.json、图片生成/文生图/Krea_2_Turbo高美学文生图｜出图质感直接拉满_2099662369931751426.json、图片生成/文生图/Qwen2.1文生图写实风格 照片级质感画面直出_2105475614315737089.json、图片生成/文生图/Qwen朋友圈海报设计V1.0文生图工具_2100273790323351553.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 7 个 workflow 都包含：
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
- `ModelSamplingAuraFlow` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `孤海注释` —— 5/7 个有
- `CR Text` —— 3/7 个有
- `EmptySD3LatentImage` —— 3/7 个有
- `LoraLoader` —— 3/7 个有
- `PathchSageAttentionKJ` —— 3/7 个有
- `easy loraStack` —— 3/7 个有
- `easy loraStackApply` —— 3/7 个有
- `EmptyImage` —— 2/7 个有
- `UltimateSDUpscale` —— 2/7 个有
- `UpscaleModelLoader` —— 2/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |
| LoRA 模型强度 | 0.8 | 0.8 - 0.8 | 3 | 100% |
| LoRA 文本强度 | 0.8 | 0.8 - 1 | 3 | 89% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 0.8，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.8，观测区间 0.8 - 1，3 个样本，取值集中（一致性 89%）
- 高发问题（12/7 个样本）：Steps较低可能导致细节不足
