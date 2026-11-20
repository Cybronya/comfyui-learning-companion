---
name: unknown_workflow_video_lora_sampler_215
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.683
common_nodes: [CLIPVisionLoader, GetImageSizeAndCount, GetNode, INTConstant, Int, LayerUtility: PurgeVRAM V2, LoadImage, SetNode, Text Multiline, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTeaCache, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/Animate超长视频舞蹈迁移-24G 动作精准_2000947142715899905.json, 平台全量/Animate超长视频舞蹈迁移-或武打动作迁移人物一致性高清电影级_1962961994305482754.json, 平台全量/超长视频动作迁移人物一致性高清电影级_2032339676601786370.json, 视频生成/图生视频/Animate超长视频动作迁移 动作精准_2030683109536043010.json, 视频生成/图生视频/Animate超长视频动作迁移（人物一致性高清电影级）_2007757058510168066.json, 视频生成/图生视频/Animate超长视频舞蹈迁移-24G 支持20s+_2000895108826398721.json, 视频生成/图生视频/Animate超长视频舞蹈迁移-24G_1999108736645988353.json, 视频生成/图生视频/Animate超长视频舞蹈迁移-动作迁移人物一致_2013783129579851778.json, 视频生成/图生视频/基尼太美Animate_2046453872159367169.json, 视频生成/图生视频/最新Animate 超长视频舞蹈迁移 单人—多人_2032725036360011777.json, 视频生成/图生视频/超长视频舞蹈迁移-或武打动作迁移人物一致性电影级高清Animate_1985123438920683522.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_215

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Animate超长视频舞蹈迁移-24G 动作精准_2000947142715899905.json、平台全量/Animate超长视频舞蹈迁移-或武打动作迁移人物一致性高清电影级_1962961994305482754.json、平台全量/超长视频动作迁移人物一致性高清电影级_2032339676601786370.json、视频生成/图生视频/Animate超长视频动作迁移 动作精准_2030683109536043010.json、视频生成/图生视频/Animate超长视频动作迁移（人物一致性高清电影级）_2007757058510168066.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `Int`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `SetNode`
- `Text Multiline`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTeaCache`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Florence2Run` —— 9/11 个有
- `GroundingDinoModelLoader (segment anything2)` —— 9/11 个有
- `ImageResizeKJ` —— 9/11 个有
- `RHHiddenNodes` —— 9/11 个有
- `RH_Captioner` —— 9/11 个有
- `SDPoseOODLoader` —— 9/11 个有
- `SDPoseOODProcessor` —— 9/11 个有
- `ShowText|pysssss` —— 9/11 个有
- `Text Concatenate` —— 9/11 个有
- `Wan_video_prompt_generator` —— 9/11 个有
- `YOLOModelLoader` —— 9/11 个有
- `DrawViTPose` —— 8/11 个有
- `OnnxDetectionModelLoader` —— 8/11 个有
- `PoseAndFaceDetection` —— 8/11 个有
- `WanVideoLoraSelectMulti` —— 8/11 个有
- `ImageUpscaleWithModel` —— 6/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/11 个有
- `UpscaleModelLoader` —— 6/11 个有
- `FlashVSRNode` —— 1/11 个有
- `easy anythingIndexSwitch` —— 1/11 个有
- `easy rangeInt` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
