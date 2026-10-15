---
key: 视频生成/文生视频/hunyuan_video_1.5_720p_t2v FlashVSR-视频放大_1993327685495619586.json
name: hunyuan_video_1.5_720p_t2v FlashVSR-视频放大_1993327685495619586
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/hunyuan_video_1.5_720p_t2v FlashVSR-视频放大_1993327685495619586.json
hash: ecf34b3f74546e67
coverage: 0.818182
learned_at: 2026-10-15 22:47:20
nodes: [DualCLIPLoader, VAELoader, AILab_QwenVL, FlashVSR_SM_Model, VHS_VideoCombine, UNETLoader, AddLabel, FlashVSR_SM_KSampler, CLIPTextEncode, KSampler, VAEDecode, CLIPTextEncode, PreviewAny, ModelSamplingSD3, PathchSageAttentionKJ, Note, LoadImage, MarkdownNote, MarkdownNote, VHS_VideoCombine, EmptyHunyuanVideo15Latent, ImageResizeKJ]
patterns: []
missing: []
parameters: {"cfg": 6, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 741415495458177, "steps": 20}
---

# 视频生成/文生视频/hunyuan_video_1.5_720p_t2v FlashVSR-视频放大_1993327685495619586.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/hunyuan_video_1.5_720p_t2v FlashVSR-视频放大_1993327685495619586.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（22 个）：
- `DualCLIPLoader`
- `VAELoader`
- `AILab_QwenVL`
- `FlashVSR_SM_Model`
- `VHS_VideoCombine`
- `UNETLoader` ★核心
- `AddLabel`
- `FlashVSR_SM_KSampler` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `Note`
- `LoadImage`
- `MarkdownNote`
- `MarkdownNote`
- `VHS_VideoCombine`
- `EmptyHunyuanVideo15Latent`
- `ImageResizeKJ`

## 关键参数

- `seed` = `741415495458177`
- `steps` = `20`
- `cfg` = `6`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（18/22）

**有卡**：`DualCLIPLoader`、`VAELoader`、`AILab_QwenVL`、`FlashVSR_SM_Model`、`VHS_VideoCombine`、`UNETLoader`、`AddLabel`、`FlashVSR_SM_KSampler`、`CLIPTextEncode`、`KSampler`、`VAEDecode`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`LoadImage`、`EmptyHunyuanVideo15Latent`、`ImageResizeKJ`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、LoadImage、UNETLoader、FlashVSR_SM_KSampler、EmptyHunyuanVideo15Latent
