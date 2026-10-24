---
key: 图片生成/图生图/FLUX.1D 真人转动漫图生图_1928750805300711426.json
name: FLUX.1D 真人转动漫图生图_1928750805300711426
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FLUX.1D 真人转动漫图生图_1928750805300711426.json
hash: 787d6193f460c596
coverage: 0.888889
learned_at: 2026-10-23 10:54:02
nodes: [FaceDetailer, SaveImage, workflow>模型, WD14Tagger|pysssss, CLIPTextEncode, UltralyticsDetectorProvider, workflow>cn, ShowText|pysssss, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/FLUX.1D 真人转动漫图生图_1928750805300711426.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FLUX.1D 真人转动漫图生图_1928750805300711426.json`

## 结构

**生成流程**：Condition → Output → Other

**节点**（9 个）：
- `FaceDetailer`
- `SaveImage`
- `workflow>模型`
- `WD14Tagger|pysssss`
- `CLIPTextEncode` ★核心
- `UltralyticsDetectorProvider`
- `workflow>cn`
- `ShowText|pysssss`
- `LoadImage`

## 知识

覆盖率 **89%**（8/9）

**有卡**：`FaceDetailer`、`SaveImage`、`workflow>模型`、`WD14Tagger|pysssss`、`CLIPTextEncode`、`UltralyticsDetectorProvider`、`workflow>cn`、`LoadImage`

**用到的条目**：CLIPTextEncode、LoadImage、workflow>模型、SaveImage、FaceDetailer、UltralyticsDetectorProvider、WD14Tagger|pysssss、workflow>cn
