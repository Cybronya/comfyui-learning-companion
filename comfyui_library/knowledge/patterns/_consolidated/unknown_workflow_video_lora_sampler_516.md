---
name: unknown_workflow_video_lora_sampler_516
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.822
common_nodes: [ApplyFaceProcessor, FaceProcessorLoader, ImageFromBatch+, ImpactSwitch, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, PreviewImage, RH_LLMAPI_NODE, Text Concatenate, VHS_VideoCombine, Wan22PromptSelector, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoDecode, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1956219463043612673.json, 视频生成/图生视频/1956357600432541698.json, 视频生成/图生视频/1958494701273903106.json, 视频生成/文生视频/1956406110863458305.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_516

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1956219463043612673.json、视频生成/图生视频/1956357600432541698.json、视频生成/图生视频/1958494701273903106.json、视频生成/文生视频/1956406110863458305.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `ApplyFaceProcessor`
- `FaceProcessorLoader`
- `ImageFromBatch+`
- `ImpactSwitch`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `PreviewImage`
- `RH_LLMAPI_NODE`
- `Text Concatenate`
- `VHS_VideoCombine`
- `Wan22PromptSelector`
- `WanVideoAddStandInLatent`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 3/4 个有
- `AudioSeparation` —— 3/4 个有
- `CR Text` —— 3/4 个有
- `DownloadAndLoadWav2VecModel` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `ImageConcatMulti` —— 3/4 个有
- `ImageResizeKJv2` —— 3/4 个有
- `InspyrenetRembg` —— 3/4 个有
- `JWInteger` —— 3/4 个有
- `LayerUtility: ImageRemoveAlpha` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `MultiTalkWav2VecEmbeds` —— 3/4 个有
- `OpenposePreprocessor` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `SimpleMath+` —— 3/4 个有
- `VHS_LoadVideo` —— 3/4 个有
- `VHS_VideoInfo` —— 3/4 个有
- `WanVideoVACEEncode` —— 3/4 个有
- `WanVideoVACEModelSelect` —— 3/4 个有
- `WanVideoVACEStartToEndFrame` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `easy imageScaleDownToSize` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `ImageConcanate` —— 2/4 个有
- `JWIntegerToString` —— 2/4 个有
- `LoadAudio` —— 2/4 个有
- `MathExpression|pysssss` —— 2/4 个有
- `Audio Duration (mtb)` —— 1/4 个有
- `PreviewAudio` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `RHHiddenNodes` —— 1/4 个有
- `SaveAudio` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `WanVideoEmptyEmbeds` —— 1/4 个有
- `easy clearCacheAll` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
