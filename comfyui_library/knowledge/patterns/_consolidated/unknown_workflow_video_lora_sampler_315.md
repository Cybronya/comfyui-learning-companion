---
name: unknown_workflow_video_lora_sampler_315
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.384222
common_nodes: [BOOLConstant, CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, GetNode, INTConstant, ImageResizeKJv2, LoadImage, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMask, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanAnimatePlus BlockSwap, WanAnimatePlus ClipVisionEncode, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SCAIL_2 Embeds, WanAnimatePlus Sampler, WanAnimatePlus SetLoRAs, WanAnimatePlus TextEncodeCached, WanAnimatePlus TorchCompileSettings, WanAnimatePlus VAELoader]
problems: []
missing: []
members: [平台全量/SCAIL2优化版+多图参考 By 像素幻想Lab_2067599527623872514.json, 平台全量/SCAIL2优化版+多图参考 By 像素自用_2105315594722701314.json, 视频生成/图生视频/81.SCAIL2优化版+多图参考_2096980051706339330.json, 视频生成/图生视频/SCAIL2 动作迁移（多图参考）_2079086131693572098.json, 视频生成/图生视频/SCAIL2 角色替换&动作迁移_2076542724727201794.json, 视频生成/图生视频/SCAIL2+深度图动作参考（自然表情）降低原视频细节干扰方案_2081964333583654914.json, 视频生成/图生视频/SCAIL2人物替换+重打光lora 优化版工作流（清晰布局_小白适用_效果超夯）_2078736579782340610.json, 视频生成/图生视频/SCAIL2人物替换+首帧自动姿态对齐（一键自动工作流）_2079575491580878850.json, 视频生成/图生视频/SCAIL2系列优化版--动作迁移专用工作流（清晰布局_小白适用_效果超夯）_2075772380282187777.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_315

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（平台全量/SCAIL2优化版+多图参考 By 像素幻想Lab_2067599527623872514.json、平台全量/SCAIL2优化版+多图参考 By 像素自用_2105315594722701314.json、视频生成/图生视频/81.SCAIL2优化版+多图参考_2096980051706339330.json、视频生成/图生视频/SCAIL2 动作迁移（多图参考）_2079086131693572098.json、视频生成/图生视频/SCAIL2 角色替换&动作迁移_2076542724727201794.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：38%

## 共有节点

全部 9 个 workflow 都包含：
- `BOOLConstant`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `PreviewImage`
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
- `easy imageRemBg` —— 7/9 个有
- `Fast Groups Bypasser (rgthree)` —— 5/9 个有
- `ImageBatchMulti` —— 5/9 个有
- `ImageConcanate` —— 5/9 个有
- `ImageConcatMulti` —— 5/9 个有
- `Switch any [Crystools]` —— 5/9 个有
- `ComfyNumberConvert` —— 4/9 个有
- `PrimitiveBoolean` —— 4/9 个有
- `PrimitiveInt` —— 4/9 个有
- `PrimitiveStringMultiline` —— 4/9 个有
- `Label (rgthree)` —— 3/9 个有
- `AIO_Preprocessor` —— 1/9 个有
- `BiRefNet_Hugo` —— 1/9 个有
- `CR Prompt Text` —— 1/9 个有
- `ImageScaleToTotalPixels` —— 1/9 个有
- `RH_RhartImageG2ImageToImage` —— 1/9 个有
- `SaveImage` —— 1/9 个有
- `Seed (rgthree)` —— 1/9 个有
- `SeedVR2LoadDiTModel` —— 1/9 个有
- `SeedVR2LoadVAEModel` —— 1/9 个有
- `SeedVR2VideoUpscaler` —— 1/9 个有
- `VideoFrameSelector` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
