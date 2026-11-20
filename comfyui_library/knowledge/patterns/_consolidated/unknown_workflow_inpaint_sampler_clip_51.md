---
name: unknown_workflow_inpaint_sampler_clip_51
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8678
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, Image Comparer (rgthree), InpaintModelConditioning, KSampler, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/无痕去水印_自动精准定位与智能修补_2055111697836322818.json, 图片生成/图生图/无痕去水印_自动精准定位与智能修补_2055462741342736386.json, 平台全量/Flux局部重绘去除指定水印工作流_2019656808087949313.json, 平台全量/无痕去水印：自动精准定位与智能修补_2042845361303195650.json, 平台全量/自动修手工作流_1930533437222866946.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_51

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/无痕去水印_自动精准定位与智能修补_2055111697836322818.json、图片生成/图生图/无痕去水印_自动精准定位与智能修补_2055462741342736386.json、平台全量/Flux局部重绘去除指定水印工作流_2019656808087949313.json、平台全量/无痕去水印：自动精准定位与智能修补_2042845361303195650.json、平台全量/自动修手工作流_1930533437222866946.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
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
- `GrowMask` —— 4/5 个有
- `CheckpointLoaderSimple` —— 3/5 个有
- `ConditioningZeroOut` —— 3/5 个有
- `DrawMaskOnImage` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `SAM3_Detect` —— 3/5 个有
- `TextInput_` —— 2/5 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/5 个有
- `MaskToImage` —— 1/5 个有
- `preview_mask` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 5 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | normal | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，5 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 normal，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
