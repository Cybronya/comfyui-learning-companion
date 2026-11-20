---
name: unknown_workflow_checkpoint_unet
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7335
common_nodes: [CreateVideo, DrawBBoxes, GetVideoComponents, ImageBlend, LoadVideo, PreviewImage, PrimitiveInt, ResizeImageMaskNode, SaveVideo]
problems: []
missing: []
members: [comfyui-workflow-templates-json/utility_sdpose_multi_person_video.json, 平台全量/提取视频人物动态姿态骨骼_2081940321721737217.json]
source: knowledge_consolidation
---

# unknown_workflow_checkpoint_unet

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（comfyui-workflow-templates-json/utility_sdpose_multi_person_video.json、平台全量/提取视频人物动态姿态骨骼_2081940321721737217.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `CreateVideo`
- `DrawBBoxes`
- `GetVideoComponents`
- `ImageBlend`
- `LoadVideo`
- `PreviewImage`
- `PrimitiveInt`
- `ResizeImageMaskNode`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `01b6a731-fb78-4070-9a38-c87146da9604` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `RTDETR_detect` —— 1/2 个有
- `SDPoseDrawKeypoints` —— 1/2 个有
- `SDPoseKeypointExtractor` —— 1/2 个有
- `UNETLoader` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
