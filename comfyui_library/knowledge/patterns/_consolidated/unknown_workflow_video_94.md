---
name: unknown_workflow_video_94
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.814
common_nodes: [CR Text, DeleteVideoSegmentXC, DownloadAndLoadTransNetModelXC, GetVideoComponents, Int, LoadImage, PreviewAny, PreviewImage, RHHiddenNodes, RH_LLMAPI_NODE, RH_Nano_Banana2_Image2Image, SaveImage, SaveVideo, TransNetV2_Run, VHS_LoadVideoPath, VHS_VideoCombine, VideoConcatenatorXC, easy imageConcat]
problems: []
missing: []
members: [图片生成/文生图/25秒 TVB广告从分镜到视频 一键生成工作流 V2.5_2013535333492723713.json, 视频生成/文生视频/TVB广告从分镜到视频一键生成工作流 V1.0_2011854019462959106.json]
source: knowledge_consolidation
---

# unknown_workflow_video_94

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/25秒 TVB广告从分镜到视频 一键生成工作流 V2.5_2013535333492723713.json、视频生成/文生视频/TVB广告从分镜到视频一键生成工作流 V1.0_2011854019462959106.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `DeleteVideoSegmentXC`
- `DownloadAndLoadTransNetModelXC`
- `GetVideoComponents`
- `Int`
- `LoadImage`
- `PreviewAny`
- `PreviewImage`
- `RHHiddenNodes`
- `RH_LLMAPI_NODE`
- `RH_Nano_Banana2_Image2Image`
- `SaveImage`
- `SaveVideo`
- `TransNetV2_Run`
- `VHS_LoadVideoPath`
- `VHS_VideoCombine`
- `VideoConcatenatorXC`
- `easy imageConcat`

**可变部分**（部分 workflow 才有）：
- `FlashVSRNode` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `MuyeTextEditOutput` —— 1/2 个有
- `RH_Sora2_I2V` —— 1/2 个有
- `RH_Sora2_I2V_PRO` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
