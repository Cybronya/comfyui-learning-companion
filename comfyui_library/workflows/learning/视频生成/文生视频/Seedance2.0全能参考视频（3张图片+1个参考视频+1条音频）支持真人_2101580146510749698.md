---
key: 视频生成/文生视频/Seedance2.0全能参考视频（3张图片+1个参考视频+1条音频）支持真人_2101580146510749698.json
name: Seedance2.0全能参考视频（3张图片+1个参考视频+1条音频）支持真人_2101580146510749698
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Seedance2.0全能参考视频（3张图片+1个参考视频+1条音频）支持真人_2101580146510749698.json
hash: d95f2b87857faa89
coverage: 0.846154
learned_at: 2026-10-15 22:46:58
nodes: [LoadImage, RH_SparkVideoAssetCreate, RH_SparkVideoAssetCreate, LoadImage, SaveVideo, LoadImage, RH_SparkVideoAssetCreate, LoadVideo, RH_RhartVideoSparkvideo20MultimodalVideo, LoadAudio, RH_SparkVideoAssetIdsMerge, MarkdownNote, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/文生视频/Seedance2.0全能参考视频（3张图片+1个参考视频+1条音频）支持真人_2101580146510749698.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Seedance2.0全能参考视频（3张图片+1个参考视频+1条音频）支持真人_2101580146510749698.json`

## 结构

**生成流程**：Output → Other

**节点**（13 个）：
- `LoadImage`
- `RH_SparkVideoAssetCreate`
- `RH_SparkVideoAssetCreate`
- `LoadImage`
- `SaveVideo`
- `LoadImage`
- `RH_SparkVideoAssetCreate`
- `LoadVideo`
- `RH_RhartVideoSparkvideo20MultimodalVideo`
- `LoadAudio`
- `RH_SparkVideoAssetIdsMerge`
- `MarkdownNote`
- `MarkdownNote`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`LoadImage`、`RH_SparkVideoAssetCreate`、`SaveVideo`、`LoadVideo`、`RH_RhartVideoSparkvideo20MultimodalVideo`、`LoadAudio`、`RH_SparkVideoAssetIdsMerge`

**用到的条目**：LoadImage、SaveVideo、LoadAudio、LoadVideo、RH_RhartVideoSparkvideo20MultimodalVideo、RH_SparkVideoAssetCreate、RH_SparkVideoAssetIdsMerge、sd15-t2i-basic
