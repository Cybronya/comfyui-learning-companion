---
name: unknown_workflow_video_lora_sampler_198
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.677111
common_nodes: [CLIPVisionLoader, GetImageSizeAndCount, GetNode, INTConstant, Int, LayerUtility: PurgeVRAM V2, LoadImage, SetNode, Text Multiline, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTeaCache, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/Animate超长视频舞蹈迁移-24G 动作精准_2000947142715899905.json, 视频生成/图生视频/Animate超长视频动作迁移 动作精准_2030683109536043010.json, 视频生成/图生视频/Animate超长视频动作迁移（人物一致性高清电影级）_2007757058510168066.json, 视频生成/图生视频/Animate超长视频舞蹈迁移-24G 支持20s+_2000895108826398721.json, 视频生成/图生视频/Animate超长视频舞蹈迁移-24G_1999108736645988353.json, 视频生成/图生视频/Animate超长视频舞蹈迁移-动作迁移人物一致_2013783129579851778.json, 视频生成/图生视频/基尼太美Animate_2046453872159367169.json, 视频生成/图生视频/最新Animate 超长视频舞蹈迁移 单人—多人_2032725036360011777.json, 视频生成/图生视频/超长视频舞蹈迁移-或武打动作迁移人物一致性电影级高清Animate_1985123438920683522.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_198

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Animate超长视频舞蹈迁移-24G 动作精准_2000947142715899905.json、视频生成/图生视频/Animate超长视频动作迁移 动作精准_2030683109536043010.json、视频生成/图生视频/Animate超长视频动作迁移（人物一致性高清电影级）_2007757058510168066.json、视频生成/图生视频/Animate超长视频舞蹈迁移-24G 支持20s+_2000895108826398721.json、视频生成/图生视频/Animate超长视频舞蹈迁移-24G_1999108736645988353.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 9 个 workflow 都包含：
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
- `ImageResizeKJ` —— 8/9 个有
- `WanVideoLoraSelectMulti` —— 8/9 个有
- `Florence2Run` —— 7/9 个有
- `GroundingDinoModelLoader (segment anything2)` —— 7/9 个有
- `RHHiddenNodes` —— 7/9 个有
- `RH_Captioner` —— 7/9 个有
- `SDPoseOODLoader` —— 7/9 个有
- `SDPoseOODProcessor` —— 7/9 个有
- `ShowText|pysssss` —— 7/9 个有
- `Text Concatenate` —— 7/9 个有
- `Wan_video_prompt_generator` —— 7/9 个有
- `YOLOModelLoader` —— 7/9 个有
- `DrawViTPose` —— 6/9 个有
- `OnnxDetectionModelLoader` —— 6/9 个有
- `PoseAndFaceDetection` —— 6/9 个有
- `ImageUpscaleWithModel` —— 4/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/9 个有
- `UpscaleModelLoader` —— 4/9 个有
- `FlashVSRNode` —— 1/9 个有
- `easy anythingIndexSwitch` —— 1/9 个有
- `easy rangeInt` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
