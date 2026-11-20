---
name: unknown_workflow_video_lora_sampler_358
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.73675
common_nodes: [CLIPVisionLoader, CM_IntToFloat, DrawViTPose, GetImageSizeAndCount, GetNode, ImageResizeKJv2, Int, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SetNode, SimpleMath+, VHS_LoadVideo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Wan2.2 Animate 人物替换（背景保持）_2078709416081317890.json, 平台全量/Wan22Animate动作迁移-AIGC大赏_2041797532950470658.json, 平台全量/真正好用的Wan-Animate动作迁移_1979754783361896449.json, 平台全量/视频人物替换_2120067228040253441.json, 视频生成/图生视频/Wan-Animate人物替换V3_1989226857599995905.json, 视频生成/图生视频/Wan-Animate人物替换V3_2002723614807998465.json, 视频生成/图生视频/Wan-Animate人物替换_1988762483311652866.json, 视频生成/图生视频/Wan-Animate人物替换遮罩版V3_2001920042348494850.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_358

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（平台全量/Wan2.2 Animate 人物替换（背景保持）_2078709416081317890.json、平台全量/Wan22Animate动作迁移-AIGC大赏_2041797532950470658.json、平台全量/真正好用的Wan-Animate动作迁移_1979754783361896449.json、平台全量/视频人物替换_2120067228040253441.json、视频生成/图生视频/Wan-Animate人物替换V3_1989226857599995905.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：74%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPVisionLoader`
- `CM_IntToFloat`
- `DrawViTPose`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `Int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `SetNode`
- `SimpleMath+`
- `VHS_LoadVideo`
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
- `CR Text` —— 7/8 个有
- `ImageConcatMulti` —— 7/8 个有
- `LayerUtility: PurgeVRAM V2` —— 7/8 个有
- `RHHiddenNodes` —— 7/8 个有
- `SeCModelLoader` —— 7/8 个有
- `SeCVideoSegmentation` —— 7/8 个有
- `VHS_VideoCombine` —— 7/8 个有
- `BBoxesToSAM2` —— 6/8 个有
- `DownloadAndLoadQwenModel` —— 6/8 个有
- `ImageFromBatch` —— 6/8 个有
- `LayerMask: SAM2Ultra` —— 6/8 个有
- `MaskPreview+` —— 6/8 个有
- `QwenVLDetection` —— 6/8 个有
- `BlockifyMask` —— 4/8 个有
- `DrawMaskOnImage` —— 4/8 个有
- `GrowMask` —— 4/8 个有
- `ImageFromBatch+` —— 1/8 个有
- `MathExpression|pysssss` —— 1/8 个有
- `SaveImage` —— 1/8 个有
- `TT_img_enc_v2` —— 1/8 个有
- `WanVideoLoraSelect` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有
- `easy int` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
