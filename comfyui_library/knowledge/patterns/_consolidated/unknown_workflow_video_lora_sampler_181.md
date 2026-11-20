---
name: unknown_workflow_video_lora_sampler_181
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.554538
common_nodes: [CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, INTConstant, ImageResizeKJv2, LoadImage, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMaskV2, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanAnimatePlus BlockSwap, WanAnimatePlus ClipVisionEncode V2, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SCAIL_2 Embeds, WanAnimatePlus SamplerFromSettings, WanAnimatePlus SamplerSettings, WanAnimatePlus SetBlockSwap, WanAnimatePlus SetLoRAs, WanAnimatePlus VAELoader, WanVideoTextEncodeCached]
problems: []
missing: []
members: [视频生成/图生视频/Scail-2多人替换_2076308191373254658.json, 视频生成/图生视频/Scail2单人替换_2076932640346828801.json, 视频生成/图生视频/Scail2姿态迁移_2076583160242065410.json, 视频生成/图生视频/【人物替换】Scail-2+【长视频+动作迁移+背景替换】_2109558961455325186.json, 视频生成/图生视频/【人物替换】Scail-2+高阶工作流Plus+V4.1版【长视频+动作迁移+背景替换】_2096555365210083330.json, 视频生成/图生视频/【人物替换】Scail-2+高阶工作流Plus+V4.1版【长视频+动作迁移+背景替换】_2100180765987401729.json, 视频生成/图生视频/【人物替换】Scail-2+高阶工作流Plus+V4.1版【长视频+动作迁移+背景替换】_2100547577077911554.json, 视频生成/图生视频/【人物替换】Scail-2+高阶工作流Plus+V4.1版【长视频+动作迁移+背景替换】_2101866496606695426.json, 视频生成/图生视频/【人物替换】Scail-2+高阶工作流Plus+V4.1版【长视频+动作迁移+背景替换】_2105471008286273538.json, 视频生成/图生视频/【人物替换】Scail-2+高阶工作流Plus+V4.2版【长视频不崩坏+动作迁移+背景替换】_2078094936641200130.json, 视频生成/图生视频/【人物替换】高定版_2074076654124752897.json, 视频生成/图生视频/视频动作迁移 Scail-2_2116196009201197057.json, 视频生成/文生视频/人物替换_2085001992212140034.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_181

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/Scail-2多人替换_2076308191373254658.json、视频生成/图生视频/Scail2单人替换_2076932640346828801.json、视频生成/图生视频/Scail2姿态迁移_2076583160242065410.json、视频生成/图生视频/【人物替换】Scail-2+【长视频+动作迁移+背景替换】_2109558961455325186.json、视频生成/图生视频/【人物替换】Scail-2+高阶工作流Plus+V4.1版【长视频+动作迁移+背景替换】_2096555365210083330.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `PreviewImage`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMaskV2`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus ClipVisionEncode V2`
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
- `FastGroupsBypassSwitch` —— 12/13 个有
- `Image Blank` —— 12/13 个有
- `ImageCompositeMasked` —— 12/13 个有
- `RepeatImageBatch` —— 12/13 个有
- `SAM3_TrackToMask` —— 12/13 个有
- `Seed (rgthree)` —— 12/13 个有
- `GetNode` —— 10/13 个有
- `Int` —— 10/13 个有
- `SetNode` —— 10/13 个有
- `PlaySound|pysssss` —— 9/13 个有
- `WanAnimatePlus ContextOptions` —— 9/13 个有
- `WanAnimatePlus LoraSelect` —— 9/13 个有
- `Fast Groups Bypasser (rgthree)` —— 8/13 个有
- `WanAnimatePlus SCAIL_2 TwoPhase Settings` —— 8/13 个有
- `Label (rgthree)` —— 6/13 个有
- `CR Text` —— 3/13 个有
- `EmptyImage` —— 3/13 个有
- `MaskAdd_UTK` —— 2/13 个有
- `ImageUpscaleWithModelBatched` —— 1/13 个有
- `LayerMask: MaskPreview` —— 1/13 个有
- `MuyeTextEditOutput` —— 1/13 个有
- `RHSettingsNode` —— 1/13 个有
- `RIFE VFI` —— 1/13 个有
- `SimpleMath+` —— 1/13 个有
- `UpscaleModelLoader` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
