---
name: unknown_workflow_face_detailer_clip_checkpoint_4
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.675
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ComfyWordCloud, FaceDetailer, GetNode, Image Blending Mode, Image Film Grain, Image Rembg (Remove Background), Image Style Filter, PreviewImage, RH_Prompter, SAMLoader, SaveImage, SetNode, UltralyticsDetectorProvider]
problems: []
missing: []
members: [平台全量/图生词云海报_1820653662459834370.json, 平台全量/词云海报_1804039343433572353.json]
source: knowledge_consolidation
---

# unknown_workflow_face_detailer_clip_checkpoint_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/图生词云海报_1820653662459834370.json、平台全量/词云海报_1804039343433572353.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyWordCloud`
- `FaceDetailer`
- `GetNode`
- `Image Blending Mode`
- `Image Film Grain`
- `Image Rembg (Remove Background)`
- `Image Style Filter`
- `PreviewImage`
- `RH_Prompter`
- `SAMLoader`
- `SaveImage`
- `SetNode`
- `UltralyticsDetectorProvider`

**可变部分**（部分 workflow 才有）：
- `ArgosTranslateTextNode` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `RH_Imagine` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `Textbox` —— 1/2 个有
- `WD14Tagger|pysssss` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
