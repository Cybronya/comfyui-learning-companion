---
name: unknown_workflow_lora_sampler_unet_67
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.827444
common_nodes: [CLIPLoader, ImageConcanate, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FireRed Image Edit 1.1单图编辑（效果比qwen强）_2033358154595049474.json, 图片生成/图生图/FireRed Image Edit 1.1多图编辑（效果比qwen强）_2029803829331501058.json, 图片生成/图生图/Qwen Edit 2509，提示词改图_1987504679863169026.json, 图片生成/图生图/Qwen Edit 2509，社区Lora，切换多镜头拍摄_1987508199920177154.json, 图片生成/图生图/Qwen Edit 2509，社区Lora，去掉光影_1987518092307795970.json, 图片生成/图生图/Qwen Edit 2509，社区Lora，重新打光_1987516185564655618.json, 图片生成/图生图/Qwen Edit 2509，社区Lora，预测未来下一帧场景_1987519513975525377.json, 图片生成/图生图/Qwen Edit 2509，社区Lora，高清图像_1987514462464880642.json, 图片生成/图生图/Qwen动漫转真人，动漫仿真人剧必备！_2052317417342291970.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_67

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/FireRed Image Edit 1.1单图编辑（效果比qwen强）_2033358154595049474.json、图片生成/图生图/FireRed Image Edit 1.1多图编辑（效果比qwen强）_2029803829331501058.json、图片生成/图生图/Qwen Edit 2509，提示词改图_1987504679863169026.json、图片生成/图生图/Qwen Edit 2509，社区Lora，切换多镜头拍摄_1987508199920177154.json、图片生成/图生图/Qwen Edit 2509，社区Lora，去掉光影_1987518092307795970.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `ImageConcanate`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 8/9 个有
- `CFGNorm` —— 7/9 个有
- `Image Comparer (rgthree)` —— 7/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/9 个有
- `ModelSamplingAuraFlow` —— 7/9 个有
- `TextEncodeQwenImageEdit_lrzjason` —— 6/9 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 3/9 个有
- `CR Prompt List` —— 2/9 个有
- `CR Text` —— 2/9 个有
- `ImageResize+` —— 2/9 个有
- `Qwen3_VQA` —— 2/9 个有
- `TextInput_` —— 2/9 个有
- `easy showAnything` —— 2/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/9 个有
- `INTConstant` —— 1/9 个有
- `JoinStrings` —— 1/9 个有
- `ReferenceLatent` —— 1/9 个有
- `ShowText|pysssss` —— 1/9 个有
- `Text Concatenate (JPS)` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 9 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler_ancestral | - | 9 | 56% |
| 调度器 | simple | - | 9 | 78% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，9 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，9 个样本，一致性 56%
- 调度器 最常用 simple，9 个样本，一致性 78%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
