---
name: unknown_workflow_video_lora_sampler_222
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.611778
common_nodes: [CLIPVisionLoader, DrawViTPose, GetNode, ImageResizeKJv2, Int, LoadImage, MathExpression|pysssss, OnnxDetectionModelLoader, PoseAndFaceDetection, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan22Animate动作迁移抖版_2004522934133817346.json, 视频生成/图生视频/Wan22Animate动作迁移抖版_2029116870359519233.json, 视频生成/图生视频/万能动作表情_姿势迁移唱歌跳舞加长版_2020345629322518529.json, 视频生成/图生视频/动作迁移人物替换主体替换_2046604886866927617.json, 视频生成/图生视频/动作迁移人物替换主体替换_2059509696591122433.json, 视频生成/图生视频/姿势参考_1980236223493136385.json, 视频生成/图生视频/自用动作模仿动作迁移_2013906240371429377.json, 视频生成/图生视频/舞蹈克隆改变原图背景_Wan2.2_2062169414258221058.json, 视频生成/文生视频/图生视频 极速版 动作模仿 动作迁移 人物替换 Wan 2.2_2044310101514788865.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_222

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/Wan22Animate动作迁移抖版_2004522934133817346.json、视频生成/图生视频/Wan22Animate动作迁移抖版_2029116870359519233.json、视频生成/图生视频/万能动作表情_姿势迁移唱歌跳舞加长版_2020345629322518529.json、视频生成/图生视频/动作迁移人物替换主体替换_2046604886866927617.json、视频生成/图生视频/动作迁移人物替换主体替换_2059509696591122433.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：61%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `GetNode`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `MathExpression|pysssss`
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
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/9 个有
- `ImageConcatMulti` —— 7/9 个有
- `PreviewImage` —— 7/9 个有
- `WanVideoTorchCompileSettings` —— 7/9 个有
- `BlockifyMask` —— 5/9 个有
- `DownloadAndLoadSAM2Model` —— 5/9 个有
- `DrawMaskOnImage` —— 5/9 个有
- `GetImageSizeAndCount` —— 5/9 个有
- `GrowMask` —— 5/9 个有
- `Sam2Segmentation` —— 5/9 个有
- `CR Text` —— 4/9 个有
- `ImageFromBatch` —— 4/9 个有
- `ImpactInt` —— 4/9 个有
- `Textbox` —— 4/9 个有
- `DownloadAndLoadGIMMVFIModel` —— 3/9 个有
- `GIMMVFI_interpolate` —— 3/9 个有
- `INTConstant` —— 3/9 个有
- `ImageBlend` —— 3/9 个有
- `CM_IntToFloat` —— 2/9 个有
- `ImageFromBatch+` —— 2/9 个有
- `LayerUtility: PurgeVRAM` —— 2/9 个有
- `LayerUtility: PurgeVRAM V2` —— 2/9 个有
- `SimpleMath+` —— 2/9 个有
- `WanVideoLoraSelect` —— 2/9 个有
- `easy int` —— 2/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `SaveImage` —— 1/9 个有
- `SaveLatent` —— 1/9 个有
- `TT_img_enc_v2` —— 1/9 个有
- `WanVideoEncode` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
