---
name: unknown_workflow_video_sampler_vae_182
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6375
common_nodes: [AIO_Preprocessor, CR Color Panel, CR Image Input Switch, DWPreprocessor, EsesImageEffectLevels, Float, GetImageRangeFromBatch, GetNode, INTConstant, ImageBatchMulti, ImageBlend, ImageCompositeMasked, ImageFromBatch, ImageResizeKJv2, InspyrenetRembg, Label (rgthree), LayerMask: MaskGrow, LayerUtility: ImageBlendAdvance, LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoT5TextEncoder, MaskPreview+, MaskToImage, MathExpression|pysssss, PreviewImage, RHHiddenNodes, RH_Captioner, SetNode, Switch image [Crystools], Text Multiline, VHS_GetImageCount, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddStandInLatent, WanVideoDecode, WanVideoEncode, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEStartToEndFrame, WanVideoVAELoader, easy cleanGpuUsed, easy forLoopEnd, easy forLoopStart, easy seed, easy showAnything]
problems: []
missing: []
members: [数字人/数字人/视频换人 动作迁移 人物替换  重大升级_1980645672854704129.json, 视频生成/图生视频/人物替换背景（提示词）浮云_1993626350875590658.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_182

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/视频换人 动作迁移 人物替换  重大升级_1980645672854704129.json、视频生成/图生视频/人物替换背景（提示词）浮云_1993626350875590658.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CR Color Panel`
- `CR Image Input Switch`
- `DWPreprocessor`
- `EsesImageEffectLevels`
- `Float`
- `GetImageRangeFromBatch`
- `GetNode`
- `INTConstant`
- `ImageBatchMulti`
- `ImageBlend`
- `ImageCompositeMasked`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `InspyrenetRembg`
- `Label (rgthree)`
- `LayerMask: MaskGrow`
- `LayerUtility: ImageBlendAdvance`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MaskPreview+`
- `MaskToImage`
- `MathExpression|pysssss`
- `PreviewImage`
- `RHHiddenNodes`
- `RH_Captioner`
- `SetNode`
- `Switch image [Crystools]`
- `Text Multiline`
- `VHS_GetImageCount`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddStandInLatent`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `InvertMask` —— 1/2 个有
- `LayerMask: PersonMaskUltra V2` —— 1/2 个有
- `RMBG` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
