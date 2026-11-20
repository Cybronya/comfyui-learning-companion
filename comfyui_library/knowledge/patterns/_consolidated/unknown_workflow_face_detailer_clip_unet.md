---
name: unknown_workflow_face_detailer_clip_unet
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.923
common_nodes: [CLIPTextEncode, DualCLIPLoader, FaceDetailer, LoadImage, SAMLoader, SaveImage, UNETLoader, UltralyticsDetectorProvider, VAELoader]
problems: []
missing: []
members: [平台全量/lora 换脸 - F.1_1899062120691187714.json, 平台全量/修图之脸部修复Flux版_1933308088730431489.json]
source: knowledge_consolidation
---

# unknown_workflow_face_detailer_clip_unet

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/lora 换脸 - F.1_1899062120691187714.json、平台全量/修图之脸部修复Flux版_1933308088730431489.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FaceDetailer`
- `LoadImage`
- `SAMLoader`
- `SaveImage`
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncodeFlux` —— 1/2 个有
- `CR Text` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
