---
key: 平台全量/基于 Qwen3-ASR 与 Qwen3 ForcedAligner 的音频识别与时间戳字幕制作工作流_2019863556694482945.json
name: 基于 Qwen3-ASR 与 Qwen3 ForcedAligner 的音频识别与时间戳字幕制作工作流_2019863556694482945
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/基于 Qwen3-ASR 与 Qwen3 ForcedAligner 的音频识别与时间戳字幕制作工作流_2019863556694482945.json
hash: 65bc7e8b493ea260
coverage: 0.538462
learned_at: 2026-11-14 01:56:52
nodes: [ShowText|pysssss, Qwen3ASRLoader, ShowText|pysssss, ShowText|pysssss, ShowText|pysssss, Qwen3ForcedAlignerLoader, ShowText|pysssss, Qwen3ForcedAlign, Qwen3ASRTranscribe, ShowText|pysssss, easy saveText, LoadAudio, easy saveText]
patterns: []
missing: []
---

# 平台全量/基于 Qwen3-ASR 与 Qwen3 ForcedAligner 的音频识别与时间戳字幕制作工作流_2019863556694482945.json

> 来源文件 `comfyui_library/workflows/平台全量/基于 Qwen3-ASR 与 Qwen3 ForcedAligner 的音频识别与时间戳字幕制作工作流_2019863556694482945.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（13 个）：
- `ShowText|pysssss`
- `Qwen3ASRLoader`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `Qwen3ForcedAlignerLoader`
- `ShowText|pysssss`
- `Qwen3ForcedAlign`
- `Qwen3ASRTranscribe`
- `ShowText|pysssss`
- `easy saveText`
- `LoadAudio`
- `easy saveText`

## 知识

覆盖率 **54%**（7/13）

**有卡**：`Qwen3ASRLoader`、`Qwen3ForcedAlignerLoader`、`Qwen3ForcedAlign`、`Qwen3ASRTranscribe`、`easy saveText`、`LoadAudio`

**用到的条目**：easy saveText、LoadAudio、Qwen3ASRLoader、Qwen3ASRTranscribe、Qwen3ForcedAlign、Qwen3ForcedAlignerLoader、image_to_image_controlnet_face_detailer_lora、image_to_image_controlnet_face_detailer_lora_2
