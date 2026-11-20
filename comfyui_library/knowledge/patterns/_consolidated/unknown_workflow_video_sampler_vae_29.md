---
name: unknown_workflow_video_sampler_vae_29
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.671167
common_nodes: [AddLabel, EmptyImage, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImagePadKJ, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, Primitive integer [Crystools], RH_Captioner, SetNode, ShowText|pysssss, Text Concatenate, Text Multiline, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/VACE14B-极致完美动作姿势迁移_1926653380469624833.json, 平台全量/吉卜力Ghibli视频转绘_CausVid3-9步VACE关键帧+姿势视频转换工作流_1978328443202985986.json, 平台全量/通义万相统一模型FusionX-VACE视频转绘美女跳舞转绘_1934542153010094082.json, 平台全量/通过动作Pose迁移极速WanVACE+CausVid（3-9步生图步骤）_1938069669180018690.json, 视频生成/图生视频/3-9步极速WanVACE_Pose迁移_1932617969560383490.json, 视频生成/图生视频/AccVid加速+VACE14B-极致完美动作姿势迁移_1927527393152634881.json, 视频生成/图生视频/吉卜力视频转绘_CausVid3-9步VACE关键帧+姿势和深度双控制_1925046681505886210.json, 视频生成/图生视频/突击侦查动作迁移-FLORA版本-动作迁移FusionX_1934654875315675138.json, 视频生成/图生视频/突击侦查动作迁移-FusionX-VACE大师级视频_1933860099905773569.json, 视频生成/图生视频/舞蹈迁移-FusionX-VACE大师级视频_1933562748272033793.json, 视频生成/图生视频/舞蹈迁移-FusionX-VACE大师级视频ott_1940038425300860930.json, 视频生成/图生视频/通义万相统一模型FusionX-LORA版本美女跳舞转绘工作流_1935676000963321857.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_29

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（平台全量/VACE14B-极致完美动作姿势迁移_1926653380469624833.json、平台全量/吉卜力Ghibli视频转绘_CausVid3-9步VACE关键帧+姿势视频转换工作流_1978328443202985986.json、平台全量/通义万相统一模型FusionX-VACE视频转绘美女跳舞转绘_1934542153010094082.json、平台全量/通过动作Pose迁移极速WanVACE+CausVid（3-9步生图步骤）_1938069669180018690.json、视频生成/图生视频/3-9步极速WanVACE_Pose迁移_1932617969560383490.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 12 个 workflow 都包含：
- `AddLabel`
- `EmptyImage`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImagePadKJ`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `Primitive integer [Crystools]`
- `RH_Captioner`
- `SetNode`
- `ShowText|pysssss`
- `Text Concatenate`
- `Text Multiline`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 11/12 个有
- `Fast Groups Bypasser (rgthree)` —— 11/12 个有
- `WanVideoLoraSelect` —— 11/12 个有
- `ColorMatch` —— 10/12 个有
- `DWPreprocessor` —— 9/12 个有
- `ImageBlend` —— 9/12 个有
- `Zoe-DepthMapPreprocessor` —— 5/12 个有
- `GetImageRangeFromBatch` —— 4/12 个有
- `PreviewImage` —— 3/12 个有
- `WanVideoExperimentalArgs` —— 3/12 个有
- `WanVideoSLG` —— 3/12 个有
- `WanVideoTeaCache` —— 3/12 个有
- `easy cleanGpuUsed` —— 3/12 个有
- `DepthAnything_V2` —— 2/12 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 2/12 个有
- `EasyControlGenerate` —— 2/12 个有
- `EasyControlLoadFlux` —— 2/12 个有
- `EasyControlLoadLora` —— 2/12 个有
- `ImageResizeTo8x` —— 2/12 个有
- `Bjornulf_ShowInt` —— 1/12 个有
- `Bookmark (rgthree)` —— 1/12 个有
- `LeReS-DepthMapPreprocessor` —— 1/12 个有
- `PrimitiveStringMultiline` —— 1/12 个有
- `WanVideoEnhanceAVideo` —— 1/12 个有
- `WanVideoVACEStartToEndFrame` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
