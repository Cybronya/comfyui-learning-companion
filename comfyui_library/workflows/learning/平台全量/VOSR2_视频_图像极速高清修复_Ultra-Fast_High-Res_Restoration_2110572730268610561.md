---
key: 平台全量/VOSR2_视频_图像极速高清修复_Ultra-Fast_High-Res_Restoration_2110572730268610561.json
name: VOSR2_视频_图像极速高清修复_Ultra-Fast_High-Res_Restoration_2110572730268610561
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/VOSR2_视频_图像极速高清修复_Ultra-Fast_High-Res_Restoration_2110572730268610561.json
hash: 7230784e3bb21b14
coverage: 0.653846
learned_at: 2026-11-14 01:03:03
nodes: [Reroute, Reroute, 孤海注释, Int, 数学运算_孤海, MarkdownNote, VHS_LoadVideo, VOSR2Upscale, VOSR2ModelLoader, LayerFilter: GaussianBlur, easy imageSizeByLongerSide, VHS_VideoCombine, VOSR2ModelLoader, easy imageSizeByLongerSide, Reroute, Reroute, LayerFilter: GaussianBlur, 数学运算_孤海, 孤海注释, 忽略多组孤海, 孤海注释, LoadImage, GoohaiUniversalSlider, Image Comparer (rgthree), VOSR2Upscale, SaveImage]
patterns: []
missing: []
---

# 平台全量/VOSR2_视频_图像极速高清修复_Ultra-Fast_High-Res_Restoration_2110572730268610561.json

> 来源文件 `comfyui_library/workflows/平台全量/VOSR2_视频_图像极速高清修复_Ultra-Fast_High-Res_Restoration_2110572730268610561.json`

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

**用到的条目**：LoadImage、VOSR2Upscale、easy imageSizeByLongerSide、SaveImage、GoohaiUniversalSlider、Int、LayerFilter: GaussianBlur、忽略多组孤海
