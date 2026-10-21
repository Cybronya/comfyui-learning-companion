---
name: unknown_workflow_video_lora_sampler_111
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.760786
common_nodes: [AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1957667803581050882.json, 视频生成/图生视频/1958061014984118274.json, 视频生成/图生视频/1958075798320197633.json, 视频生成/图生视频/2014174614657703937.json, 视频生成/图生视频/1977385230757699586.json, 视频生成/图生视频/1948766276714934274.json, 视频生成/图生视频/2018299977335840769.json, 视频生成/图生视频/1989886464651612162.json, 视频生成/图生视频/1986797048806764545.json, 视频生成/图生视频/1962734249734483970.json, 视频生成/图生视频/1971581572791136257.json, 视频生成/图生视频/1942210266623053825.json, 视频生成/图生视频/1937733481621557249.json, 视频生成/图生视频/1958430229331132417.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_111

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/1957667803581050882.json、视频生成/图生视频/1958061014984118274.json、视频生成/图生视频/1958075798320197633.json、视频生成/图生视频/2014174614657703937.json、视频生成/图生视频/1977385230757699586.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 14 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 13/14 个有
- `LoadImage` —— 13/14 个有
- `VHS_LoadVideo` —— 13/14 个有
- `AudioCrop` —— 12/14 个有
- `INTConstant` —— 12/14 个有
- `MultiTalkWav2VecEmbeds` —— 12/14 个有
- `WanVideoTextEncode` —— 12/14 个有
- `CR Text` —— 11/14 个有
- `JWIntegerToString` —— 11/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/14 个有
- `SimpleMath+` —— 11/14 个有
- `easy showAnything` —— 11/14 个有
- `ImageResizeKJ` —— 10/14 个有
- `LayerUtility: PurgeVRAM V2` —— 10/14 个有
- `VHS_DuplicateImages` —— 10/14 个有
- `WanVideoImageToVideoEncode` —— 10/14 个有
- `WanVideoUni3C_ControlnetLoader` —— 10/14 个有
- `WanVideoUni3C_embeds` —— 10/14 个有
- `easy anythingIndexSwitch` —— 10/14 个有
- `WanVideoContextOptions` —— 8/14 个有
- `ImpactInt` —— 7/14 个有
- `WanVideoTorchCompileSettings` —— 7/14 个有
- `easy int` —— 7/14 个有
- `ImageFromBatch+` —— 6/14 个有
- `WanVideoEncode` —— 6/14 个有
- `PrimitiveInt` —— 4/14 个有
- `RHHiddenNodes` —— 4/14 个有
- `WanVideoImageToVideoMultiTalk` —— 4/14 个有
- `GetNode` —— 3/14 个有
- `ImageResizeKJv2` —— 3/14 个有
- `SetNode` —— 3/14 个有
- `Int` —— 2/14 个有
- `CR Text Concatenate` —— 1/14 个有
- `Fast Groups Bypasser (rgthree)` —— 1/14 个有
- `Note Plus (mtb)` —— 1/14 个有
- `PrimitiveBoolean` —— 1/14 个有
- `RH_Captioner` —— 1/14 个有
- `RH_LLMAPI_NODE` —— 1/14 个有
- `RH_Prompter` —— 1/14 个有
- `RH_Translator` —— 1/14 个有
- `SaveAudio` —— 1/14 个有
- `ShowText|pysssss` —— 1/14 个有
- `SongGeneration_Sampler` —— 1/14 个有
- `SongGeneration_Stage1` —— 1/14 个有
- `SongGeneration_Stage2` —— 1/14 个有
- `Text Multiline` —— 1/14 个有
- `easy ifElse` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
