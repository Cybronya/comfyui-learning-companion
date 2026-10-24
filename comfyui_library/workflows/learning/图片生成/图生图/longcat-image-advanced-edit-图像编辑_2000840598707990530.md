---
key: 图片生成/图生图/longcat-image-advanced-edit-图像编辑_2000840598707990530.json
name: longcat-image-advanced-edit-图像编辑_2000840598707990530
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/longcat-image-advanced-edit-图像编辑_2000840598707990530.json
hash: 5502f50360c723b4
coverage: 0.888889
learned_at: 2026-10-23 11:40:53
nodes: [PreviewImage, LongCatImageModelLoader, GetImageSize, EmptyImage, ImageCompositeMasked, LongCatImageEdit, AddLabel, SaveImage, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/longcat-image-advanced-edit-图像编辑_2000840598707990530.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/longcat-image-advanced-edit-图像编辑_2000840598707990530.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（9 个）：
- `PreviewImage`
- `LongCatImageModelLoader`
- `GetImageSize`
- `EmptyImage`
- `ImageCompositeMasked`
- `LongCatImageEdit`
- `AddLabel`
- `SaveImage`
- `LoadImage`

## 知识

覆盖率 **89%**（8/9）

**有卡**：`LongCatImageModelLoader`、`GetImageSize`、`EmptyImage`、`ImageCompositeMasked`、`LongCatImageEdit`、`AddLabel`、`SaveImage`、`LoadImage`

**用到的条目**：LoadImage、GetImageSize、GetImageSize、SaveImage、AddLabel、EmptyImage、ImageCompositeMasked、LongCatImageModelLoader
