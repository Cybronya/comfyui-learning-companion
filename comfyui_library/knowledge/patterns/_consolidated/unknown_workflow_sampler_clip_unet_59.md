---
name: unknown_workflow_sampler_clip_unet_59
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.88125
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2]
members: [comfyui-workflow-templates-json/flux_canny_model_example.json, comfyui-workflow-templates-json/flux_fill_outpaint_example.json, 图片生成/图生图/2040689200806236162.json, 图片生成/文生图/1965638484138577921.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_59

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（comfyui-workflow-templates-json/flux_canny_model_example.json、comfyui-workflow-templates-json/flux_fill_outpaint_example.json、图片生成/图生图/2040689200806236162.json、图片生成/文生图/1965638484138577921.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
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
- `PreviewImage` —— 3/4 个有
- `Canny` —— 2/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `DifferentialDiffusion` —— 2/4 个有
- `InpaintModelConditioning` —— 2/4 个有
- `InstructPixToPixConditioning` —— 2/4 个有
- `ImagePadForOutpaint` —— 1/4 个有
- `Int` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `LoraLoader` —— 1/4 个有
- `RepeatLatentBatch` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 4 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，4 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2
