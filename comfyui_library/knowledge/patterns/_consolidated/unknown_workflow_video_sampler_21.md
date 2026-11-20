---
name: unknown_workflow_video_sampler_21
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.571857
common_nodes: [CLIPVisionLoader, DrawViTPose, GetImageSizeAndCount, GetNode, ImageResizeKJv2, LoadImage, PoseAndFaceDetection, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached]
problems: []
missing: []
members: [平台全量/Wan2.2_Animate Q弹动作迁移_2040534663193694209.json, 平台全量/替换视频人物背景_2030952490664988674.json, 平台全量/最新动作迁移_不偏移、不变色、人物一致性_2091168971730018306.json, 平台全量/迁移2.0_2031738322158100482.json, 数字人/数字人/wanvideo_WanAnimate_V2_1974837982966493186.json, 数字人/数字人/舞蹈克隆_动作迁移表情迁移_改变原图背景_Wan2.2_1995364899742265346.json, 视频生成/图生视频/舞蹈克隆改变原图背景_Wan2.2_2062169414258221058.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_21

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/Wan2.2_Animate Q弹动作迁移_2040534663193694209.json、平台全量/替换视频人物背景_2030952490664988674.json、平台全量/最新动作迁移_不偏移、不变色、人物一致性_2091168971730018306.json、平台全量/迁移2.0_2031738322158100482.json、数字人/数字人/wanvideo_WanAnimate_V2_1974837982966493186.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `PoseAndFaceDetection`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 6/7 个有
- `Int` —— 6/7 个有
- `OnnxDetectionModelLoader` —— 6/7 个有
- `WanVideoLoraSelectMulti` —— 6/7 个有
- `WanVideoModelLoader` —— 6/7 个有
- `WanVideoSetLoRAs` —— 6/7 个有
- `WanVideoVAELoader` —— 6/7 个有
- `BlockifyMask` —— 5/7 个有
- `DownloadAndLoadSAM2Model` —— 5/7 个有
- `DrawMaskOnImage` —— 5/7 个有
- `Sam2Segmentation` —— 5/7 个有
- `WanVideoContextOptions` —— 5/7 个有
- `VHS_VideoInfo` —— 4/7 个有
- `WanVideoTorchCompileSettings` —— 4/7 个有
- `easy cleanGpuUsed` —— 4/7 个有
- `GrowMaskWithBlur` —— 3/7 个有
- `ImageConcatMulti` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `SaveImage` —— 3/7 个有
- `TT_img_enc_v2` —— 3/7 个有
- `DownloadAndLoadGIMMVFIModel` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `GIMMVFI_interpolate` —— 2/7 个有
- `GrowMask` —— 2/7 个有
- `ImageBlend` —— 2/7 个有
- `MathExpression|pysssss` —— 2/7 个有
- `RHHiddenNodes` —— 2/7 个有
- `SaveLatent` —— 2/7 个有
- `WanVideoEncode` —— 2/7 个有
- `MemoryCleaner` —— 1/7 个有
- `RIFE VFI` —— 1/7 个有
- `TextInput_` —— 1/7 个有
- `WanVideoTeaCache` —— 1/7 个有
- `workflow>1` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
