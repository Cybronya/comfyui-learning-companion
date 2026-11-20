---
name: unknown_workflow_sampler_clip_unet_402
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.891
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Int, KSamplerAdvanced, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: []
missing: []
members: [图片生成/图生图/Krea2-风格迁移_2075792357995405314.json, 图片生成/文生图/Zimage Base+turbo双采样工作流_2074842071952875522.json, 图片生成/文生图/anima双采样工作流_2063507441417019394.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_402

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Krea2-风格迁移_2075792357995405314.json、图片生成/文生图/Zimage Base+turbo双采样工作流_2074842071952875522.json、图片生成/文生图/anima双采样工作流_2063507441417019394.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Int`
- `KSamplerAdvanced`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `Text Multiline` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `llama_cpp_parameters` —— 2/3 个有
- `ComfyMathExpression` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `PreviewAny` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `ResolutionSelector` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 960 - 1080 | 3 | 95% |
| 高度 | 1536 | 1440 - 1920 | 3 | 87% |
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 20 | 3 | 8% |
| 采样算法 | 1 | 1 - 2 | 3 | 65% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 960 - 1080，3 个样本，取值集中（一致性 95%）
- 高度 中位数 1536，观测区间 1440 - 1920，3 个样本，取值集中（一致性 87%）
- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 20，3 个样本，取值分散，一致性仅 8%
- 采样算法 中位数 1，观测区间 1 - 2，3 个样本
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
