---
name: unknown_workflow_upscale_sampler_clip_53
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.814
common_nodes: [CLIPLoader, CLIPTextEncode, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), KSampler, ModelSamplingAuraFlow, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1-ZimageTubro-文生图-V1-提示词自动优化-RH_2079445104896598017.json, 图片生成/文生图/ainmap3反推画风选择放大_2044263221657341953.json, 图片生成/文生图/bangdream_mygo_2046920939073445889.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_53

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1-ZimageTubro-文生图-V1-提示词自动优化-RH_2079445104896598017.json、图片生成/文生图/ainmap3反推画风选择放大_2044263221657341953.json、图片生成/文生图/bangdream_mygo_2046920939073445889.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `SDXLEmptyLatentSizePicker+` —— 1/3 个有
- `Seed Everywhere` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `easy saveText` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | 9 - 28 | 3 | 59% |
| Prompt 约束强度(CFG) | 5 | 1 - 5 | 3 | 49% |
| 采样算法 | dpmpp_2m | - | 3 | 67% |
| 调度器 | sgm_uniform | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1024x1024 (1.0) | - | 1 | 100% |
| 高度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 28，观测区间 9 - 28，3 个样本
- Prompt 约束强度(CFG) 中位数 5，观测区间 1 - 5，3 个样本，取值分散，一致性仅 49%
- 采样算法 最常用 dpmpp_2m，3 个样本，一致性 67%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
