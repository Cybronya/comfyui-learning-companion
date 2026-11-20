---
name: unknown_workflow_video_inpaint_vae
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.774938
common_nodes: [AIO_Preprocessor, AddLabel, DownloadAndLoadFlorence2Model, EmptyImage, Florence2Run, Florence2toCoordinates, GetImageSizeAndCount, GetNode, GrowMaskWithBlur, ImageConcatMulti, ImageFromBatch, ImageResizeKJ, InpaintPreprocessor, LayerUtility: ImageBlend, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, Primitive integer [Crystools], PrimitiveString, RHHiddenNodes, RH_Translator, SetNode, ShowText|pysssss, SimpleMath+, Text Concatenate, Text Multiline, VHS_LoadVideo, VHS_VideoCombine, WanVideoDecode, WanVideoSLG, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/文生图/[众馨]V2版本人物替换_1970731121958920193.json, 平台全量/Nuash版-产品视频人物替换_1955873309890105345.json, 平台全量/Nuash版-产品视频人物替换（人脸加强版） v2-加密节点修复_1960936206878085122.json, 平台全量/Nuash版-产品视频人物替换（口型+语音翻译+语音克隆） v3-加密_1964117775050526721.json, 平台全量/WAN视频自动人物替换最新版工作流_1969342086048870402.json, 平台全量/人物替换(针对单人电商优化)_1971151772242845697.json, 平台全量/视频人物替换-超强版本_1957429271709020162.json, 平台全量/视频自动人物替换-V2版本-循环版_1978447054970179586.json, 数字人/数字人/视频自动人物替换-V2版本-循环版_1964248185155801090.json, 数字人/数字人/视频自动人物替换-纵_2089698980228849665.json, 数字人/数字人/跨境换装展示 自动人物替换-V2版本-循环版_2089735308039516162.json, 视频生成/图生视频/Nuash版-产品视频人物替换（声音情绪复刻+翻译）v4-加密_1967792232470315009.json, 视频生成/图生视频/【gen全能视频Si】视频自动人物替换-v2版本_1961326580301762562.json, 视频生成/图生视频/人物替换v2视频_2009156507505532930.json, 视频生成/图生视频/人物替换，保留产品及场景，_2041570599998328833.json, 视频生成/文生视频/美女跳舞转绘视频人物替换视频主体替换V1.0_1958502748553637889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_vae

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/文生图/[众馨]V2版本人物替换_1970731121958920193.json、平台全量/Nuash版-产品视频人物替换_1955873309890105345.json、平台全量/Nuash版-产品视频人物替换（人脸加强版） v2-加密节点修复_1960936206878085122.json、平台全量/Nuash版-产品视频人物替换（口型+语音翻译+语音克隆） v3-加密_1964117775050526721.json、平台全量/WAN视频自动人物替换最新版工作流_1969342086048870402.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 16 个 workflow 都包含：
- `AIO_Preprocessor`
- `AddLabel`
- `DownloadAndLoadFlorence2Model`
- `EmptyImage`
- `Florence2Run`
- `Florence2toCoordinates`
- `GetImageSizeAndCount`
- `GetNode`
- `GrowMaskWithBlur`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ImageResizeKJ`
- `InpaintPreprocessor`
- `LayerUtility: ImageBlend`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `Primitive integer [Crystools]`
- `PrimitiveString`
- `RHHiddenNodes`
- `RH_Translator`
- `SetNode`
- `ShowText|pysssss`
- `SimpleMath+`
- `Text Concatenate`
- `Text Multiline`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoSLG`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadSAM2Model` —— 15/16 个有
- `PreviewImage` —— 15/16 个有
- `Sam2Segmentation` —— 15/16 个有
- `WanVideoSampler` —— 15/16 个有
- `RH_Captioner` —— 13/16 个有
- `WanVideoEnhanceAVideo` —— 13/16 个有
- `DepthAnything_V2` —— 12/16 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 12/16 个有
- `ImageBlend` —— 12/16 个有
- `ImpactSwitch` —— 12/16 个有
- `WanVideoExperimentalArgs` —— 12/16 个有
- `easy imageRemBg` —— 11/16 个有
- `ColorMatch` —— 10/16 个有
- `Primitive float [Crystools]` —— 9/16 个有
- `UnloadModel` —— 6/16 个有
- `RMBG` —— 5/16 个有
- `WanVideoModelLoader` —— 5/16 个有
- `ApplyFaceProcessor` —— 4/16 个有
- `FaceProcessorLoader` —— 4/16 个有
- `ImageUpscaleWithModel` —— 4/16 个有
- `UpscaleModelLoader` —— 4/16 个有
- `WanVideoAddStandInLatent` —— 4/16 个有
- `WanVideoBlockSwap` —— 4/16 个有
- `WanVideoEncode` —— 4/16 个有
- `WanVideoLoraSelect` —— 4/16 个有
- `WanVideoTorchCompileSettings` —— 4/16 个有
- `AudioSeparation` —— 3/16 个有
- `DownloadAndLoadWav2VecModel` —— 3/16 个有
- `LayerUtility: PurgeVRAM` —— 3/16 个有
- `MultiTalkModelLoader` —— 3/16 个有
- `MultiTalkWav2VecEmbeds` —— 3/16 个有
- `VHS_VideoInfo` —— 3/16 个有
- `MegaTTS3Run` —— 2/16 个有
- `MultiLinePromptMG` —— 2/16 个有
- `PreviewAudio` —— 2/16 个有
- `RH_LLMAPI_NODE` —— 2/16 个有
- `ShowText` —— 2/16 个有
- `ImageResizeKJv2` —— 1/16 个有
- `IndexTTS2Run` —— 1/16 个有
- `InspyrenetRembg` —— 1/16 个有
- `LayerUtility: ColorImage V2` —— 1/16 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/16 个有
- `WanVideoSetBlockSwap` —— 1/16 个有
- `WanVideoSetLoRAs` —— 1/16 个有
- `WanVideoVACEModelSelect` —— 1/16 个有
- `easy showAnything` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
