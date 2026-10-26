---
name: unknown_workflow_controlnet_lora_sampler_8
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8178
common_nodes: [AIO_Preprocessor, CLIPLoader, ControlNetApplySD3, ControlNetLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, SetUnionControlNetType, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Controlne图片生成——图片更可控_1962689042620002305.json, 图片生成/图生图/Qwen-image ControlNet工作流_2091486320215552002.json, 图片生成/图生图/真正的控制模型image_qwen_image+InstantXControlnet工作流_1960380425870913537.json, 图片生成/图生图/🥨Qwen Image 千问 InstantX 最强万能控制🥨_1961302899596967938.json, 图片生成/文生图/Qwen Image InstantX Controlnet 3合1_2073374577723531266.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_lora_sampler_8

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen Controlne图片生成——图片更可控_1962689042620002305.json、图片生成/图生图/Qwen-image ControlNet工作流_2091486320215552002.json、图片生成/图生图/真正的控制模型image_qwen_image+InstantXControlnet工作流_1960380425870913537.json、图片生成/图生图/🥨Qwen Image 千问 InstantX 最强万能控制🥨_1961302899596967938.json、图片生成/文生图/Qwen Image InstantX Controlnet 3合1_2073374577723531266.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `ControlNetApplySD3`
- `ControlNetLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `SetUnionControlNetType`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 4/5 个有
- `EmptySD3LatentImage` —— 4/5 个有
- `CFGNorm` —— 3/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `ImageConcanate` —— 2/5 个有
- `ImageConcatMulti` —— 2/5 个有
- `Int` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `SeedVR2BlockSwap` —— 2/5 个有
- `SeedVR2GGUF` —— 2/5 个有
- `CR SDXL Aspect Ratio` —— 1/5 个有
- `CR Text` —— 1/5 个有
- `EmptyImage` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `ImpactSwitch` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `SaveLatent` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有
- `TextEncodeQwenImageEdit` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| ControlNet 权重 | 0.75 | 0.7 - 2 | 5 | 49% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.75，观测区间 0.7 - 2，5 个样本，取值分散，一致性仅 49%
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
