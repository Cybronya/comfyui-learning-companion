---
name: unknown_workflow_lora_sampler_clip_186
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.929333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen 2512海报洗图工作流（图中文字都能直出）_2021063722009108481.json, 图片生成/图生图/Qwen千问反推生图8步lora加速_1954719425863794689.json, 图片生成/图生图/千问图像编辑，加速版，Qwen edit_1958440567510351873.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_186

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen 2512海报洗图工作流（图中文字都能直出）_2021063722009108481.json、图片生成/图生图/Qwen千问反推生图8步lora加速_1954719425863794689.json、图片生成/图生图/千问图像编辑，加速版，Qwen edit_1958440567510351873.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `AILab_QwenVL` —— 1/3 个有
- `CFGNorm` —— 1/3 个有
- `Display Any (rgthree)` —— 1/3 个有
- `Int` —— 1/3 个有
- `LayerColor: ColorAdapter` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `TextEncodeQwenImageEdit` —— 1/3 个有
- `TextInput_` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 3 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 3 | 29% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，3 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
