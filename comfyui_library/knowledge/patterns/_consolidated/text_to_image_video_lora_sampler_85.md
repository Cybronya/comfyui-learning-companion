---
name: text_to_image_video_lora_sampler_85
type: Text To Image
frequency: 9
level: weak
coverage: 0.630333
common_nodes: [BatchImagesNode, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, EmptyLatentImage, FillMaskWithColor, GetNode, ImageConcatenate_UTK, ImageResizeKJv2, Int, InvertMask, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, PlaySound|pysssss, PointsEditor, PreviewImage, PrimitiveInt, RH_Captioner, SAM3_VideoTrack, SCAIL2ColoredMaskV2, SeCModelLoader, SeCVideoSegmentation, SetNode, SimpleMath+, Text, VAEDecode, VAELoader, VHS_VideoCombine, VHS_VideoInfoLoaded, WanAnimatePlus BlockSwap, WanAnimatePlus ClipVisionEncode V2, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SCAIL_2 Embeds, WanAnimatePlus SCAIL_2 TwoPhase Settings, WanAnimatePlus SamplerFromSettings, WanAnimatePlus SamplerSettings, WanAnimatePlus SetBlockSwap, WanAnimatePlus SetLoRAs, WanAnimatePlus VAELoader, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, easy cleanGpuUsed, easy clearCacheAll, easy indexAnything, easy mathInt, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2082351084420558850.json, 视频生成/图生视频/多角色替换影视二创｜长时视频生图生视频生成_2093418632721293314.json, 视频生成/图生视频/影视二创神器 长视频多角色批量替换第2版_2097823943913721857.json, 视频生成/图生视频/影视二创神器 长视频多角色批量替换第2版_2101447299451936769.json, 视频生成/图生视频/影视二创神器_长视频多角色批量替换第2版_2109437055964110850.json, 视频生成/图生视频/影视二创第2弹｜长时长视频多角色替换保持原片质感_2101494880974495746.json, 视频生成/图生视频/影视二创长时多角色替换2｜换角色不换剧情_2097180512333942786.json, 视频生成/图生视频/影视二创长时多角色替换｜视频生视频图生视频工作流_2097031796901896194.json, 视频生成/图生视频/长时多角色替换2｜影视二创视频生视频一键处理_2093744499456561153.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_85

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/2082351084420558850.json、视频生成/图生视频/多角色替换影视二创｜长时视频生图生视频生成_2093418632721293314.json、视频生成/图生视频/影视二创神器 长视频多角色批量替换第2版_2097823943913721857.json、视频生成/图生视频/影视二创神器 长视频多角色批量替换第2版_2101447299451936769.json、视频生成/图生视频/影视二创神器_长视频多角色批量替换第2版_2109437055964110850.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：63%

## 共有节点

全部 9 个 workflow 都包含：
- `BatchImagesNode`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `FillMaskWithColor`
- `GetNode`
- `ImageConcatenate_UTK`
- `ImageResizeKJv2`
- `Int`
- `InvertMask`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PlaySound|pysssss`
- `PointsEditor`
- `PreviewImage`
- `PrimitiveInt`
- `RH_Captioner`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMaskV2`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `SetNode`
- `SimpleMath+`
- `Text`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus ClipVisionEncode V2`
- `WanAnimatePlus Decode`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus SCAIL_2 Embeds`
- `WanAnimatePlus SCAIL_2 TwoPhase Settings`
- `WanAnimatePlus SamplerFromSettings`
- `WanAnimatePlus SamplerSettings`
- `WanAnimatePlus SetBlockSwap`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus VAELoader`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy indexAnything`
- `easy mathInt`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `1hew_MaskMathOps` —— 8/9 个有
- `JjkText` —— 8/9 个有
- `PrimitiveBoolean` —— 8/9 个有
- `RH_RhartImageG2OfficialImageToImage` —— 8/9 个有
- `UNETLoader` —— 8/9 个有
- `VHS_LoadVideoFFmpeg` —— 8/9 个有
- `solarL_SaveImagesToZip` —— 8/9 个有
- `孤海注释` —— 7/9 个有
- `SaveImage` —— 2/9 个有
- `CFGNorm` —— 1/9 个有
- `ConditioningZeroOut` —— 1/9 个有
- `ControlNetApplySD3` —— 1/9 个有
- `ControlNetLoader` —— 1/9 个有
- `DepthAnything_V2` —— 1/9 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/9 个有
- `ETN_ApplyMaskToImage` —— 1/9 个有
- `EnhancedLoadDiffusionModel` —— 1/9 个有
- `ExtractStoryboards_xuhuan1024` —— 1/9 个有
- `Float` —— 1/9 个有
- `Float to Int` —— 1/9 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/9 个有
- `GetImageSize` —— 1/9 个有
- `INPAINT_MaskedFill` —— 1/9 个有
- `ImageScaleToTotalPixels` —— 1/9 个有
- `LayerUtility: ImageBlendAdvance` —— 1/9 个有
- `ModelSamplingAuraFlow` —— 1/9 个有
- `RMBG` —— 1/9 个有
- `SetUnionControlNetType` —— 1/9 个有
- `TextConcatenate_UTK` —— 1/9 个有
- `TextEncodeQwenImageEditPlus` —— 1/9 个有
- `VHS_LoadVideo` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 512 | 9 | 0% |
| 高度 | 80 | 80 - 512 | 9 | 0% |
| 采样步数 | 4 | 4 - 8 | 9 | 72% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 9 | 73% |
| 采样算法 | er_sde | - | 9 | 89% |
| 调度器 | beta | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| ControlNet 权重 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 512，9 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 512，9 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 8，9 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，9 个样本
- 采样算法 最常用 er_sde，9 个样本，一致性 89%
- 调度器 最常用 beta，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
