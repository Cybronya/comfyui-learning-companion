---
key: 视频生成/图生视频/丝滑快速-图生视频--视频生成神器WAN2.1480P_2054086996280266753.json
name: 丝滑快速-图生视频--视频生成神器WAN2.1480P_2054086996280266753.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/丝滑快速-图生视频--视频生成神器WAN2.1480P_2054086996280266753.json
hash: 90bd88699327db78
coverage: 0.978723
learned_at: 2026-10-15 22:37:45
nodes: [Get resolution [Crystools], LayerUtility: BooleanOperatorV2, LayerUtility: BooleanOperatorV2, LayerUtility: If , LayerUtility: PurgeVRAM, CLIPVisionEncode, CLIPVisionLoader, CLIPLoader, VAELoader, LayerUtility: PurgeVRAM, CLIPTextEncode, LayerUtility: PurgeVRAM, DownloadAndLoadGIMMVFIModel, LayerUtility: PurgeVRAM, ImageUpscaleWithModel, ImageResizeKJ, VAEDecode, CR Text Replace, CR Text Replace, RH_Captioner, CR Text Replace, GIMMVFI_interpolate, Load Image Batch, CR Text Concatenate, RH_Translator, easy showAnything, Pick From Batch (mtb), SaveImage, VHS_VideoCombine, LayerUtility: If , UpscaleModelLoader, ImageUpscaleWithModel, UnetLoaderGGUF, StringConstantMultiline, Int, RHHiddenNodes, WanImageToVideo, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, Get resolution [Crystools], UNETLoader, WanVideoKsampler, VHS_VideoCombine, VHS_VideoCombine, CLIPTextEncode, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/丝滑快速-图生视频--视频生成神器WAN2.1480P_2054086996280266753.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2054086996280266753.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `Get resolution [Crystools]`
- `LayerUtility: BooleanOperatorV2`
- `LayerUtility: BooleanOperatorV2`
- `LayerUtility: If `
- `LayerUtility: PurgeVRAM`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `LayerUtility: PurgeVRAM`
- `DownloadAndLoadGIMMVFIModel`
- `LayerUtility: PurgeVRAM`
- `ImageUpscaleWithModel`
- `ImageResizeKJ`
- `VAEDecode` ★核心
- `CR Text Replace`
- `CR Text Replace`
- `RH_Captioner`
- `CR Text Replace`
- `GIMMVFI_interpolate`
- `Load Image Batch`
- `CR Text Concatenate`
- `RH_Translator`
- `easy showAnything`
- `Pick From Batch (mtb)`
- `SaveImage`
- `VHS_VideoCombine`
- `LayerUtility: If `
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `UnetLoaderGGUF` ★核心
- `StringConstantMultiline`
- `Int`
- `RHHiddenNodes`
- `WanImageToVideo`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `Get resolution [Crystools]`
- `UNETLoader` ★核心
- `WanVideoKsampler` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `CLIPTextEncode` ★核心
- `LoadImage`

## 知识

覆盖率 **98%**（46/47）

**有卡**：`Get resolution [Crystools]`、`LayerUtility: BooleanOperatorV2`、`LayerUtility: If `、`LayerUtility: PurgeVRAM`、`CLIPVisionEncode`、`CLIPVisionLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`DownloadAndLoadGIMMVFIModel`、`ImageUpscaleWithModel`、`ImageResizeKJ`、`VAEDecode`、`CR Text Replace`、`RH_Captioner`、`GIMMVFI_interpolate`、`Load Image Batch`、`CR Text Concatenate`、`RH_Translator`、`Pick From Batch (mtb)`、`SaveImage`、`VHS_VideoCombine`、`UpscaleModelLoader`、`UnetLoaderGGUF`、`StringConstantMultiline`、`Int`、`RHHiddenNodes`、`WanImageToVideo`、`UNETLoader`、`WanVideoKsampler`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanVideoKsampler、CLIPVisionEncode
