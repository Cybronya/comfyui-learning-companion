---
name: unknown_workflow_video_clip_unet_13
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.5708
common_nodes: [BlockifyMask, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, Display Int (rgthree), DrawMaskOnImage, DrawViTPose, GetImageRangeFromBatch, GetNode, GrowMask, ImageBatchMulti, ImageResizeKJv2, Int, LayerUtility: PurgeVRAM, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, OnnxDetectionModelLoader, PathchSageAttentionKJ, PoseAndFaceDetection, PoseDetectionOneToAllAnimation, PreviewImage, Primitive integer [Crystools], RH_Translator, SDPoseOODLoader, SDPoseOODProcessor, SetNode, SimpleMath+, TorchCompileModelWanVideoV2, UNETLoader, VAELoader, VHS_GetImageCount, VHS_LoadVideo, VHS_VideoCombine, YOLOModelLoader, easy float, easy sam3ModelLoader, easy sam3VideoSegmentation, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/玩法5：门店引流舞蹈视频（换背景+人物替换_2009937148253835266.json, 平台全量/视频换背景+人物替换+动作迁移_2055902331270639617.json, 视频生成/图生视频/Animate人物替全能版_2009039132361756673.json, 视频生成/图生视频/视频换背景+人物替换+动作迁移_2045437666572898306.json, 视频生成/图生视频/（换背景+人物替换_2039239856160772097.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_13

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/玩法5：门店引流舞蹈视频（换背景+人物替换_2009937148253835266.json、平台全量/视频换背景+人物替换+动作迁移_2055902331270639617.json、视频生成/图生视频/Animate人物替全能版_2009039132361756673.json、视频生成/图生视频/视频换背景+人物替换+动作迁移_2045437666572898306.json、视频生成/图生视频/（换背景+人物替换_2039239856160772097.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：57%

## 共有节点

全部 5 个 workflow 都包含：
- `BlockifyMask`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `Display Int (rgthree)`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetImageRangeFromBatch`
- `GetNode`
- `GrowMask`
- `ImageBatchMulti`
- `ImageResizeKJv2`
- `Int`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `OnnxDetectionModelLoader`
- `PathchSageAttentionKJ`
- `PoseAndFaceDetection`
- `PoseDetectionOneToAllAnimation`
- `PreviewImage`
- `Primitive integer [Crystools]`
- `RH_Translator`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SetNode`
- `SimpleMath+`
- `TorchCompileModelWanVideoV2`
- `UNETLoader`
- `VAELoader`
- `VHS_GetImageCount`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `YOLOModelLoader`
- `easy float`
- `easy sam3ModelLoader`
- `easy sam3VideoSegmentation`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `Float` —— 4/5 个有
- `ImageConcatMulti` —— 4/5 个有
- `Text` —— 4/5 个有
- `VHS_VideoInfoLoaded` —— 4/5 个有
- `easy convertAnything` —— 4/5 个有
- `easy showAnything` —— 4/5 个有
- `KSampler` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `TrimVideoLatent` —— 3/5 个有
- `VAEDecode` —— 3/5 个有
- `WanAnimateToVideo` —— 3/5 个有
- `AILab_MaskPreview` —— 2/5 个有
- `GrowMaskWithBlur` —— 2/5 个有
- `ImageFromBatch` —— 2/5 个有
- `Label (rgthree)` —— 2/5 个有
- `MaskPreview+` —— 2/5 个有
- `RHHiddenNodes` —— 2/5 个有
- `Sa2VANodeTpl` —— 2/5 个有
- `SeCModelLoader` —— 2/5 个有
- `SeCVideoSegmentation` —— 2/5 个有
- `WanVideoBlockSwap` —— 2/5 个有
- `WanVideoLoraSelectMulti` —— 2/5 个有
- `WanVideoModelLoader` —— 2/5 个有
- `WanVideoSetBlockSwap` —— 2/5 个有
- `WanVideoSetLoRAs` —— 2/5 个有
- `WanVideoVAELoader` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `workflow>采集` —— 2/5 个有
- `workflow>采集2` —— 2/5 个有
- `workflow>采集3` —— 2/5 个有
- `CM_IntToFloat` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `GroundingDinoModelLoader_SDPose` —— 1/5 个有
- `ImageBlend` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 63 | 63 - 63 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 63，观测区间 63 - 63，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 63，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 高发问题（6/5 个样本）：Steps较低可能导致细节不足
