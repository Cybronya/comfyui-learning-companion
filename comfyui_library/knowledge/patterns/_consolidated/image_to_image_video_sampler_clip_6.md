---
name: image_to_image_video_sampler_clip_6
type: Image To Image
frequency: 2
level: weak
coverage: 0.5035
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DWPreprocessor, DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, DualCLIPLoader, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), FluxGuidance, GetImageRangeFromBatch, GetNode, INTConstant, ImageBatchMulti, ImageFromBatch, ImageResizeKJv2, KSampler, Label (rgthree), LayerUtility: PurgeVRAM, LoadImage, MathExpression|pysssss, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, ReferenceLatent, SetNode, TorchCompileModelWanVideo, TrimVideoLatent, UNETLoader, VAEDecode, VAEEncode, VAELoader, VHS_GetImageCount, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVaceToVideo, WanVideoVACEStartToEndFrame]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/重叠帧For循环让视频转绘无限时长_1943134599507828738.json, 平台全量/重叠帧视频转视频生成  Wan 2.1  fusionX Vace_1941737675923865602.json]
source: knowledge_consolidation
---

# image_to_image_video_sampler_clip_6

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/重叠帧For循环让视频转绘无限时长_1943134599507828738.json、平台全量/重叠帧视频转视频生成  Wan 2.1  fusionX Vace_1941737675923865602.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：50%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DWPreprocessor`
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `GetImageRangeFromBatch`
- `GetNode`
- `INTConstant`
- `ImageBatchMulti`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `KSampler`
- `Label (rgthree)`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `ReferenceLatent`
- `SetNode`
- `TorchCompileModelWanVideo`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_GetImageCount`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVaceToVideo`
- `WanVideoVACEStartToEndFrame`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 1/2 个有
- `CLIPVisionEncode` —— 1/2 个有
- `CLIPVisionLoader` —— 1/2 个有
- `DiffusionModelLoaderKJ` —— 1/2 个有
- `FloatConstant` —— 1/2 个有
- `ImageColorMatch+` —— 1/2 个有
- `LoadImageFromPath` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `MaskToImage` —— 1/2 个有
- `NunchakuFluxDiTLoader` —— 1/2 个有
- `NunchakuFluxLoraLoader` —— 1/2 个有
- `PatchModelPatcherOrder` —— 1/2 个有
- `Power Lora Loader (rgthree)` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `TextEncodeHunyuanVideo_ImageToVideo` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有
- `easy forLoopEnd` —— 1/2 个有
- `easy forLoopStart` —— 1/2 个有
- `easy imageConcat` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | uni_pc | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
