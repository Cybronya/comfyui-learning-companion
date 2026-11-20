---
name: unknown_workflow_video_lora_sampler_448
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.4486
common_nodes: [CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, Fast Groups Bypasser (rgthree), GetNode, Image Blank, ImageCompositeMasked, ImageResizeKJv2, Int, LoadImage, PlaySound|pysssss, PreviewImage, RepeatImageBatch, SAM3_TrackToMask, SAM3_VideoTrack, SCAIL2ColoredMaskV2, Seed (rgthree), SetNode, VHS_LoadVideo, VHS_VideoCombine, WanAnimatePlus BlockSwap, WanAnimatePlus ClipVisionEncode V2, WanAnimatePlus ContextOptions, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SCAIL_2 Embeds, WanAnimatePlus SamplerFromSettings, WanAnimatePlus SamplerSettings, WanAnimatePlus SetBlockSwap, WanAnimatePlus SetLoRAs, WanAnimatePlus VAELoader, WanVideoTextEncodeCached]
problems: []
missing: []
members: [图片生成/图生图/Scail-2_2087796642505383938.json, 数字人/数字人/Scail-2 人物替换高阶工作流Plus V4版【长视频 +背景替换】_2074383470415147009.json, 数字人/数字人/【人物替换】Scail-2+高阶工作流Plus+V4.1版【长视频+动作迁移+背景替换】_2073792349171441665.json, 数字人/数字人/【动作迁移】Scail-2 高阶工作流Plus V4版【长视频 + 多图参考 + 动作迁移】_1988236407191814145.json, 视频生成/图生视频/10号特工：Scail2动作迁移+爆款舞蹈+背景替换+多图参考+影视二创_2085948916603904001.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_448

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Scail-2_2087796642505383938.json、数字人/数字人/Scail-2 人物替换高阶工作流Plus V4版【长视频 +背景替换】_2074383470415147009.json、数字人/数字人/【人物替换】Scail-2+高阶工作流Plus+V4.1版【长视频+动作迁移+背景替换】_2073792349171441665.json、数字人/数字人/【动作迁移】Scail-2 高阶工作流Plus V4版【长视频 + 多图参考 + 动作迁移】_1988236407191814145.json、视频生成/图生视频/10号特工：Scail2动作迁移+爆款舞蹈+背景替换+多图参考+影视二创_2085948916603904001.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：45%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Image Blank`
- `ImageCompositeMasked`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `PlaySound|pysssss`
- `PreviewImage`
- `RepeatImageBatch`
- `SAM3_TrackToMask`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMaskV2`
- `Seed (rgthree)`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus ClipVisionEncode V2`
- `WanAnimatePlus ContextOptions`
- `WanAnimatePlus Decode`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus SCAIL_2 Embeds`
- `WanAnimatePlus SamplerFromSettings`
- `WanAnimatePlus SamplerSettings`
- `WanAnimatePlus SetBlockSwap`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus VAELoader`
- `WanVideoTextEncodeCached`

**可变部分**（部分 workflow 才有）：
- `FastGroupsBypassSwitch` —— 4/5 个有
- `INTConstant` —— 4/5 个有
- `VHS_VideoInfoLoaded` —— 4/5 个有
- `WanAnimatePlus LoraSelect` —— 4/5 个有
- `Label (rgthree)` —— 3/5 个有
- `WanAnimatePlus SCAIL_2 TwoPhase Settings` —— 3/5 个有
- `ImageBatchMulti` —— 2/5 个有
- `LayerUtility: PurgeVRAM` —— 2/5 个有
- `WanVideoEncode` —— 2/5 个有
- `WanVideoUni3C_ControlnetLoader` —— 2/5 个有
- `WanVideoUni3C_embeds` —— 2/5 个有
- `CR Prompt Text` —— 1/5 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/5 个有
- `GIMMVFI_interpolate` —— 1/5 个有
- `Image Switch (JPS)` —— 1/5 个有
- `ImageBatchMultiV2` —— 1/5 个有
- `ImageConcanate` —— 1/5 个有
- `LayerUtility: PurgeVRAM V2` —— 1/5 个有
- `PrimitiveBoolean` —— 1/5 个有
- `SAM3_TrackPreview` —— 1/5 个有
- `SaveImage` —— 1/5 个有
- `SeedVR2LoadDiTModel` —— 1/5 个有
- `SeedVR2LoadVAEModel` —— 1/5 个有
- `SeedVR2VideoUpscaler` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `VideoInfoLoaded` —— 1/5 个有
- `easy imageSwitch` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
