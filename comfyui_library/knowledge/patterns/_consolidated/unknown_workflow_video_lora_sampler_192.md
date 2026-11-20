---
name: unknown_workflow_video_lora_sampler_192
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.840083
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, LoadImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Animate美女图片跳舞工作流_1969296190498107394.json, 平台全量/Wan Animate 2.2：动作参考--许老师专用_1969779987081535490.json, 平台全量/Wan Animate 视频动作模仿生成_2032765479860834305.json, 平台全量/Wan Animate最强动作迁移_1970025398790746113.json, 平台全量/Wan2.2 Animate-动作迁移_2000068753591332865.json, 平台全量/Wan2.2 Animate-动作迁移_2012121126498996225.json, 平台全量/Wan2.2+Animate：角色动作迁移 美女跳舞 角色替换、动作迁移、图生视频_1981904836633477121.json, 平台全量/Wanvideo动作迁移_1989136982154547201.json, 平台全量/wan2.2Animate舞蹈三转二_1974447662953050113.json, 平台全量/工作流视频篇4-wan2.2视频转视频Animate-动f作迁移_2018222930089480194.json, 平台全量/抖音爆火武侠Animate wan2.2_1999710374268108801.json, 平台全量/视频换装换头加服装互动 Animate Wan2.2_2039621617348780033.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_192

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（平台全量/Animate美女图片跳舞工作流_1969296190498107394.json、平台全量/Wan Animate 2.2：动作参考--许老师专用_1969779987081535490.json、平台全量/Wan Animate 视频动作模仿生成_2032765479860834305.json、平台全量/Wan Animate最强动作迁移_1970025398790746113.json、平台全量/Wan2.2 Animate-动作迁移_2000068753591332865.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
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
- `JWInteger` —— 11/12 个有
- `PixelPerfectResolution` —— 11/12 个有
- `ImageResizeKJv2` —— 9/12 个有
- `Text` —— 8/12 个有
- `ImageConcatMulti` —— 7/12 个有
- `LayerUtility: PurgeVRAM` —— 7/12 个有
- `WanVideoAnimateEmbeds` —— 7/12 个有
- `easy cleanGpuUsed` —— 7/12 个有
- `GetImageSizeAndCount` —— 6/12 个有
- `RHHiddenNodes` —— 6/12 个有
- `VHS_VideoInfo` —— 5/12 个有
- `GetNode` —— 3/12 个有
- `Int` —— 3/12 个有
- `PreviewImage` —— 3/12 个有
- `SetNode` —— 3/12 个有
- `ImageResize+` —— 2/12 个有
- `PrimitiveStringMultiline` —— 2/12 个有
- `SimpleMath+` —— 2/12 个有
- `Audio Duration (mtb)` —— 1/12 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/12 个有
- `EmptyImage` —— 1/12 个有
- `GIMMVFI_interpolate` —— 1/12 个有
- `GetImageRangeFromBatch` —— 1/12 个有
- `ImageFromBatch+` —— 1/12 个有
- `ImageResizeKJ` —— 1/12 个有
- `ImpactInt` —— 1/12 个有
- `JjkText` —— 1/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/12 个有
- `MathExpression|pysssss` —— 1/12 个有
- `PrimitiveInt` —— 1/12 个有
- `easy imageConcat` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
