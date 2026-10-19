---
name: text_to_image_video_inpaint_lora
type: Text To Image
frequency: 8
level: strong
coverage: 0.8065
common_nodes: [AIO_Preprocessor, AddLabel, CLIPLoader, CLIPTextEncode, DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, DownloadAndLoadFlorence2Model, DownloadAndLoadSAM2Model, EmptyImage, EmptyLatentImage, Florence2Run, Florence2toCoordinates, GetImageSizeAndCount, GetNode, GrowMaskWithBlur, ImageBlend, ImageConcatMulti, ImageFromBatch, ImageResizeKJ, ImpactSwitch, InpaintPreprocessor, JjkText, KSampler, LayerUtility: ImageBlend, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, LoraLoaderModelOnly, PreviewImage, Primitive float [Crystools], Primitive integer [Crystools], PrimitiveString, RHHiddenNodes, RH_Captioner, RH_Translator, Sam2Segmentation, SetNode, ShowText|pysssss, SimpleMath+, Text Concatenate, Text Multiline, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader, easy cleanGpuUsed, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/循环版V2 视频人物自动替换无缝输出不停顿_2094817394312175618.json, 数字人/数字人/循环版V2人物替换｜视频数字人动作迁移自动生成_2092179820305281025.json, 视频生成/图生视频/180帧娱乐版本人物替换视频换装动作迁移图生视频_2087413980452184066.json, 视频生成/图生视频/V2版本升级 视频里的人物一键自动替换更自然_2094814775535554561.json, 视频生成/图生视频/V2自动人物替换｜视频人物类特效图生视频生成_2092164278324391938.json, 视频生成/图生视频/人物替换换装娱乐版180帧｜动作迁移图生视频换装方案_2091292199714648066.json, 视频生成/图生视频/人物替换视频换装娱乐版180帧 动作迁移图生视频换装方案_2089710797663592450.json, 视频生成/图生视频/人物替换视频换装娱乐版180帧 动作迁移图生视频换装方案_2092135880885620737.json]
source: knowledge_consolidation
---

# text_to_image_video_inpaint_lora

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（数字人/数字人/循环版V2 视频人物自动替换无缝输出不停顿_2094817394312175618.json、数字人/数字人/循环版V2人物替换｜视频数字人动作迁移自动生成_2092179820305281025.json、视频生成/图生视频/180帧娱乐版本人物替换视频换装动作迁移图生视频_2087413980452184066.json、视频生成/图生视频/V2版本升级 视频里的人物一键自动替换更自然_2094814775535554561.json、视频生成/图生视频/V2自动人物替换｜视频人物类特效图生视频生成_2092164278324391938.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 8 个 workflow 都包含：
- `AIO_Preprocessor`
- `AddLabel`
- `CLIPLoader`
- `CLIPTextEncode`
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `DownloadAndLoadFlorence2Model`
- `DownloadAndLoadSAM2Model`
- `EmptyImage`
- `EmptyLatentImage`
- `Florence2Run`
- `Florence2toCoordinates`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMaskWithBlur`
- `ImageBlend`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ImageResizeKJ`
- `ImpactSwitch`
- `InpaintPreprocessor`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageBlend`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `Primitive float [Crystools]`
- `Primitive integer [Crystools]`
- `PrimitiveString`
- `RHHiddenNodes`
- `RH_Captioner`
- `RH_Translator`
- `Sam2Segmentation`
- `SetNode`
- `ShowText|pysssss`
- `SimpleMath+`
- `Text Concatenate`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 4/8 个有
- `CLIPVisionLoader` —— 4/8 个有
- `CM_BoolToInt` —— 4/8 个有
- `DifferentialDiffusion` —— 4/8 个有
- `DualCLIPLoader` —— 4/8 个有
- `FluxGuidance` —— 4/8 个有
- `GrowMask` —— 4/8 个有
- `Image To Mask` —— 4/8 个有
- `ImageConcanate` —— 4/8 个有
- `ImageResize+` —— 4/8 个有
- `ImageScale` —— 4/8 个有
- `InpaintCrop` —— 4/8 个有
- `InpaintModelConditioning` —— 4/8 个有
- `InpaintStitch` —— 4/8 个有
- `LayerMask: SegmentAnythingUltra V2` —— 4/8 个有
- `LayerUtility: ColorImage V2` —— 4/8 个有
- `LayerUtility: CropByMask` —— 4/8 个有
- `LayerUtility: ImageRemoveAlpha` —— 4/8 个有
- `MaskPreview+` —— 4/8 个有
- `MaskToImage` —— 4/8 个有
- `RMBG` —— 4/8 个有
- `SaveImage` —— 4/8 个有
- `StyleModelApply` —— 4/8 个有
- `StyleModelLoader` —— 4/8 个有
- `easy imageInsetCrop` —— 4/8 个有
- `easy imageRemBg` —— 4/8 个有
- `easy imageSize` —— 4/8 个有
- `easy isMaskEmpty` —— 4/8 个有
- `easy showAnything` —— 4/8 个有
- `ColorMatch` —— 2/8 个有
- `UnloadModel` —— 2/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（9/8 个样本）：Steps较低可能导致细节不足
