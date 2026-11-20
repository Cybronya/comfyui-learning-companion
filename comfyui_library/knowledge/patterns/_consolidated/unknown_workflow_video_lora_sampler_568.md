---
name: unknown_workflow_video_lora_sampler_568
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.5094
common_nodes: [CLIPTextEncode, CLIPVisionLoader, CM_IntToFloat, CR Text, CheckpointLoaderSimple, GetNode, INTConstant, ImageBatchMulti, ImageResizeKJv2, Int, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, PrimitiveBoolean, RH_Translator, SAM3_VideoTrack, SCAIL2ColoredMaskV2, SetNode, Switch any [Crystools], Text, VHS_VideoCombine, WanAnimatePlus BlockSwap, WanAnimatePlus ClipVisionEncode, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SCAIL_2 Embeds, WanAnimatePlus Sampler, WanAnimatePlus TextEncodeCached, WanAnimatePlus VAELoader, easy boolean, easy imageRemBg, 忽略多组孤海]
problems: []
missing: []
members: [平台全量/20260930更新！单人动作迁移、替换视频人物新王！支持多参 Scail 2_2065817354185043969.json, 视频生成/图生视频/20260717更新！多人动作迁移、替换视频人物新王！支持多参 Scail 2_2066443352299622401.json, 视频生成/图生视频/2026_10_02_替换视频的人物和背景专用流_支持人物多参 _Scail 2_2105681606760550401.json, 视频生成/图生视频/261003单人动作迁移、替换视频人物 可多参 高质量极简版_2106393442275385346.json, 视频生成/图生视频/视频换人！人物替换新王！支持多参 Scail 2_20260724_2080301898942476289.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_568

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/20260930更新！单人动作迁移、替换视频人物新王！支持多参 Scail 2_2065817354185043969.json、视频生成/图生视频/20260717更新！多人动作迁移、替换视频人物新王！支持多参 Scail 2_2066443352299622401.json、视频生成/图生视频/2026_10_02_替换视频的人物和背景专用流_支持人物多参 _Scail 2_2105681606760550401.json、视频生成/图生视频/261003单人动作迁移、替换视频人物 可多参 高质量极简版_2106393442275385346.json、视频生成/图生视频/视频换人！人物替换新王！支持多参 Scail 2_20260724_2080301898942476289.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：51%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CM_IntToFloat`
- `CR Text`
- `CheckpointLoaderSimple`
- `GetNode`
- `INTConstant`
- `ImageBatchMulti`
- `ImageResizeKJv2`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `PrimitiveBoolean`
- `RH_Translator`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMaskV2`
- `SetNode`
- `Switch any [Crystools]`
- `Text`
- `VHS_VideoCombine`
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus ClipVisionEncode`
- `WanAnimatePlus Decode`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus SCAIL_2 Embeds`
- `WanAnimatePlus Sampler`
- `WanAnimatePlus TextEncodeCached`
- `WanAnimatePlus VAELoader`
- `easy boolean`
- `easy imageRemBg`
- `忽略多组孤海`

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 4/5 个有
- `ImageConcanate` —— 4/5 个有
- `LoadVideoUI` —— 4/5 个有
- `RH_RhartImageG2ImageToImage` —— 4/5 个有
- `SaveImage` —— 4/5 个有
- `孤海注释` —— 4/5 个有
- `InvertBoolean` —— 3/5 个有
- `Fast Bypasser (rgthree)` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有
- `VHS_VideoInfo` —— 1/5 个有
- `WanAnimatePlus LoraSelect` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
