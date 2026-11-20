---
name: unknown_workflow_video_lora_sampler_183
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.841538
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, ImageResizeKJv2, LoadImage, PixelPerfectResolution, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/优化加速升级Wan Animate动作迁移v2版_1983091241221038082.json, 视频生成/图生视频/全新 Animate美女跳舞动作迁移V8极速版_2017854030659194882.json, 视频生成/图生视频/全新图片跳舞 保留原图背景 Animate Wan2.2_2018250280189562881.json, 视频生成/图生视频/啊癫 全新图片跳舞 保留原图背景 Animate Wan2.2_1970493244759044098.json, 视频生成/图生视频/图生视频 -快生成- AI动作模仿+跳舞+剑舞-Animate wan2.2_2034534867488219137.json, 视频生成/图生视频/图生视频 快生成 AI动作模仿+跳舞+剑舞-Animate wan2.2_2034431517451096065.json, 视频生成/图生视频/图生视频 快生成 AI动作模仿+跳舞+剑舞-Animate wan2.2_2046830049172656129.json, 视频生成/图生视频/图生视频+快生成Animate+wan2.2_2047135621176627201.json, 视频生成/图生视频/新版动作迁移美女跳舞！Wan2.2-Animate V2超极速版_1974863458778918913.json, 视频生成/图生视频/美女图片生成跳舞视频_1975800896795881473.json, 视频生成/图生视频/美女跳舞视频复刻_1975790920316620801.json, 视频生成/图生视频/高清流畅！AI动作模仿+跳舞+剑舞=AnimaAI动作模仿+跳舞+剑舞=Animate wan2.2_2047571961420713986.json, 视频生成/文生视频/Wan2.2 Animate美女图片跳舞 视频动作迁移_1970282441866964994.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_183

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/优化加速升级Wan Animate动作迁移v2版_1983091241221038082.json、视频生成/图生视频/全新 Animate美女跳舞动作迁移V8极速版_2017854030659194882.json、视频生成/图生视频/全新图片跳舞 保留原图背景 Animate Wan2.2_2018250280189562881.json、视频生成/图生视频/啊癫 全新图片跳舞 保留原图背景 Animate Wan2.2_1970493244759044098.json、视频生成/图生视频/图生视频 -快生成- AI动作模仿+跳舞+剑舞-Animate wan2.2_2034534867488219137.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `LoadImage`
- `PixelPerfectResolution`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
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
- `GetNode` —— 12/13 个有
- `JWInteger` —— 12/13 个有
- `LayerUtility: PurgeVRAM` —— 12/13 个有
- `SetNode` —— 12/13 个有
- `WanVideoLoraSelectMulti` —— 12/13 个有
- `easy cleanGpuUsed` —— 12/13 个有
- `Text` —— 10/13 个有
- `SimpleMath+` —— 7/13 个有
- `PrimitiveInt` —— 5/13 个有
- `ttN float` —— 5/13 个有
- `ImageConcatMulti` —— 4/13 个有
- `ImpactInt` —— 2/13 个有
- `PrimitiveStringMultiline` —— 2/13 个有
- `CR Prompt Text` —— 1/13 个有
- `FirstFrameSelector` —— 1/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/13 个有
- `RHHiddenNodes` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
