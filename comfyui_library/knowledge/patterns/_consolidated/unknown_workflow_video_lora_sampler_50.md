---
name: unknown_workflow_video_lora_sampler_50
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.802048
common_nodes: [CLIPVisionLoader, JWInteger, LoadImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1995333956365115393.json, 视频生成/图生视频/2053044709232263170.json, 视频生成/图生视频/2011410598436806658.json, 视频生成/图生视频/2011439752528011266.json, 视频生成/图生视频/1969252099450150913.json, 视频生成/图生视频/1969217356767653890.json, 视频生成/图生视频/1993551269581225986.json, 视频生成/图生视频/1979432276058607617.json, 视频生成/图生视频/2067088794045734914.json, 视频生成/图生视频/2069232638564593665.json, 视频生成/图生视频/2004038728341438465.json, 视频生成/图生视频/1982315306993500162.json, 视频生成/图生视频/2046042390951108610.json, 视频生成/图生视频/1995682413978193921.json, 视频生成/图生视频/2017854030659194882.json, 视频生成/图生视频/2034534867488219137.json, 视频生成/图生视频/2034431517451096065.json, 视频生成/图生视频/2046830049172656129.json, 视频生成/图生视频/2047135621176627201.json, 视频生成/图生视频/1974863458778918913.json, 视频生成/图生视频/2047571961420713986.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_50

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（视频生成/图生视频/1995333956365115393.json、视频生成/图生视频/2053044709232263170.json、视频生成/图生视频/2011410598436806658.json、视频生成/图生视频/2011439752528011266.json、视频生成/图生视频/1969252099450150913.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 21 个 workflow 都包含：
- `CLIPVisionLoader`
- `JWInteger`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 20/21 个有
- `FaceMaskFromPoseKeypoints` —— 20/21 个有
- `ImageCropByMaskAndResize` —— 20/21 个有
- `ImageResizeKJv2` —— 20/21 个有
- `PixelPerfectResolution` —— 20/21 个有
- `WanVideoLoraSelectMulti` —— 20/21 个有
- `WanVideoAnimateEmbeds` —— 15/21 个有
- `GetNode` —— 13/21 个有
- `SetNode` —— 13/21 个有
- `Text` —— 13/21 个有
- `easy cleanGpuUsed` —— 11/21 个有
- `GetImageSizeAndCount` —— 10/21 个有
- `ImageConcatMulti` —— 10/21 个有
- `VHS_VideoInfo` —— 10/21 个有
- `LayerUtility: PurgeVRAM` —— 9/21 个有
- `SimpleMath+` —— 9/21 个有
- `PrimitiveInt` —— 7/21 个有
- `RHHiddenNodes` —— 7/21 个有
- `ttN float` —— 7/21 个有
- `PrimitiveStringMultiline` —— 4/21 个有
- `CR Text` —— 3/21 个有
- `Int` —— 3/21 个有
- `ImpactInt` —— 2/21 个有
- `ImageFromBatch` —— 1/21 个有
- `ImageResize+` —— 1/21 个有
- `LayerUtility: PurgeVRAM V2` —— 1/21 个有
- `PreviewImage` —— 1/21 个有
- `SaveImage` —— 1/21 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
