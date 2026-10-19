---
name: unknown_workflow_video_lora_sampler_370
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.803
common_nodes: [AudioCrop, AudioSeparation, CLIPVisionLoader, DownloadAndLoadWav2VecModel, ImageResizeKJv2, LoadAudio, LoadImage, MultiTalkModelLoader, MultiTalkWav2VecEmbeds, PreviewAny, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoMultiTalk, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.1 InfiniTetalk 图像数字人配口型 KJ节点版_2044728496185937922.json, 视频生成/图生视频/2054610077646114818.json, 视频生成/图生视频/1993501240730599426.json, 视频生成/图生视频/1960547168962641921.json, 视频生成/图生视频/1977757445852463106.json, 视频生成/图生视频/2012499953494528001.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_370

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/Wan2.1 InfiniTetalk 图像数字人配口型 KJ节点版_2044728496185937922.json、视频生成/图生视频/2054610077646114818.json、视频生成/图生视频/1993501240730599426.json、视频生成/图生视频/1960547168962641921.json、视频生成/图生视频/1977757445852463106.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 6 个 workflow 都包含：
- `AudioCrop`
- `AudioSeparation`
- `CLIPVisionLoader`
- `DownloadAndLoadWav2VecModel`
- `ImageResizeKJv2`
- `LoadAudio`
- `LoadImage`
- `MultiTalkModelLoader`
- `MultiTalkWav2VecEmbeds`
- `PreviewAny`
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
- `GetImageSizeAndCount` —— 5/6 个有
- `INTConstant` —— 5/6 个有
- `WanVideoTorchCompileSettings` —— 5/6 个有
- `GetNode` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `WanVideoTextEncodeCached` —— 4/6 个有
- `JWInteger` —— 2/6 个有
- `LoadWanVideoT5TextEncoder` —— 2/6 个有
- `WanVideoTextEncode` —— 2/6 个有
- `Audio Duration (mtb)` —— 1/6 个有
- `CR Prompt Text` —— 1/6 个有
- `DF_Int_to_Float` —— 1/6 个有
- `MathExpression|pysssss` —— 1/6 个有
- `PixaromaLabel` —— 1/6 个有
- `PixaromaResolution` —— 1/6 个有
- `PlaySound|pysssss` —— 1/6 个有
- `easy compare` —— 1/6 个有
- `easy ifElse` —— 1/6 个有
- `easy imageSize` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
