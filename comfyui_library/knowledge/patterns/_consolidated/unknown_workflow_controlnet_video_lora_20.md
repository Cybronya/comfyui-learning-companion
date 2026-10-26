---
name: unknown_workflow_controlnet_video_lora_20
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.4732
common_nodes: [CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, ComfyMathExpression, Fast Groups Bypasser (rgthree), GetImageRangeFromBatch, GetNode, INTConstant, ImageConcanate, ImageResizeKJv2, ImpactConditionalBranch, LoadImage, PreviewImage, SAM3_VideoTrack, SCAIL2ColoredMask, SetNode, TTResolutionSelector, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanAnimatePlus BlockSwap, WanAnimatePlus ClipVisionEncode, WanAnimatePlus ContextOptions, WanAnimatePlus Decode, WanAnimatePlus Encode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus SCAIL_2 Embeds, WanAnimatePlus SamplerFromSettings, WanAnimatePlus SamplerSettings, WanAnimatePlus TextEncodeCached, WanAnimatePlus Uni3C ControlnetLoader, WanAnimatePlus Uni3C Embeds, WanAnimatePlus VAELoader, easy boolean, easy imageRemBg]
problems: []
missing: []
members: [图片生成/图生图/Scail2-GGUF版本_2067110261546381314.json, 图片生成/图生图/【Aaron寄语秋歌】Scail-2无劣化+长视频手动分段工作流_2065490120324767746.json, 视频生成/图生视频/SCAIL-2长视频分段｜Aaron寄语秋歌工作流复用版_2101630581737091074.json, 视频生成/图生视频/【南音Scail-2客户高定版，会员专享_2074092071199272961.json, 视频生成/图生视频/（王炸版）Scail-2万能分段无缝视频替换工作流_2072271297572331522.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_20

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Scail2-GGUF版本_2067110261546381314.json、图片生成/图生图/【Aaron寄语秋歌】Scail-2无劣化+长视频手动分段工作流_2065490120324767746.json、视频生成/图生视频/SCAIL-2长视频分段｜Aaron寄语秋歌工作流复用版_2101630581737091074.json、视频生成/图生视频/【南音Scail-2客户高定版，会员专享_2074092071199272961.json、视频生成/图生视频/（王炸版）Scail-2万能分段无缝视频替换工作流_2072271297572331522.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：47%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `Fast Groups Bypasser (rgthree)`
- `GetImageRangeFromBatch`
- `GetNode`
- `INTConstant`
- `ImageConcanate`
- `ImageResizeKJv2`
- `ImpactConditionalBranch`
- `LoadImage`
- `PreviewImage`
- `SAM3_VideoTrack`
- `SCAIL2ColoredMask`
- `SetNode`
- `TTResolutionSelector`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus ClipVisionEncode`
- `WanAnimatePlus ContextOptions`
- `WanAnimatePlus Decode`
- `WanAnimatePlus Encode`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus SCAIL_2 Embeds`
- `WanAnimatePlus SamplerFromSettings`
- `WanAnimatePlus SamplerSettings`
- `WanAnimatePlus TextEncodeCached`
- `WanAnimatePlus Uni3C ControlnetLoader`
- `WanAnimatePlus Uni3C Embeds`
- `WanAnimatePlus VAELoader`
- `easy boolean`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 4/5 个有
- `ImageFromBatch` —— 4/5 个有
- `SimpleMath+` —— 4/5 个有
- `easy int` —— 4/5 个有
- `孤海注释` —— 3/5 个有
- `CR Prompt Text` —— 1/5 个有
- `EmptyImage` —— 1/5 个有
- `ImageFromBatch+` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy showAnything` —— 1/5 个有
- `easy string` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
