---
key: 平台全量/qwen3.5-9B VS gemma4-26B-A4B 反推对比_2042174973921464321.json
name: qwen3.5-9B VS gemma4-26B-A4B 反推对比_2042174973921464321
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/qwen3.5-9B VS gemma4-26B-A4B 反推对比_2042174973921464321.json
hash: 58b13964bbebe106
coverage: 0.857143
learned_at: 2026-11-14 01:16:36
nodes: [llama_cpp_parameters, ShowText|pysssss, ShowText|pysssss, llama_cpp_parameters, LoadImage, LoadImage, llama_cpp_model_loader, llama_cpp_model_loader, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, llama_cpp_instruct_adv, easy saveText, llama_cpp_instruct_adv, easy saveText]
patterns: []
missing: []
---

# 平台全量/qwen3.5-9B VS gemma4-26B-A4B 反推对比_2042174973921464321.json

> 来源文件 `comfyui_library/workflows/平台全量/qwen3.5-9B VS gemma4-26B-A4B 反推对比_2042174973921464321.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（14 个）：
- `llama_cpp_parameters`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `llama_cpp_parameters`
- `LoadImage`
- `LoadImage`
- `llama_cpp_model_loader`
- `llama_cpp_model_loader`
- `LayerUtility: PurgeVRAM V2`
- `LayerUtility: PurgeVRAM V2`
- `llama_cpp_instruct_adv`
- `easy saveText`
- `llama_cpp_instruct_adv`
- `easy saveText`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`llama_cpp_parameters`、`LoadImage`、`llama_cpp_model_loader`、`LayerUtility: PurgeVRAM V2`、`llama_cpp_instruct_adv`、`easy saveText`

**用到的条目**：LoadImage、easy saveText、LayerUtility: PurgeVRAM V2、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、image_to_image_controlnet_face_detailer_lora、image_to_image_controlnet_face_detailer_lora_2
