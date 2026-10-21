---
name: unknown_workflow_video_lora_sampler_114
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.862786
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, CR Prompt Text, DownloadAndLoadWav2VecModel, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadAudio, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1957839924697427969.json, 视频生成/图生视频/1957830385059164161.json, 视频生成/图生视频/1957825819450208257.json, 视频生成/图生视频/1963526777896521730.json, 视频生成/图生视频/1988918406697070593.json, 视频生成/图生视频/2026180704601645057.json, 视频生成/图生视频/1961400191553355778.json, 视频生成/图生视频/1963526752599511041.json, 视频生成/图生视频/1959825457199919105.json, 视频生成/图生视频/1977593107141283841.json, 视频生成/文生视频/(正面）Infinite talk数字人动态加强高版V4（Lightx2v+Rcm）_2035404909490741250.json, 视频生成/文生视频/Infinite+talk数字人动态加强高版V3.5_1991175069309448194.json, 视频生成/文生视频/对口型数字人Infinite talk_2013508435370840066.json, "音频生成/音频生成/MV,音乐达人，高动态音乐数字人_2046930658349555714.json"]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_114

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/1957839924697427969.json、视频生成/图生视频/1957830385059164161.json、视频生成/图生视频/1957825819450208257.json、视频生成/图生视频/1963526777896521730.json、视频生成/图生视频/1988918406697070593.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 14 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `DownloadAndLoadWav2VecModel`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadAudio`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoMultiTalk`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 13/14 个有
- `LoadWanVideoT5TextEncoder` —— 12/14 个有
- `WanVideoTextEncode` —— 12/14 个有
- `GetImageSizeAndCount` —— 11/14 个有
- `PreviewAny` —— 10/14 个有
- `JWFloat` —— 5/14 个有
- `Bjornulf_ShowInt` —— 2/14 个有
- `WanVideoTextEncodeCached` —— 2/14 个有
- `AudioToFPS` —— 1/14 个有
- `ColorMatch` —— 1/14 个有
- `ImageScaleBy` —— 1/14 个有
- `MathExpression|pysssss` —— 1/14 个有
- `Pick From Batch (mtb)` —— 1/14 个有
- `SaveImage` —— 1/14 个有
- `SimpleMath+` —— 1/14 个有
- `SoundFlow_GetLength` —— 1/14 个有
- `ToInt` —— 1/14 个有
- `VHS_LoadVideo` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
