---
name: unknown_workflow_face_detailer_clip_checkpoint_3
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.92
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, FaceDetailer, LoadImage, PreviewImage, SAMLoader, SaveImage, UltralyticsDetectorProvider, WD14Tagger|pysssss]
problems: []
missing: []
members: [图片生成/图生图/脸部精修_1928302431636209665.json, 图片生成/文生图/sd1.5文生图换脸_1894364757380497410.json]
source: knowledge_consolidation
---

# unknown_workflow_face_detailer_clip_checkpoint_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/脸部精修_1928302431636209665.json、图片生成/文生图/sd1.5文生图换脸_1894364757380497410.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `FaceDetailer`
- `LoadImage`
- `PreviewImage`
- `SAMLoader`
- `SaveImage`
- `UltralyticsDetectorProvider`
- `WD14Tagger|pysssss`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `IPAdapterFaceID` —— 1/2 个有
- `IPAdapterUnifiedLoaderFaceID` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
