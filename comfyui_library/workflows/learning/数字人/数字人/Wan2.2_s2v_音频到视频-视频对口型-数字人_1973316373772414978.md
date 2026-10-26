---
key: 数字人/数字人/Wan2.2_s2v_音频到视频-视频对口型-数字人_1973316373772414978.json
name: Wan2.2_s2v_音频到视频-视频对口型-数字人_1973316373772414978
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan2.2_s2v_音频到视频-视频对口型-数字人_1973316373772414978.json
hash: 06dc8e798e322164
coverage: 0.923077
learned_at: 2026-10-26 01:57:59
nodes: [LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, ModelSamplingSD3, KSampler, AudioEncoderEncode, AudioEncoderLoader, WanSoundImageToVideo, VAEDecode, VHS_SelectImages, VHS_LoadVideo, VHS_LoadVideo, PreviewImage, VHS_VideoInfo, DF_Integer, SimpleMath+, DF_Integer, DF_Integer, ImageConcatMulti, VHS_VideoCombine, Bjornulf_ShowFloat, VHS_VideoInfo, CLIPTextEncode, JjkText]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "uni_pc", "scheduler": "simple", "seed": 106368627822605, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/Wan2.2_s2v_音频到视频-视频对口型-数字人_1973316373772414978.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan2.2_s2v_音频到视频-视频对口型-数字人_1973316373772414978.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `KSampler` ★核心
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `WanSoundImageToVideo`
- `VAEDecode` ★核心
- `VHS_SelectImages`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `PreviewImage`
- `VHS_VideoInfo`
- `DF_Integer`
- `SimpleMath+`
- `DF_Integer`
- `DF_Integer`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `Bjornulf_ShowFloat`
- `VHS_VideoInfo`
- `CLIPTextEncode` ★核心
- `JjkText`

## 关键参数

- `seed` = `106368627822605`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（24/26）

**有卡**：`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`ModelSamplingSD3`、`KSampler`、`AudioEncoderEncode`、`AudioEncoderLoader`、`WanSoundImageToVideo`、`VAEDecode`、`VHS_SelectImages`、`VHS_LoadVideo`、`VHS_VideoInfo`、`DF_Integer`、`SimpleMath+`、`ImageConcatMulti`、`VHS_VideoCombine`、`Bjornulf_ShowFloat`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、UNETLoader、AudioEncoderLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
