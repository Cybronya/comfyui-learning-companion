---
key: 视频生成/图生视频/王炸自动反推首尾换装 Wan2.2-Insight_1982023011672956929.json
name: 王炸自动反推首尾换装 Wan2.2-Insight_1982023011672956929.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/王炸自动反推首尾换装 Wan2.2-Insight_1982023011672956929.json
hash: a5193b5bd6254276
coverage: 0.847826
learned_at: 2026-10-15 22:32:39
nodes: [JWInteger, GetImageSizeAndCount, RIFE VFI, JWInteger, CreateCFGScheduleFloatList, LoadWanVideoT5TextEncoder, VHS_VideoCombine, SetNode, LayerUtility: PurgeVRAM V2, WanVideoDecode, LayerUtility: PurgeVRAM V2, LoadImage, LoadImage, ImageConcanate, MathExpression|pysssss, WanVideoVAELoader, WanVideoTextEncode, INTConstant, RHHiddenNodes, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSampler, WanVideoImageToVideoEncode, INTConstant, WanVideoSampler, VHS_VideoCombine, LayerUtility: ImageScaleByAspectRatio V2, CR Text Concatenate, CR Text Concatenate, RH_Translator, CR Text, ShowText|pysssss, CR Text, AILab_QwenVL, ShowText|pysssss, Wan22PromptSelector, Note, ImpactSwitch, GetNode, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, SaveImage, LoadImage, RH_Nano_Banana_Image2Image, CR Text, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/王炸自动反推首尾换装 Wan2.2-Insight_1982023011672956929.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1982023011672956929.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（46 个）：
- `JWInteger`
- `GetImageSizeAndCount`
- `RIFE VFI`
- `JWInteger`
- `CreateCFGScheduleFloatList`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `SetNode`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadImage`
- `ImageConcanate`
- `MathExpression|pysssss`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `INTConstant`
- `RHHiddenNodes`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`
- `INTConstant`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `RH_Translator`
- `CR Text`
- `ShowText|pysssss`
- `CR Text`
- `AILab_QwenVL`
- `ShowText|pysssss`
- `Wan22PromptSelector`
- `Note`
- `ImpactSwitch`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `SaveImage`
- `LoadImage`
- `RH_Nano_Banana_Image2Image`
- `CR Text`
- `LoadImage`

## 知识

覆盖率 **85%**（39/46）

**有卡**：`JWInteger`、`GetImageSizeAndCount`、`RIFE VFI`、`CreateCFGScheduleFloatList`、`LoadWanVideoT5TextEncoder`、`VHS_VideoCombine`、`LayerUtility: PurgeVRAM V2`、`WanVideoDecode`、`LoadImage`、`ImageConcanate`、`MathExpression|pysssss`、`WanVideoVAELoader`、`WanVideoTextEncode`、`INTConstant`、`RHHiddenNodes`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoImageToVideoEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Text Concatenate`、`RH_Translator`、`CR Text`、`AILab_QwenVL`、`Wan22PromptSelector`、`SaveImage`、`RH_Nano_Banana_Image2Image`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
