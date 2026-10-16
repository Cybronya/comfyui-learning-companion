---
key: 视频生成/图生视频/Wan2.2图生视频长视频生成_1974083427450400769.json
name: Wan2.2图生视频长视频生成_1974083427450400769.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1974083427450400769.json
hash: 19113a5b3ab9c1d5
coverage: 0.863636
learned_at: 2026-10-15 22:32:04
nodes: [ModelSamplingSD3, ModelSamplingSD3, VAELoader, PrimitiveInt, PrimitiveInt, easy cleanGpuUsed, easy cleanGpuUsed, LoraLoaderModelOnly, ImageResizeKJv2, UNETLoader, CLIPLoader, ColorMatch, LoadImage, UNETLoader, easy cleanGpuUsed, LoraLoaderModelOnly, VHS_VideoCombine, VHS_VideoCombine, VantageProject, MarkdownNote, LoadImage, VantageI2VDualLooper]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2图生视频长视频生成_1974083427450400769.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1974083427450400769.json`

## 结构

**生成流程**：Model → Process → Other

**节点**（22 个）：
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `VAELoader`
- `PrimitiveInt`
- `PrimitiveInt`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly` ★核心
- `ImageResizeKJv2`
- `UNETLoader` ★核心
- `CLIPLoader`
- `ColorMatch`
- `LoadImage`
- `UNETLoader` ★核心
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VantageProject`
- `MarkdownNote`
- `LoadImage`
- `VantageI2VDualLooper`

## 知识

覆盖率 **86%**（19/22）

**有卡**：`ModelSamplingSD3`、`VAELoader`、`easy cleanGpuUsed`、`LoraLoaderModelOnly`、`ImageResizeKJv2`、`UNETLoader`、`CLIPLoader`、`ColorMatch`、`LoadImage`、`VHS_VideoCombine`、`VantageProject`、`VantageI2VDualLooper`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、ImageResizeKJv2、ModelSamplingSD3、VHS_VideoCombine
