---
name: unknown_workflow_lora_sampler_unet_136
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7878
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-edit-线稿参考生图（转绘）_2080838546805575681.json, 图片生成/图生图/Qwen-图像编辑-产品精修-批量_2082282335566917634.json, 图片生成/图生图/Qwen-图像编辑-产品精修-批量_2082295149513764866.json, 图片生成/图生图/Qwen-电商专用-产品海报图像模仿(洗图)_2082033056369692673.json, 图片生成/图生图/Qwen-编辑图像-模仿产品模特_2082053215369125889.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_136

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen-edit-线稿参考生图（转绘）_2080838546805575681.json、图片生成/图生图/Qwen-图像编辑-产品精修-批量_2082282335566917634.json、图片生成/图生图/Qwen-图像编辑-产品精修-批量_2082295149513764866.json、图片生成/图生图/Qwen-电商专用-产品海报图像模仿(洗图)_2082033056369692673.json、图片生成/图生图/Qwen-编辑图像-模仿产品模特_2082053215369125889.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DF_Text_Box` —— 4/5 个有
- `Image Comparer (rgthree)` —— 4/5 个有
- `ImageUpscaleWithModel` —— 4/5 个有
- `ModelSamplingAuraFlow` —— 4/5 个有
- `UpscaleModelLoader` —— 4/5 个有
- `CR Text` —— 3/5 个有
- `TextEncodeQwenImageEditPlusPro_lrzjason` —— 3/5 个有
- `LayerUtility: LoadImagesFromPath` —— 2/5 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 2/5 个有
- `AILab_QwenVL` —— 1/5 个有
- `CLIPTextEncode` —— 1/5 个有
- `LineArtPreprocessor` —— 1/5 个有
- `OpenposePreprocessor` —— 1/5 个有
- `QwenImageLatentAspectRatio` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 10 | 5 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 0.75 - 1 | 5 | 89% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 10，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.75 - 1，5 个样本，取值集中（一致性 89%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
