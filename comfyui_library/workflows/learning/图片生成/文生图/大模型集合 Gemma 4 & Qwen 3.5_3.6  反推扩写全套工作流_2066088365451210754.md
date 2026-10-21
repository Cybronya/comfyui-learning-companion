---
key: 图片生成/文生图/大模型集合 Gemma 4 & Qwen 3.5_3.6  反推扩写全套工作流_2066088365451210754.json
name: 大模型集合 Gemma 4 & Qwen 3.5_3.6  反推扩写全套工作流_2066088365451210754
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/大模型集合 Gemma 4 & Qwen 3.5_3.6  反推扩写全套工作流_2066088365451210754.json
hash: 6ac6fc94953c6523
coverage: 0.689655
learned_at: 2026-10-19 23:23:04
nodes: [Gemma4TE_ImageInfer, Gemma4TE_ModelLoader, ShowText|pysssss, QwenTE_ImageInfer, ShowText|pysssss, QwenTE_ModelLoader, CR Text, QwenTE_ImageInfer, CR Text, Gemma4TE_ModelLoader, ShowText|pysssss, CR Text, CR Text, QwenTE_ModelLoader, ShowText|pysssss, ShowText|pysssss, Gemma4TE_ImageInfer, QwenTE_ImageInfer, Gemma4TE_ModelLoader, Gemma4TE_ImageInfer, ShowText|pysssss, MultiImageLoader, Fast Groups Bypasser (rgthree), QwenTE_ModelLoader, Note, MultiImageLoader, MultiImageLoader, SaveImage, 孤海注释]
patterns: []
missing: []
---

# 图片生成/文生图/大模型集合 Gemma 4 & Qwen 3.5_3.6  反推扩写全套工作流_2066088365451210754.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/大模型集合 Gemma 4 & Qwen 3.5_3.6  反推扩写全套工作流_2066088365451210754.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（29 个）：
- `Gemma4TE_ImageInfer`
- `Gemma4TE_ModelLoader`
- `ShowText|pysssss`
- `QwenTE_ImageInfer`
- `ShowText|pysssss`
- `QwenTE_ModelLoader`
- `CR Text`
- `QwenTE_ImageInfer`
- `CR Text`
- `Gemma4TE_ModelLoader`
- `ShowText|pysssss`
- `CR Text`
- `CR Text`
- `QwenTE_ModelLoader`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `Gemma4TE_ImageInfer`
- `QwenTE_ImageInfer`
- `Gemma4TE_ModelLoader`
- `Gemma4TE_ImageInfer`
- `ShowText|pysssss`
- `MultiImageLoader`
- `Fast Groups Bypasser (rgthree)`
- `QwenTE_ModelLoader`
- `Note`
- `MultiImageLoader`
- `MultiImageLoader`
- `SaveImage`
- `孤海注释`

## 知识

覆盖率 **69%**（20/29）

**有卡**：`Gemma4TE_ImageInfer`、`Gemma4TE_ModelLoader`、`QwenTE_ImageInfer`、`QwenTE_ModelLoader`、`CR Text`、`MultiImageLoader`、`SaveImage`

**用到的条目**：SaveImage、MultiImageLoader、CR Text、QwenTE_ImageInfer、QwenTE_ModelLoader、Gemma4TE_ImageInfer、Gemma4TE_ModelLoader、sd15-t2i-basic
