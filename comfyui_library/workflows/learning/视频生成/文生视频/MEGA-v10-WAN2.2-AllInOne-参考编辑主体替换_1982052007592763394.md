---
key: 视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-参考编辑主体替换_1982052007592763394.json
name: MEGA-v10-WAN2.2-AllInOne-参考编辑主体替换_1982052007592763394
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-参考编辑主体替换_1982052007592763394.json
hash: 55491de518082be7
coverage: 0.923077
learned_at: 2026-10-11 02:45:00
nodes: [TrimVideoLatent, VAEDecode, ModelSamplingSD3, InvertMask, MaskToImage, GetImageSize+, VHS_DuplicateMasks, GrowMaskWithBlur, SolidMask, VHS_VideoCombine, PreviewImage, INTConstant, InspyrenetRembg, ImageCompositeMasked, ImageResizeKJv2, VHS_LoadVideo, LoadImage, Miaoshouai_Tagger, VHS_VideoCombine, WanVaceToVideo, CLIPTextEncode, CLIPTextEncode, AV_VAELoader, UNETLoader, CLIPLoader, KSampler]
patterns: []
missing: [GetImageSize+]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 192054346835137, "steps": 4}
discoveries: [次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-参考编辑主体替换_1982052007592763394.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-参考编辑主体替换_1982052007592763394.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `InvertMask`
- `MaskToImage`
- `GetImageSize+`
- `VHS_DuplicateMasks`
- `GrowMaskWithBlur`
- `SolidMask`
- `VHS_VideoCombine`
- `PreviewImage`
- `INTConstant`
- `InspyrenetRembg`
- `ImageCompositeMasked`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `LoadImage`
- `Miaoshouai_Tagger`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `AV_VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `KSampler` ★核心

## 关键参数

- `seed` = `192054346835137`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **92%**（24/26）

**有卡**：`TrimVideoLatent`、`VAEDecode`、`ModelSamplingSD3`、`InvertMask`、`MaskToImage`、`VHS_DuplicateMasks`、`GrowMaskWithBlur`、`SolidMask`、`VHS_VideoCombine`、`INTConstant`、`InspyrenetRembg`、`ImageCompositeMasked`、`ImageResizeKJv2`、`VHS_LoadVideo`、`LoadImage`、`Miaoshouai_Tagger`、`WanVaceToVideo`、`CLIPTextEncode`、`AV_VAELoader`、`UNETLoader`、`CLIPLoader`、`KSampler`

**缺卡**（1）：`GetImageSize+`

**用到的条目**：KSampler、VAEDecode、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、TrimVideoLatent、AV_VAELoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
