---
name: unknown_workflow_video_clip_checkpoint_4
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, MaskToImage, SAM3_Detect, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded]
problems: []
missing: []
members: [平台全量/Sam3.1更精准的遮罩提取_2051996677657116673.json, 平台全量/视频Sam3.1遮罩提取_2054085347423866881.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_checkpoint_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Sam3.1更精准的遮罩提取_2051996677657116673.json、平台全量/视频Sam3.1遮罩提取_2054085347423866881.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `MaskToImage`
- `SAM3_Detect`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`

**可变部分**（部分 workflow 才有）：
- `DeepTranslatorTextNode` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
