---
key: 图片生成/图生图/Image Masking Collection7合1抠图+抠图去除背景_2097859749982334977.json
name: Image Masking Collection7合1抠图+抠图去除背景_2097859749982334977
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Image Masking Collection7合1抠图+抠图去除背景_2097859749982334977.json
hash: 67a15d88c38fe0b8
coverage: 0.652174
learned_at: 2026-10-21 00:40:21
nodes: [Reroute, PreviewImage, LoadImage, PreviewImage, PreviewImage, PreviewImage, SaveImage, SaveImage, SaveImage, SaveImage, PreviewImage, PreviewImage, LayerMask: SegmentAnythingUltra V2, LayerMask: SegmentAnythingUltra V2, BiRefNet_Zho, BiRefNet_ModelLoader_Zho, LayerMask: BiRefNetUltra, SaveImage, InspyrenetRembg, SaveImage, easy imageRemBg, LayerMask: BiRefNetUltra, PreviewImage]
patterns: []
missing: []
---

# 图片生成/图生图/Image Masking Collection7合1抠图+抠图去除背景_2097859749982334977.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Image Masking Collection7合1抠图+抠图去除背景_2097859749982334977.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（23 个）：
- `Reroute`
- `PreviewImage`
- `LoadImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerMask: SegmentAnythingUltra V2`
- `BiRefNet_Zho`
- `BiRefNet_ModelLoader_Zho`
- `LayerMask: BiRefNetUltra`
- `SaveImage`
- `InspyrenetRembg`
- `SaveImage`
- `easy imageRemBg`
- `LayerMask: BiRefNetUltra`
- `PreviewImage`

## 知识

覆盖率 **65%**（15/23）

**有卡**：`LoadImage`、`SaveImage`、`LayerMask: SegmentAnythingUltra V2`、`BiRefNet_Zho`、`BiRefNet_ModelLoader_Zho`、`LayerMask: BiRefNetUltra`、`InspyrenetRembg`、`easy imageRemBg`

**用到的条目**：LoadImage、SaveImage、InspyrenetRembg、BiRefNet_ModelLoader_Zho、BiRefNet_Zho、easy imageRemBg、LayerMask: BiRefNetUltra、LayerMask: SegmentAnythingUltra V2
