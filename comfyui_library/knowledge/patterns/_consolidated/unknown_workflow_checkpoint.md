---
name: unknown_workflow_checkpoint
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.659714
common_nodes: [CheckpointLoaderSimple, Image Comparer (rgthree), LoadImage, SUPIR_conditioner, SUPIR_decode, SUPIR_encode, SUPIR_first_stage, SUPIR_model_loader_v2, SUPIR_sample, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/SUPIR图像修复工作流_1969062503655370754.json, 图片生成/图生图/【阡陌】SUPIR超高清细节修复放大工作流_1902930665241743361.json, 图片生成/图生图/模糊图一键变清晰_V1_1958057559603236865.json, 平台全量/SDXL SUPIR高清放大_1909468387745869825.json, 平台全量/SUPIR高清图片超分放大一键4KLightning极速版_2080366816697872385.json, 平台全量/SUPIR高质量图像修复，风景、人脸、动物、游戏画面、老电影和老照片，可增强图像细节_1953666826658041857.json, 平台全量/高清放大_1806603389481996289.json]
source: knowledge_consolidation
---

# unknown_workflow_checkpoint

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/SUPIR图像修复工作流_1969062503655370754.json、图片生成/图生图/【阡陌】SUPIR超高清细节修复放大工作流_1902930665241743361.json、图片生成/图生图/模糊图一键变清晰_V1_1958057559603236865.json、平台全量/SDXL SUPIR高清放大_1909468387745869825.json、平台全量/SUPIR高清图片超分放大一键4KLightning极速版_2080366816697872385.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 7 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `Image Comparer (rgthree)`
- `LoadImage`
- `SUPIR_conditioner`
- `SUPIR_decode`
- `SUPIR_encode`
- `SUPIR_first_stage`
- `SUPIR_model_loader_v2`
- `SUPIR_sample`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 6/7 个有
- `PreviewImage` —— 4/7 个有
- `ColorMatch` —— 3/7 个有
- `GetNode` —— 3/7 个有
- `SetNode` —— 3/7 个有
- `SUPIR_Upscale` —— 2/7 个有
- `CLIPTextEncode` —— 1/7 个有
- `DF_Image_scale_to_side` —— 1/7 个有
- `Display Int (rgthree)` —— 1/7 个有
- `HD UltimateSDUpscale` —— 1/7 个有
- `ImpactInt` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `Seed (rgthree)` —— 1/7 个有
- `UpscaleModelLoader` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
