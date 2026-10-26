---
key: 图片生成/反推提示词/图片打标保存节点示例 image_tagger_save_example_1899791787827802114.json
name: 图片打标保存节点示例 image_tagger_save_example_1899791787827802114
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/图片打标保存节点示例 image_tagger_save_example_1899791787827802114.json
hash: 7722fc2d39928dee
coverage: 0.8
learned_at: 2026-10-26 01:47:55
nodes: [LayerMask: LoadFlorence2Model, LayerUtility: Florence2Image2Prompt, Reroute, Reroute, LayerMask: YoloV8Detect, LayerUtility: String, LayerUtility: ImageTaggerSave, LayerUtility: ImageAutoCrop V3, SaveImage, LoadImageListFromDir //Inspire]
patterns: []
missing: []
---

# 图片生成/反推提示词/图片打标保存节点示例 image_tagger_save_example_1899791787827802114.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/图片打标保存节点示例 image_tagger_save_example_1899791787827802114.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（10 个）：
- `LayerMask: LoadFlorence2Model`
- `LayerUtility: Florence2Image2Prompt`
- `Reroute`
- `Reroute`
- `LayerMask: YoloV8Detect`
- `LayerUtility: String`
- `LayerUtility: ImageTaggerSave`
- `LayerUtility: ImageAutoCrop V3`
- `SaveImage`
- `LoadImageListFromDir //Inspire`

## 知识

覆盖率 **80%**（8/10）

**有卡**：`LayerMask: LoadFlorence2Model`、`LayerUtility: Florence2Image2Prompt`、`LayerMask: YoloV8Detect`、`LayerUtility: String`、`LayerUtility: ImageTaggerSave`、`LayerUtility: ImageAutoCrop V3`、`SaveImage`、`LoadImageListFromDir //Inspire`

**用到的条目**：LayerUtility: Florence2Image2Prompt、SaveImage、LayerUtility: ImageTaggerSave、LayerMask: LoadFlorence2Model、LayerUtility: ImageAutoCrop V3、LoadImageListFromDir //Inspire、LayerMask: YoloV8Detect、LayerUtility: String
