---
name: unknown_workflow_face_detailer_clip_checkpoint_2
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9545
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, FaceDetailer, LoadImage, SAMLoader, SaveImage, UltralyticsDetectorProvider]
problems: []
missing: []
members: [图片生成/图生图/Lora版脸部修复工作流_1968371597436432386.json, 图片生成/图生图/PS人脸修复 磨皮、去油、去痘、祛疤痕_1921577936384884738.json]
source: knowledge_consolidation
---

# unknown_workflow_face_detailer_clip_checkpoint_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Lora版脸部修复工作流_1968371597436432386.json、图片生成/图生图/PS人脸修复 磨皮、去油、去痘、祛疤痕_1921577936384884738.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `FaceDetailer`
- `LoadImage`
- `SAMLoader`
- `SaveImage`
- `UltralyticsDetectorProvider`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有
- `Lora Loader Stack (rgthree)` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `SEGSRangeFilterDetailerHookProvider` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.6 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
