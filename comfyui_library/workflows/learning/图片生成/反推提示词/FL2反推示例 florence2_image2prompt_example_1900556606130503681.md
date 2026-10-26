---
key: 图片生成/反推提示词/FL2反推示例 florence2_image2prompt_example_1900556606130503681.json
name: FL2反推示例 florence2_image2prompt_example_1900556606130503681
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/FL2反推示例 florence2_image2prompt_example_1900556606130503681.json
hash: a5419569cd8612b9
coverage: 1
learned_at: 2026-10-26 01:45:01
nodes: [LoadImage, LayerMask: LoadFlorence2Model, LayerUtility: Florence2Image2Prompt, LayerUtility: ImageRemoveAlpha, SaveImage, LayerUtility: SimpleTextImage]
patterns: []
missing: []
---

# 图片生成/反推提示词/FL2反推示例 florence2_image2prompt_example_1900556606130503681.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/FL2反推示例 florence2_image2prompt_example_1900556606130503681.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（6 个）：
- `LoadImage`
- `LayerMask: LoadFlorence2Model`
- `LayerUtility: Florence2Image2Prompt`
- `LayerUtility: ImageRemoveAlpha`
- `SaveImage`
- `LayerUtility: SimpleTextImage`

## 知识

覆盖率 **100%**（6/6）

**有卡**：`LoadImage`、`LayerMask: LoadFlorence2Model`、`LayerUtility: Florence2Image2Prompt`、`LayerUtility: ImageRemoveAlpha`、`SaveImage`、`LayerUtility: SimpleTextImage`

**用到的条目**：LoadImage、LayerUtility: Florence2Image2Prompt、SaveImage、LayerMask: LoadFlorence2Model、LayerUtility: ImageRemoveAlpha、LayerUtility: SimpleTextImage、sd15-t2i-basic、sd15-t2i-lora
