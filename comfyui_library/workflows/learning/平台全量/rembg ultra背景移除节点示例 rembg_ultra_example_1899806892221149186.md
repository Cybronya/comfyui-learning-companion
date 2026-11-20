---
key: 平台全量/rembg ultra背景移除节点示例 rembg_ultra_example_1899806892221149186.json
name: rembg ultra背景移除节点示例 rembg_ultra_example_1899806892221149186
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/rembg ultra背景移除节点示例 rembg_ultra_example_1899806892221149186.json
hash: 1f791eedbf50e1cf
coverage: 0.846154
learned_at: 2026-11-14 01:16:54
nodes: [LayerMask: MaskPreview, LayerMask: MaskPreview, Reroute, Image Remove Background Rembg (mtb), Reroute, LayerMask: PixelSpread, LoadImage, LoadImage, LayerUtility: ImageBlendAdvance, LayerUtility: ImageBlendAdvance, SaveImage, SaveImage, LayerMask: RemBgUltra]
patterns: []
missing: []
---

# 平台全量/rembg ultra背景移除节点示例 rembg_ultra_example_1899806892221149186.json

> 来源文件 `comfyui_library/workflows/平台全量/rembg ultra背景移除节点示例 rembg_ultra_example_1899806892221149186.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（13 个）：
- `LayerMask: MaskPreview`
- `LayerMask: MaskPreview`
- `Reroute`
- `Image Remove Background Rembg (mtb)`
- `Reroute`
- `LayerMask: PixelSpread`
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageBlendAdvance`
- `LayerUtility: ImageBlendAdvance`
- `SaveImage`
- `SaveImage`
- `LayerMask: RemBgUltra`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`LayerMask: MaskPreview`、`Image Remove Background Rembg (mtb)`、`LayerMask: PixelSpread`、`LoadImage`、`LayerUtility: ImageBlendAdvance`、`SaveImage`、`LayerMask: RemBgUltra`

**用到的条目**：LoadImage、LayerMask: MaskPreview、SaveImage、Image Remove Background Rembg (mtb)、LayerMask: RemBgUltra、LayerUtility: ImageBlendAdvance、LayerMask: PixelSpread、image_to_image_controlnet_face_detailer_lora
