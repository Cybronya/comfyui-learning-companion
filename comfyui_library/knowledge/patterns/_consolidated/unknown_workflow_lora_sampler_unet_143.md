---
name: unknown_workflow_lora_sampler_unet_143
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8946
common_nodes: [CFGNorm, CLIPLoader, EmptyLatentImage, ImageConcanate, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit 2509，社区Lora，保持人脸_1987522076376502273.json, 图片生成/图生图/Qwen Edit 2509，社区Lora，双人合照_1987922191335493633.json, 图片生成/图生图/Qwen Edit 2509，社区Lora，双人接吻_1987930666904039426.json, 图片生成/图生图/Qwen Edit 2509，社区Lora，添加人物_1987939997108121602.json, 图片生成/图生图/疯狂动物城合照_1992252774878433281.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_143

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen Edit 2509，社区Lora，保持人脸_1987522076376502273.json、图片生成/图生图/Qwen Edit 2509，社区Lora，双人合照_1987922191335493633.json、图片生成/图生图/Qwen Edit 2509，社区Lora，双人接吻_1987930666904039426.json、图片生成/图生图/Qwen Edit 2509，社区Lora，添加人物_1987939997108121602.json、图片生成/图生图/疯狂动物城合照_1992252774878433281.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `EmptyLatentImage`
- `ImageConcanate`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 4/5 个有
- `Image Comparer (rgthree)` —— 3/5 个有
- `UltimateSDUpscaleNoUpscale` —— 3/5 个有
- `CR Prompt List` —— 1/5 个有
- `ImageAndMaskPreview` —— 1/5 个有
- `InvertMask` —— 1/5 个有
- `LayerMask: PersonMaskUltra V2` —— 1/5 个有
- `LayerUtility: CropByMask V3` —— 1/5 个有
- `ReActorFaceSwap` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
