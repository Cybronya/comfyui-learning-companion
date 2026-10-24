---
name: unknown_workflow_sampler_clip_unet_359
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.87
common_nodes: [Anything Everywhere, Anything Everywhere3, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, DepthAnythingPreprocessor, DualCLIPLoader, FluxGuidance, InstructPixToPixConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: TextBox, LoadImage, RHHiddenNodes, SaveImage, StyleModelAdvancedApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/服装换材质丨Flux.1 Depth＋Redux丨面料纹理迁移_2100137522218229761.json, 图片生成/图生图/服装换材质丨Flux.1_Depth＋Redux丨面料纹理迁移_2101210273989357570.json, 图片生成/图生图/服装换材质丨Flux.1_Depth＋Redux丨面料纹理迁移_2102210198915076097.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_359

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/服装换材质丨Flux.1 Depth＋Redux丨面料纹理迁移_2100137522218229761.json、图片生成/图生图/服装换材质丨Flux.1_Depth＋Redux丨面料纹理迁移_2101210273989357570.json、图片生成/图生图/服装换材质丨Flux.1_Depth＋Redux丨面料纹理迁移_2102210198915076097.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere`
- `Anything Everywhere3`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DepthAnythingPreprocessor`
- `DualCLIPLoader`
- `FluxGuidance`
- `InstructPixToPixConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: TextBox`
- `LoadImage`
- `RHHiddenNodes`
- `SaveImage`
- `StyleModelAdvancedApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | sgm_uniform | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
