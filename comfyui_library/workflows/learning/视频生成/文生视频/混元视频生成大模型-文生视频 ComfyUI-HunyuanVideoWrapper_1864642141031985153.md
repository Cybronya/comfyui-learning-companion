---
key: 视频生成/文生视频/混元视频生成大模型-文生视频 ComfyUI-HunyuanVideoWrapper_1864642141031985153.json
name: 混元视频生成大模型-文生视频 ComfyUI-HunyuanVideoWrapper_1864642141031985153.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1864642141031985153.json
hash: 91b60f9074ad4241
coverage: 1
learned_at: 2026-10-15 22:43:19
nodes: [HyVideoVAELoader, HyVideoModelLoader, HyVideoSampler, HyVideoDecode, DownloadAndLoadHyVideoTextEncoder, VHS_VideoCombine, RH_Prompter, easy cleanGpuUsed, HyVideoTextEncode]
patterns: []
missing: []
---

# 视频生成/文生视频/混元视频生成大模型-文生视频 ComfyUI-HunyuanVideoWrapper_1864642141031985153.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1864642141031985153.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（9 个）：
- `HyVideoVAELoader`
- `HyVideoModelLoader`
- `HyVideoSampler` ★核心
- `HyVideoDecode`
- `DownloadAndLoadHyVideoTextEncoder`
- `VHS_VideoCombine`
- `RH_Prompter`
- `easy cleanGpuUsed`
- `HyVideoTextEncode`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`HyVideoVAELoader`、`HyVideoModelLoader`、`HyVideoSampler`、`HyVideoDecode`、`DownloadAndLoadHyVideoTextEncoder`、`VHS_VideoCombine`、`RH_Prompter`、`easy cleanGpuUsed`、`HyVideoTextEncode`

**用到的条目**：HyVideoSampler、DownloadAndLoadHyVideoTextEncoder、HyVideoDecode、HyVideoTextEncode、HyVideoVAELoader、RH_Prompter、VHS_VideoCombine、HyVideoModelLoader
