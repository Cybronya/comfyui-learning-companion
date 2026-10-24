---
name: unknown_workflow_inpaint_upscale_sampler_2
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.876692
common_nodes: [CLIPTextEncodeFlux, ConditioningZeroOut, DualCLIPLoader, Florence2ModelLoader, Florence2Run, GetImageSize, Image Comparer (rgthree), ImagePadForOutpaint, ImageScale, ImageScaleToTotalPixelsX, ImageUpscaleWithModel, InpaintModelConditioning, KSampler, LayerMask: MaskGrow, LayerUtility: ImageBlend, LayerUtility: ImageMaskScaleAsV2, LoadImage, PreviewImage, SaveImage, Seed (rgthree), SimpleMath+, SimpleMathFloat+, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux-fill-dev-OneReward-扩图-按比例_2002986774337056769.json, 图片生成/图生图/flux-fill-dev-OneReward-扩图-按比例_2082040121574117378.json, 图片生成/图生图/flux-fill-dev-OneReward-扩图-按比例_2084529890614931457.json, 图片生成/图生图/flux-fill-dev-OneReward-扩图-按比例_2084840467795103746.json, 图片生成/图生图/flux-fill-dev-OneReward-扩图-按比例_2084902178304647170.json, 图片生成/图生图/flux-fill-dev-OneReward-扩图-按比例_2096052561496338434.json, 图片生成/图生图/flux-fill-dev-OneReward-扩图-按比例_2096163204056567809.json, 图片生成/图生图/flux-fill-dev-OneReward-扩图-按比例_2096513544480186369.json, 图片生成/图生图/flux-fill-dev-OneReward-扩图-按比例_2096871274583777281.json, 图片生成/图生图/flux-fill-dev-OneReward-扩图-按比例_2111071227153571842.json, 图片生成/图生图/随意阔图--自定义比例尺寸_2067151199186538498.json, 图片生成/图生图/随意阔图自定义比例尺寸智能扩图外扩工作流_2083005303968321538.json, 图片生成/图生图/随意阔图自定义比例尺寸智能扩图外扩工作流_2083022185874157569.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_upscale_sampler_2

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/flux-fill-dev-OneReward-扩图-按比例_2002986774337056769.json、图片生成/图生图/flux-fill-dev-OneReward-扩图-按比例_2082040121574117378.json、图片生成/图生图/flux-fill-dev-OneReward-扩图-按比例_2084529890614931457.json、图片生成/图生图/flux-fill-dev-OneReward-扩图-按比例_2084840467795103746.json、图片生成/图生图/flux-fill-dev-OneReward-扩图-按比例_2084902178304647170.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Florence2ModelLoader`
- `Florence2Run`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImagePadForOutpaint`
- `ImageScale`
- `ImageScaleToTotalPixelsX`
- `ImageUpscaleWithModel`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageMaskScaleAsV2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `Seed (rgthree)`
- `SimpleMath+`
- `SimpleMathFloat+`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 10/13 个有
- `SeedVR2LoadDiTModel` —— 10/13 个有
- `SeedVR2LoadVAEModel` —— 10/13 个有
- `SeedVR2VideoUpscaler` —— 10/13 个有
- `easy imageSizeBySide` —— 10/13 个有
- `DifferentialDiffusion` —— 2/13 个有
- `ImageConcanate` —— 2/13 个有
- `ImageResize+` —— 2/13 个有
- `KOOK_SaveJPGImage` —— 2/13 个有
- `TeaCache` —— 2/13 个有
- `LoraLoaderModelOnly` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 13 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | res_multistep | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
