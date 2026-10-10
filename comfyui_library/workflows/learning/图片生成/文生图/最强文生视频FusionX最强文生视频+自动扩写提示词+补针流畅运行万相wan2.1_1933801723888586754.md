---
key: 最强文生视频FusionX最强文生视频+自动扩写提示词+补针流畅运行万相wan2.1_1933801723888586754.json
name: 最强文生视频FusionX最强文生视频+自动扩写提示词+补针流畅运行万相wan2.1_1933801723888586754
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/最强文生视频FusionX最强文生视频+自动扩写提示词+补针流畅运行万相wan2.1_1933801723888586754.json
hash: 236bd9ad5b84c92d
coverage: 0.875
learned_at: 2026-10-10 20:59:50
nodes: [WanVideoSLG, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoDecode, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, VHS_VideoCombine, LayerUtility: PurgeVRAM V2, Primitive integer [Crystools], WanVideoSampler, JWInteger, JWInteger, VHS_VideoCombine, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, RH_OneShot_Prompter, CR Text, WanVideoEmptyEmbeds, WanVideoBlockSwap, WanVideoApplyNAG, WanVideoTextEncodeSingle, WanVideoTextEncodeSingle, WanVideoMagCache]
patterns: []
missing: [CR Text, LayerUtility: PurgeVRAM V2, Primitive integer [Crystools]]
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识]
---

# 最强文生视频FusionX最强文生视频+自动扩写提示词+补针流畅运行万相wan2.1_1933801723888586754.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/最强文生视频FusionX最强文生视频+自动扩写提示词+补针流畅运行万相wan2.1_1933801723888586754.json`

## 结构

**生成流程**：Model → Sampling → Other

**节点**（24 个）：
- `WanVideoSLG`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoDecode`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM V2`
- `Primitive integer [Crystools]`
- `WanVideoSampler` ★核心
- `JWInteger`
- `JWInteger`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `RH_OneShot_Prompter`
- `CR Text`
- `WanVideoEmptyEmbeds`
- `WanVideoBlockSwap`
- `WanVideoApplyNAG`
- `WanVideoTextEncodeSingle`
- `WanVideoTextEncodeSingle`
- `WanVideoMagCache`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`WanVideoSLG`、`WanVideoEnhanceAVideo`、`WanVideoExperimentalArgs`、`WanVideoDecode`、`DownloadAndLoadGIMMVFIModel`、`GIMMVFI_interpolate`、`VHS_VideoCombine`、`WanVideoSampler`、`JWInteger`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`RH_OneShot_Prompter`、`WanVideoEmptyEmbeds`、`WanVideoBlockSwap`、`WanVideoApplyNAG`、`WanVideoTextEncodeSingle`、`WanVideoMagCache`

**缺卡**（3）：`CR Text`、`LayerUtility: PurgeVRAM V2`、`Primitive integer [Crystools]`

**用到的条目**：WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoTextEncodeSingle、RH_OneShot_Prompter、VHS_VideoCombine、WanVideoBlockSwap

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
