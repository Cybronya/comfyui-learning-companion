---
name: unknown_workflow_video_sampler_vae_6
type: Unknown Workflow
frequency: 27
level: moderate
coverage: 0.766778
common_nodes: [GetImageSizeAndCount, GetNode, ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, Primitive integer [Crystools], RHHiddenNodes, RH_Captioner, SetNode, ShowText|pysssss, Text Concatenate, Text Multiline, VHS_LoadVideo, VHS_VideoCombine, WanVideoDecode, WanVideoExperimentalArgs, WanVideoSLG, WanVideoSampler, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/自定义遮罩换背景_2008732012235988993.json, 平台全量/视频替换背景-V2版本（测试版）_2016782882668290050.json, 平台全量/视频替换背景-高级版_1985941558384046081.json, 平台全量/视频替换背景_2003339868539387905.json, 平台全量/视频替换背景_2042481839343931393.json, 平台全量/视频替换背景_2049383007345184769.json, 平台全量/视频替换背景_2085937275782909953.json, 数字人/数字人/视频替换背景-2.0版_1970430717945651201.json, 数字人/数字人/视频替换背景_2029154385007222786.json, 视频生成/图生视频/160帧-舞蹈-超高拟态-直出1920高清-V2版本_1942202708122341377.json, 视频生成/图生视频/wan2.2数字人人物迁移动作一致性_1992633923415109634.json, 视频生成/图生视频/wan2.2数字人人物迁移动作一致性_1992639334528643074.json, 视频生成/图生视频/啊癫 视频换背景V2_1964703426166800385.json, 视频生成/图生视频/啊癫 视频跳舞 动作迁移  动作模仿 姿态迁移 美女跳舞_1966126625408675842.json, 视频生成/图生视频/无限时长-角色替换-动作迁移）_1964342957782482945.json, 视频生成/图生视频/电商版-视频人物替换-3.0_1972870732168515586.json, 视频生成/图生视频/视频人物替换电商版_1967843353356283906.json, 视频生成/图生视频/视频人物自动替换-V2版本_2054089279747444738.json, 视频生成/图生视频/视频换人！！！--一键操作_1978308100690173954.json, 视频生成/图生视频/视频自动人物替换-V2版本_1955086878557048833.json, 视频生成/图生视频/视频自动人物替换-V2版本_2040327330937180162.json, 视频生成/图生视频/视频自动人物替换-V2版本_2041353977224241153.json, 视频生成/图生视频/视频自动人物替换-V2版本_2041775285426720769.json, 视频生成/图生视频/视频自动人物替换-V2版本_2115269816037756930.json, 视频生成/图生视频/视频自动人物替换_1970398580701884418.json, 视频生成/图生视频/跨境换装展示 自动人物替换-V2版本-循环版_2037789752887353346.json, 视频生成/文生视频/啊癫 视频人物替换 视频换人 人物迁移 视频主体替换 V3版 支持20S_1966149260637106178.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_6

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（平台全量/自定义遮罩换背景_2008732012235988993.json、平台全量/视频替换背景-V2版本（测试版）_2016782882668290050.json、平台全量/视频替换背景-高级版_1985941558384046081.json、平台全量/视频替换背景_2003339868539387905.json、平台全量/视频替换背景_2042481839343931393.json…）

- **类型**：Unknown Workflow
- **样本数**：27
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 27 个 workflow 都包含：
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `Primitive integer [Crystools]`
- `RHHiddenNodes`
- `RH_Captioner`
- `SetNode`
- `ShowText|pysssss`
- `Text Concatenate`
- `Text Multiline`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoExperimentalArgs`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `SimpleMath+` —— 26/27 个有
- `ColorMatch` —— 25/27 个有
- `EmptyImage` —— 25/27 个有
- `ImageConcatMulti` —— 25/27 个有
- `ImpactSwitch` —— 25/27 个有
- `PreviewImage` —— 25/27 个有
- `ImageFromBatch` —— 23/27 个有
- `WanVideoEnhanceAVideo` —— 23/27 个有
- `LayerUtility: ImageBlend` —— 21/27 个有
- `AIO_Preprocessor` —— 17/27 个有
- `AddLabel` —— 17/27 个有
- `DownloadAndLoadFlorence2Model` —— 13/27 个有
- `DownloadAndLoadSAM2Model` —— 13/27 个有
- `Florence2Run` —— 13/27 个有
- `Florence2toCoordinates` —— 13/27 个有
- `GrowMaskWithBlur` —— 13/27 个有
- `InpaintPreprocessor` —— 13/27 个有
- `LayerUtility: PurgeVRAM V2` —— 13/27 个有
- `PrimitiveString` —— 13/27 个有
- `RH_Translator` —— 13/27 个有
- `Sam2Segmentation` —— 13/27 个有
- `DepthAnything_V2` —— 12/27 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 12/27 个有
- `ImageBlend` —— 12/27 个有
- `Primitive float [Crystools]` —— 12/27 个有
- `RMBG` —— 7/27 个有
- `easy imageRemBg` —— 6/27 个有
- `WanVideoTeaCache` —— 4/27 个有
- `easy seed` —— 4/27 个有
- `InvertMask (segment anything)` —— 2/27 个有
- `UnloadModel` —— 2/27 个有
- `BiRefNetRMBG` —— 1/27 个有
- `Image To Mask` —— 1/27 个有
- `InvertMask` —— 1/27 个有
- `LayerUtility: ColorImage V2` —— 1/27 个有
- `PIP_IntegerCalculator` —— 1/27 个有
- `遮罩叠加处理` —— 1/27 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
