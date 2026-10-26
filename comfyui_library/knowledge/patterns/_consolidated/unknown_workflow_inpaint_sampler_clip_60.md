---
name: unknown_workflow_inpaint_sampler_clip_60
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8395
common_nodes: [CLIPTextEncodeFlux, ConditioningZeroOut, DualCLIPLoader, Fast Groups Bypasser (rgthree), Image Comparer (rgthree), ImagePadForOutpaint, InpaintModelConditioning, KSampler, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux  tools 工具集（重绘）_1985551441249161217.json, 图片生成/图生图/局部修改（局部重绘）+ 扩图 flux tool_1905087419341787138.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_60

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux  tools 工具集（重绘）_1985551441249161217.json、图片生成/图生图/局部修改（局部重绘）+ 扩图 flux tool_1905087419341787138.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `ImagePadForOutpaint`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 1/2 个有
- `DepthAnythingV2Preprocessor` —— 1/2 个有
- `InstructPixToPixConditioning` —— 1/2 个有
- `LineartStandardPreprocessor` —— 1/2 个有
- `LoraLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
