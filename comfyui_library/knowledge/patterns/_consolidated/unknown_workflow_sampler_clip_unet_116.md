---
name: unknown_workflow_sampler_clip_unet_116
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.965
common_nodes: [CLIPTextEncodeFlux, ConditioningZeroOut, DualCLIPLoader, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/flux_schnell_full_text_to_image.json, 图片生成/图生图/OneReward Fill局部重绘工作流_2068347330910310401.json, 图片生成/图生图/OneReward Fill扩图工作流_2068355013654695937.json, 图片生成/图生图/OneReward_Fill局部重绘、扩图工作流_2038613347419033601.json, 图片生成/图生图/OneReward_Fill局部重绘工作流_2008781795990446082.json, 图片生成/图生图/OneReward_Fill扩图工作流_2008787024437841921.json, 图片生成/图生图/flux-扩图_1977705117887725570.json, 图片生成/图生图/tonnie-flux-fill扩图_1992516908226506754.json, 图片生成/文生图/00.flux生成脸模_许老师专用_1976289488496402434.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_116

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（comfyui-workflow-templates-json/flux_schnell_full_text_to_image.json、图片生成/图生图/OneReward Fill局部重绘工作流_2068347330910310401.json、图片生成/图生图/OneReward Fill扩图工作流_2068355013654695937.json、图片生成/图生图/OneReward_Fill局部重绘、扩图工作流_2038613347419033601.json、图片生成/图生图/OneReward_Fill局部重绘工作流_2008781795990446082.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `InpaintModelConditioning` —— 7/9 个有
- `LoadImage` —— 7/9 个有
- `ImagePadForOutpaint` —— 5/9 个有
- `LoraLoaderModelOnly` —— 3/9 个有
- `PreviewImage` —— 3/9 个有
- `EmptySD3LatentImage` —— 2/9 个有
- `RH_Translator` —— 2/9 个有
- `DifferentialDiffusion` —— 1/9 个有
- `FluxGuidance` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 25 | 9 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 78% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 25，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 78%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
