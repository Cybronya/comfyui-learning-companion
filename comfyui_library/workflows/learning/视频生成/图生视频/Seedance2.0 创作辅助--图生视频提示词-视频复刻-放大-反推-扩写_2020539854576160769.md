---
key: 视频生成/图生视频/Seedance2.0 创作辅助--图生视频提示词-视频复刻-放大-反推-扩写_2020539854576160769.json
name: Seedance2.0 创作辅助--图生视频提示词-视频复刻-放大-反推-扩写_2020539854576160769.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2020539854576160769.json
hash: 0b2e6f3cddc22acf
coverage: 0.806452
learned_at: 2026-10-15 22:35:06
nodes: [ImageScaleToTotalPixels, easy saveText, LayerUtility: PurgeVRAM, easy showAnything, Qwen3_VQA, ShellAgentPluginOutputText, CR Prompt Text, SaveVideo, LoadVideo, Note, CR Prompt Text, CR Prompt Text, Comfly_LLm_API, easy showAnything, ShellAgentPluginOutputText, LoadImage, SeedVR2LoadVAEModel, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, SaveImage, Note, Reroute, Reroute, ShowAnything|Mie, Reroute, FlashVSRNode, Reroute, VHS_VideoInfo, JWInteger, VHS_LoadVideo, VHS_VideoCombine, CR Prompt Text, RH_LLMAPI_Pro_Node, easy showAnything, Fast Groups Bypasser (rgthree), LoadImage, SaveImage, LayerUtility: TextJoin, CR Prompt Text, ShowText|pysssss, ShellAgentPluginOutputText, easy showAnything, RH_LLMAPI_Pro_Node, CR Prompt Text, CR Prompt Text, LoadImage, LoadImage, VHS_LoadVideo, VHS_VideoInfo, SeedVR2LoadVAEModel, INTConstant, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, ImageFromBatch+, SeedVR2LoadDiTModel, SaveImage, ImageFromBatch+, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, SaveImage, VHS_LoadVideo, INTConstant]
patterns: []
missing: []
---

# 视频生成/图生视频/Seedance2.0 创作辅助--图生视频提示词-视频复刻-放大-反推-扩写_2020539854576160769.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2020539854576160769.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（62 个）：
- `ImageScaleToTotalPixels`
- `easy saveText`
- `LayerUtility: PurgeVRAM`
- `easy showAnything`
- `Qwen3_VQA`
- `ShellAgentPluginOutputText`
- `CR Prompt Text`
- `SaveVideo`
- `LoadVideo`
- `Note`
- `CR Prompt Text`
- `CR Prompt Text`
- `Comfly_LLm_API`
- `easy showAnything`
- `ShellAgentPluginOutputText`
- `LoadImage`
- `SeedVR2LoadVAEModel`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `Note`
- `Reroute`
- `Reroute`
- `ShowAnything|Mie`
- `Reroute`
- `FlashVSRNode`
- `Reroute`
- `VHS_VideoInfo`
- `JWInteger`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `RH_LLMAPI_Pro_Node`
- `easy showAnything`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `SaveImage`
- `LayerUtility: TextJoin`
- `CR Prompt Text`
- `ShowText|pysssss`
- `ShellAgentPluginOutputText`
- `easy showAnything`
- `RH_LLMAPI_Pro_Node`
- `CR Prompt Text`
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_VideoInfo`
- `SeedVR2LoadVAEModel`
- `INTConstant`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `ImageFromBatch+`
- `SeedVR2LoadDiTModel`
- `SaveImage`
- `ImageFromBatch+`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `SaveImage`
- `VHS_LoadVideo`
- `INTConstant`

## 知识

覆盖率 **81%**（50/62）

**有卡**：`ImageScaleToTotalPixels`、`easy saveText`、`LayerUtility: PurgeVRAM`、`Qwen3_VQA`、`ShellAgentPluginOutputText`、`CR Prompt Text`、`SaveVideo`、`LoadVideo`、`Comfly_LLm_API`、`LoadImage`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`SaveImage`、`ShowAnything|Mie`、`FlashVSRNode`、`VHS_VideoInfo`、`JWInteger`、`VHS_LoadVideo`、`VHS_VideoCombine`、`RH_LLMAPI_Pro_Node`、`LayerUtility: TextJoin`、`INTConstant`、`ImageFromBatch+`

**用到的条目**：SaveImage、LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler、CR Prompt Text、SaveVideo、ShellAgentPluginOutputText
