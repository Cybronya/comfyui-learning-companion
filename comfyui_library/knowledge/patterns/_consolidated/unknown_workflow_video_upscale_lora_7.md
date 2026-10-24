---
name: unknown_workflow_video_upscale_lora_7
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8356
common_nodes: [Anything Everywhere, CLIPVisionLoader, CR Text, ColorMatch, DWPreprocessor, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, GetNode, INTConstant, ImageResizeKJv2, ImageUpscaleWithModel, LoadImage, MathExpression|pysssss, PixelPerfectResolution, SetNode, UpscaleModelLoader, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan Animate 动作迁移（整活版）_1987934084561350657.json, 视频生成/图生视频/Wan Animate 动作迁移（背景不变）_1984675303345766402.json, 视频生成/图生视频/Wan Animate 视频换人物（主体迁移）_1984537427039633410.json, 视频生成/图生视频/Wan Animate 视频换人物（主体迁移）_2070675644220002306.json, 视频生成/图生视频/Wan Animate动作迁移V2（长视频可用，不劣化）_2015730877476642818.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_7

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Wan Animate 动作迁移（整活版）_1987934084561350657.json、视频生成/图生视频/Wan Animate 动作迁移（背景不变）_1984675303345766402.json、视频生成/图生视频/Wan Animate 视频换人物（主体迁移）_1984537427039633410.json、视频生成/图生视频/Wan Animate 视频换人物（主体迁移）_2070675644220002306.json、视频生成/图生视频/Wan Animate动作迁移V2（长视频可用，不劣化）_2015730877476642818.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 5 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPVisionLoader`
- `CR Text`
- `ColorMatch`
- `DWPreprocessor`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `ImageUpscaleWithModel`
- `LoadImage`
- `MathExpression|pysssss`
- `PixelPerfectResolution`
- `SetNode`
- `UpscaleModelLoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ACE_ImageFaceCrop` —— 4/5 个有
- `OnnxDetectionModelLoader` —— 4/5 个有
- `PoseAndFaceDetection` —— 4/5 个有
- `VHS_VideoInfo` —— 3/5 个有
- `BlockifyMask` —— 2/5 个有
- `DF_Int_to_Float` —— 2/5 个有
- `DrawMaskOnImage` —— 2/5 个有
- `GrowMask` —— 2/5 个有
- `MaskToImage` —— 2/5 个有
- `SeCModelLoader` —— 2/5 个有
- `SeCVideoSegmentation` —— 2/5 个有
- `WanVideoContextOptions` —— 1/5 个有
- `easy imageRemBg` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
