---
name: unknown_workflow_video_lora_sampler_48
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.802048
common_nodes: [CLIPVisionLoader, JWInteger, LoadImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan+AnimateV2动作迁移工作流_1995333956365115393.json, 视频生成/图生视频/Wan2.2 Animate 动作迁移（手动版）_2053044709232263170.json, 视频生成/图生视频/Wan2.2 Animate-动作迁移_2011410598436806658.json, 视频生成/图生视频/Wan2.2 Animate-动作迁移_2011439752528011266.json, 视频生成/图生视频/Wan2.2 Animate动作迁移长视频生成加速版_1969252099450150913.json, 视频生成/图生视频/Wan2.2 Animate：角色动画革新，表演艺术的完美复刻！角色替换、动作迁移、图生视频_1969217356767653890.json, 视频生成/图生视频/Wan2.2+Animate+角色替换视频动作迁移+KJ加速版_1993551269581225986.json, 视频生成/图生视频/Wan2.2+Animate：角色替换、动作迁移、图生视频 美女跳舞视频，表演艺术的完美复刻！_1979432276058607617.json, 视频生成/图生视频/Wan2.2-Animate-视频动作迁移_2067088794045734914.json, 视频生成/图生视频/Wan2.2-Animate-视频动作迁移_2069232638564593665.json, 视频生成/图生视频/wan2.2 animate 动作迁移_2004038728341438465.json, 视频生成/图生视频/【人物替换】Wan2.2+Animate+角色替换视频动作迁移+KJ加速版-StarAI_1982315306993500162.json, 视频生成/图生视频/人物角色迁移 动作模仿+唱歌跳舞+舞剑 Wan2.2 图生视频  动作迁移 人物替换_2046042390951108610.json, 视频生成/图生视频/优化版 人物模特替换 动作克隆 首尾帧+角色替换 Wan2.2+Animate+角色替换视频动作迁移_1995682413978193921.json, 视频生成/图生视频/全新 Animate美女跳舞动作迁移V8极速版_2017854030659194882.json, 视频生成/图生视频/图生视频 -快生成- AI动作模仿+跳舞+剑舞-Animate wan2.2_2034534867488219137.json, 视频生成/图生视频/图生视频 快生成 AI动作模仿+跳舞+剑舞-Animate wan2.2_2034431517451096065.json, 视频生成/图生视频/图生视频 快生成 AI动作模仿+跳舞+剑舞-Animate wan2.2_2046830049172656129.json, 视频生成/图生视频/图生视频+快生成Animate+wan2.2_2047135621176627201.json, 视频生成/图生视频/新版动作迁移美女跳舞！Wan2.2-Animate V2超极速版_1974863458778918913.json, 视频生成/图生视频/高清流畅！AI动作模仿+跳舞+剑舞=AnimaAI动作模仿+跳舞+剑舞=Animate wan2.2_2047571961420713986.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_48

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（视频生成/图生视频/Wan+AnimateV2动作迁移工作流_1995333956365115393.json、视频生成/图生视频/Wan2.2 Animate 动作迁移（手动版）_2053044709232263170.json、视频生成/图生视频/Wan2.2 Animate-动作迁移_2011410598436806658.json、视频生成/图生视频/Wan2.2 Animate-动作迁移_2011439752528011266.json、视频生成/图生视频/Wan2.2 Animate动作迁移长视频生成加速版_1969252099450150913.json…）

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
