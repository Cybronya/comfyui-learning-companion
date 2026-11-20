---
name: unknown_workflow_face_detailer_clip
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.889
common_nodes: [CLIPTextEncode, FaceDetailer, LoadImage, SaveImage, ShowText|pysssss, UltralyticsDetectorProvider, WD14Tagger|pysssss]
problems: []
missing: []
members: [图片生成/图生图/34号特工：真人转动漫图生图FLUX.1D_2030916206550585346.json, 图片生成/图生图/FLUX.1D 真人转动漫图生_1890367713309806593.json, 图片生成/图生图/FLUX.1D 真人转动漫图生图_1928750805300711426.json, 图片生成/文生图/最完善文生图像升级和增强版本_1890350193689141250.json]
source: knowledge_consolidation
---

# unknown_workflow_face_detailer_clip

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/34号特工：真人转动漫图生图FLUX.1D_2030916206550585346.json、图片生成/图生图/FLUX.1D 真人转动漫图生_1890367713309806593.json、图片生成/图生图/FLUX.1D 真人转动漫图生图_1928750805300711426.json、图片生成/文生图/最完善文生图像升级和增强版本_1890350193689141250.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `FaceDetailer`
- `LoadImage`
- `SaveImage`
- `ShowText|pysssss`
- `UltralyticsDetectorProvider`
- `WD14Tagger|pysssss`

**可变部分**（部分 workflow 才有）：
- `workflow/cn` —— 2/4 个有
- `workflow/模型` —— 2/4 个有
- `workflow>cn` —— 2/4 个有
- `workflow>模型` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
