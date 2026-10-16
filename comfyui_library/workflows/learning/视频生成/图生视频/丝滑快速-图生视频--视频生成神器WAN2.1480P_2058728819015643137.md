---
key: 视频生成/图生视频/丝滑快速-图生视频--视频生成神器WAN2.1480P_2058728819015643137.json
name: 丝滑快速-图生视频--视频生成神器WAN2.1480P_2058728819015643137.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2058728819015643137.json
hash: a41208f639c49691
coverage: 0.978723
learned_at: 2026-10-15 22:38:27
nodes: [Get resolution [Crystools], LayerUtility: BooleanOperatorV2, LayerUtility: BooleanOperatorV2, LayerUtility: If , LayerUtility: PurgeVRAM, CLIPVisionEncode, CLIPVisionLoader, CLIPLoader, VAELoader, LayerUtility: PurgeVRAM, CLIPTextEncode, LayerUtility: PurgeVRAM, DownloadAndLoadGIMMVFIModel, LayerUtility: PurgeVRAM, ImageUpscaleWithModel, ImageResizeKJ, VAEDecode, CR Text Replace, CR Text Replace, RH_Captioner, CR Text Replace, GIMMVFI_interpolate, Load Image Batch, CR Text Concatenate, RH_Translator, easy showAnything, Pick From Batch (mtb), SaveImage, VHS_VideoCombine, LayerUtility: If , UpscaleModelLoader, ImageUpscaleWithModel, UnetLoaderGGUF, Int, RHHiddenNodes, WanImageToVideo, RHHiddenNodes, RHHiddenNodes, RHHiddenNodes, Get resolution [Crystools], UNETLoader, WanVideoKsampler, VHS_VideoCombine, VHS_VideoCombine, CLIPTextEncode, LoadImage, StringConstantMultiline]
patterns: []
missing: []
---

# 视频生成/图生视频/丝滑快速-图生视频--视频生成神器WAN2.1480P_2058728819015643137.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2058728819015643137.json`

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
- `StringConstantMultiline`

## 知识

覆盖率 **98%**（46/47）

**有卡**：`Get resolution [Crystools]`、`LayerUtility: BooleanOperatorV2`、`LayerUtility: If `、`LayerUtility: PurgeVRAM`、`CLIPVisionEncode`、`CLIPVisionLoader`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`DownloadAndLoadGIMMVFIModel`、`ImageUpscaleWithModel`、`ImageResizeKJ`、`VAEDecode`、`CR Text Replace`、`RH_Captioner`、`GIMMVFI_interpolate`、`Load Image Batch`、`CR Text Concatenate`、`RH_Translator`、`Pick From Batch (mtb)`、`SaveImage`、`VHS_VideoCombine`、`UpscaleModelLoader`、`UnetLoaderGGUF`、`Int`、`RHHiddenNodes`、`WanImageToVideo`、`UNETLoader`、`WanVideoKsampler`、`LoadImage`、`StringConstantMultiline`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、WanVideoKsampler、CLIPVisionEncode
