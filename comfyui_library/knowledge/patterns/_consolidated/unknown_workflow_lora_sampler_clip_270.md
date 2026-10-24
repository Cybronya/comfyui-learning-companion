---
name: unknown_workflow_lora_sampler_clip_270
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.938
common_nodes: [CLIPTextEncode, CLIPTextEncodeFlux, CR Latent Batch Size, CR Prompt Text, DualCLIPLoader, FluxGuidance, InstructPixToPixConditioning, KSampler, LoadImage, LoraLoader, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader, Zoe-DepthMapPreprocessor]
problems: []
missing: []
members: [图片生成/文生图/FLUX Depth深度控制工作流_1965644174517223426.json, 图片生成/文生图/flux文生图+depth工作流_1988875432810393601.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_270

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/FLUX Depth深度控制工作流_1965644174517223426.json、图片生成/文生图/flux文生图+depth工作流_1988875432810393601.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPTextEncodeFlux`
- `CR Latent Batch Size`
- `CR Prompt Text`
- `DualCLIPLoader`
- `FluxGuidance`
- `InstructPixToPixConditioning`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `Zoe-DepthMapPreprocessor`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
