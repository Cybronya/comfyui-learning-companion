---
name: unknown_workflow_lora_sampler_unet_51
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.84
common_nodes: [CFGNorm, CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, Text Multiline, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader, easy promptLine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/ComfyUI分镜工作流：多角度多视角一次出完，附全节点注释_2060961151034417153.json, 图片生成/文生图/多角度-生图_2077359821246001153.json, 视频生成/图生视频/2079109724708102146.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_51

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/ComfyUI分镜工作流：多角度多视角一次出完，附全节点注释_2060961151034417153.json、图片生成/文生图/多角度-生图_2077359821246001153.json、视频生成/图生视频/2079109724708102146.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `Text Multiline`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy promptLine`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/3 个有
- `MultiTextConcatenate` —— 1/3 个有
- `ProcessString` —— 1/3 个有
- `SeedVR2LoadDiTModel` —— 1/3 个有
- `SeedVR2LoadVAEModel` —— 1/3 个有
- `SeedVR2VideoUpscaler` —— 1/3 个有
- `easy imageBatchToImageList` —— 1/3 个有
- `easy imageListToImageBatch` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
