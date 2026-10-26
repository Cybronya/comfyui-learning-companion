---
name: unknown_workflow_sampler_clip_unet_246
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.873
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [comfyui-workflow-templates-json/flux_canny_model_example.json, comfyui-workflow-templates-json/flux_fill_outpaint_example.json, 图片生成/图生图/@flux-fill扩图_1959879943473803266.json, 图片生成/图生图/Flux无缝扩图V2_1955240957747740674.json, 图片生成/文生图/OneReward扩图_1989998999480487937.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_246

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（comfyui-workflow-templates-json/flux_canny_model_example.json、comfyui-workflow-templates-json/flux_fill_outpaint_example.json、图片生成/图生图/@flux-fill扩图_1959879943473803266.json、图片生成/图生图/Flux无缝扩图V2_1955240957747740674.json、图片生成/文生图/OneReward扩图_1989998999480487937.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `ImagePadForOutpaint` —— 4/5 个有
- `InpaintModelConditioning` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `DifferentialDiffusion` —— 3/5 个有
- `MaskToImage` —— 3/5 个有
- `Canny` —— 1/5 个有
- `FeatheredMask` —— 1/5 个有
- `ImageCompositeMasked` —— 1/5 个有
- `ImageConcatMulti` —— 1/5 个有
- `ImageStitch` —— 1/5 个有
- `InstructPixToPixConditioning` —— 1/5 个有
- `LayerMask: MaskPreview` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `SetLatentNoiseMask` —— 1/5 个有
- `easy imageSize` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 5 | 83% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，5 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
