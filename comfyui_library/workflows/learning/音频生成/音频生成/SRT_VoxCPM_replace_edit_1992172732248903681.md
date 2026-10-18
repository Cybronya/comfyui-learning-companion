---
key: 音频生成/音频生成/SRT_VoxCPM_replace_edit_1992172732248903681.json
name: SRT_VoxCPM_replace_edit_1992172732248903681
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/SRT_VoxCPM_replace_edit_1992172732248903681.json
hash: 921ec8e75c638cba
coverage: 0.875
learned_at: 2026-10-18 01:46:52
nodes: [VoxCPM_Loader, Note, Audio_Trimmer_By_Timestamp, VoxCPM_Cache_Combiner, VoxCPM_Cache_Builder, LoadAudio, SaveAudio, VoxCPM_SRT_Processor]
patterns: []
missing: []
---

# 音频生成/音频生成/SRT_VoxCPM_replace_edit_1992172732248903681.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/SRT_VoxCPM_replace_edit_1992172732248903681.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（8 个）：
- `VoxCPM_Loader`
- `Note`
- `Audio_Trimmer_By_Timestamp`
- `VoxCPM_Cache_Combiner`
- `VoxCPM_Cache_Builder`
- `LoadAudio`
- `SaveAudio`
- `VoxCPM_SRT_Processor`

## 知识

覆盖率 **88%**（7/8）

**有卡**：`VoxCPM_Loader`、`Audio_Trimmer_By_Timestamp`、`VoxCPM_Cache_Combiner`、`VoxCPM_Cache_Builder`、`LoadAudio`、`SaveAudio`、`VoxCPM_SRT_Processor`

**用到的条目**：SaveAudio、LoadAudio、Audio_Trimmer_By_Timestamp、VoxCPM_Cache_Builder、VoxCPM_Cache_Combiner、VoxCPM_Loader、VoxCPM_SRT_Processor、sd15-t2i-basic
