---
name: unknown_workflow_lora_sampler_unet_78
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.900125
common_nodes: [CFGNorm, CLIPLoader, ImageConcanate, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit 2509，社区Lora，保持人脸_1987522076376502273.json, 图片生成/图生图/Qwen Edit 2509，社区Lora，切换多镜头拍摄_1987508199920177154.json, 图片生成/图生图/Qwen Edit 2509，社区Lora，双人合照_1987922191335493633.json, 图片生成/图生图/Qwen Edit 2509，社区Lora，双人接吻_1987930666904039426.json, 图片生成/图生图/Qwen Edit 2509，社区Lora，添加人物_1987939997108121602.json, 图片生成/图生图/Qwen Edit 2509，社区Lora，重新打光_1987516185564655618.json, 图片生成/图生图/Qwen Edit 2509，社区Lora，预测未来下一帧场景_1987519513975525377.json, 图片生成/图生图/疯狂动物城合照_1992252774878433281.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_78

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen Edit 2509，社区Lora，保持人脸_1987522076376502273.json、图片生成/图生图/Qwen Edit 2509，社区Lora，切换多镜头拍摄_1987508199920177154.json、图片生成/图生图/Qwen Edit 2509，社区Lora，双人合照_1987922191335493633.json、图片生成/图生图/Qwen Edit 2509，社区Lora，双人接吻_1987930666904039426.json、图片生成/图生图/Qwen Edit 2509，社区Lora，添加人物_1987939997108121602.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
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
- `EmptyLatentImage` —— 5/8 个有
- `INTConstant` —— 4/8 个有
- `Image Comparer (rgthree)` —— 4/8 个有
- `CR Prompt List` —— 3/8 个有
- `TextEncodeQwenImageEdit_lrzjason` —— 3/8 个有
- `UltimateSDUpscaleNoUpscale` —— 3/8 个有
- `ImageAndMaskPreview` —— 1/8 个有
- `InvertMask` —— 1/8 个有
- `LayerMask: PersonMaskUltra V2` —— 1/8 个有
- `LayerUtility: CropByMask V3` —— 1/8 个有
- `ReActorFaceSwap` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 6 | 8 | 88% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 5 | 100% |
| 高度 | 1024 | 1024 - 1024 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 6，8 个样本，取值集中（一致性 88%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，5 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
