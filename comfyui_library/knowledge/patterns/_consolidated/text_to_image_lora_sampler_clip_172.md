---
name: text_to_image_lora_sampler_clip_172
type: Text To Image
frequency: 5
level: strong
coverage: 0.8514
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2102588489098424321.json, 图片生成/文生图/G Image2低价版文生图工作流，低成本文本到图像生成方案_2106128186449944577.json, 图片生成/文生图/Krea2人物四视图工作流，人物角色角色设计文生图工具_2107516751167713281.json, 图片生成/文生图/Qwen Image 2.1 PE文生图优化版｜出图质量再打磨｜细节党放心冲_2102587044131336194.json, 视频生成/文生视频/Qwen_Image_2.1提示词强化PE工作流，中文白话输入自动扩写专业提示词出图_2106552276637802498.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_172

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/2102588489098424321.json、图片生成/文生图/G Image2低价版文生图工作流，低成本文本到图像生成方案_2106128186449944577.json、图片生成/文生图/Krea2人物四视图工作流，人物角色角色设计文生图工具_2107516751167713281.json、图片生成/文生图/Qwen Image 2.1 PE文生图优化版｜出图质量再打磨｜细节党放心冲_2102587044131336194.json、视频生成/文生视频/Qwen_Image_2.1提示词强化PE工作流，中文白话输入自动扩写专业提示词出图_2106552276637802498.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `孤海注释` —— 4/5 个有
- `PreviewAny` —— 3/5 个有
- `QwenPECanvasT8` —— 3/5 个有
- `QwenPERewriteT8` —— 3/5 个有
- `SaveImage` —— 3/5 个有
- `SaveText` —— 2/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `EmptyImage` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `QwenImage21Cache` —— 1/5 个有
- `RH_RhartImageG2TextToImage` —— 1/5 个有
- `TextEncodeQwenImage21` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
