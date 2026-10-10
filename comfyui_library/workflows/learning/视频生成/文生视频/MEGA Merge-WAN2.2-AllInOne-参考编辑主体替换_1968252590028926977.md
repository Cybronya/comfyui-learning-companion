---
key: 视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-参考编辑主体替换_1968252590028926977.json
name: MEGA Merge-WAN2.2-AllInOne-参考编辑主体替换_1968252590028926977
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-参考编辑主体替换_1968252590028926977.json
hash: 57955a7d92342943
coverage: 0.916667
learned_at: 2026-10-10 23:00:41
nodes: [TrimVideoLatent, VAEDecode, KSampler, ModelSamplingSD3, InvertMask, MaskToImage, GetImageSize+, VHS_DuplicateMasks, GrowMaskWithBlur, SolidMask, VHS_VideoCombine, PreviewImage, INTConstant, InspyrenetRembg, ImageCompositeMasked, ImageResizeKJv2, VHS_LoadVideo, LoadImage, Miaoshouai_Tagger, VHS_VideoCombine, WanVaceToVideo, CLIPTextEncode, CLIPTextEncode, CheckpointLoaderSimple]
patterns: []
missing: [GetImageSize+]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "wan2.2-rapid-mega-aio-v1.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 192054346835137, "steps": 6}
discoveries: [次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-参考编辑主体替换_1968252590028926977.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-参考编辑主体替换_1968252590028926977.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `KSampler` ★核心
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
- `CheckpointLoaderSimple` ★核心

## 关键参数

- `seed` = `192054346835137`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `wan2.2-rapid-mega-aio-v1.safetensors`

## 知识

覆盖率 **92%**（22/24）

**有卡**：`TrimVideoLatent`、`VAEDecode`、`KSampler`、`ModelSamplingSD3`、`InvertMask`、`MaskToImage`、`VHS_DuplicateMasks`、`GrowMaskWithBlur`、`SolidMask`、`VHS_VideoCombine`、`INTConstant`、`InspyrenetRembg`、`ImageCompositeMasked`、`ImageResizeKJv2`、`VHS_LoadVideo`、`LoadImage`、`Miaoshouai_Tagger`、`WanVaceToVideo`、`CLIPTextEncode`、`CheckpointLoaderSimple`

**缺卡**（1）：`GetImageSize+`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、TrimVideoLatent、ImageResizeKJv2、INTConstant

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
