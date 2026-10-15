---
key: 视频生成/文生视频/Wan2.2-Rapid-AIO_1989341238669307906.json
name: Wan2.2-Rapid-AIO_1989341238669307906
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2-Rapid-AIO_1989341238669307906.json
hash: fe7718412e3b2a2a
coverage: 0.952381
learned_at: 2026-10-15 22:47:12
nodes: [DownloadAndLoadGIMMVFIModel, LayerUtility: PurgeVRAM V2, GIMMVFI_interpolate, WanVaceToVideo, INTConstant, VHS_VideoCombine, ModelSamplingSD3, PathchSageAttentionKJ, CLIPTextEncode, VAEDecode, INTConstant, CLIPTextEncode, WanVideoVACEStartToEndFrame, CLIPLoader, VAELoader, KSampler, Note, LoadImage, UnetLoaderGGUF, LoadImage, INTConstant]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 677960728391576, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan2.2-Rapid-AIO_1989341238669307906.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2-Rapid-AIO_1989341238669307906.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Other

**节点**（21 个）：
- `DownloadAndLoadGIMMVFIModel`
- `LayerUtility: PurgeVRAM V2`
- `GIMMVFI_interpolate`
- `WanVaceToVideo`
- `INTConstant`
- `VHS_VideoCombine`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `INTConstant`
- `CLIPTextEncode` ★核心
- `WanVideoVACEStartToEndFrame`
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `Note`
- `LoadImage`
- `UnetLoaderGGUF` ★核心
- `LoadImage`
- `INTConstant`

## 关键参数

- `seed` = `677960728391576`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **95%**（20/21）

**有卡**：`DownloadAndLoadGIMMVFIModel`、`LayerUtility: PurgeVRAM V2`、`GIMMVFI_interpolate`、`WanVaceToVideo`、`INTConstant`、`VHS_VideoCombine`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`VAEDecode`、`WanVideoVACEStartToEndFrame`、`CLIPLoader`、`VAELoader`、`KSampler`、`LoadImage`、`UnetLoaderGGUF`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、INTConstant、ModelSamplingSD3

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
