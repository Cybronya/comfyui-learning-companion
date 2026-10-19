---
name: unknown_workflow_video_lora_sampler_420
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.3582
common_nodes: [BOOLConstant, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, ComfyNumberConvert, GetNode, INTConstant, ImageResizeKJv2, LoadImage, PreviewImage, PrimitiveStringMultiline, SAM3_VideoTrack, SCAIL2ColoredMask, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanAnimatePlus BlockSwap, WanAnimatePlus ClipVisionEncode, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SCAIL_2 Embeds, WanAnimatePlus Sampler, WanAnimatePlus SetLoRAs, WanAnimatePlus TextEncodeCached, WanAnimatePlus TorchCompileSettings, WanAnimatePlus VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2081964333583654914.json, 视频生成/图生视频/2078736579782340610.json, 视频生成/图生视频/2079575491580878850.json, 视频生成/图生视频/2075772380282187777.json, 视频生成/图生视频/2074416012107272194.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_420

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2081964333583654914.json、视频生成/图生视频/2078736579782340610.json、视频生成/图生视频/2079575491580878850.json、视频生成/图生视频/2075772380282187777.json、视频生成/图生视频/2074416012107272194.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：36%

## 共有节点

全部 5 个 workflow 都包含：
- `BOOLConstant`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ComfyNumberConvert`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus ClipVisionEncode`
- `WanAnimatePlus Decode`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus SCAIL_2 Embeds`
- `WanAnimatePlus Sampler`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus TextEncodeCached`
- `WanAnimatePlus TorchCompileSettings`
- `WanAnimatePlus VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveBoolean` —— 4/5 个有
- `PrimitiveInt` —— 4/5 个有
- `easy imageRemBg` —— 2/5 个有
- `AIO_Preprocessor` —— 1/5 个有
- `BiRefNet_Hugo` —— 1/5 个有
- `CR Prompt Text` —— 1/5 个有
- `ImageBatchMulti` —— 1/5 个有
- `RH_RhartImageG2ImageToImage` —— 1/5 个有
- `SaveImage` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有
- `VideoFrameSelector` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
