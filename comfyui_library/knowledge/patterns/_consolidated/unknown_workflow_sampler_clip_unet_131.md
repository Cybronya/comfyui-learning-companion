---
name: unknown_workflow_sampler_clip_unet_131
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9194
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: ["图片生成/文生图/LLM+Z-Image文生图放大工作流,彻底解放Z-Image_1993901432334123010.json", 图片生成/文生图/Y-Z-Image-turbo-workflow_1995084581466464257.json, 图片生成/文生图/Z-IAMGE 文生图_2042789497263362049.json, "图片生成/文生图/Z-Image+LLM反推洗图工作流,彻底解放_1993900840161312770.json", 图片生成/文生图/Z_image_seedvr2_1993859723476877313.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_131

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/LLM+Z-Image文生图放大工作流,彻底解放Z-Image_1993901432334123010.json、图片生成/文生图/Y-Z-Image-turbo-workflow_1995084581466464257.json、图片生成/文生图/Z-IAMGE 文生图_2042789497263362049.json、图片生成/文生图/Z-Image+LLM反推洗图工作流,彻底解放_1993900840161312770.json、图片生成/文生图/Z_image_seedvr2_1993859723476877313.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `ModelSamplingAuraFlow` —— 4/5 个有
- `PreviewAny` —— 3/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `LoadImage` —— 2/5 个有
- `SeedVR2BlockSwap` —— 2/5 个有
- `AILab_QwenVL` —— 1/5 个有
- `LoadLoraOnly` —— 1/5 个有
- `Qwen3_VQA` —— 1/5 个有
- `RH_LLMAPI_NODE` —— 1/5 个有
- `SeedVR2` —— 1/5 个有
- `SeedVR2ExtraArgs` —— 1/5 个有
- `SeedVR2GGUF` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 9 | 5 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | res_multistep | - | 5 | 60% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 9，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
