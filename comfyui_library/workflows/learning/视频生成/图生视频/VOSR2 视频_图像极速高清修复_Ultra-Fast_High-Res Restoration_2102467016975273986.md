---
key: 视频生成/图生视频/VOSR2 视频_图像极速高清修复_Ultra-Fast_High-Res Restoration_2102467016975273986.json
name: VOSR2 视频_图像极速高清修复_Ultra-Fast_High-Res Restoration_2102467016975273986
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/VOSR2 视频_图像极速高清修复_Ultra-Fast_High-Res Restoration_2102467016975273986.json
hash: 1f1d08d522e0d9f6
coverage: 0.653846
learned_at: 2026-10-15 22:42:57
nodes: [Reroute, Reroute, 孤海注释, Int, 数学运算_孤海, MarkdownNote, VHS_LoadVideo, VOSR2Upscale, VOSR2ModelLoader, LayerFilter: GaussianBlur, easy imageSizeByLongerSide, VHS_VideoCombine, VOSR2ModelLoader, easy imageSizeByLongerSide, Reroute, Reroute, LayerFilter: GaussianBlur, 数学运算_孤海, 孤海注释, 忽略多组孤海, 孤海注释, LoadImage, GoohaiUniversalSlider, Image Comparer (rgthree), VOSR2Upscale, SaveImage]
patterns: []
missing: []
---

# 视频生成/图生视频/VOSR2 视频_图像极速高清修复_Ultra-Fast_High-Res Restoration_2102467016975273986.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/VOSR2 视频_图像极速高清修复_Ultra-Fast_High-Res Restoration_2102467016975273986.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（26 个）：
- `Reroute`
- `Reroute`
- `孤海注释`
- `Int`
- `数学运算_孤海`
- `MarkdownNote`
- `VHS_LoadVideo`
- `VOSR2Upscale`
- `VOSR2ModelLoader`
- `LayerFilter: GaussianBlur`
- `easy imageSizeByLongerSide`
- `VHS_VideoCombine`
- `VOSR2ModelLoader`
- `easy imageSizeByLongerSide`
- `Reroute`
- `Reroute`
- `LayerFilter: GaussianBlur`
- `数学运算_孤海`
- `孤海注释`
- `忽略多组孤海`
- `孤海注释`
- `LoadImage`
- `GoohaiUniversalSlider`
- `Image Comparer (rgthree)`
- `VOSR2Upscale`
- `SaveImage`

## 知识

覆盖率 **65%**（17/26）

**有卡**：`Int`、`数学运算_孤海`、`VHS_LoadVideo`、`VOSR2Upscale`、`VOSR2ModelLoader`、`LayerFilter: GaussianBlur`、`easy imageSizeByLongerSide`、`VHS_VideoCombine`、`忽略多组孤海`、`LoadImage`、`GoohaiUniversalSlider`、`SaveImage`

**用到的条目**：LoadImage、VOSR2Upscale、easy imageSizeByLongerSide、SaveImage、Int、VHS_LoadVideo、VHS_VideoCombine、VOSR2ModelLoader
