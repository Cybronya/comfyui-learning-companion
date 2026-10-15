---
key: 视频生成/文生视频/WAN2.1 ControlNet VACE丝滑跳舞生成 文生视频图生视频融合_2088679303167959042.json
name: WAN2.1 ControlNet VACE丝滑跳舞生成 文生视频图生视频融合_2088679303167959042
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/WAN2.1 ControlNet VACE丝滑跳舞生成 文生视频图生视频融合_2088679303167959042.json
hash: ef9fbe929b6e0740
coverage: 0.87931
learned_at: 2026-10-15 22:47:03
nodes: [ImageScale, ImageUpscaleWithModel, WanVideoSLG, Reroute, WanVideoExperimentalArgs, ShowText|pysssss, ImageResizeKJ, WanVideoDecode, RIFE VFI, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoTeaCache, WanVideoSampler, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, WanVideoVACEEncode, CR Combine Prompt, Florence2, LoadFlorence2Model, Reroute, AIO_Preprocessor, LoadWanVideoT5TextEncoder, WanVideoVAELoader, UpscaleModelLoader, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoBlockSwap, ImageScale, LoadImage, VHS_LoadVideo, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/WAN2.1 ControlNet VACE丝滑跳舞生成 文生视频图生视频融合_2088679303167959042.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/WAN2.1 ControlNet VACE丝滑跳舞生成 文生视频图生视频融合_2088679303167959042.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `ImageScale`
- `ImageUpscaleWithModel`
- `WanVideoSLG`
- `Reroute`
- `WanVideoExperimentalArgs`
- `ShowText|pysssss`
- `ImageResizeKJ`
- `WanVideoDecode`
- `RIFE VFI`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoTeaCache`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoVACEEncode`
- `CR Combine Prompt`
- `Florence2`
- `LoadFlorence2Model`
- `Reroute`
- `AIO_Preprocessor`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `UpscaleModelLoader`
- `WanVideoModelLoader`
- `WanVideoVACEModelSelect`
- `WanVideoBlockSwap`
- `ImageScale`
- `LoadImage`
- `VHS_LoadVideo`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **88%**（51/58）

**有卡**：`ImageScale`、`ImageUpscaleWithModel`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`ImageResizeKJ`、`WanVideoDecode`、`RIFE VFI`、`WanVideoTextEncode`、`WanVideoTorchCompileSettings`、`WanVideoTeaCache`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoVACEEncode`、`CR Combine Prompt`、`Florence2`、`LoadFlorence2Model`、`AIO_Preprocessor`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`UpscaleModelLoader`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`WanVideoBlockSwap`、`LoadImage`、`VHS_LoadVideo`、`UNETLoader`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
