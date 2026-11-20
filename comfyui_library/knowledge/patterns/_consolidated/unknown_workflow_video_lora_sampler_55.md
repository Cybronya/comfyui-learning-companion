---
name: unknown_workflow_video_lora_sampler_55
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.748143
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, ImageResizeKJv2, JWInteger, LoadImage, PixelPerfectResolution, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/Wan Animate 2.2：角色动作迁移_1969987148046868481.json, 数字人/数字人/animi跳舞_1989222596455575553.json, 数字人/数字人/视频-动作表情口型-wan2.2-animate-KJ_1973995545582768129.json, 数字人/数字人/视频换装_1993900689311154178.json, 视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞 Animate_2082283032458907650.json, 视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞=AnimateWan2.2=艾橘溪_1969244065881595906.json, 视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞=AnimateWan2.2_2058552984040198146.json, 视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞=AnimateWan2.2_2058894447605280770.json, 视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞=AnimateWan2.2_2058904092608651265.json, 视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞=AnimateWan2.2_2060366272411557890.json, 视频生成/图生视频/AI动作模仿+唱歌跳舞对口型=AnimateWan2.2_2094462690289868801.json, 视频生成/图生视频/AI动作模仿+跳舞+剑舞=Animate wan2.2_2030816272992178178.json, 视频生成/图生视频/AI动作模仿+跳舞+剑舞=Animate wan2.2_2047151840906711042.json, 视频生成/图生视频/AI动作模仿+高清流畅！_2072563254043430913.json, 视频生成/图生视频/wan2.2 animate 动作迁移_2004038728341438465.json, 视频生成/图生视频/人物角色迁移 动作模仿+唱歌跳舞+舞剑 Wan2.2 图生视频  动作迁移 人物替换_2046042390951108610.json, 视频生成/图生视频/最强视频换装+Animate+Wan2.2_1985660962449629185.json, 视频生成/图生视频/表哥超级画质动作复刻V2.1_2002002967475699713.json, 视频生成/图生视频/视频换装 Animate Wan2.2_1976261739643838466.json, 视频生成/图生视频/高清流畅！AI动作模仿+跳舞+剑舞=AnimaAI动作模仿+跳舞+剑舞=Animate wan2.2_2047571961420713986.json, 视频生成/文生视频/Animate+Wan2.2 视频换装 模特服装更换_1970644180198453250.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_55

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（数字人/数字人/Wan Animate 2.2：角色动作迁移_1969987148046868481.json、数字人/数字人/animi跳舞_1989222596455575553.json、数字人/数字人/视频-动作表情口型-wan2.2-animate-KJ_1973995545582768129.json、数字人/数字人/视频换装_1993900689311154178.json、视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞 Animate_2082283032458907650.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 21 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `FaceMaskFromPoseKeypoints`
- `ImageCropByMaskAndResize`
- `ImageResizeKJv2`
- `JWInteger`
- `LoadImage`
- `PixelPerfectResolution`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `SetNode` —— 20/21 个有
- `WanVideoAnimateEmbeds` —— 20/21 个有
- `WanVideoModelLoader` —— 20/21 个有
- `GetNode` —— 19/21 个有
- `LayerUtility: PurgeVRAM` —— 18/21 个有
- `easy cleanGpuUsed` —— 18/21 个有
- `VHS_VideoInfo` —— 17/21 个有
- `PrimitiveInt` —— 14/21 个有
- `SimpleMath+` —— 14/21 个有
- `Text` —— 14/21 个有
- `ttN float` —— 14/21 个有
- `ImageFromBatch` —— 8/21 个有
- `ImageConcatMulti` —— 6/21 个有
- `BlockifyMask` —— 4/21 个有
- `DrawMaskOnImage` —— 4/21 个有
- `GrowMask` —— 4/21 个有
- `GetImageSizeAndCount` —— 3/21 个有
- `LayerMask: SegformerB2ClothesUltra` —— 3/21 个有
- `CR Prompt Text` —— 2/21 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/21 个有
- `RHHiddenNodes` —— 2/21 个有
- `VHS_VideoInfoLoaded` —— 2/21 个有
- `easy seed` —— 2/21 个有
- `LayerMask: BiRefNetUltraV2` —— 1/21 个有
- `LayerMask: LoadBiRefNetModelV2` —— 1/21 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
