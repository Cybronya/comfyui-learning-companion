---
key: 视频生成/文生视频/混元文生视频+LORA hunyuanvideo lora_1870173036715347969.json
name: 混元文生视频+LORA hunyuanvideo lora_1870173036715347969.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1870173036715347969.json
hash: 6ed2d7581cd1597a
coverage: 1
learned_at: 2026-10-15 22:43:19
nodes: [HyVideoVAELoader, HyVideoDecode, HyVideoTextEncode, VHS_VideoCombine, HyVideoSampler, HyVideoModelLoader, HyVideoLoraSelect, Text Multiline, DownloadAndLoadHyVideoTextEncoder]
patterns: []
missing: []
---

# 视频生成/文生视频/混元文生视频+LORA hunyuanvideo lora_1870173036715347969.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1870173036715347969.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（9 个）：
- `HyVideoVAELoader`
- `HyVideoDecode`
- `HyVideoTextEncode`
- `VHS_VideoCombine`
- `HyVideoSampler` ★核心
- `HyVideoModelLoader`
- `HyVideoLoraSelect`
- `Text Multiline`
- `DownloadAndLoadHyVideoTextEncoder`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`HyVideoVAELoader`、`HyVideoDecode`、`HyVideoTextEncode`、`VHS_VideoCombine`、`HyVideoSampler`、`HyVideoModelLoader`、`HyVideoLoraSelect`、`Text Multiline`、`DownloadAndLoadHyVideoTextEncoder`

**用到的条目**：HyVideoSampler、DownloadAndLoadHyVideoTextEncoder、HyVideoDecode、HyVideoTextEncode、HyVideoVAELoader、HyVideoLoraSelect、VHS_VideoCombine、HyVideoModelLoader
