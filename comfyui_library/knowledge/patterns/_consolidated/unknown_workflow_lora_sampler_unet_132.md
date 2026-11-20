---
name: unknown_workflow_lora_sampler_unet_132
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.721
common_nodes: [CLIPLoader, EmptyLatentImage, GetImageSize, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/002.Qwen编辑之王005.服装特征-手动遮罩_2034495312068354049.json, 图片生成/图生图/Qwen_Edit_2511-一键生成LoRA训练数据集_2005194952508407809.json, 图片生成/图生图/Qwen_image_edit2509人物和服装一致性 换装工作流_1992137315663368193.json, 图片生成/图生图/qwen_image_edit_outfit_transfer_1988863663043907586.json, 图片生成/图生图/商用级-换装工作流_1989291892481380354.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_132

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/002.Qwen编辑之王005.服装特征-手动遮罩_2034495312068354049.json、图片生成/图生图/Qwen_Edit_2511-一键生成LoRA训练数据集_2005194952508407809.json、图片生成/图生图/Qwen_image_edit2509人物和服装一致性 换装工作流_1992137315663368193.json、图片生成/图生图/qwen_image_edit_outfit_transfer_1988863663043907586.json、图片生成/图生图/商用级-换装工作流_1989291892481380354.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `EmptyLatentImage`
- `GetImageSize`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `GetNode` —— 4/5 个有
- `ImageScaleToTotalPixels` —— 4/5 个有
- `SetNode` —— 4/5 个有
- `CR Prompt List` —— 1/5 个有
- `ImageScaleBy` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有
- `SeedVR2LoadDiTModel` —— 1/5 个有
- `SeedVR2LoadVAEModel` —— 1/5 个有
- `SeedVR2VideoUpscaler` —— 1/5 个有
- `easy imageConcat` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1024 | 5 | 89% |
| 高度 | 1024 | 768 - 1024 | 5 | 89% |
| 采样步数 | 8 | 6 - 8 | 5 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1024，5 个样本，取值集中（一致性 89%）
- 高度 中位数 1024，观测区间 768 - 1024，5 个样本，取值集中（一致性 89%）
- 采样步数 中位数 8，观测区间 6 - 8，5 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（8/5 个样本）：Steps较低可能导致细节不足
