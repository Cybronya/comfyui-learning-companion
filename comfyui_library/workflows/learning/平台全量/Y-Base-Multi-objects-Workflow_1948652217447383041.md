---
key: 平台全量/Y-Base-Multi-objects-Workflow_1948652217447383041.json
name: Y-Base-Multi-objects-Workflow_1948652217447383041
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Y-Base-Multi-objects-Workflow_1948652217447383041.json
hash: 60edd2918cd8d5a4
coverage: 1
learned_at: 2026-11-14 01:07:40
nodes: [basic_Ksampler_simple, SaveImage, Mask_split_mulMask, pre_Kontext_mul, LoadImage, LoadImage, sum_load_adv]
patterns: []
missing: []
---

# 平台全量/Y-Base-Multi-objects-Workflow_1948652217447383041.json

> 来源文件 `comfyui_library/workflows/平台全量/Y-Base-Multi-objects-Workflow_1948652217447383041.json`

## 结构

**生成流程**：Sampling → Output → Other

**节点**（7 个）：
- `basic_Ksampler_simple` ★核心
- `SaveImage`
- `Mask_split_mulMask`
- `pre_Kontext_mul`
- `LoadImage`
- `LoadImage`
- `sum_load_adv`

## 知识

覆盖率 **100%**（7/7）

**有卡**：`basic_Ksampler_simple`、`SaveImage`、`Mask_split_mulMask`、`pre_Kontext_mul`、`LoadImage`、`sum_load_adv`

**用到的条目**：LoadImage、basic_Ksampler_simple、SaveImage、Mask_split_mulMask、pre_Kontext_mul、sum_load_adv、KSampler、image_to_image_controlnet_face_detailer_lora
