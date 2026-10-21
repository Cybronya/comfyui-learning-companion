---
name: unknown_workflow_lora_clip_unet_9
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.909
common_nodes: [CLIPTextEncodeFlux, DualCLIPLoader, EmptyLatentImage, LoraLoader, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [FluxSamplerParams+]
members: [图片生成/文生图/1988984318296985601.json, 图片生成/文生图/【汽水】Flux基础文生图工作流_1894635344313122817.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_clip_unet_9

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1988984318296985601.json、图片生成/文生图/【汽水】Flux基础文生图工作流_1894635344313122817.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `LoraLoader`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 1/2 个有
- `FluxSamplerParams+` —— 1/2 个有
- `KSampler //Inspire` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `easy positive` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.85 | - | 2 | 94% |
| LoRA 文本强度 | 0.85 | - | 2 | 82% |
| 宽度 | 1016 | - | 2 | 82% |
| 高度 | 1476 | - | 2 | 92% |
| 采样步数 | 30 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | beta | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.85，样本不足，未给区间，2 个样本，取值集中（一致性 94%）
- LoRA 文本强度 中位数 0.85，样本不足，未给区间，2 个样本，取值集中（一致性 82%）
- 宽度 中位数 1016，样本不足，未给区间，2 个样本，取值集中（一致性 82%）
- 高度 中位数 1476，样本不足，未给区间，2 个样本，取值集中（一致性 92%）
- 这些节点还没有知识卡，系统对它们的理解有限：FluxSamplerParams+
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
