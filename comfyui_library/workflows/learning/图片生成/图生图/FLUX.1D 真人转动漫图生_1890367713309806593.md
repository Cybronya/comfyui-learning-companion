---
key: 图片生成/图生图/FLUX.1D 真人转动漫图生_1890367713309806593.json
name: FLUX.1D 真人转动漫图生_1890367713309806593
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.1D 真人转动漫图生_1890367713309806593.json
hash: 8df15907eb923c73
coverage: 0.888889
learned_at: 2026-10-23 10:54:02
nodes: [UltralyticsDetectorProvider, WD14Tagger|pysssss, ShowText|pysssss, LoadImage, CLIPTextEncode, workflow/模型, FaceDetailer, workflow/cn, SaveImage]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.1D 真人转动漫图生_1890367713309806593.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.1D 真人转动漫图生_1890367713309806593.json`

## 结构

**生成流程**：Condition → Output → Other

**节点**（9 个）：
- `UltralyticsDetectorProvider`
- `WD14Tagger|pysssss`
- `ShowText|pysssss`
- `LoadImage`
- `CLIPTextEncode` ★核心
- `workflow/模型`
- `FaceDetailer`
- `workflow/cn`
- `SaveImage`

## 知识

覆盖率 **89%**（8/9）

**有卡**：`UltralyticsDetectorProvider`、`WD14Tagger|pysssss`、`LoadImage`、`CLIPTextEncode`、`workflow/模型`、`FaceDetailer`、`workflow/cn`、`SaveImage`

**用到的条目**：CLIPTextEncode、LoadImage、workflow/模型、SaveImage、FaceDetailer、UltralyticsDetectorProvider、WD14Tagger|pysssss、workflow/cn
