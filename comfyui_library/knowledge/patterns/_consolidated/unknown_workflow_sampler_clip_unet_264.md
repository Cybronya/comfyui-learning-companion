---
name: unknown_workflow_sampler_clip_unet_264
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.875667
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ConditioningZeroOut, DepthAnythingPreprocessor, DualCLIPLoader, FluxGuidance, InstructPixToPixConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/服装换材质丨Flux.1 Depth＋Redux丨面料纹理迁移_2100137522218229761.json, 图片生成/图生图/服装换材质丨Flux.1_Depth＋Redux丨面料纹理迁移_2101210273989357570.json, 图片生成/图生图/服装换材质丨Flux.1_Depth＋Redux丨面料纹理迁移_2102210198915076097.json, 平台全量/Flux 任意材质转移 depth_1864218750022254594.json, 平台全量/一键换装材质版_1863906465076674562.json, 平台全量/风格转绘FLUX_1863872323550920705.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_264

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/服装换材质丨Flux.1 Depth＋Redux丨面料纹理迁移_2100137522218229761.json、图片生成/图生图/服装换材质丨Flux.1_Depth＋Redux丨面料纹理迁移_2101210273989357570.json、图片生成/图生图/服装换材质丨Flux.1_Depth＋Redux丨面料纹理迁移_2102210198915076097.json、平台全量/Flux 任意材质转移 depth_1864218750022254594.json、平台全量/一键换装材质版_1863906465076674562.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
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
- `LoadImage`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: TextBox` —— 5/6 个有
- `StyleModelAdvancedApply` —— 5/6 个有
- `Anything Everywhere` —— 4/6 个有
- `Anything Everywhere3` —— 4/6 个有
- `RHHiddenNodes` —— 4/6 个有
- `PreviewImage` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `Note _O` —— 1/6 个有
- `StyleAdvancedApply` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | sgm_uniform | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
