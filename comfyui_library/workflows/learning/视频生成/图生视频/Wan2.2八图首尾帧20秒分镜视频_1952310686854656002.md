---
key: 视频生成/图生视频/Wan2.2八图首尾帧20秒分镜视频_1952310686854656002.json
name: Wan2.2八图首尾帧20秒分镜视频_1952310686854656002.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1952310686854656002.json
hash: b99edeba266c870e
coverage: 0.969072
learned_at: 2026-10-15 22:31:01
nodes: [DownloadAndLoadGIMMVFIModel, LoadImage, LoadImage, CLIPLoader, KSamplerAdvanced, PathchSageAttentionKJ, PathchSageAttentionKJ, VAEDecode, WanFirstLastFrameToVideo, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, KSamplerAdvanced, KSamplerAdvanced, CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, GIMMVFI_interpolate, CLIPVisionEncode, CLIPVisionEncode, PathchSageAttentionKJ, PathchSageAttentionKJ, CLIPLoader, VAELoader, CLIPVisionEncode, KSamplerAdvanced, WanFirstLastFrameToVideo, CLIPTextEncode, VAEDecode, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, LoadImage, DownloadAndLoadGIMMVFIModel, KSamplerAdvanced, PathchSageAttentionKJ, PathchSageAttentionKJ, VAEDecode, WanFirstLastFrameToVideo, DownloadAndLoadGIMMVFIModel, KSamplerAdvanced, CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, PathchSageAttentionKJ, PathchSageAttentionKJ, CLIPLoader, CLIPVisionEncode, CLIPVisionEncode, WanFirstLastFrameToVideo, CLIPTextEncode, VAEDecode, ModelSamplingSD3, ModelSamplingSD3, CLIPTextEncode, CLIPVisionEncode, CLIPVisionEncode, VAELoader, GIMMVFI_interpolate, GIMMVFI_interpolate, ImageBatchMultiple+, GetImageSizeAndCount, CreateVideo, CR Text, CR Text, CR Text, CR Text, KSamplerAdvanced, KSamplerAdvanced, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, MarkdownNote, UNETLoader, UNETLoader, CLIPVisionEncode, CLIPVisionLoader, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, PrimitiveInt, PrimitiveInt, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, SaveVideo, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"cfg": 20, "denoise": "simple", "sampler_name": 4, "scheduler": "euler", "seed": "disable", "steps": "fixed"}
---

# 视频生成/图生视频/Wan2.2八图首尾帧20秒分镜视频_1952310686854656002.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952310686854656002.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（97 个）：
- `DownloadAndLoadGIMMVFIModel`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `VAEDecode` ★核心
- `WanFirstLastFrameToVideo`
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `GIMMVFI_interpolate`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `VAELoader`
- `CLIPVisionEncode`
- `KSamplerAdvanced` ★核心
- `WanFirstLastFrameToVideo`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `DownloadAndLoadGIMMVFIModel`
- `KSamplerAdvanced` ★核心
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `VAEDecode` ★核心
- `WanFirstLastFrameToVideo`
- `DownloadAndLoadGIMMVFIModel`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PathchSageAttentionKJ`
- `CLIPLoader`
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `WanFirstLastFrameToVideo`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `CLIPTextEncode` ★核心
- `CLIPVisionEncode`
- `CLIPVisionEncode`
- `VAELoader`
- `GIMMVFI_interpolate`
- `GIMMVFI_interpolate`
- `ImageBatchMultiple+`
- `GetImageSizeAndCount`
- `CreateVideo`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `PrimitiveInt`
- `PrimitiveInt`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `SaveVideo`
- `VHS_VideoCombine`

## 关键参数

- `seed` = `disable`
- `steps` = `fixed`
- `cfg` = `20`
- `sampler_name` = `4`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **97%**（94/97）

**有卡**：`DownloadAndLoadGIMMVFIModel`、`LoadImage`、`CLIPLoader`、`KSamplerAdvanced`、`PathchSageAttentionKJ`、`VAEDecode`、`WanFirstLastFrameToVideo`、`GIMMVFI_interpolate`、`CLIPTextEncode`、`ModelSamplingSD3`、`CLIPVisionEncode`、`VAELoader`、`ImageBatchMultiple+`、`GetImageSizeAndCount`、`CreateVideo`、`CR Text`、`UNETLoader`、`CLIPVisionLoader`、`easy cleanGpuUsed`、`SaveVideo`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced、CLIPVisionEncode
