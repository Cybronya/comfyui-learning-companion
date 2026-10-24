---
name: unknown_workflow_face_detailer_lora_clip
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9425
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FaceDetailer, FluxGuidance, LoadImage, LoraLoaderModelOnly, PreviewImage, SDXLPromptStyler, SaveImage, UNETLoader, UltralyticsDetectorProvider, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/图片-修复脸跟手+高清放大_1966402567116894209.json, 图片生成/图生图/高清人像放大+修复手脸_1934782742540558337.json, 图片生成/图生图/高清放大+修复（人像）_1900359565094039554.json, 图片生成/图生图/高清放大+修复（人像）_1920760596969754626.json]
source: knowledge_consolidation
---

# unknown_workflow_face_detailer_lora_clip

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/图片-修复脸跟手+高清放大_1966402567116894209.json、图片生成/图生图/高清人像放大+修复手脸_1934782742540558337.json、图片生成/图生图/高清放大+修复（人像）_1900359565094039554.json、图片生成/图生图/高清放大+修复（人像）_1920760596969754626.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FaceDetailer`
- `FluxGuidance`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SDXLPromptStyler`
- `SaveImage`
- `UNETLoader`
- `UltralyticsDetectorProvider`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DF_Image_scale_to_side` —— 2/4 个有
- `Efficient Loader` —— 2/4 个有
- `SUPIR_Upscale` —— 2/4 个有
- `UltimateSDUpscale` —— 2/4 个有
- `UpscaleModelLoader` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
