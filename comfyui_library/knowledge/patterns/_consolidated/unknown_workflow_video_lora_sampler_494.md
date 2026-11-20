---
name: unknown_workflow_video_lora_sampler_494
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.750833
common_nodes: [AudioSeparation, CLIPVisionLoader, CR Text, DownloadAndLoadWav2VecModel, GetNode, ImpactSwitch, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadWanVideoT5TextEncoder, MathExpression|pysssss, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAudio, RH_LLMAPI_NODE, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTorchCompileSettings, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [平台全量/v2v视频+音频生成数字人带货视频 infinitetalk-上传视频+一段音频驱动=支持长视频_1976912864780947457.json, 平台全量/最新数字人InfiniteTalk -视频+音频=高质量数字人（支持超长时间）_1957986592572981249.json, 数字人/数字人/双人版-数字人InfiniteTalk -图片+音频=高质量数字人（支持超长时间）_1963963504116027393.json, 数字人/数字人/数字人infinitetalk（视频+音频驱动）_1958735631235067905.json, 数字人/数字人/数字人带货最强数字人infinitetalk（视频+音频驱动）支持长视频_1958311795096240130.json, 数字人/数字人/最新数字人InfiniteTalk -图片+音频=高质量数字人（支持超长时间）_1957814463565066242.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_494

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/v2v视频+音频生成数字人带货视频 infinitetalk-上传视频+一段音频驱动=支持长视频_1976912864780947457.json、平台全量/最新数字人InfiniteTalk -视频+音频=高质量数字人（支持超长时间）_1957986592572981249.json、数字人/数字人/双人版-数字人InfiniteTalk -图片+音频=高质量数字人（支持超长时间）_1963963504116027393.json、数字人/数字人/数字人infinitetalk（视频+音频驱动）_1958735631235067905.json、数字人/数字人/数字人带货最强数字人infinitetalk（视频+音频驱动）支持长视频_1958311795096240130.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `CR Text`
- `DownloadAndLoadWav2VecModel`
- `GetNode`
- `ImpactSwitch`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAudio`
- `RH_LLMAPI_NODE`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Audio Duration (mtb)` —— 5/6 个有
- `AudioCrop` —— 5/6 个有
- `ImageFromBatch+` —— 5/6 个有
- `JWIntegerToString` —— 5/6 个有
- `WanVideoTextEncode` —— 5/6 个有
- `PreviewImage` —— 4/6 个有
- `VHS_LoadVideo` —— 4/6 个有
- `easy compare` —— 4/6 个有
- `easy ifElse` —— 4/6 个有
- `easy imageScaleDownToSize` —— 4/6 个有
- `easy imageSize` —— 4/6 个有
- `GetImagesFromBatchIndexed` —— 3/6 个有
- `LoadImage` —— 2/6 个有
- `Bookmark (rgthree)` —— 1/6 个有
- `GetImageRangeFromBatch` —— 1/6 个有
- `GetImageSizeAndCount` —— 1/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `MaskPreview+` —— 1/6 个有
- `SeparateMasks` —— 1/6 个有
- `WanVideoEncode` —— 1/6 个有
- `WanVideoTextEncodeCached` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
