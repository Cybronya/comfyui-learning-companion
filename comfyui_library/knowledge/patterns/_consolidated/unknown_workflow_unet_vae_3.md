---
name: unknown_workflow_unet_vae_3
type: Unknown Workflow
frequency: 19
level: weak
coverage: 0.945842
common_nodes: [ConditioningZeroOut, DualCLIPLoader, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [comfyui-workflow-templates-json/flux_schnell_full_text_to_image.json, 图片生成/图生图/OneReward Fill局部重绘工作流_2068347330910310401.json, 图片生成/图生图/OneReward Fill扩图工作流_2068355013654695937.json, 图片生成/图生图/OneReward_Fill局部重绘、扩图工作流_2038613347419033601.json, 图片生成/图生图/OneReward_Fill局部重绘工作流_2008781795990446082.json, 图片生成/图生图/OneReward_Fill扩图工作流_2008787024437841921.json, 图片生成/图生图/flux-扩图_1977705117887725570.json, 图片生成/图生图/tonnie-flux-fill扩图_1992516908226506754.json, 图片生成/文生图/00.flux生成脸模_许老师专用_1976289488496402434.json, 平台全量/Fill One reward扩图工作流_1966517903581491201.json, 平台全量/Fill-OneReward局部重绘_1965834350589841409.json, 平台全量/Flux 扩展图像流_2081307166522298369.json, 平台全量/Flux-Fill-OneReward扩图_1966404380306157569.json, 平台全量/Flux-Fill-dev_OneReward_扩图-图像边界外扩_1890257481967476738.json, 平台全量/Flux-fill-OneReward局部重绘工作流_2003858175654830082.json, 平台全量/Flux-fill-Oneward超强扩图(原图无损)_1986104126394302465.json, 平台全量/Flux1-OneReward(扩图工作流)_2031262107773181953.json, 平台全量/完美扩图-Flux-OneReward_1989245729254289410.json, 平台全量/扩图   flux.1-onereward-fp8模型_2062721666807058433.json]
source: knowledge_consolidation
---

# unknown_workflow_unet_vae_3

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（comfyui-workflow-templates-json/flux_schnell_full_text_to_image.json、图片生成/图生图/OneReward Fill局部重绘工作流_2068347330910310401.json、图片生成/图生图/OneReward Fill扩图工作流_2068355013654695937.json、图片生成/图生图/OneReward_Fill局部重绘、扩图工作流_2038613347419033601.json、图片生成/图生图/OneReward_Fill局部重绘工作流_2008781795990446082.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 19 个 workflow 都包含：
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `InpaintModelConditioning` —— 17/19 个有
- `LoadImage` —— 17/19 个有
- `KSampler` —— 16/19 个有
- `ImagePadForOutpaint` —— 12/19 个有
- `DifferentialDiffusion` —— 11/19 个有
- `FluxGuidance` —— 11/19 个有
- `CLIPTextEncode` —— 10/19 个有
- `CLIPTextEncodeFlux` —— 9/19 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/19 个有
- `LoraLoaderModelOnly` —— 9/19 个有
- `PreviewImage` —— 9/19 个有
- `Image Comparer (rgthree)` —— 6/19 个有
- `GrowMaskWithBlur` —— 5/19 个有
- `RH_Translator` —— 5/19 个有
- `ImageComposite+` —— 4/19 个有
- `LayerMask: MaskGrow` —— 4/19 个有
- `KSamplerAdvanced` —— 3/19 个有
- `easy clearCacheAll` —— 3/19 个有
- `EmptySD3LatentImage` —— 2/19 个有
- `easy cleanGpuUsed` —— 2/19 个有
- `easy seed` —— 2/19 个有
- `ImageAndMaskPreview` —— 1/19 个有
- `ImagePadForOutpaintMasked` —— 1/19 个有
- `MemoryCleaner` —— 1/19 个有
- `PreviewTextNode` —— 1/19 个有
- `easy ifElse` —— 1/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 27 | 16 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 19 | 0% |
| 采样算法 | euler | - | 19 | 79% |
| 调度器 | simple | - | 19 | 47% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/19 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 27，16 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，19 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，19 个样本，一致性 79%
- 调度器 最常用 simple，19 个样本，一致性 47%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
