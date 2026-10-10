---
key: 图片生成/图生图/Qwen Image 2.1姿态编辑图生图处理生成工具_2102549583330111489.json
name: Qwen Image 2.1姿态编辑图生图处理生成工具_2102549583330111489
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1姿态编辑图生图处理生成工具_2102549583330111489.json
hash: 53e3c15f0e5822ad
coverage: 0.722222
learned_at: 2026-10-10 20:48:07
nodes: [Image Comparer (rgthree), OpenposePreprocessor, Reroute, GetImageSize, NuiKr.OpenPoseEditor, ResolutionSelector, EmptyLatentImage, Reroute, GroupSwitcher, Reroute, PreviewImage, PreviewImage, Reroute, Reroute, SaveImage, PrimitiveStringMultiline, PrimitiveBoolean, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, ComfySwitchNode, KSampler, VAEDecode, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [NuiKr.OpenPoseEditor]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `NuiKr.OpenPoseEditor` 仅有 ControlNet/KSampler 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1姿态编辑图生图处理生成工具_2102549583330111489.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1姿态编辑图生图处理生成工具_2102549583330111489.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `Image Comparer (rgthree)`
- `OpenposePreprocessor`
- `Reroute`
- `GetImageSize`
- `NuiKr.OpenPoseEditor`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `Reroute`
- `GroupSwitcher`
- `Reroute`
- `PreviewImage`
- `PreviewImage`
- `Reroute`
- `Reroute`
- `SaveImage`
- `PrimitiveStringMultiline`
- `PrimitiveBoolean`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
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
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
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

覆盖率 **72%**（39/54）

**有卡**：`OpenposePreprocessor`、`GetImageSize`、`ResolutionSelector`、`EmptyLatentImage`、`GroupSwitcher`、`SaveImage`、`PrimitiveBoolean`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`LoadImage`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（1）：`NuiKr.OpenPoseEditor`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `NuiKr.OpenPoseEditor` 仅有 ControlNet/KSampler 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
