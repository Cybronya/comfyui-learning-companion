---
name: unknown_workflow_sampler_clip_unet_84
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.785667
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, InstructPixToPixConditioning, KSampler, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [CR Latent Batch Size, CR Prompt Text, Zoe-DepthMapPreprocessor]
members: [图片生成/文生图/1965644174517223426.json, 图片生成/文生图/1988873413324312577.json, 图片生成/文生图/1988875432810393601.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_84

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1965644174517223426.json、图片生成/文生图/1988873413324312577.json、图片生成/文生图/1988875432810393601.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `InstructPixToPixConditioning`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncodeFlux` —— 2/3 个有
- `CR Latent Batch Size` —— 2/3 个有
- `CR Prompt Text` —— 2/3 个有
- `LoraLoader` —— 2/3 个有
- `Zoe-DepthMapPreprocessor` —— 2/3 个有
- `Canny` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 20 - 30 | 3 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 20 - 30，3 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Latent Batch Size、CR Prompt Text、Zoe-DepthMapPreprocessor
