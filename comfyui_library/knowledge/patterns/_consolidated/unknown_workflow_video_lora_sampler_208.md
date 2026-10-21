---
name: unknown_workflow_video_lora_sampler_208
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.544222
common_nodes: [CLIPVisionLoader, DrawViTPose, GetNode, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1971474322126782465.json, 视频生成/图生视频/1975351604679413761.json, 视频生成/图生视频/2030543201047678977.json, 视频生成/图生视频/4V商用版本 支持 运镜，切镜头，武术，跳舞，侧面迁移，_2093353108847030274.json, 视频生成/图生视频/1976931314983161857.json, 视频生成/图生视频/1975030930718986242.json, 视频生成/图生视频/1980113724029702145.json, 视频生成/图生视频/2013906240371429377.json, 视频生成/文生视频/图生视频 极速版 动作模仿 动作迁移 人物替换 Wan 2.2_2044310101514788865.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_208

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1971474322126782465.json、视频生成/图生视频/1975351604679413761.json、视频生成/图生视频/2030543201047678977.json、视频生成/图生视频/4V商用版本 支持 运镜，切镜头，武术，跳舞，侧面迁移，_2093353108847030274.json、视频生成/图生视频/1976931314983161857.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：54%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 8/9 个有
- `DrawMaskOnImage` —— 8/9 个有
- `ImageConcatMulti` —— 8/9 个有
- `PreviewImage` —— 8/9 个有
- `WanVideoTorchCompileSettings` —— 8/9 个有
- `DownloadAndLoadSAM2Model` —— 7/9 个有
- `Int` —— 7/9 个有
- `Sam2Segmentation` —— 7/9 个有
- `GetImageSizeAndCount` —— 6/9 个有
- `GrowMask` —— 6/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/9 个有
- `MathExpression|pysssss` —— 5/9 个有
- `INTConstant` —— 4/9 个有
- `ImageBlend` —— 4/9 个有
- `ImpactInt` —— 4/9 个有
- `DownloadAndLoadGIMMVFIModel` —— 3/9 个有
- `GIMMVFI_interpolate` —— 3/9 个有
- `ImageFromBatch` —— 3/9 个有
- `LayerUtility: PurgeVRAM V2` —— 3/9 个有
- `CR Text` —— 2/9 个有
- `GrowMaskWithBlur` —— 2/9 个有
- `GemmaAPITextEncode` —— 1/9 个有
- `ImageRemoveBackground+` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `RIFE VFI` —— 1/9 个有
- `RemBGSession+` —— 1/9 个有
- `ShellAgentPluginSaveAudios` —— 1/9 个有
- `Text` —— 1/9 个有
- `Textbox` —— 1/9 个有
- `WanVideoContextOptions` —— 1/9 个有
- `easy positive` —— 1/9 个有
- `int _O` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
