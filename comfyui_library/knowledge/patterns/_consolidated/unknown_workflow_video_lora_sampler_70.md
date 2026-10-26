---
name: unknown_workflow_video_lora_sampler_70
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.8242
common_nodes: [CLIPVisionLoader, LoadImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan+AnimateV2动作迁移工作流_1995333956365115393.json, 视频生成/图生视频/Wan2.2 Animate 动作迁移（手动版）_2053044709232263170.json, 视频生成/图生视频/Wan2.2 Animate-动作迁移_2011410598436806658.json, 视频生成/图生视频/Wan2.2 Animate-动作迁移_2011439752528011266.json, 视频生成/图生视频/Wan2.2 Animate动作迁移长视频生成加速版_1969252099450150913.json, 视频生成/图生视频/Wan2.2 Animate：角色动画革新，表演艺术的完美复刻！角色替换、动作迁移、图生视频_1969217356767653890.json, 视频生成/图生视频/Wan2.2+Animate+角色替换视频动作迁移+KJ加速版_1993551269581225986.json, 视频生成/图生视频/Wan2.2+Animate：角色替换、动作迁移、图生视频 美女跳舞视频，表演艺术的完美复刻！_1979432276058607617.json, 视频生成/图生视频/Wan2.2-Animate-视频动作迁移_2067088794045734914.json, 视频生成/图生视频/Wan2.2-Animate-视频动作迁移_2069232638564593665.json, 视频生成/图生视频/Wan2.2Animate+DWPose动作模仿工作流！墙裂推荐！表情精准迁移_2038302872932192257.json, 视频生成/图生视频/【人物替换】Wan2.2+Animate+角色替换视频动作迁移+KJ加速版-StarAI_1982315306993500162.json, 视频生成/图生视频/优化版 人物模特替换 动作克隆 首尾帧+角色替换 Wan2.2+Animate+角色替换视频动作迁移_1995682413978193921.json, 视频生成/图生视频/全新 Animate美女跳舞动作迁移V8极速版_2017854030659194882.json, 视频生成/图生视频/新Wan2.2 Animate-动作迁移_1983713271683457025.json, 视频生成/图生视频/新版动作迁移美女跳舞！Wan2.2-Animate V2超极速版_1974863458778918913.json, 视频生成/图生视频/男用动作迁移复制一键跳舞Wan2.2-Animate-视频动作迁移_2067576219452919809.json, 视频生成/图生视频/美女图片生成跳舞视频_1975800896795881473.json, 视频生成/图生视频/美女跳舞视频复刻_1975790920316620801.json, 视频生成/文生视频/Wan2.2 Animate美女图片跳舞 视频动作迁移_1970282441866964994.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_70

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/Wan+AnimateV2动作迁移工作流_1995333956365115393.json、视频生成/图生视频/Wan2.2 Animate 动作迁移（手动版）_2053044709232263170.json、视频生成/图生视频/Wan2.2 Animate-动作迁移_2011410598436806658.json、视频生成/图生视频/Wan2.2 Animate-动作迁移_2011439752528011266.json、视频生成/图生视频/Wan2.2 Animate动作迁移长视频生成加速版_1969252099450150913.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 20 个 workflow 都包含：
- `CLIPVisionLoader`
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
- `DWPreprocessor` —— 19/20 个有
- `FaceMaskFromPoseKeypoints` —— 19/20 个有
- `ImageCropByMaskAndResize` —— 19/20 个有
- `ImageResizeKJv2` —— 19/20 个有
- `JWInteger` —— 19/20 个有
- `PixelPerfectResolution` —— 19/20 个有
- `WanVideoLoraSelectMulti` —— 19/20 个有
- `ImageConcatMulti` —— 13/20 个有
- `GetImageSizeAndCount` —— 12/20 个有
- `Text` —— 12/20 个有
- `WanVideoAnimateEmbeds` —— 12/20 个有
- `GetNode` —— 10/20 个有
- `SetNode` —— 10/20 个有
- `RHHiddenNodes` —— 9/20 个有
- `easy cleanGpuUsed` —— 8/20 个有
- `VHS_VideoInfo` —— 7/20 个有
- `LayerUtility: PurgeVRAM` —— 6/20 个有
- `PrimitiveStringMultiline` —— 4/20 个有
- `CR Text` —— 3/20 个有
- `Int` —— 3/20 个有
- `ImpactInt` —— 2/20 个有
- `PreviewImage` —— 2/20 个有
- `SaveImage` —— 2/20 个有
- `SimpleMath+` —— 2/20 个有
- `ImageResize+` —— 1/20 个有
- `LayerUtility: PurgeVRAM V2` —— 1/20 个有
- `TT_img_enc` —— 1/20 个有
- `VHS_VideoInfoLoaded` —— 1/20 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
