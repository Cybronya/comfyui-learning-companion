---
name: unknown_workflow_video_lora_sampler_107
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.862571
common_nodes: [AudioCrop, DownloadAndLoadWav2VecModel, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2007459382434471938.json, 视频生成/图生视频/Lip-syncing + Emotional Voice-over对口型+情感口播++数字人_2097495815702007810.json, 视频生成/图生视频/2062430418598711297.json, 视频生成/图生视频/2062556213728071682.json, 视频生成/图生视频/1955928297832153090.json, 视频生成/图生视频/1958474058688053249.json, 视频生成/图生视频/2067838359027929089.json, 视频生成/图生视频/2080570679388364802.json, 视频生成/图生视频/2075939070710206466.json, 视频生成/图生视频/数字人对口型 情感口播  数字人 InfiniTetalk 超自然数字人对口型_2090021885932294145.json, 视频生成/图生视频/数字人对口型 情感口播  数字人 InfiniTetalk 超自然数字人对口型_2090054337321070594.json, 视频生成/图生视频/2079450772135309313.json, 视频生成/图生视频/2068963777298657282.json, 视频生成/图生视频/1994726030126555137.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_107

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/2007459382434471938.json、视频生成/图生视频/Lip-syncing + Emotional Voice-over对口型+情感口播++数字人_2097495815702007810.json、视频生成/图生视频/2062430418598711297.json、视频生成/图生视频/2062556213728071682.json、视频生成/图生视频/1955928297832153090.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 14 个 workflow 都包含：
- `AudioCrop`
- `DownloadAndLoadWav2VecModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 13/14 个有
- `WanVideoClipVisionEncode` —— 13/14 个有
- `AudioSeparation` —— 12/14 个有
- `Audio Duration (mtb)` —— 11/14 个有
- `GetImageRangeFromBatch` —— 11/14 个有
- `GetNode` —— 11/14 个有
- `MathExpression|pysssss` —— 11/14 个有
- `SetNode` —— 11/14 个有
- `PlaySound|pysssss` —— 10/14 个有
- `WanVideoTorchCompileSettings` —— 4/14 个有
- `CR Text` —— 3/14 个有
- `ImpactInt` —— 3/14 个有
- `JWIntegerToString` —— 3/14 个有
- `SimpleMath+` —— 3/14 个有
- `RHHiddenNodes` —— 2/14 个有
- `Anything Everywhere` —— 1/14 个有
- `CogVideoEnhanceAVideo` —— 1/14 个有
- `HyVideoBlockSwap` —— 1/14 个有
- `ImageCASharpening+` —— 1/14 个有
- `ImageSizeInfo` —— 1/14 个有
- `LayerUtility: PurgeVRAM V2` —— 1/14 个有
- `WanVideoExperimentalArgs` —— 1/14 个有
- `easy showAnything` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
