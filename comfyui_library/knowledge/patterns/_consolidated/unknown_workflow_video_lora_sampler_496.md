---
name: unknown_workflow_video_lora_sampler_496
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.94775
common_nodes: [CLIPVisionLoader, GetImageSize, INTConstant, Image Blank, ImageCompositeMasked, ImagePadKJ, ImageResizeKJ, ImageResizeKJv2, InspyrenetRembg, KepStringLiteral, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, PreviewImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MAGREF+IndexTTS+HeyGem带货数字人_1937836880912105473.json, 视频生成/图生视频/MAGREF三图参考_1936376393980874754.json, 视频生成/图生视频/MAGREF双图参考（对比）_1936333084193361922.json, 视频生成/图生视频/字节MAGREF+IndexTTS+HeyGem超级带货数字人_1937839794074619905.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_496

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/MAGREF+IndexTTS+HeyGem带货数字人_1937836880912105473.json、视频生成/图生视频/MAGREF三图参考_1936376393980874754.json、视频生成/图生视频/MAGREF双图参考（对比）_1936333084193361922.json、视频生成/图生视频/字节MAGREF+IndexTTS+HeyGem超级带货数字人_1937839794074619905.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageSize`
- `INTConstant`
- `Image Blank`
- `ImageCompositeMasked`
- `ImagePadKJ`
- `ImageResizeKJ`
- `ImageResizeKJv2`
- `InspyrenetRembg`
- `KepStringLiteral`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 3/4 个有
- `Seed Everywhere` —— 3/4 个有
- `CreateVideo` —— 2/4 个有
- `D_VideoLengthAdjuster` —— 2/4 个有
- `IndexTTSRun` —— 2/4 个有
- `LoadAudio` —— 2/4 个有
- `PreviewAudio` —— 2/4 个有
- `RH_HeyGemNode` —— 2/4 个有
- `SaveVideo` —— 2/4 个有
- `String Literal` —— 2/4 个有
- `ImageConcanate` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
