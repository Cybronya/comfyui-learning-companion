---
name: unknown_workflow_controlnet_ipadapter_video
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.922
common_nodes: [ADE_LoopedUniformContextOptions, Apply ControlNet Stack, ColorModEdges, ColorModPivot, Control Net Stacker, ControlNetLoaderAdvanced, Efficient Loader, EmptyLatentImage, IPAdapterAdvanced, IPAdapterUnifiedLoader, ImageScale, ImageScaleBy, ImageToMask, ImageUpscaleWithModel, KSampler (Efficient), LoadImage, PreviewImage, RIFE VFI, UpscaleModelLoader, VAEEncode, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1812675194140942337.json, 视频生成/文生视频/1951651903946084353.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_ipadapter_video

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1812675194140942337.json、视频生成/文生视频/1951651903946084353.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `ADE_LoopedUniformContextOptions`
- `Apply ControlNet Stack`
- `ColorModEdges`
- `ColorModPivot`
- `Control Net Stacker`
- `ControlNetLoaderAdvanced`
- `Efficient Loader`
- `EmptyLatentImage`
- `IPAdapterAdvanced`
- `IPAdapterUnifiedLoader`
- `ImageScale`
- `ImageScaleBy`
- `ImageToMask`
- `ImageUpscaleWithModel`
- `KSampler (Efficient)`
- `LoadImage`
- `PreviewImage`
- `RIFE VFI`
- `UpscaleModelLoader`
- `VAEEncode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ADE_AnimateDiffLoRALoader` —— 1/2 个有
- `ADE_AnimateDiffLoaderWithContext` —— 1/2 个有
- `ADE_AnimateDiffSamplingSettings` —— 1/2 个有
- `ADE_ApplyAnimateDiffModelSimple` —— 1/2 个有
- `ADE_LoadAnimateDiffModel` —— 1/2 个有
- `ADE_MultivalDynamic` —— 1/2 个有
- `ADE_UseEvolvedSampling` —— 1/2 个有
- `BRIA_RMBG_ModelLoader_Zho` —— 1/2 个有
- `BRIA_RMBG_Zho` —— 1/2 个有
- `Images to RGB` —— 1/2 个有
- `InvertMask` —— 1/2 个有
- `LineArtPreprocessor` —— 1/2 个有
- `Zoe-DepthMapPreprocessor` —— 1/2 个有
- `preview_mask` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1.25 | - | 2 | 80% |
| 采样算法 | lcm | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 0.75 | - | 2 | 67% |
| 宽度 | 288 | - | 2 | 100% |
| 高度 | 512 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1.25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- 采样算法 最常用 lcm，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 0.75，样本不足，未给区间，2 个样本
- 宽度 中位数 288，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 512，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
