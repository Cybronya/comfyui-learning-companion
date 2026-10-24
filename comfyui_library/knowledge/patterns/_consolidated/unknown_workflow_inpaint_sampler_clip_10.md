---
name: unknown_workflow_inpaint_sampler_clip_10
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.818
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/F1 FILL局部重绘260815_2088532375281160193.json, 图片生成/图生图/F1 FILL扩图260815_2088550017731743745.json, 图片生成/图生图/FLUX Fill 局部重绘工作流_2087433093295730690.json, 图片生成/图生图/FLUX扩图_2106382999725105153.json, 图片生成/图生图/FLUX超强无缝图像扩展_1942168738030579714.json, 图片生成/图生图/Flux Fill dev  扩图 - 增强版_1979620328458588161.json, 图片生成/图生图/Flux Fill 局部重绘工作流_1969746265812705281.json, 图片生成/图生图/Flux Fill 扩图工作流_1969741377540157441.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_10

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/F1 FILL局部重绘260815_2088532375281160193.json、图片生成/图生图/F1 FILL扩图260815_2088550017731743745.json、图片生成/图生图/FLUX Fill 局部重绘工作流_2087433093295730690.json、图片生成/图生图/FLUX扩图_2106382999725105153.json、图片生成/图生图/FLUX超强无缝图像扩展_1942168738030579714.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 8 个 workflow 都包含：
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
- `Image Comparer (rgthree)` —— 7/8 个有
- `Anything Everywhere` —— 5/8 个有
- `ImagePadForOutpaint` —— 5/8 个有
- `JWImageResizeByLongerSide` —— 5/8 个有
- `PreviewImage` —— 4/8 个有
- `ImageToMask` —— 2/8 个有
- `MaskToImage` —— 2/8 个有
- `ConditioningZeroOut` —— 1/8 个有
- `ImageResizeKJ` —— 1/8 个有
- `LatentUpscale` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `RH_Captioner` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | dpmpp_2m | - | 8 | 62% |
| 调度器 | sgm_uniform | - | 8 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，8 个样本，一致性 62%
- 调度器 最常用 sgm_uniform，8 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
