---
key: 平台全量/【CN姿势控制】Qwen-Image  超强洗图模式 controlnet 姿态控制_1959407821030895617.json
name: 【CN姿势控制】Qwen-Image  超强洗图模式 controlnet 姿态控制_1959407821030895617
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【CN姿势控制】Qwen-Image  超强洗图模式 controlnet 姿态控制_1959407821030895617.json
hash: 49c6b139435b4acb
coverage: 0.777778
learned_at: 2026-11-14 01:21:37
nodes: [SaveImage, PreviewImage, QwenImageRatio2Size, GetControlImage, LoadQwenImageDiffSynthLora, LoadQwenImageDiffSynthiPipe, QwenImageDiffSynthSampler, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 平台全量/【CN姿势控制】Qwen-Image  超强洗图模式 controlnet 姿态控制_1959407821030895617.json

> 来源文件 `comfyui_library/workflows/平台全量/【CN姿势控制】Qwen-Image  超强洗图模式 controlnet 姿态控制_1959407821030895617.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（9 个）：
- `SaveImage`
- `PreviewImage`
- `QwenImageRatio2Size`
- `GetControlImage`
- `LoadQwenImageDiffSynthLora`
- `LoadQwenImageDiffSynthiPipe`
- `QwenImageDiffSynthSampler` ★核心
- `LoadImage`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **78%**（7/9）

**有卡**：`SaveImage`、`QwenImageRatio2Size`、`GetControlImage`、`LoadQwenImageDiffSynthLora`、`LoadQwenImageDiffSynthiPipe`、`QwenImageDiffSynthSampler`、`LoadImage`

**用到的条目**：LoadImage、QwenImageDiffSynthSampler、LoadQwenImageDiffSynthLora、QwenImageRatio2Size、SaveImage、GetControlImage、LoadQwenImageDiffSynthiPipe、image_to_image_controlnet_face_detailer_lora
