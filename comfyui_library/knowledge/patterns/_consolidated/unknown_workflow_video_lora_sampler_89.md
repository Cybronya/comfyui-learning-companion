---
name: unknown_workflow_video_lora_sampler_89
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.620647
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, DrawViTPose, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SeCModelLoader, SeCVideoSegmentation, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/Wan2.2 Animate sec自动抠像人物替换_2057002999330988034.json, 图片生成/图生图/Wan2.2Animate点编辑器指定替换人物局部_2028106785063702529.json, 数字人/数字人/alan自用-主体替换sec video segmentation_1983904795276836866.json, 数字人/数字人/人物替换   角色替换   二创首选  Wan2.2 wan22_2045772090871123969.json, 数字人/数字人/人物替换  角色替换   二创首选_2052270878615977985.json, 视频生成/图生视频/(Relight修正版)Wan Animate KJ V2版+Sec稳定遮罩视频换装V1_1978363035192549378.json, 视频生成/图生视频/Wan Animate KJ V2版+Sec稳定自动遮罩视频换装_1977311321710567425.json, 视频生成/图生视频/Wan2.2  Wan22 角色替换   动作迁移  二创首选_2042132086164819970.json, 视频生成/图生视频/Wan2.2  wan 二创首选 角色替换 动作模仿 图生视频_2042131699907170305.json, 视频生成/图生视频/Wan2.2  wan 角色替换 动作模仿 图生视频_2042176153171009537.json, 视频生成/图生视频/Wan2.2  wan 角色替换 动作模仿 图生视频_2042932527039516674.json, 视频生成/图生视频/Wan2.2  二创首选 角色替换 动作模仿 图生视频_2041872588984557569.json, 视频生成/图生视频/Wan2.2  人物替换_角色替换_动作模仿_二创首选_2039518740357844993.json, 视频生成/图生视频/Wan2.2  角色替换_动作模仿_图生视频_2039615736561274882.json, 视频生成/图生视频/视频换装稳定版，可切镜头V3_1990353025669754881.json, 视频生成/图生视频/（自用）Wan Animate KJ V2版+Sec稳定遮罩Mix视频V3（换装前置）_1977639019339239426.json, 视频生成/文生视频/Wan Animate KJ V2版+Sec稳定遮罩视频换装V3_1976929662687420417.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_89

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/Wan2.2 Animate sec自动抠像人物替换_2057002999330988034.json、图片生成/图生图/Wan2.2Animate点编辑器指定替换人物局部_2028106785063702529.json、数字人/数字人/alan自用-主体替换sec video segmentation_1983904795276836866.json、数字人/数字人/人物替换   角色替换   二创首选  Wan2.2 wan22_2045772090871123969.json、数字人/数字人/人物替换  角色替换   二创首选_2052270878615977985.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 17 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `DrawViTPose`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `SeCModelLoader`
- `SeCVideoSegmentation`
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
- `GetImageSizeAndCount` —— 16/17 个有
- `PreviewImage` —— 16/17 个有
- `GetNode` —— 15/17 个有
- `GrowMask` —— 15/17 个有
- `ImageConcanate` —— 15/17 个有
- `JWInteger` —— 15/17 个有
- `PointsEditor` —— 15/17 个有
- `SetNode` —— 15/17 个有
- `VHS_VideoInfo` —— 14/17 个有
- `INTConstant` —— 11/17 个有
- `CR Text` —— 10/17 个有
- `InvertMask` —— 10/17 个有
- `LayerUtility: ImageBlend` —— 10/17 个有
- `MaskToImage` —— 10/17 个有
- `easy cleanGpuUsed` —— 10/17 个有
- `ImageFromBatch+` —— 9/17 个有
- `ImageConcatMulti` —— 7/17 个有
- `ImageFromBatch` —— 7/17 个有
- `PrimitiveInt` —— 7/17 个有
- `ACE_ImageFaceCrop` —— 6/17 个有
- `ClothesSegment` —— 6/17 个有
- `EmptyImage` —— 6/17 个有
- `PDIMAGE_LongerSize` —— 6/17 个有
- `CR Prompt Text` —— 5/17 个有
- `DownloadAndLoadSAM2Model` —— 5/17 个有
- `PoseRetargetPromptHelper` —— 5/17 个有
- `Sam2Segmentation` —— 5/17 个有
- `WanVideoEncode` —— 5/17 个有
- `WanVideoTorchCompileSettings` —— 5/17 个有
- `WanVideoUni3C_ControlnetLoader` —— 5/17 个有
- `WanVideoUni3C_embeds` —— 5/17 个有
- `easy showAnything` —— 5/17 个有
- `WanVideoContextOptions` —— 4/17 个有
- `segformer_b2_clothes` —— 3/17 个有
- `GrowMaskWithBlur` —— 2/17 个有
- `CoordinatePlotter` —— 1/17 个有
- `ImageUpscaleWithModel` —— 1/17 个有
- `LayerMask: MaskPreview` —— 1/17 个有
- `SaveImage` —— 1/17 个有
- `SimpleMath+` —— 1/17 个有
- `TT_img_enc_v2` —— 1/17 个有
- `UpscaleModelLoader` —— 1/17 个有
- `easy framesEditor` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
