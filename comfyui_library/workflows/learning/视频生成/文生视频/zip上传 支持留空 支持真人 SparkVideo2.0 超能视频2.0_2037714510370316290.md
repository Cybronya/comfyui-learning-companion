---
key: 视频生成/文生视频/zip上传 支持留空 支持真人 SparkVideo2.0 超能视频2.0_2037714510370316290.json
name: zip上传 支持留空 支持真人 SparkVideo2.0 超能视频2.0_2037714510370316290
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/zip上传 支持留空 支持真人 SparkVideo2.0 超能视频2.0_2037714510370316290.json
hash: 24c1038ec098b44f
coverage: 1
learned_at: 2026-10-11 03:48:39
nodes: [RHExtractImage, RHExtractAudio, RHExtractImage, RHExtractImage, RHExtractImage, RHExtractImage, RHExtractImage, RHExtractImage, RHExtractImage, RHExtractVideo, RHExtractVideo, RHExtractVideo, RHExtractAudio, RHExtractAudio, RHExtractImage, SaveVideo, HAIGC_LoadImagesFromZip, RH_RhartVideoSparkvideo20MultimodalVideo]
patterns: []
missing: []
---

# 视频生成/文生视频/zip上传 支持留空 支持真人 SparkVideo2.0 超能视频2.0_2037714510370316290.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/zip上传 支持留空 支持真人 SparkVideo2.0 超能视频2.0_2037714510370316290.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（18 个）：
- `RHExtractImage`
- `RHExtractAudio`
- `RHExtractImage`
- `RHExtractImage`
- `RHExtractImage`
- `RHExtractImage`
- `RHExtractImage`
- `RHExtractImage`
- `RHExtractImage`
- `RHExtractVideo`
- `RHExtractVideo`
- `RHExtractVideo`
- `RHExtractAudio`
- `RHExtractAudio`
- `RHExtractImage`
- `SaveVideo`
- `HAIGC_LoadImagesFromZip`
- `RH_RhartVideoSparkvideo20MultimodalVideo`

## 知识

覆盖率 **100%**（18/18）

**有卡**：`RHExtractImage`、`RHExtractAudio`、`RHExtractVideo`、`SaveVideo`、`HAIGC_LoadImagesFromZip`、`RH_RhartVideoSparkvideo20MultimodalVideo`

**用到的条目**：SaveVideo、RHExtractImage、RH_RhartVideoSparkvideo20MultimodalVideo、HAIGC_LoadImagesFromZip、RHExtractAudio、RHExtractVideo、sd15-t2i-basic、sd15-t2i-lora
