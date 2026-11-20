---
name: unknown_workflow_lora_sampler_unet_127
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.632167
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen 2509 写实转动漫-八步生图-娱乐向_1990960188683399169.json, 图片生成/图生图/Qwen-edit-2511高清放大工作流_2006259489204346882.json, 图片生成/图生图/qwen-image-edit 工作流_1960293162407309313.json, 图片生成/图生图/qwen-image-edit编辑图片_1962516845456670721.json, 图片生成/图生图/qwen-提取人物衣物服饰_2044977240127049729.json, 平台全量/qwen-image-edit 工作流_1957689069872541698.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_127

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen 2509 写实转动漫-八步生图-娱乐向_1990960188683399169.json、图片生成/图生图/Qwen-edit-2511高清放大工作流_2006259489204346882.json、图片生成/图生图/qwen-image-edit 工作流_1960293162407309313.json、图片生成/图生图/qwen-image-edit编辑图片_1962516845456670721.json、图片生成/图生图/qwen-提取人物衣物服饰_2044977240127049729.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 5/6 个有
- `SetNode` —— 5/6 个有
- `CLIPTextEncode` —— 4/6 个有
- `EmptySD3LatentImage` —— 4/6 个有
- `FluxKontextImageScale` —— 4/6 个有
- `GetImageSize` —— 4/6 个有
- `Image Comparer (rgthree)` —— 3/6 个有
- `TextEncodeQwenImageEdit` —— 3/6 个有
- `CFGNorm` —— 2/6 个有
- `ConditioningZeroOut` —— 2/6 个有
- `TextEncodeQwenImageEditPlusPro_lrzjason` —— 2/6 个有
- `TextEncodeQwenImageEditPlus` —— 1/6 个有
- `easy imageConcat` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 25 | 6 | 25% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 25，6 个样本，取值分散，一致性仅 25%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
