---
name: unknown_workflow_video_lora_sampler_386
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.5566
common_nodes: [BlockifyMask, CLIPVisionLoader, DownloadAndLoadSAM2Model, DrawMaskOnImage, GetNode, ImageResizeKJv2, LoadImage, Sam2Segmentation, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/去掉字幕水印 wan2.2 animate_1971821276849434626.json, 图片生成/图生图/视频去水印去字幕_2042494499506626561.json, 视频生成/图生视频/自动抠图--最新Animate图片主体替换视频主体_1970425229413654530.json, 视频生成/文生视频/Wan2.2 Animate KJ版 人物动作迁移视频生成视频_1970355314094710785.json, 视频生成/文生视频/Wan2.2 Animate-KJ 美女跳舞 动作一键迁移复制姿势_1971474322126782465.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_386

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/去掉字幕水印 wan2.2 animate_1971821276849434626.json、图片生成/图生图/视频去水印去字幕_2042494499506626561.json、视频生成/图生视频/自动抠图--最新Animate图片主体替换视频主体_1970425229413654530.json、视频生成/文生视频/Wan2.2 Animate KJ版 人物动作迁移视频生成视频_1970355314094710785.json、视频生成/文生视频/Wan2.2 Animate-KJ 美女跳舞 动作一键迁移复制姿势_1971474322126782465.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：56%

## 共有节点

全部 5 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `Sam2Segmentation`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadGIMMVFIModel` —— 4/5 个有
- `GIMMVFI_interpolate` —— 4/5 个有
- `GetImageSizeAndCount` —— 4/5 个有
- `INTConstant` —— 4/5 个有
- `ImageConcatMulti` —— 4/5 个有
- `OnnxDetectionModelLoader` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `GrowMask` —— 3/5 个有
- `ImageBlend` —— 3/5 个有
- `PoseAndFaceDetection` —— 3/5 个有
- `Frame Select` —— 2/5 个有
- `PointsEditor` —— 2/5 个有
- `Textbox` —— 2/5 个有
- `VHS_VideoInfo` —— 2/5 个有
- `AILab_MaskPreview` —— 1/5 个有
- `Bookmark (rgthree)` —— 1/5 个有
- `DF_Get_image_size` —— 1/5 个有
- `DrawViTPose` —— 1/5 个有
- `Int` —— 1/5 个有
- `RH_Translator` —— 1/5 个有
- `WanVideoEncode` —— 1/5 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/5 个有
- `WanVideoUni3C_embeds` —— 1/5 个有
- `easy showAnything` —— 1/5 个有
- `easy showTensorShape` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
