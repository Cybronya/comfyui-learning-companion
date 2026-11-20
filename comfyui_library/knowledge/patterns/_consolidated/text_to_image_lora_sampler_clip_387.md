---
name: text_to_image_lora_sampler_clip_387
type: Text To Image
frequency: 5
level: moderate
coverage: 0.8546
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image 电商海报+详情页洗图_1984093020838625282.json, 图片生成/图生图/【电商海报洗图仿图】Qwen+8步快速生成 电商首图详情页自动反推洗图仿图 海报平面设计_1984158037869002754.json, 图片生成/图生图/【阡陌】Qwen-Image Canny ControlNet提示词反推精准控图工作流_1959553457558597634.json, 图片生成/图生图/【阡陌】Qwen-Image Depth ControlNet 提示词反推精准控图工作流_1959643499979288577.json, 图片生成/图生图/跨境电商自动反推洗图仿图-Qwen 8步快速_1959442541798174721.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_387

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen-Image 电商海报+详情页洗图_1984093020838625282.json、图片生成/图生图/【电商海报洗图仿图】Qwen+8步快速生成 电商首图详情页自动反推洗图仿图 海报平面设计_1984158037869002754.json、图片生成/图生图/【阡陌】Qwen-Image Canny ControlNet提示词反推精准控图工作流_1959553457558597634.json、图片生成/图生图/【阡陌】Qwen-Image Depth ControlNet 提示词反推精准控图工作流_1959643499979288577.json、图片生成/图生图/跨境电商自动反推洗图仿图-Qwen 8步快速_1959442541798174721.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/5 个有
- `ShowText|pysssss` —— 4/5 个有
- `JanusImage2Text` —— 3/5 个有
- `LayerUtility: PurgeVRAM` —— 3/5 个有
- `LayerUtility: TextJoin` —— 3/5 个有
- `LoadJanusModel` —— 3/5 个有
- `TextInput_` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `JanusImageUnderstanding` —— 2/5 个有
- `JanusModelLoader` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `workflow>controlnet` —— 2/5 个有
- `ConditioningZeroOut` —— 1/5 个有
- `DownloadAndLoadQwen2_5_VLModel` —— 1/5 个有
- `Qwen2_5_VL_Run_Advanced` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 35 | 5 | 15% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1024 | 768 - 1024 | 5 | 86% |
| 高度 | 1232 | 1024 - 1680 | 5 | 81% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 35，5 个样本，取值分散，一致性仅 15%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 768 - 1024，5 个样本，取值集中（一致性 86%）
- 高度 中位数 1232，观测区间 1024 - 1680，5 个样本，取值集中（一致性 81%）
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足
