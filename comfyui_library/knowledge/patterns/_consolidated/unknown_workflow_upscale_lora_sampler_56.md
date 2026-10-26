---
name: unknown_workflow_upscale_lora_sampler_56
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.736333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, Image Comparer (rgthree), KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Qwen3-VL反推图片提示词_1980889291398234113.json, 图片生成/文生图/Ultimate SD 图像升频放大 Z-Image Turbo_2036815909616099329.json, 图片生成/文生图/qwen_image_Qwen3VL_txt2img   文本到图像工作流_1981021439052615681.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_56

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/Qwen3-VL反推图片提示词_1980889291398234113.json、图片生成/文生图/Ultimate SD 图像升频放大 Z-Image Turbo_2036815909616099329.json、图片生成/文生图/qwen_image_Qwen3VL_txt2img   文本到图像工作流_1981021439052615681.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL_Advanced` —— 2/3 个有
- `GetImageSize` —— 2/3 个有
- `LatentUpscaleBy` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `Label (rgthree)` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 9 | 3 | 94% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.2 | 0.2 - 1 | 3 | 19% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 9，3 个样本，取值集中（一致性 94%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.2，观测区间 0.2 - 1，3 个样本，取值分散，一致性仅 19%
- 高发问题（5/3 个样本）：Steps较低可能导致细节不足
