---
name: unknown_workflow_video_lora_sampler_292
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.5231
common_nodes: [BasicScheduler, BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, ColorTransfer, ComfyMathExpression, DiffusionModelLoaderKJ, GetImageRangeFromBatch, GetImageSize, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewAny, PrimitiveInt, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, TensorLoopClose, TensorLoopOpen, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/pipi-SCAIL2-动作迁移 不限时长 （国内版）_2068457565150867458.json, 视频生成/图生视频/pipi-SCAIL2-动作迁移 不限时长 （国内版）_2072184154577530881.json, 视频生成/图生视频/scail2双人异步动作迁移_2065350812397817858.json, 视频生成/图生视频/scail2双人异步动作迁移_2065428476076843010.json, 视频生成/图生视频/scail2双人替换_2065454404580495362.json, 视频生成/图生视频/scail2大模型sam抠人像动作迁移长视频动作迁移舞蹈复刻性感网红扭臀复刻动作复制快速版_2092834091065503746.json, 视频生成/图生视频/scail2带货视频 电商带货，人货互动_2067282833252634625.json, 视频生成/图生视频/scail2替换指定角色_2065428027999342594.json, 视频生成/图生视频/scial版本后裔摇_2069813471377711106.json, 视频生成/图生视频/两张单人图组合双人互动_2068714620197625858.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_292

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/pipi-SCAIL2-动作迁移 不限时长 （国内版）_2068457565150867458.json、视频生成/图生视频/pipi-SCAIL2-动作迁移 不限时长 （国内版）_2072184154577530881.json、视频生成/图生视频/scail2双人异步动作迁移_2065350812397817858.json、视频生成/图生视频/scail2双人异步动作迁移_2065428476076843010.json、视频生成/图生视频/scail2双人替换_2065454404580495362.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：52%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicScheduler`
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ColorTransfer`
- `ComfyMathExpression`
- `DiffusionModelLoaderKJ`
- `GetImageRangeFromBatch`
- `GetImageSize`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewAny`
- `PrimitiveInt`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SamplerCustom`
- `TensorLoopClose`
- `TensorLoopOpen`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 9/10 个有
- `PreviewImage` —— 9/10 个有
- `DownloadAndLoadGIMMVFIModel` —— 8/10 个有
- `GIMMVFI_interpolate` —— 8/10 个有
- `GetNode` —— 8/10 个有
- `SetNode` —— 8/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/10 个有
- `VHS_VideoInfoSource` —— 7/10 个有
- `easy imageCount` —— 7/10 个有
- `easy showAnything` —— 7/10 个有
- `Bjornulf_ShowInt` —— 6/10 个有
- `EmptyImage` —— 6/10 个有
- `ImageCompositeMasked` —— 6/10 个有
- `ImageConcatMulti` —— 6/10 个有
- `SAM3_TrackToMask` —— 6/10 个有
- `ResizeImageMaskNode` —— 5/10 个有
- `Int` —— 3/10 个有
- `Text` —— 3/10 个有
- `CR Prompt Text` —— 2/10 个有
- `CR Text` —— 2/10 个有
- `ImagePadKJ` —— 2/10 个有
- `InvertMask` —— 2/10 个有
- `MathExpression|pysssss` —— 2/10 个有
- `Seed (rgthree)` —— 2/10 个有
- `ShowAnything|Mie` —— 2/10 个有
- `TextConcatenate_UTK` —— 2/10 个有
- `VHS_VideoInfo` —— 2/10 个有
- `WanChunkFeedForward` —— 2/10 个有
- `easy indexAnything` —— 2/10 个有
- `ConditioningZeroOut` —— 1/10 个有
- `DrawMaskOnImage` —— 1/10 个有
- `FillMaskWithColor` —— 1/10 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/10 个有
- `ImageScaleToTotalPixels` —— 1/10 个有
- `KSampler` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/10 个有
- `LayerUtility: PurgeVRAM V2` —— 1/10 个有
- `QwenEditAdaptiveLongestEdge` —— 1/10 个有
- `QwenEditConfigPreparer` —— 1/10 个有
- `RH_Captioner` —— 1/10 个有
- `RMBG` —— 1/10 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 1/10 个有
- `UNETLoader` —— 1/10 个有
- `孤海注释` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | beta | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
