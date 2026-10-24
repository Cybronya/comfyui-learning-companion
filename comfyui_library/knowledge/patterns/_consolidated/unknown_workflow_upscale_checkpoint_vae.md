---
name: unknown_workflow_upscale_checkpoint_vae
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.632
common_nodes: [BlockifyMask, CLIPLoader, CheckpointLoaderSimple, ConditioningZeroOut, DWPreprocessor, Fast Groups Bypasser (rgthree), GetNode, INTConstant, Image Comparer (rgthree), ImageFromBatch, ImageScaleToTotalPixels, LayerUtility: CropByMask V2, LayerUtility: ImageBlend, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: RestoreCropBox, LoadImage, MaskToImage, PreviewImage, QwenEditConfigPreparer, RMBG, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, TextEncodeQwenImageEditPlusCustom_lrzjason, VAEDecode, VHS_LoadVideoPath, easy convertAnything, easy framesEditor, easy imageSizeBySide, easy positive, easy promptReplace, easy sam3ImageSegmentation, easy sam3ModelLoader]
problems: []
missing: []
members: [图片生成/图生图/QwenAIO编辑-人物替换V1_2031353512512200705.json, 图片生成/图生图/QwenAIO编辑-人物替换V2_2039166020341997569.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_checkpoint_vae

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/QwenAIO编辑-人物替换V1_2031353512512200705.json、图片生成/图生图/QwenAIO编辑-人物替换V2_2039166020341997569.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：63%

## 共有节点

全部 2 个 workflow 都包含：
- `BlockifyMask`
- `CLIPLoader`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `DWPreprocessor`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `INTConstant`
- `Image Comparer (rgthree)`
- `ImageFromBatch`
- `ImageScaleToTotalPixels`
- `LayerUtility: CropByMask V2`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `QwenEditConfigPreparer`
- `RMBG`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `VAEDecode`
- `VHS_LoadVideoPath`
- `easy convertAnything`
- `easy framesEditor`
- `easy imageSizeBySide`
- `easy positive`
- `easy promptReplace`
- `easy sam3ImageSegmentation`
- `easy sam3ModelLoader`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 1/2 个有
- `CFGNorm` —— 1/2 个有
- `Flux2Scheduler` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `KSampler` —— 1/2 个有
- `KSamplerSelect` —— 1/2 个有
- `ModelPatchTorchSettings` —— 1/2 个有
- `PathchSageAttentionKJ` —— 1/2 个有
- `RandomNoise` —— 1/2 个有
- `SamplerCustomAdvanced` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | lcm | - | 1 | 100% |
| 调度器 | normal | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
