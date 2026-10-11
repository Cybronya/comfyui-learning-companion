---
key: 视频生成/文生视频/丝滑跳舞视频生成WAN2.1 ControlNet VACE深度控制文生视频图生视频_2088429518905233409.json
name: 丝滑跳舞视频生成WAN2.1 ControlNet VACE深度控制文生视频图生视频_2088429518905233409
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/丝滑跳舞视频生成WAN2.1 ControlNet VACE深度控制文生视频图生视频_2088429518905233409.json
hash: d9e767dd73fade63
coverage: 0.85
learned_at: 2026-10-11 20:53:51
nodes: [ImageScale, ImageUpscaleWithModel, WanVideoSLG, Reroute, WanVideoExperimentalArgs, ShowText|pysssss, ImageResizeKJ, WanVideoDecode, RIFE VFI, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoTeaCache, WanVideoSampler, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, WanVideoVACEEncode, CR Combine Prompt, Florence2, LoadFlorence2Model, Reroute, AIO_Preprocessor, LoadWanVideoT5TextEncoder, WanVideoVAELoader, UpscaleModelLoader, WanVideoModelLoader, WanVideoVACEModelSelect, WanVideoBlockSwap, ImageScale, LoadImage, VHS_LoadVideo, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: [RIFE VFI, CR Combine Prompt]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识, 次要节点 `CR Combine Prompt` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/丝滑跳舞视频生成WAN2.1 ControlNet VACE深度控制文生视频图生视频_2088429518905233409.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/丝滑跳舞视频生成WAN2.1 ControlNet VACE深度控制文生视频图生视频_2088429518905233409.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（60 个）：
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
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **85%**（51/60）

**有卡**：`ImageScale`、`ImageUpscaleWithModel`、`WanVideoSLG`、`WanVideoExperimentalArgs`、`ImageResizeKJ`、`WanVideoDecode`、`WanVideoTextEncode`、`WanVideoTorchCompileSettings`、`WanVideoTeaCache`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoVACEEncode`、`Florence2`、`LoadFlorence2Model`、`AIO_Preprocessor`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`UpscaleModelLoader`、`WanVideoModelLoader`、`WanVideoVACEModelSelect`、`WanVideoBlockSwap`、`LoadImage`、`VHS_LoadVideo`、`LoraLoaderModelOnly`、`UNETLoader`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`VAEDecode`、`VAELoader`、`CLIPLoader`、`EmptyLatentImage`

**缺卡**（2）：`RIFE VFI`、`CR Combine Prompt`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `RIFE VFI` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Combine Prompt` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
