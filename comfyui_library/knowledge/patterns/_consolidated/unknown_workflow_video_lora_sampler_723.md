---
name: unknown_workflow_video_lora_sampler_723
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9655
common_nodes: [AudioSeparation, CLIPVisionLoader, CR Prompt Text, DownloadAndLoadWav2VecModel, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, LoadImage, LoadWanVideoT5TextEncoder, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/InfiniteTalk+Lynx人脸一致性_无限长音频驱动数字人_20251117_1990595971572785153.json, 视频生成/图生视频/InfiniteTalk无限长音频驱动数字人_20251117_1990339469129732098.json, 视频生成/图生视频/祝福视频测试 InfiniteTalk Lightx2v+Rcm_2037816256153264129.json, 视频生成/图生视频/（双人版）Infinite Talk超自然无限长度图生视频数字人V5_1957825819450208257.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_723

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/InfiniteTalk+Lynx人脸一致性_无限长音频驱动数字人_20251117_1990595971572785153.json、视频生成/图生视频/InfiniteTalk无限长音频驱动数字人_20251117_1990339469129732098.json、视频生成/图生视频/祝福视频测试 InfiniteTalk Lightx2v+Rcm_2037816256153264129.json、视频生成/图生视频/（双人版）Infinite Talk超自然无限长度图生视频数字人V5_1957825819450208257.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `AudioSeparation`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `DownloadAndLoadWav2VecModel`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 2/4 个有
- `Frames Slice` —— 2/4 个有
- `MathExpression|pysssss` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `SoundFlow_GetLength` —— 2/4 个有
- `WanVideoBlockSwap` —— 2/4 个有
- `JWFloat` —— 1/4 个有
- `LoadLynxResampler` —— 1/4 个有
- `LynxEncodeFaceIP` —— 1/4 个有
- `LynxInsightFaceCrop` —— 1/4 个有
- `WanVideoAddLynxEmbeds` —— 1/4 个有
- `WanVideoExtraModelSelect` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
