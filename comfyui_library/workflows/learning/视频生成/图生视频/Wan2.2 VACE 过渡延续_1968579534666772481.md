---
key: 视频生成/图生视频/Wan2.2 VACE 过渡延续_1968579534666772481.json
name: Wan2.2 VACE 过渡延续_1968579534666772481.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1968579534666772481.json
hash: a7f30bc7e8612b03
coverage: 0.598765
learned_at: 2026-10-15 22:31:45
nodes: [LayerUtility: ImageScaleByAspectRatio V2, Int, Note, easy imageSize, ImageConcanate, CR Text, PreviewImage, ShowText|pysssss, RH_Translator, ImageConcanate, PreviewImage, ShowText|pysssss, RH_Translator, Reroute, CR Text, RH_LLMAPI_NODE, LayerUtility: ImageScaleByAspectRatio V2, WanVideoModelLoader, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoVACEModelSelect, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, WanVideoSetLoRAs, SetNode, SetNode, SetNode, GetNode, CreateCFGScheduleFloatList, GetNode, WanVideoScheduler, WanVideoSigmaToStep, WanVideoScheduler, WanVideoSampler, WanVideoLoraSelect, WanVideoLoraSelect, PrimitiveFloat, easy cleanGpuUsed, easy clearCacheAll, WanVideoBlockSwap, WanVideoVAELoader, Int, GetNode, WanVideoSampler, SetNode, WanVideoTextEncodeCached, SetNode, WanVideoVACEStartToEndFrame, GetNode, WanVideoVACEEncode, VideoContinuationGenerator, GetNode, GetNode, GetNode, CreateCFGScheduleFloatList, GetNode, WanVideoScheduler, WanVideoSigmaToStep, WanVideoScheduler, PrimitiveFloat, easy cleanGpuUsed, easy clearCacheAll, Int, WanVideoSampler, WanVideoSampler, Reroute, WanVideoTextEncodeCached, SetNode, VHS_VideoCombine, VHS_VideoCombine, SetNode, WanVideoVACEEncode, Reroute, Int, GetNode, Note, Note, ImageConcanate, PreviewImage, ShowText|pysssss, RH_Translator, ImpactSwitch, ShowText|pysssss, CR Text, RH_LLMAPI_NODE, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, GetNode, CreateCFGScheduleFloatList, GetNode, WanVideoScheduler, WanVideoSigmaToStep, WanVideoScheduler, PrimitiveFloat, easy cleanGpuUsed, easy clearCacheAll, Int, WanVideoSampler, WanVideoSampler, Reroute, WanVideoTextEncodeCached, VHS_VideoCombine, VHS_VideoCombine, Reroute, Int, GetNode, LayerUtility: ImageScaleByAspectRatio V2, Note, SetNode, VideoContinuationGenerator, GetNode, SetNode, GetNode, SetNode, GetNode, WanVideoVACEEncode, GetNode, SaveImage, WanVideoLoraSelect, SetNode, WanVideoVACEModelSelect, SetNode, WanVideoBlender, SetNode, WanVideoDecode, SimpleMath+, GetNode, WanVideoDecode, DownloadAndLoadGIMMVFIModel, VHS_VideoCombine, Int, Int, Reroute, GetNode, VHS_VideoCombine, VHS_LoadVideo, Note, LoadImage, LoadImage, WanVideoDecode, PrimitiveInt, RH_LLMAPI_NODE, ShowText|pysssss, CR Text, Fast Groups Bypasser (rgthree), LoadImage, WanVideoBlender, LoadImage, Fast Groups Bypasser (rgthree), PrimitiveInt, ShowText|pysssss, CR Text, TT_img_enc, SaveImage, TT_img_enc, GIMMVFI_interpolate, PrimitiveInt, ImpactSwitch, ImpactSwitch, CR Text]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 VACE 过渡延续_1968579534666772481.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1968579534666772481.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（162 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Int`
- `Note`
- `easy imageSize`
- `ImageConcanate`
- `CR Text`
- `PreviewImage`
- `ShowText|pysssss`
- `RH_Translator`
- `ImageConcanate`
- `PreviewImage`
- `ShowText|pysssss`
- `RH_Translator`
- `Reroute`
- `CR Text`
- `RH_LLMAPI_NODE`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoVACEModelSelect`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoSetLoRAs`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `CreateCFGScheduleFloatList`
- `GetNode`
- `WanVideoScheduler`
- `WanVideoSigmaToStep`
- `WanVideoScheduler`
- `WanVideoSampler` ★核心
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `PrimitiveFloat`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `Int`
- `GetNode`
- `WanVideoSampler` ★核心
- `SetNode`
- `WanVideoTextEncodeCached`
- `SetNode`
- `WanVideoVACEStartToEndFrame`
- `GetNode`
- `WanVideoVACEEncode`
- `VideoContinuationGenerator`
- `GetNode`
- `GetNode`
- `GetNode`
- `CreateCFGScheduleFloatList`
- `GetNode`
- `WanVideoScheduler`
- `WanVideoSigmaToStep`
- `WanVideoScheduler`
- `PrimitiveFloat`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `Int`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `Reroute`
- `WanVideoTextEncodeCached`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `WanVideoVACEEncode`
- `Reroute`
- `Int`
- `GetNode`
- `Note`
- `Note`
- `ImageConcanate`
- `PreviewImage`
- `ShowText|pysssss`
- `RH_Translator`
- `ImpactSwitch`
- `ShowText|pysssss`
- `CR Text`
- `RH_LLMAPI_NODE`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `GetNode`
- `CreateCFGScheduleFloatList`
- `GetNode`
- `WanVideoScheduler`
- `WanVideoSigmaToStep`
- `WanVideoScheduler`
- `PrimitiveFloat`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `Int`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `Reroute`
- `WanVideoTextEncodeCached`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Reroute`
- `Int`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `SetNode`
- `VideoContinuationGenerator`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoVACEEncode`
- `GetNode`
- `SaveImage`
- `WanVideoLoraSelect`
- `SetNode`
- `WanVideoVACEModelSelect`
- `SetNode`
- `WanVideoBlender`
- `SetNode`
- `WanVideoDecode`
- `SimpleMath+`
- `GetNode`
- `WanVideoDecode`
- `DownloadAndLoadGIMMVFIModel`
- `VHS_VideoCombine`
- `Int`
- `Int`
- `Reroute`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `Note`
- `LoadImage`
- `LoadImage`
- `WanVideoDecode`
- `PrimitiveInt`
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `WanVideoBlender`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveInt`
- `ShowText|pysssss`
- `CR Text`
- `TT_img_enc`
- `SaveImage`
- `TT_img_enc`
- `GIMMVFI_interpolate`
- `PrimitiveInt`
- `ImpactSwitch`
- `ImpactSwitch`
- `CR Text`

## 知识

覆盖率 **60%**（97/162）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`Int`、`easy imageSize`、`ImageConcanate`、`CR Text`、`RH_Translator`、`RH_LLMAPI_NODE`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoVACEModelSelect`、`WanVideoSetLoRAs`、`CreateCFGScheduleFloatList`、`WanVideoScheduler`、`WanVideoSigmaToStep`、`WanVideoSampler`、`WanVideoLoraSelect`、`easy cleanGpuUsed`、`easy clearCacheAll`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`WanVideoVACEStartToEndFrame`、`WanVideoVACEEncode`、`VideoContinuationGenerator`、`VHS_VideoCombine`、`SaveImage`、`WanVideoBlender`、`WanVideoDecode`、`SimpleMath+`、`DownloadAndLoadGIMMVFIModel`、`VHS_LoadVideo`、`LoadImage`、`TT_img_enc`、`GIMMVFI_interpolate`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、WanVideoDecode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoTextEncodeCached、WanVideoLoraSelect
