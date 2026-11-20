---
name: unknown_workflow_video_lora_sampler_212
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.811
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, ImageBatchMulti, ImageConcatMulti, ImageResizeKJv2, LoadImage, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMask, VHS_LoadVideo, VHS_VideoCombine, WanAnimatePlus BlockSwap, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SCAIL_2 Embeds, WanAnimatePlus Sampler, WanAnimatePlus SetLoRAs, WanAnimatePlus TextEncodeCached, WanAnimatePlus VAELoader]
problems: []
missing: []
members: [数字人/数字人/动作迁移   Scail-V2  更强的人物一致性 多参+ 换背景_2066157381343596545.json, 数字人/数字人/视频动作迁移  scail2 多参考图 可换背景_2065797278249607169.json, 视频生成/图生视频/SCAIL-2多参考图角色动作迁移与替换——支持长视频_2066386680499761154.json, 视频生成/图生视频/Scail2 多参动作迁移＆人物替换_支持超长视频_2066423753369808897.json, 视频生成/图生视频/Wan-Scail2-多图参考换姿势+换背景_2066016584279347201.json, 视频生成/图生视频/Wan-Scail2-多图姿势迁移_2066001113731649537.json, 视频生成/图生视频/scail2 多参人物图动作模仿工作流_2066378010617540610.json, 视频生成/图生视频/scail2 多参工作流-多图参考-动作迁移_2073343102223470594.json, 视频生成/图生视频/scail2 多参工作流动作迁移保持人物多角度不崩_2065965062183018498.json, 视频生成/图生视频/史上最强的scail2 多图参考工作流_2066889873231015938.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_212

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（数字人/数字人/动作迁移   Scail-V2  更强的人物一致性 多参+ 换背景_2066157381343596545.json、数字人/数字人/视频动作迁移  scail2 多参考图 可换背景_2065797278249607169.json、视频生成/图生视频/SCAIL-2多参考图角色动作迁移与替换——支持长视频_2066386680499761154.json、视频生成/图生视频/Scail2 多参动作迁移＆人物替换_支持超长视频_2066423753369808897.json、视频生成/图生视频/Wan-Scail2-多图参考换姿势+换背景_2066016584279347201.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `ImageBatchMulti`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `LoadImage`
- `PreviewImage`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus Decode`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus SCAIL_2 Embeds`
- `WanAnimatePlus Sampler`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus TextEncodeCached`
- `WanAnimatePlus VAELoader`

**可变部分**（部分 workflow 才有）：
- `WanAnimatePlus ContextOptions` —— 9/10 个有
- `Int` —— 5/10 个有
- `JjkText` —— 4/10 个有
- `easy boolean` —— 3/10 个有
- `Text` —— 2/10 个有
- `ToBoolNode` —— 2/10 个有
- `VHS_VideoInfo` —— 2/10 个有
- `easy showAnything` —— 2/10 个有
- `CLIPVisionLoader` —— 1/10 个有
- `If ANY execute A else B` —— 1/10 个有
- `ImpactNeg` —— 1/10 个有
- `PrimitiveBoolean` —— 1/10 个有
- `PrimitiveInt` —— 1/10 个有
- `WanAnimatePlus ClipVisionEncode` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
