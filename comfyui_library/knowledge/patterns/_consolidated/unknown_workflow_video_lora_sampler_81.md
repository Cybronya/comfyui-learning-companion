---
name: unknown_workflow_video_lora_sampler_81
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.752118
common_nodes: [CLIPVisionLoader, DWPreprocessor, FaceMaskFromPoseKeypoints, ImageCropByMaskAndResize, ImageResizeKJv2, JWInteger, LoadImage, PixelPerfectResolution, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/文生图/换脸图生视频动作迁移视频换装Wan2.2人物替换动作迁移（支持10s以上_2049085267893555202.json, 视频生成/图生视频/02角色迁移更新+全节点注释_2055549996304478210.json, 视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞 Animate_2082283032458907650.json, 视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞=AnimateWan2.2=艾橘溪_1969244065881595906.json, 视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞=AnimateWan2.2_2058552984040198146.json, 视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞=AnimateWan2.2_2058894447605280770.json, 视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞=AnimateWan2.2_2058904092608651265.json, 视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞=AnimateWan2.2_2060366272411557890.json, 视频生成/图生视频/AI动作模仿+唱歌跳舞对口型=AnimateWan2.2_2094462690289868801.json, 视频生成/图生视频/AI动作模仿+跳舞+剑舞=Animate wan2.2_2030816272992178178.json, 视频生成/图生视频/AI动作模仿+跳舞+剑舞=Animate wan2.2_2047151840906711042.json, 视频生成/图生视频/AI动作模仿+高清流畅！_2072563254043430913.json, 视频生成/图生视频/Animate Wan2.2 动作迁移2_1992566625708691457.json, 视频生成/图生视频/Animate wan2.2   抖音快手爆火美女跳舞_1986294172028207106.json, 视频生成/图生视频/Animate优化人物一致性精准替换_1969765016436154369.json, 视频生成/图生视频/Animate优化人物一致性精准替换【人物动作表情背景】_1971382393225592834.json, 视频生成/图生视频/Animate优化颜色匹配精准替换人换脸_1971226836661420034.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_81

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/文生图/换脸图生视频动作迁移视频换装Wan2.2人物替换动作迁移（支持10s以上_2049085267893555202.json、视频生成/图生视频/02角色迁移更新+全节点注释_2055549996304478210.json、视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞 Animate_2082283032458907650.json、视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞=AnimateWan2.2=艾橘溪_1969244065881595906.json、视频生成/图生视频/AI动作模仿+唱歌跳舞+剑舞=AnimateWan2.2_2058552984040198146.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 17 个 workflow 都包含：
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
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 16/17 个有
- `LayerUtility: PurgeVRAM` —— 16/17 个有
- `SetNode` —— 16/17 个有
- `VHS_VideoInfo` —— 16/17 个有
- `WanVideoLoraSelectMulti` —— 16/17 个有
- `easy cleanGpuUsed` —— 16/17 个有
- `Text` —— 13/17 个有
- `PrimitiveInt` —— 11/17 个有
- `SimpleMath+` —— 11/17 个有
- `ttN float` —— 11/17 个有
- `ImageFromBatch` —— 7/17 个有
- `BlockifyMask` —— 6/17 个有
- `DrawMaskOnImage` —— 6/17 个有
- `GrowMask` —— 6/17 个有
- `ImageConcatMulti` —— 4/17 个有
- `PreviewImage` —— 4/17 个有
- `DownloadAndLoadSAM2Model` —— 3/17 个有
- `GetImageSizeAndCount` —— 3/17 个有
- `INTConstant` —— 3/17 个有
- `LayerMask: SegformerB2ClothesUltra` —— 3/17 个有
- `PointsEditor` —— 3/17 个有
- `Sam2Segmentation` —— 3/17 个有
- `WanVideoEncode` —— 3/17 个有
- `WanVideoUni3C_ControlnetLoader` —— 3/17 个有
- `WanVideoUni3C_embeds` —— 3/17 个有
- `easy showAnything` —— 3/17 个有
- `CR Text` —— 1/17 个有
- `ImageBatchGet` —— 1/17 个有
- `ImitationHueNode` —— 1/17 个有
- `Int` —— 1/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/17 个有
- `LayerUtility: PurgeVRAM V2` —— 1/17 个有
- `LoadRembgByBiRefNetModel` —— 1/17 个有
- `MathExpression|pysssss` —— 1/17 个有
- `RembgByBiRefNet` —— 1/17 个有
- `WanVideoLoraSelect` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
