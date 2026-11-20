---
name: unknown_workflow_video_lora_sampler_352
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.867875
common_nodes: [Bjornulf_ShowJson, DWPreprocessor, DownloadAndLoadGIMMVFIModel, GIMMVFI_interpolate, GetImageSizeAndCount, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, WanVideoVAELoader, easy clearCacheAll]
problems: []
missing: []
members: [平台全量/AI动作迁移大师 _ 精准动作捕捉与迁移系统_1957288105319526402.json, 视频生成/图生视频/万相wan2.2动作迁移 +vace+radial+补帧_1957679362386620417.json, 视频生成/图生视频/动作迁移wan2.2 lora 加强版_1953648697265586178.json, 视频生成/图生视频/啊癫 动作迁移wan2.2 lora 加强版_1961001361997500417.json, 视频生成/图生视频/最强视频跳舞打拳万相wan2.2动作迁移 +MiniCPM4.5V+补帧_1963854925186961409.json, 视频生成/图生视频/视频-动作迁移wan2.2 lora 加强版_1960782180505071617.json, 视频生成/文生视频/WAN_VACE_14B + CAUSVID + 视频姿态控制 【跳舞视频流程】- 视频课程配套_1931599157772136450.json, 视频生成/文生视频/【动作迁移】wan2.2 lora 视频生视频加强版_1955515292903358465.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_352

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（平台全量/AI动作迁移大师 _ 精准动作捕捉与迁移系统_1957288105319526402.json、视频生成/图生视频/万相wan2.2动作迁移 +vace+radial+补帧_1957679362386620417.json、视频生成/图生视频/动作迁移wan2.2 lora 加强版_1953648697265586178.json、视频生成/图生视频/啊癫 动作迁移wan2.2 lora 加强版_1961001361997500417.json、视频生成/图生视频/最强视频跳舞打拳万相wan2.2动作迁移 +MiniCPM4.5V+补帧_1963854925186961409.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
- `Bjornulf_ShowJson`
- `DWPreprocessor`
- `DownloadAndLoadGIMMVFIModel`
- `GIMMVFI_interpolate`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `RH_Captioner` —— 7/8 个有
- `easy cleanGpuUsed` —— 7/8 个有
- `Display Int (rgthree)` —— 6/8 个有
- `EmptyImage` —— 6/8 个有
- `GetNode` —— 6/8 个有
- `ImageScaleToMegapixels` —— 6/8 个有
- `MaskToImage` —— 6/8 个有
- `PreviewImage` —— 6/8 个有
- `SetNode` —— 6/8 个有
- `UpscaleModelLoader` —— 6/8 个有
- `VHS_SplitImages` —— 6/8 个有
- `WanVideoTeaCache` —— 6/8 个有
- `Int` —— 2/8 个有
- `LayerUtility: PurgeVRAM V2` —— 2/8 个有
- `WanVideoEasyCache` —— 2/8 个有
- `WanVideoEnhanceAVideo` —— 2/8 个有
- `AILab_MiniCPM_4_V` —— 1/8 个有
- `ImagePadKJ` —— 1/8 个有
- `WanVideoSetRadialAttention` —— 1/8 个有
- `WanVideoTorchCompileSettings` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
