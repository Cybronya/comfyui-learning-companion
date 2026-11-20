---
name: unknown_workflow_video_lora_sampler_583
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.565
common_nodes: [CLIPVisionLoader, DrawViTPose, GetNode, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/动作迁移-WanAnimate- LightX2V-I2V_2001308075027988481.json, 平台全量/动作迁移人物替换主体替换_2041482113752506370.json, 平台全量/商K唱歌🎤动作模仿_1988936344661536770.json, 平台全量/工作流基础系列24-Wan2.2-Animate-角色替换_2055099733953261569.json, 平台全量/视频人物替换 wan2.2 animate 哥布林 买瓜_1971799688485793793.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_583

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/动作迁移-WanAnimate- LightX2V-I2V_2001308075027988481.json、平台全量/动作迁移人物替换主体替换_2041482113752506370.json、平台全量/商K唱歌🎤动作模仿_1988936344661536770.json、平台全量/工作流基础系列24-Wan2.2-Animate-角色替换_2055099733953261569.json、平台全量/视频人物替换 wan2.2 animate 哥布林 买瓜_1971799688485793793.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：57%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 4/5 个有
- `DownloadAndLoadSAM2Model` —— 4/5 个有
- `DrawMaskOnImage` —— 4/5 个有
- `GrowMask` —— 4/5 个有
- `Sam2Segmentation` —— 4/5 个有
- `GetImageSizeAndCount` —— 3/5 个有
- `INTConstant` —— 3/5 个有
- `ImageConcatMulti` —— 3/5 个有
- `Textbox` —— 3/5 个有
- `DownloadAndLoadGIMMVFIModel` —— 2/5 个有
- `GIMMVFI_interpolate` —— 2/5 个有
- `ImageFromBatch` —— 2/5 个有
- `ImpactInt` —— 2/5 个有
- `Int` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `MathExpression|pysssss` —— 2/5 个有
- `PointsEditor` —— 2/5 个有
- `VHS_VideoInfo` —— 2/5 个有
- `AILab_ImageCombiner` —— 1/5 个有
- `Bjornulf_ShowInt` —— 1/5 个有
- `DF_Get_image_size` —— 1/5 个有
- `Frame Select` —— 1/5 个有
- `ImageBlend` —— 1/5 个有
- `LayerUtility: ColorImage V2` —— 1/5 个有
- `LayerUtility: NumberCalculatorV2` —— 1/5 个有
- `RHHiddenNodes` —— 1/5 个有
- `RH_Translator` —— 1/5 个有
- `RMBG` —— 1/5 个有
- `RepeatImageBatch` —— 1/5 个有
- `ResizeAndPadImage` —— 1/5 个有
- `WanVideoContextOptions` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
