---
key: 图片生成/反推提示词/反推-视频提示词2-Qwen3.8_2093273320954355714.json
name: 反推-视频提示词2-Qwen3.8_2093273320954355714
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/反推-视频提示词2-Qwen3.8_2093273320954355714.json
hash: de6c353059d75d6b
coverage: 0.8
learned_at: 2026-10-26 01:47:33
nodes: [easy saveText, llama_cpp_parameters, VHS_VideoInfoLoaded, GetImageSizeAndCount, LayerUtility: ImageScaleByAspectRatio V2, ShowText|pysssss, CreateVideo, easy showAnything, easy imageBatchToImageList, llama_cpp_model_loader, VHS_LoadVideo, easy showAnything, llama_cpp_instruct_adv, easy seed, easy positive]
patterns: []
missing: []
---

# 图片生成/反推提示词/反推-视频提示词2-Qwen3.8_2093273320954355714.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/反推-视频提示词2-Qwen3.8_2093273320954355714.json`

## 结构

**生成流程**：Model → Process → Output → Other

**节点**（15 个）：
- `easy saveText`
- `llama_cpp_parameters`
- `VHS_VideoInfoLoaded`
- `GetImageSizeAndCount`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ShowText|pysssss`
- `CreateVideo`
- `easy showAnything`
- `easy imageBatchToImageList`
- `llama_cpp_model_loader`
- `VHS_LoadVideo`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `easy seed`
- `easy positive`

## 知识

覆盖率 **80%**（12/15）

**有卡**：`easy saveText`、`llama_cpp_parameters`、`VHS_VideoInfoLoaded`、`GetImageSizeAndCount`、`LayerUtility: ImageScaleByAspectRatio V2`、`CreateVideo`、`easy imageBatchToImageList`、`llama_cpp_model_loader`、`VHS_LoadVideo`、`llama_cpp_instruct_adv`、`easy seed`、`easy positive`

**用到的条目**：easy seed、GetImageSizeAndCount、easy saveText、CreateVideo、llama_cpp_instruct_adv、llama_cpp_model_loader、llama_cpp_parameters、VHS_LoadVideo
