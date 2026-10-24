---
name: unknown_workflow_lora_sampler_unet_134
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8362
common_nodes: [CFGNorm, CLIPLoader, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen edit 人物一致性参考_1970748764862488577.json, 图片生成/图生图/Qwen image Edit 免费修图神器，中文识别能力超强_1959933347139104770.json, 图片生成/图生图/竖中指LoRA——Qwen-Image-Edit应用_1965017377282904065.json, 图片生成/图生图/精准换头LoRA——Qwen-Image-Edit应用_1961739539767300097.json, 图片生成/图生图/雪8.tonnie-edit 2509-仅头部换装_2002801811700498433.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_134

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen edit 人物一致性参考_1970748764862488577.json、图片生成/图生图/Qwen image Edit 免费修图神器，中文识别能力超强_1959933347139104770.json、图片生成/图生图/竖中指LoRA——Qwen-Image-Edit应用_1965017377282904065.json、图片生成/图生图/精准换头LoRA——Qwen-Image-Edit应用_1961739539767300097.json、图片生成/图生图/雪8.tonnie-edit 2509-仅头部换装_2002801811700498433.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
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
- `TextEncodeQwenImageEdit` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `RMBG` —— 2/5 个有
- `Image Crop Face` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `LoadImageFromUrl` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `PresetText|pysssss` —— 1/5 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 5 | 33% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 5 | 54% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1024 | 768 - 1920 | 5 | 67% |
| 高度 | 1024 | 1024 - 1280 | 5 | 90% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，5 个样本，取值分散，一致性仅 33%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，5 个样本
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 768 - 1920，5 个样本
- 高度 中位数 1024，观测区间 1024 - 1280，5 个样本，取值集中（一致性 90%）
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
