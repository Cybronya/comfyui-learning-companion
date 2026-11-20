---
name: unknown_workflow_video_lora_sampler_158
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.650714
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, ImageConcatMulti, ImageCropByMaskAndResize, ImageResizeKJv2, LayerUtility: PurgeVRAM, LoadImage, PixelPerfectResolution, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/跳舞动作迁移2.0 _ Dance Motion Transfer 2.0_2013996160695930881.json, 平台全量/👾怪獸-Animate动作迁移👾_1973065381663346690.json, 平台全量/👾怪獸-Animate视频遮罩换万物👾_1970199559613915138.json, 数字人/数字人/视频换装_1993900689311154178.json, 视频生成/图生视频/Animate Wan2.2 动作迁移2_1992566625708691457.json, 视频生成/图生视频/WAN2.2Animate美女图片跳舞工作流【动作，表情迁移】_1971382412112510978.json, 视频生成/图生视频/Wan2.2 Animate 视频换人 视频人物替换_2018529838486790146.json, 视频生成/图生视频/啊癫 Wan2.2 Animate 视频换人 视频人物替换_1970522090514358273.json, 视频生成/图生视频/快速踩健身自行车_2081656460194443265.json, 视频生成/图生视频/扭pp_2082449087105953793.json, 视频生成/图生视频/最强视频换装+Animate+Wan2.2_1985660962449629185.json, 视频生成/图生视频/视频换人_Animate_Wan2.2_2116656426738348033.json, 视频生成/图生视频/视频换装 Animate Wan2.2_1976261739643838466.json, 视频生成/文生视频/Animate+Wan2.2 视频换装 模特服装更换_1970644180198453250.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_158

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（平台全量/跳舞动作迁移2.0 _ Dance Motion Transfer 2.0_2013996160695930881.json、平台全量/👾怪獸-Animate动作迁移👾_1973065381663346690.json、平台全量/👾怪獸-Animate视频遮罩换万物👾_1970199559613915138.json、数字人/数字人/视频换装_1993900689311154178.json、视频生成/图生视频/Animate Wan2.2 动作迁移2_1992566625708691457.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `ImageConcatMulti`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `PixelPerfectResolution`
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
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `JWInteger` —— 13/14 个有
- `VHS_VideoInfo` —— 13/14 个有
- `GetNode` —— 12/14 个有
- `SetNode` —— 12/14 个有
- `BlockifyMask` —— 11/14 个有
- `DrawMaskOnImage` —— 11/14 个有
- `GrowMask` —— 11/14 个有
- `LayerMask: SegformerB2ClothesUltra` —— 10/14 个有
- `Int` —— 5/14 个有
- `SimpleMath+` —— 5/14 个有
- `Text` —— 2/14 个有
- `Fast Groups Bypasser (rgthree)` —— 1/14 个有
- `INTConstant` —— 1/14 个有
- `ImageUpscaleWithModel` —— 1/14 个有
- `LayerMask: BiRefNetUltraV2` —— 1/14 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/14 个有
- `LayerMask: MaskGrow` —— 1/14 个有
- `RIFE VFI` —— 1/14 个有
- `UpscaleModelLoader` —— 1/14 个有
- `VHS_VideoInfoSource` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
