---
name: unknown_workflow_lora_sampler_unet_171
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.9195
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-Edit+2511溶图工作流_2008110992273707010.json, 图片生成/图生图/Qwen-Image-Edit-2511图片编辑支持三图_2004904581299666946.json, 图片生成/图生图/Qwen-Next Scene 镜头多角度_1990042046666862593.json, 图片生成/图生图/next scene V2自动分镜生成_1983507892202610689.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_171

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Edit+2511溶图工作流_2008110992273707010.json、图片生成/图生图/Qwen-Image-Edit-2511图片编辑支持三图_2004904581299666946.json、图片生成/图生图/Qwen-Next Scene 镜头多角度_1990042046666862593.json、图片生成/图生图/next scene V2自动分镜生成_1983507892202610689.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
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
- `ConditioningZeroOut` —— 3/4 个有
- `EmptySD3LatentImage` —— 3/4 个有
- `TextEncodeQwenImageEditPlus` —— 3/4 个有
- `FluxKontextMultiReferenceLatentMethod` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `easy promptLine` —— 2/4 个有
- `ImageStitch` —— 1/4 个有
- `Int` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `ProcessString` —— 1/4 个有
- `Qwen2.5VL` —— 1/4 个有
- `Text Concatenate` —— 1/4 个有
- `TextEncodeQwenImageEditPlusPro_lrzjason` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 4 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
