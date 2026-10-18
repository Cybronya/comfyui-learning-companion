---
key: 视频生成/图生视频/VOSR2视频图像极速高清修复 Ultra Fast High Res Restoration_2108610426400497665.json
name: VOSR2视频图像极速高清修复 Ultra Fast High Res Restoration_2108610426400497665
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/VOSR2视频图像极速高清修复 Ultra Fast High Res Restoration_2108610426400497665.json
hash: 1708261ae50d52f6
coverage: 0.82
learned_at: 2026-10-17 22:50:18
nodes: [Reroute, Reroute, Int, 数学运算_孤海, VHS_LoadVideo, VOSR2Upscale, VOSR2ModelLoader, LayerFilter: GaussianBlur, easy imageSizeByLongerSide, VHS_VideoCombine, VOSR2ModelLoader, easy imageSizeByLongerSide, Reroute, Reroute, LayerFilter: GaussianBlur, 数学运算_孤海, LoadImage, GoohaiUniversalSlider, Image Comparer (rgthree), VOSR2Upscale, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/VOSR2视频图像极速高清修复 Ultra Fast High Res Restoration_2108610426400497665.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/VOSR2视频图像极速高清修复 Ultra Fast High Res Restoration_2108610426400497665.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（50 个）：
- `Reroute`
- `Reroute`
- `Int`
- `数学运算_孤海`
- `VHS_LoadVideo`
- `VOSR2Upscale`
- `VOSR2ModelLoader`
- `LayerFilter: GaussianBlur`
- `easy imageSizeByLongerSide`
- `VHS_VideoCombine`
- `VOSR2ModelLoader`
- `easy imageSizeByLongerSide`
- `Reroute`
- `Reroute`
- `LayerFilter: GaussianBlur`
- `数学运算_孤海`
- `LoadImage`
- `GoohaiUniversalSlider`
- `Image Comparer (rgthree)`
- `VOSR2Upscale`
- `SaveImage`
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

覆盖率 **82%**（41/50）

**有卡**：`Int`、`数学运算_孤海`、`VHS_LoadVideo`、`VOSR2Upscale`、`VOSR2ModelLoader`、`LayerFilter: GaussianBlur`、`easy imageSizeByLongerSide`、`VHS_VideoCombine`、`LoadImage`、`GoohaiUniversalSlider`、`SaveImage`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`VAEDecode`、`CLIPLoader`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
