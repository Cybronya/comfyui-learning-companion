---
key: 图片生成/图生图/万能抠图 细到发丝｜BiRefNet_V2-_Inspyrenet_Rembg_2079876944308563969.json
name: 万能抠图 细到发丝｜BiRefNet_V2-_Inspyrenet_Rembg_2079876944308563969
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/万能抠图 细到发丝｜BiRefNet_V2-_Inspyrenet_Rembg_2079876944308563969.json
hash: 931c8821b51e4ff8
coverage: 0.95
learned_at: 2026-10-21 00:47:14
nodes: [SaveImage, LoadImage, BiRefNet_Zho, LoadImage, MaskPreview+, MaskToImage, PreviewImage, MaskToImage, VHS_VideoCombine, VHS_VideoCombine, LoadImage, BiRefNet_ModelLoader_Zho, VHS_LoadVideo, BiRefNet_Hugo, BiRefNet_Hugo, SaveImage, SaveImage, MaskToImage, InspyrenetRembg, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/万能抠图 细到发丝｜BiRefNet_V2-_Inspyrenet_Rembg_2079876944308563969.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/万能抠图 细到发丝｜BiRefNet_V2-_Inspyrenet_Rembg_2079876944308563969.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（20 个）：
- `SaveImage`
- `LoadImage`
- `BiRefNet_Zho`
- `LoadImage`
- `MaskPreview+`
- `MaskToImage`
- `PreviewImage`
- `MaskToImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `BiRefNet_ModelLoader_Zho`
- `VHS_LoadVideo`
- `BiRefNet_Hugo`
- `BiRefNet_Hugo`
- `SaveImage`
- `SaveImage`
- `MaskToImage`
- `InspyrenetRembg`
- `SaveImage`

## 知识

覆盖率 **95%**（19/20）

**有卡**：`SaveImage`、`LoadImage`、`BiRefNet_Zho`、`MaskPreview+`、`MaskToImage`、`VHS_VideoCombine`、`BiRefNet_ModelLoader_Zho`、`VHS_LoadVideo`、`BiRefNet_Hugo`、`InspyrenetRembg`

**用到的条目**：LoadImage、SaveImage、MaskPreview+、MaskPreview+、VHS_LoadVideo、VHS_VideoCombine、InspyrenetRembg、MaskToImage
