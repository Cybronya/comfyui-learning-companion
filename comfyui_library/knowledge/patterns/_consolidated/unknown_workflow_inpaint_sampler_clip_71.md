---
name: unknown_workflow_inpaint_sampler_clip_71
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.9025
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/CG迷-一涂一抹 人物、物件移除工作流_1927723164393193473.json, 平台全量/HandFixer一键手部修复_1890392199497175042.json, 平台全量/flux蒙版重绘_1962127220275920898.json, 平台全量/全能移除物体和增加物体_1929016268064505858.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_71

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/CG迷-一涂一抹 人物、物件移除工作流_1927723164393193473.json、平台全量/HandFixer一键手部修复_1890392199497175042.json、平台全量/flux蒙版重绘_1962127220275920898.json、平台全量/全能移除物体和增加物体_1929016268064505858.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GrowMask` —— 2/4 个有
- `ImageCompositeMasked` —— 2/4 个有
- `ImpactGaussianBlurMask` —— 2/4 个有
- `LayerMask: MaskPreview` —— 2/4 个有
- `LoraLoader` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `ImageResizeKJ` —— 1/4 个有
- `MediapipeHandNode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 采样步数 | 16 | 12 - 30 | 4 | 60% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 16，观测区间 12 - 30，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
