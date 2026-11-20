---
name: unknown_workflow_sampler_clip_unet_399
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.863667
common_nodes: [CLIPTextEncodeFlux, ConditioningZeroOut, DualCLIPLoader, Image Comparer (rgthree), InstructPixToPixConditioning, KSampler, LoadImage, PreviewImage, RH_Translator, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux室内装修风格换装_1977731719371575297.json, 图片生成/图生图/Flux室内装修风格换装_1977738312892960769.json, 平台全量/室内装修风格换装 - Flux_1991901552944410625.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_399

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux室内装修风格换装_1977731719371575297.json、图片生成/图生图/Flux室内装修风格换装_1977738312892960769.json、平台全量/室内装修风格换装 - Flux_1991901552944410625.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Image Comparer (rgthree)`
- `InstructPixToPixConditioning`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `RH_Translator`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DepthAnythingV2Preprocessor` —— 2/3 个有
- `LoraLoader` —— 2/3 个有
- `LineArtPreprocessor` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 0.9 - 1 | 3 | 95% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 0.91 | - | 2 | 90% |
| LoRA 文本强度 | 1.04 | - | 2 | 96% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 0.9 - 1，3 个样本，取值集中（一致性 95%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.91，样本不足，未给区间，2 个样本，取值集中（一致性 90%）
- LoRA 文本强度 中位数 1.04，样本不足，未给区间，2 个样本，取值集中（一致性 96%）
- 风险：Prompt 约束强度(CFG) 观测到 0.9，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
