---
name: unknown_workflow_lora_sampler_unet_146
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9028
common_nodes: [CLIPLoader, EmptyLatentImage, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Edit图像编辑_1958194156185272321.json, 图片生成/图生图/小红书FireRed-Image-edit1.1双图编辑_2033156894868639745.json, 图片生成/图生图/小红书人物换装 双图编辑_2034550287024791553.json, 图片生成/图生图/小红书人物换装+局部变大+双图编辑_2034677242252496898.json, 图片生成/图生图/超好用🔥人物一键换装-双图编辑_2063984968640061441.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_146

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit图像编辑_1958194156185272321.json、图片生成/图生图/小红书FireRed-Image-edit1.1双图编辑_2033156894868639745.json、图片生成/图生图/小红书人物换装 双图编辑_2034550287024791553.json、图片生成/图生图/小红书人物换装+局部变大+双图编辑_2034677242252496898.json、图片生成/图生图/超好用🔥人物一键换装-双图编辑_2063984968640061441.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 4/5 个有
- `CR Prompt Text` —— 4/5 个有
- `TextEncodeQwenImageEditPlus` —— 4/5 个有
- `Anything Everywhere` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `Text` —— 1/5 个有
- `TextEncodeQwenImageEdit` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1024 | 5 | 78% |
| 高度 | 1536 | 512 - 1536 | 5 | 69% |
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1024，5 个样本
- 高度 中位数 1536，观测区间 512 - 1536，5 个样本
- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
