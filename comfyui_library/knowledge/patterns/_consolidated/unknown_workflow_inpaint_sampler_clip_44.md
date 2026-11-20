---
name: unknown_workflow_inpaint_sampler_clip_44
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9336
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux批量扩图-单张测试效果图_1920707002874396674.json, 图片生成/图生图/一键全自动快速扩图_1902348821412884481.json, 图片生成/图生图/自己用：FLUX FILL扩图_1944756810748448769.json, 图片生成/图生图/超强无缝图像扩展_1891041648606875650.json, 平台全量/电商丨flux生成场景模特，生成人物逼真_1896503390103011329.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_44

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/flux批量扩图-单张测试效果图_1920707002874396674.json、图片生成/图生图/一键全自动快速扩图_1902348821412884481.json、图片生成/图生图/自己用：FLUX FILL扩图_1944756810748448769.json、图片生成/图生图/超强无缝图像扩展_1891041648606875650.json、平台全量/电商丨flux生成场景模特，生成人物逼真_1896503390103011329.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImagePadForOutpaint` —— 3/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `INTConstant` —— 1/5 个有
- `ImagePadForOutpaintTargetSize` —— 1/5 个有
- `ImageResizeKJ` —— 1/5 个有
- `Lora Loader Stack (rgthree)` —— 1/5 个有
- `Note _O` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `TeaCache` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 5 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 5 | 33% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，5 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
