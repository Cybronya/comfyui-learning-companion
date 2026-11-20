---
name: unknown_workflow_video_lora_sampler_61
type: Unknown Workflow
frequency: 23
level: moderate
coverage: 0.562348
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, DrawViTPose, GetImageSizeAndCount, GetNode, INTConstant, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [数字人/数字人/Sec版本-视频人物替换-Wan Animate20251017_1978992368751906818.json, 数字人/数字人/alan自用-主体替换sec video segmentation_1983904795276836866.json, 数字人/数字人/人物替换   角色替换   二创首选  Wan2.2 wan22_2045772090871123969.json, 数字人/数字人/人物替换  角色替换   二创首选_2052270878615977985.json, 数字人/数字人/视频人物替换-Wan Animate_V2版_1976639386127343617.json, 数字人/数字人/视频人物替换电商跨境wan2.2-Animate_1988091546115416066.json, 数字人/数字人/长视频 人物替换动作迁移wan2.2-Animate_1976989855852961793.json, 视频生成/图生视频/Wan2.2  Wan22 角色替换   动作迁移  二创首选_2042132086164819970.json, 视频生成/图生视频/Wan2.2  wan 二创首选 角色替换 动作模仿 图生视频_2042131699907170305.json, 视频生成/图生视频/Wan2.2  wan 角色替换 动作模仿 图生视频_2042176153171009537.json, 视频生成/图生视频/Wan2.2  wan 角色替换 动作模仿 图生视频_2042932527039516674.json, 视频生成/图生视频/Wan2.2  二创首选 角色替换 动作模仿 图生视频_2041872588984557569.json, 视频生成/图生视频/Wan2.2  人物替换_角色替换_动作模仿_二创首选_2039518740357844993.json, 视频生成/图生视频/Wan2.2  角色替换_动作模仿_图生视频_2039615736561274882.json, 视频生成/图生视频/Wan2.2 Animate 人物替换 精准替换 二创首选_2021541718369247233.json, 视频生成/图生视频/Wan2.2 Animate 人物替换 精准替换 二创首选工作流_2088990764796825602.json, 视频生成/图生视频/Wan2.2 精准角色替换 动作迁移  人物替换_2039613263704494081.json, 视频生成/图生视频/Wan2.2 角色替换   动作迁移  二创首选_2039620407292076033.json, 视频生成/图生视频/kitten practicing kung fu_2084182943492300802.json, 视频生成/图生视频/kitten practicing kung fu_2091771507398762498.json, 视频生成/图生视频/人物替换  角色替换   二创首选  Wan2.2 wan22_2046064441040572417.json, 视频生成/图生视频/人物替换  角色替换   二创首选  Wan2.2 wan22_2046446441639448578.json, 视频生成/图生视频/双向引导人物主体替换2.2+sec_1984107698880970753.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_61

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（数字人/数字人/Sec版本-视频人物替换-Wan Animate20251017_1978992368751906818.json、数字人/数字人/alan自用-主体替换sec video segmentation_1983904795276836866.json、数字人/数字人/人物替换   角色替换   二创首选  Wan2.2 wan22_2045772090871123969.json、数字人/数字人/人物替换  角色替换   二创首选_2052270878615977985.json、数字人/数字人/视频人物替换-Wan Animate_V2版_1976639386127343617.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：中等可信
- **平均知识覆盖**：56%

## 共有节点

全部 23 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `SeCModelLoader` —— 21/23 个有
- `SeCVideoSegmentation` —— 21/23 个有
- `CR Text` —— 19/23 个有
- `ImageConcanate` —— 19/23 个有
- `InvertMask` —— 19/23 个有
- `LayerUtility: ImageBlend` —— 19/23 个有
- `MaskToImage` —— 19/23 个有
- `PointsEditor` —— 18/23 个有
- `GrowMask` —— 17/23 个有
- `VHS_VideoInfo` —— 17/23 个有
- `ImageFromBatch+` —— 16/23 个有
- `JWInteger` —— 16/23 个有
- `PreviewImage` —— 16/23 个有
- `easy cleanGpuUsed` —— 16/23 个有
- `GrowMaskWithBlur` —— 6/23 个有
- `ConvertAny2Int` —— 4/23 个有
- `ImageConcatMulti` —— 4/23 个有
- `Text` —— 4/23 个有
- `easy float` —— 4/23 个有
- `easy framesEditor` —— 3/23 个有
- `DownloadAndLoadSAM2Model` —— 2/23 个有
- `ImageFromBatch` —— 2/23 个有
- `ImageScaleToTotalPixels` —— 2/23 个有
- `IndexTTSNode` —— 2/23 个有
- `MemoryCleaner` —— 2/23 个有
- `Sam2Segmentation` —— 2/23 个有
- `SeedVR2LoadDiTModel` —— 2/23 个有
- `SeedVR2LoadVAEModel` —— 2/23 个有
- `SeedVR2VideoUpscaler` —— 2/23 个有
- `Text Multiline` —— 2/23 个有
- `WanVideoTorchCompileSettings` —— 2/23 个有
- `easy showAnything` —— 2/23 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
