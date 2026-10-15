---
key: 视频生成/文生视频/video_hunyuan_video_1.5_720p_t2v_1992624616432619521.json
name: video_hunyuan_video_1.5_720p_t2v_1992624616432619521
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/video_hunyuan_video_1.5_720p_t2v_1992624616432619521.json
hash: 9fecd7f6a389ebcf
coverage: 0.6875
learned_at: 2026-10-15 22:47:32
nodes: [MarkdownNote, VHS_VideoCombine, VAEDecode, CLIPTextEncode, MarkdownNote, Note, GetNode, VAEDecodeTiled, SetNode, PreviewAny, VHS_VideoCombine, UNETLoader, PathchSageAttentionKJ, ModelSamplingSD3, DualCLIPLoader, VAELoader, EmptyHunyuanVideo15Latent, LoadImage, AILab_QwenVL, CLIPTextEncode, KSampler, UNETLoader, ModelSamplingSD3, LatentUpscaleModelLoader, HunyuanVideo15LatentUpscaleWithModel, GetNode, GetNode, HunyuanVideo15SuperResolution, KSamplerAdvanced, KSamplerAdvanced, SetNode, SetNode]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize"}
---

# 视频生成/文生视频/video_hunyuan_video_1.5_720p_t2v_1992624616432619521.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/video_hunyuan_video_1.5_720p_t2v_1992624616432619521.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（32 个）：
- `MarkdownNote`
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `Note`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `SetNode`
- `PreviewAny`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `DualCLIPLoader`
- `VAELoader`
- `EmptyHunyuanVideo15Latent`
- `LoadImage`
- `AILab_QwenVL`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `LatentUpscaleModelLoader`
- `HunyuanVideo15LatentUpscaleWithModel`
- `GetNode`
- `GetNode`
- `HunyuanVideo15SuperResolution`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `SetNode`
- `SetNode`

## 关键参数

- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **69%**（22/32）

**有卡**：`VHS_VideoCombine`、`VAEDecode`、`CLIPTextEncode`、`VAEDecodeTiled`、`UNETLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`DualCLIPLoader`、`VAELoader`、`EmptyHunyuanVideo15Latent`、`LoadImage`、`AILab_QwenVL`、`KSampler`、`LatentUpscaleModelLoader`、`HunyuanVideo15LatentUpscaleWithModel`、`HunyuanVideo15SuperResolution`、`KSamplerAdvanced`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、KSamplerAdvanced、VAEDecodeTiled
