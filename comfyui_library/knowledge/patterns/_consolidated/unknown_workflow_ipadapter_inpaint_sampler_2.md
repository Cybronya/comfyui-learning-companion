---
name: unknown_workflow_ipadapter_inpaint_sampler_2
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.746
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, DF_Divide, DF_Sum, DF_To_text_(Debug), DifferentialDiffusion, GrowMask, INPAINT_ApplyFooocusInpaint, INPAINT_LoadFooocusInpaint, INPAINT_VAEEncodeInpaintConditioning, IPAdapterAdvanced, IPAdapterNoise, IPAdapterUnifiedLoader, Image Blank, ImagePadForOutpaint, ImageScale, ImageScaleBy, ImageToMask, InvertMask, KSampler, LayerColor: Brightness & Contrast, LayerMask: MaskBoxDetect, LayerMask: MaskPreview, LayerUtility: GetImageSize, LayerUtility: ImageBlend, LayerUtility: ImageScaleRestore V2, LayerUtility: LaMa, LoadImage, MaskBlur+, MaskToImage, Paste By Mask, PreviewImage, RepeatLatentBatch, SplitImageWithAlpha, VAEDecode]
problems: []
missing: []
members: [平台全量/Fooocus 扩图   BY NING_1820104906899369986.json, 平台全量/高级扩图_1822916139117621249.json]
source: knowledge_consolidation
---

# unknown_workflow_ipadapter_inpaint_sampler_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Fooocus 扩图   BY NING_1820104906899369986.json、平台全量/高级扩图_1822916139117621249.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DF_Divide`
- `DF_Sum`
- `DF_To_text_(Debug)`
- `DifferentialDiffusion`
- `GrowMask`
- `INPAINT_ApplyFooocusInpaint`
- `INPAINT_LoadFooocusInpaint`
- `INPAINT_VAEEncodeInpaintConditioning`
- `IPAdapterAdvanced`
- `IPAdapterNoise`
- `IPAdapterUnifiedLoader`
- `Image Blank`
- `ImagePadForOutpaint`
- `ImageScale`
- `ImageScaleBy`
- `ImageToMask`
- `InvertMask`
- `KSampler`
- `LayerColor: Brightness & Contrast`
- `LayerMask: MaskBoxDetect`
- `LayerMask: MaskPreview`
- `LayerUtility: GetImageSize`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageScaleRestore V2`
- `LayerUtility: LaMa`
- `LoadImage`
- `MaskBlur+`
- `MaskToImage`
- `Paste By Mask`
- `PreviewImage`
- `RepeatLatentBatch`
- `SplitImageWithAlpha`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `GetImageSize+` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `GlobalSeed //Inspire` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImpactGaussianBlurMask` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `InspyrenetRembgAdvanced` —— 1/2 个有
- `LayerMask: BiRefNetUltra` —— 1/2 个有
- `LayerUtility: GetColorTone` —— 1/2 个有
- `LayerUtility: TextBox` —— 1/2 个有
- `MaskPreview+` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `easy compare` —— 1/2 个有
- `easy if` —— 1/2 个有
- `easy int` —— 1/2 个有
- `preview_mask` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 5.02 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | karras | - | 2 | 50% |
| 重绘幅度 | 0.865 | - | 2 | 84% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5.02，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 karras，2 个样本，一致性 50%
- 重绘幅度 中位数 0.865，样本不足，未给区间，2 个样本，取值集中（一致性 84%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
