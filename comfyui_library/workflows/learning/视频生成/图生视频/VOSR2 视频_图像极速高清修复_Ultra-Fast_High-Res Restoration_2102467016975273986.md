---
key: 视频生成/图生视频/VOSR2 视频_图像极速高清修复_Ultra-Fast_High-Res Restoration_2102467016975273986.json
name: VOSR2 视频_图像极速高清修复_Ultra-Fast_High-Res Restoration_2102467016975273986
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/VOSR2 视频_图像极速高清修复_Ultra-Fast_High-Res Restoration_2102467016975273986.json
hash: 1f1d08d522e0d9f6
coverage: 0.384615
learned_at: 2026-10-10 22:54:20
nodes: [Reroute, Reroute, 孤海注释, Int, 数学运算_孤海, MarkdownNote, VHS_LoadVideo, VOSR2Upscale, VOSR2ModelLoader, LayerFilter: GaussianBlur, easy imageSizeByLongerSide, VHS_VideoCombine, VOSR2ModelLoader, easy imageSizeByLongerSide, Reroute, Reroute, LayerFilter: GaussianBlur, 数学运算_孤海, 孤海注释, 忽略多组孤海, 孤海注释, LoadImage, GoohaiUniversalSlider, Image Comparer (rgthree), VOSR2Upscale, SaveImage]
patterns: []
missing: [LayerFilter: GaussianBlur, LayerFilter: GaussianBlur, 忽略多组孤海, 数学运算_孤海, 数学运算_孤海, easy imageSizeByLongerSide, easy imageSizeByLongerSide]
discoveries: [次要节点 `LayerFilter: GaussianBlur` 知识库中没有该节点类型的任何知识, 次要节点 `LayerFilter: GaussianBlur` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `数学运算_孤海` 知识库中没有该节点类型的任何知识, 次要节点 `数学运算_孤海` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageSizeByLongerSide` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `easy imageSizeByLongerSide` 仅有 Resolution 的通用知识，没有该节点自己的说明]
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

覆盖率 **38%**（10/26）

**有卡**：`Int`、`VHS_LoadVideo`、`VOSR2Upscale`、`VOSR2ModelLoader`、`VHS_VideoCombine`、`LoadImage`、`GoohaiUniversalSlider`、`SaveImage`

**缺卡**（7）：`LayerFilter: GaussianBlur`、`LayerFilter: GaussianBlur`、`忽略多组孤海`、`数学运算_孤海`、`数学运算_孤海`、`easy imageSizeByLongerSide`、`easy imageSizeByLongerSide`

**用到的条目**：LoadImage、VOSR2Upscale、SaveImage、Int、VHS_LoadVideo、VHS_VideoCombine、VOSR2ModelLoader、GoohaiUniversalSlider

## 学习发现

- 次要节点 `LayerFilter: GaussianBlur` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerFilter: GaussianBlur` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `数学运算_孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `数学运算_孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageSizeByLongerSide` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `easy imageSizeByLongerSide` 仅有 Resolution 的通用知识，没有该节点自己的说明
