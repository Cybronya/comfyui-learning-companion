---
name: unknown_workflow_video_sampler_20
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.916
common_nodes: [DownloadAndLoadMimicMotionModel, GetImageSizeAndCount, LoadImage, MimicMotionDecode, MimicMotionGetPoses, MimicMotionSampler, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/CG迷-指定动作，视频捕抓，骨骼动画复刻_1927027434896654338.json, 视频生成/图生视频/MimicMotion 上传图片生成跳舞 图生视频跳舞_1953091916986519553.json, 视频生成/图生视频/MimicMotion 动作迁移（带教学）_2036712403487956993.json, 视频生成/图生视频/MimicMotion万能舞蹈视频_1909815248260427777.json, 视频生成/图生视频/人物视频动作迁移MimicMotion+换脸修复_1971772867861999618.json, 视频生成/图生视频/基于mimicmotion的图片跳舞工作流_1898671504601894913.json, 视频生成/图生视频/美女网红舞蹈AI视频生成器 一键图像参考视频风格转换工作流-StarAI_1898791557779410945.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_20

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/CG迷-指定动作，视频捕抓，骨骼动画复刻_1927027434896654338.json、视频生成/图生视频/MimicMotion 上传图片生成跳舞 图生视频跳舞_1953091916986519553.json、视频生成/图生视频/MimicMotion 动作迁移（带教学）_2036712403487956993.json、视频生成/图生视频/MimicMotion万能舞蹈视频_1909815248260427777.json、视频生成/图生视频/人物视频动作迁移MimicMotion+换脸修复_1971772867861999618.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `DownloadAndLoadMimicMotionModel`
- `GetImageSizeAndCount`
- `LoadImage`
- `MimicMotionDecode`
- `MimicMotionGetPoses`
- `MimicMotionSampler`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 5/7 个有
- `RIFE VFI` —— 5/7 个有
- `DiffusersScheduler` —— 4/7 个有
- `ImageScale` —— 3/7 个有
- `ImageCASharpening+` —— 2/7 个有
- `ImageConcatMulti` —— 2/7 个有
- `ReActorFaceSwap` —— 2/7 个有
- `EmptyImage` —— 1/7 个有
- `ImageResize+` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `Note Plus (mtb)` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `easy imageSize` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
