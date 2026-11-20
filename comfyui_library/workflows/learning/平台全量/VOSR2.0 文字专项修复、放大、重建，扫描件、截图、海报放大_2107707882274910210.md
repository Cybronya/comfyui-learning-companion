---
key: 平台全量/VOSR2.0 文字专项修复、放大、重建，扫描件、截图、海报放大_2107707882274910210.json
name: VOSR2.0 文字专项修复、放大、重建，扫描件、截图、海报放大_2107707882274910210
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/VOSR2.0 文字专项修复、放大、重建，扫描件、截图、海报放大_2107707882274910210.json
hash: fe1b0fe016be4272
coverage: 0.514286
learned_at: 2026-11-14 01:02:58
nodes: [VOSR2ModelLoader, GetNode, SetNode, VOSR2Upscale, Fast Groups Bypasser (rgthree), MarkdownNote, GetNode, ImageCASharpening+, LayerFilter: GaussianBlur, ImageResize+, ImpactInt, Get Image Size, ImpactMinMax, SetNode, ImageResize+, SetNode, SimpleMath+, SeedVR2, TTP_Image_Assy, TTP_Image_Tile_Batch, easy cleanGpuUsed, ImpactInt, ImageCASharpening+, GetNode, GetNode, Any Switch (rgthree), SaveImage, GetNode, GetNode, Any Switch (rgthree), GetNode, Image Comparer (rgthree), LoadImage, 孤海注释, MarkdownNote]
patterns: []
missing: []
---

# 平台全量/VOSR2.0 文字专项修复、放大、重建，扫描件、截图、海报放大_2107707882274910210.json

> 来源文件 `comfyui_library/workflows/平台全量/VOSR2.0 文字专项修复、放大、重建，扫描件、截图、海报放大_2107707882274910210.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（35 个）：
- `VOSR2ModelLoader`
- `GetNode`
- `SetNode`
- `VOSR2Upscale`
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`
- `GetNode`
- `ImageCASharpening+`
- `LayerFilter: GaussianBlur`
- `ImageResize+`
- `ImpactInt`
- `Get Image Size`
- `ImpactMinMax`
- `SetNode`
- `ImageResize+`
- `SetNode`
- `SimpleMath+`
- `SeedVR2`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `easy cleanGpuUsed`
- `ImpactInt`
- `ImageCASharpening+`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `SaveImage`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `GetNode`
- `Image Comparer (rgthree)`
- `LoadImage`
- `孤海注释`
- `MarkdownNote`

## 知识

覆盖率 **51%**（18/35）

**有卡**：`VOSR2ModelLoader`、`VOSR2Upscale`、`ImageCASharpening+`、`LayerFilter: GaussianBlur`、`ImageResize+`、`ImpactInt`、`Get Image Size`、`ImpactMinMax`、`SimpleMath+`、`SeedVR2`、`TTP_Image_Assy`、`TTP_Image_Tile_Batch`、`easy cleanGpuUsed`、`SaveImage`、`LoadImage`

**用到的条目**：LoadImage、SeedVR2、VOSR2Upscale、Get Image Size、ImageResize+、SaveImage、easy cleanGpuUsed、ImageCASharpening+
