---
key: 视频生成/图生视频/万相Wan3.0图生视频工作流｜阿里旗舰图片变视频_2095480668833804289.json
name: 万相Wan3.0图生视频工作流｜阿里旗舰图片变视频_2095480668833804289
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/万相Wan3.0图生视频工作流｜阿里旗舰图片变视频_2095480668833804289.json
hash: 11aca4fe041f2efc
coverage: 0.875
learned_at: 2026-10-17 00:02:55
nodes: [LoadImage, PrimitiveStringMultiline, SaveVideo, RHMiniMaxH3ModelLoader, RHMiniMaxH3TextEncoderLoader, RHMiniMaxH3VAELoader, RHMiniMaxH3VideoGen, CreateVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/万相Wan3.0图生视频工作流｜阿里旗舰图片变视频_2095480668833804289.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/万相Wan3.0图生视频工作流｜阿里旗舰图片变视频_2095480668833804289.json`

## 结构

**生成流程**：Model → Output → Other

**节点**（8 个）：
- `LoadImage`
- `PrimitiveStringMultiline`
- `SaveVideo`
- `RHMiniMaxH3ModelLoader`
- `RHMiniMaxH3TextEncoderLoader`
- `RHMiniMaxH3VAELoader`
- `RHMiniMaxH3VideoGen`
- `CreateVideo`

## 知识

覆盖率 **88%**（7/8）

**有卡**：`LoadImage`、`SaveVideo`、`RHMiniMaxH3ModelLoader`、`RHMiniMaxH3TextEncoderLoader`、`RHMiniMaxH3VAELoader`、`RHMiniMaxH3VideoGen`、`CreateVideo`

**用到的条目**：LoadImage、RHMiniMaxH3TextEncoderLoader、RHMiniMaxH3VAELoader、SaveVideo、CreateVideo、RHMiniMaxH3ModelLoader、RHMiniMaxH3VideoGen、sd15-t2i-basic
