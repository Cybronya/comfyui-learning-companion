---
name: unknown_workflow_sampler_clip_unet_352
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.969
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, InstructPixToPixConditioning, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/FLUX Depth深度控制工作流_1965644174517223426.json, 图片生成/文生图/flux文生图+depth工作流_1988875432810393601.json, 平台全量/ComfyUI官方示例14：Flux.1 Canny工作流_ComfyUI从入门到精通_1932795013279748097.json, 平台全量/ComfyUI官方示例15：Flux.1 Depth工作流 _ ComfyUI从入门到精通_1932799950428196865.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_352

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/FLUX Depth深度控制工作流_1965644174517223426.json、图片生成/文生图/flux文生图+depth工作流_1988875432810393601.json、平台全量/ComfyUI官方示例14：Flux.1 Canny工作流_ComfyUI从入门到精通_1932795013279748097.json、平台全量/ComfyUI官方示例15：Flux.1 Depth工作流 _ ComfyUI从入门到精通_1932799950428196865.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `InstructPixToPixConditioning`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncodeFlux` —— 2/4 个有
- `CR Latent Batch Size` —— 2/4 个有
- `CR Prompt Text` —— 2/4 个有
- `LoraLoader` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `Zoe-DepthMapPreprocessor` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 30 | 4 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 30，4 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
