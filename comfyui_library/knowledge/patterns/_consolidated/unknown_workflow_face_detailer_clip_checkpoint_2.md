---
name: unknown_workflow_face_detailer_clip_checkpoint_2
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.888
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, FaceDetailer, LoadImage, PreviewImage, SAMLoader, SaveImage, UltralyticsDetectorProvider, WD14Tagger|pysssss]
problems: []
missing: []
members: [图片生成/图生图/脸部精修_1928302431636209665.json, 图片生成/文生图/sd1.5文生图换脸_1894364757380497410.json, 平台全量/韩系甜妹妆容_1810593662605701121.json]
source: knowledge_consolidation
---

# unknown_workflow_face_detailer_clip_checkpoint_2

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/脸部精修_1928302431636209665.json、图片生成/文生图/sd1.5文生图换脸_1894364757380497410.json、平台全量/韩系甜妹妆容_1810593662605701121.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
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
- `ColorMatch` —— 2/3 个有
- `IPAdapterFaceID` —— 2/3 个有
- `IPAdapterUnifiedLoaderFaceID` —— 2/3 个有
- `CCSR_Model_Select` —— 1/3 个有
- `CCSR_Upscale` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
