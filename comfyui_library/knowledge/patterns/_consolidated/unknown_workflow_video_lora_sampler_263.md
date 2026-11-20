---
name: unknown_workflow_video_lora_sampler_263
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.4666
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, GetNode, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMask, SamplerCustom, SetNode, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanSCAILToVideo]
problems: []
missing: []
members: [平台全量/SCAIL 2视频角色替换（支持多人）_2065274035444994049.json, 平台全量/SCAIL 2视频角色替换（支持多人）_2070143834000019457.json, 平台全量/SCAIL 2角色动作、表情迁移_2064980975569956865.json, 平台全量/scail2动作迁移_人物替换工作流_2064539529503141890.json, 平台全量/长视频动作迁移_2068364416038555650.json, 数字人/数字人/SCAIL-2替换人物_动作迁移_2065095439338270721.json, 数字人/数字人/Wan21_SCAIL2多角色动作迁移_2064537633363156994.json, 数字人/数字人/视频人物替换 动作迁移 SCAIL 2（支持多人）_2065647705745084418.json, 数字人/数字人/视频人物替换 视频动作迁移 SCAIL 2（单人和多人）_2065655949918031874.json, 视频生成/图生视频/SCAIL 2 角色替换+动作迁移+表情迁移（长视频续航版）_2065651452084834306.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_263

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（平台全量/SCAIL 2视频角色替换（支持多人）_2065274035444994049.json、平台全量/SCAIL 2视频角色替换（支持多人）_2070143834000019457.json、平台全量/SCAIL 2角色动作、表情迁移_2064980975569956865.json、平台全量/scail2动作迁移_人物替换工作流_2064539529503141890.json、平台全量/长视频动作迁移_2068364416038555650.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：47%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `GetNode`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SamplerCustom`
- `SetNode`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanSCAILToVideo`

**可变部分**（部分 workflow 才有）：
- `BatchImagesNode` —— 9/10 个有
- `GetImageRangeFromBatch` —— 9/10 个有
- `ImageConcatMulti` —— 9/10 个有
- `ColorTransfer` —— 8/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/10 个有
- `easy imageRemBg` —— 8/10 个有
- `ApplySageAttention` —— 7/10 个有
- `SimpleMath+` —— 7/10 个有
- `UNETLoader` —— 7/10 个有
- `VHS_VideoInfo` —— 7/10 个有
- `CR Text` —— 6/10 个有
- `Fast Groups Bypasser (rgthree)` —— 6/10 个有
- `ImageFromBatch` —— 6/10 个有
- `Int` —— 6/10 个有
- `Seed` —— 6/10 个有
- `DiffusionModelLoaderKJ` —— 3/10 个有
- `WanChunkFeedForward` —— 3/10 个有
- `easy showAnything` —— 3/10 个有
- `ImageResizeKJv2` —— 2/10 个有
- `Text` —— 2/10 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/10 个有
- `GIMMVFI_interpolate` —— 1/10 个有
- `ImpactConditionalBranch` —— 1/10 个有
- `RH_Translator` —— 1/10 个有
- `SaveImage` —— 1/10 个有
- `WanAnimatePlus SetBlockSwap` —— 1/10 个有
- `WanVideoBlockSwap` —— 1/10 个有
- `WanVideoSetBlockSwap` —— 1/10 个有
- `wanBlock_Swap` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
