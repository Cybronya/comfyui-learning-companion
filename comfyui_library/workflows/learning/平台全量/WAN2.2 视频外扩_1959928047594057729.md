---
key: 平台全量/WAN2.2 视频外扩_1959928047594057729.json
name: WAN2.2 视频外扩_1959928047594057729
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/WAN2.2 视频外扩_1959928047594057729.json
hash: e51fa684953e1860
coverage: 0.711111
learned_at: 2026-11-14 01:03:42
nodes: [WanVideoTextEncodeSingle, WanVideoTextEncodeSingle, WanVideoApplyNAG, LayerUtility: PurgeVRAM V2, Reroute, CM_IntToFloat, Reroute, LoadLBMModel, LBMSampler, Reroute, Reroute, RH_Translator, LayerMask: RemBgUltra, Reroute, GetImageRangeFromBatch, MathExpression|pysssss, Int, Int, Bjornulf_ShowInt, RHHiddenNodes, LayerUtility: PurgeVRAM V2, WanVideoSampler, Pick From Batch (mtb), WanVideoDecode, LayerUtility: ImageScaleByAspectRatio V2, WanVideoVACEEncode, VHS_VideoCombine, VHS_VideoCombine, Int, WanVideoVAELoader, ImagePadForOutpaintMasked, Reroute, Reroute, Reroute, RH_Captioner, LayerUtility: ImageRemoveAlpha, Fast Bypasser (rgthree), WanVideoBlockSwap, JjkText, RH_Translator, VHS_LoadVideo, PrimitiveInt, PrimitiveInt, PrimitiveInt, PrimitiveInt]
patterns: []
missing: []
---

# 平台全量/WAN2.2 视频外扩_1959928047594057729.json

> 来源文件 `comfyui_library/workflows/平台全量/WAN2.2 视频外扩_1959928047594057729.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（45 个）：
- `WanVideoTextEncodeSingle`
- `WanVideoTextEncodeSingle`
- `WanVideoApplyNAG`
- `LayerUtility: PurgeVRAM V2`
- `Reroute`
- `CM_IntToFloat`
- `Reroute`
- `LoadLBMModel`
- `LBMSampler` ★核心
- `Reroute`
- `Reroute`
- `RH_Translator`
- `LayerMask: RemBgUltra`
- `Reroute`
- `GetImageRangeFromBatch`
- `MathExpression|pysssss`
- `Int`
- `Int`
- `Bjornulf_ShowInt`
- `RHHiddenNodes`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoSampler` ★核心
- `Pick From Batch (mtb)`
- `WanVideoDecode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoVACEEncode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Int`
- `WanVideoVAELoader`
- `ImagePadForOutpaintMasked`
- `Reroute`
- `Reroute`
- `Reroute`
- `RH_Captioner`
- `LayerUtility: ImageRemoveAlpha`
- `Fast Bypasser (rgthree)`
- `WanVideoBlockSwap`
- `JjkText`
- `RH_Translator`
- `VHS_LoadVideo`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`
- `PrimitiveInt`

## 知识

覆盖率 **71%**（32/45）

**有卡**：`WanVideoTextEncodeSingle`、`WanVideoApplyNAG`、`LayerUtility: PurgeVRAM V2`、`CM_IntToFloat`、`LoadLBMModel`、`LBMSampler`、`RH_Translator`、`LayerMask: RemBgUltra`、`GetImageRangeFromBatch`、`MathExpression|pysssss`、`Int`、`Bjornulf_ShowInt`、`RHHiddenNodes`、`WanVideoSampler`、`Pick From Batch (mtb)`、`WanVideoDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoVACEEncode`、`VHS_VideoCombine`、`WanVideoVAELoader`、`ImagePadForOutpaintMasked`、`RH_Captioner`、`LayerUtility: ImageRemoveAlpha`、`Fast Bypasser (rgthree)`、`WanVideoBlockSwap`、`VHS_LoadVideo`

**用到的条目**：LBMSampler、WanVideoSampler、WanVideoDecode、WanVideoTextEncodeSingle、WanVideoVACEEncode、WanVideoVAELoader、Bjornulf_ShowInt、CM_IntToFloat
