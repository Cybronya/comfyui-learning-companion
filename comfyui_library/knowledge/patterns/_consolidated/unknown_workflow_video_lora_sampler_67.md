---
name: unknown_workflow_video_lora_sampler_67
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.906944
common_nodes: [CogVideoEnhanceAVideo, CreateCFGScheduleFloatList, DF_Integer, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, RH_Captioner, SimpleMath+, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoVAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1950075530189127682.json, 视频生成/图生视频/1952043105937731585.json, 视频生成/图生视频/2067129224686821377.json, 视频生成/图生视频/Wan2.2-14B-首尾帧视频工作流_2085669231730974721.json, 视频生成/图生视频/1954893685562359810.json, 视频生成/图生视频/1955443170857422849.json, 视频生成/图生视频/1953398457706971138.json, 视频生成/图生视频/1952550941541240833.json, 视频生成/图生视频/1951465254188429313.json, 视频生成/图生视频/1953648114819321858.json, 视频生成/图生视频/2011405192771674114.json, 视频生成/图生视频/2012117442817953793.json, 视频生成/图生视频/1956190750184755201.json, 视频生成/图生视频/2011413743489523713.json, 视频生成/图生视频/2009530449273561089.json, 视频生成/图生视频/1964548830723231746.json, 视频生成/图生视频/2018219380894601218.json, 视频生成/图生视频/1964562297249218562.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_67

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/1950075530189127682.json、视频生成/图生视频/1952043105937731585.json、视频生成/图生视频/2067129224686821377.json、视频生成/图生视频/Wan2.2-14B-首尾帧视频工作流_2085669231730974721.json、视频生成/图生视频/1954893685562359810.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 18 个 workflow 都包含：
- `CogVideoEnhanceAVideo`
- `CreateCFGScheduleFloatList`
- `DF_Integer`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `RH_Captioner`
- `SimpleMath+`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `PrimitiveBoolean` —— 17/18 个有
- `VHS_VideoCombine` —— 17/18 个有
- `WanVideoSetLoRAs` —— 17/18 个有
- `easy ifElse` —— 17/18 个有
- `easy int` —— 17/18 个有
- `WanVideoClipVisionEncode` —— 13/18 个有
- `WanVideoTorchCompileSettings` —— 13/18 个有
- `ImageStitch` —— 12/18 个有
- `LayerUtility: ImageMaskScaleAs` —— 12/18 个有
- `LoadWanVideoClipTextEncoder` —— 12/18 个有
- `RH_Translator` —— 12/18 个有
- `Textbox` —— 11/18 个有
- `CLIPVisionLoader` —— 8/18 个有
- `CR Text Replace` —— 6/18 个有
- `TextBox` —— 6/18 个有
- `easy seed` —— 5/18 个有
- `ColorCorrectOfUtils` —— 1/18 个有
- `ColorMatchToReference` —— 1/18 个有
- `CreateVideo` —— 1/18 个有
- `EsesImageEffectLevels` —— 1/18 个有
- `FloatToSigmas` —— 1/18 个有
- `ImageCASharpening+` —— 1/18 个有
- `Int` —— 1/18 个有
- `LayerUtility: PurgeVRAM` —— 1/18 个有
- `SaveVideo` —— 1/18 个有
- `StringToFloatList` —— 1/18 个有
- `WanVideoExperimentalArgs` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
