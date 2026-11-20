---
name: unknown_workflow_inpaint_sampler_clip_87
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.823333
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), InpaintModelConditioning, KSampler, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/全能改图+精准遮罩+细节重绘_1978468740792733697.json, 图片生成/图生图/啥都能修复，手脚等_1962888178334142466.json, 平台全量/Flux修复万物头手脚等_1941899826034536450.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_87

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/全能改图+精准遮罩+细节重绘_1978468740792733697.json、图片生成/图生图/啥都能修复，手脚等_1962888178334142466.json、平台全量/Flux修复万物头手脚等_1941899826034536450.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 2/3 个有
- `ArgosTranslateTextNode` —— 1/3 个有
- `CR Simple Image Compare` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `LayerMask: MaskPreview` —— 1/3 个有
- `MaskBlur+` —— 1/3 个有
- `MaskFillHoles` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 3 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
