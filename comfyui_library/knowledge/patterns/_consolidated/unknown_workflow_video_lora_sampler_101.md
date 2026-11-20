---
name: unknown_workflow_video_lora_sampler_101
type: Unknown Workflow
frequency: 17
level: strong
coverage: 0.593706
common_nodes: [CLIPVisionLoader, DrawViTPose, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/迁移_2095869972676440066.json, 平台全量/KR：视频人物姿态迁移（13号流）_2062732875350503426.json, 平台全量/tiktok摇头晃脑_2081935140942602242.json, 平台全量/本地开源免费， tiktok dancing_2080650163344986114.json, 视频生成/图生视频/刀马刀马_2055133948241563650.json, 视频生成/图生视频/我最红#南音#_2055152024093765633.json, 视频生成/图生视频/本地开源免费， tiktok dancing_2054138634953084930.json, 视频生成/图生视频/本地开源免费，4 minutes_2054476614616010753.json, 视频生成/图生视频/本地开源免费，bubblepop_2054151947208413186.json, 视频生成/图生视频/本地开源免费，kpop jennie进行曲_2054190698328535041.json, 视频生成/图生视频/本地开源免费，tiktok dancing_2053700198567817217.json, 视频生成/图生视频/本地开源免费，tiktok dancing_2053885364179357697.json, 视频生成/图生视频/本地开源免费，tiktok dancing_2054085546393260034.json, 视频生成/图生视频/本地开源免费，tiktok dancing_2054098992224579585.json, 视频生成/图生视频/本地开源免费，刀马舞真人版_2055285137239232514.json, 视频生成/图生视频/本地开源免费，动作迁移_2053895835615809538.json, 视频生成/图生视频/本地开源免费，我最红真人版_2055202834680950786.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_101

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/迁移_2095869972676440066.json、平台全量/KR：视频人物姿态迁移（13号流）_2062732875350503426.json、平台全量/tiktok摇头晃脑_2081935140942602242.json、平台全量/本地开源免费， tiktok dancing_2080650163344986114.json、视频生成/图生视频/刀马刀马_2055133948241563650.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：59%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
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
- `CR Prompt Text` —— 16/17 个有
- `GetNode` —— 16/17 个有
- `LayerUtility: PurgeVRAM V2` —— 16/17 个有
- `SetNode` —— 16/17 个有
- `WanVideoBlockSwap` —— 16/17 个有
- `WanVideoTorchCompileSettings` —— 16/17 个有
- `JWInteger` —— 15/17 个有
- `easy showAnything` —— 15/17 个有
- `FlashVSR_SM_KSampler` —— 14/17 个有
- `FlashVSR_SM_Model` —— 14/17 个有
- `GetImageRangeFromBatch` —— 14/17 个有
- `GetImageSize` —— 14/17 个有
- `VHS_VideoInfoSource` —— 14/17 个有
- `easy indexAnything` —— 5/17 个有
- `GetImageSizeAndCount` —— 2/17 个有
- `INTConstant` —— 2/17 个有
- `Int` —— 2/17 个有
- `easy mathInt` —— 2/17 个有
- `CM_IntToFloat` —— 1/17 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/17 个有
- `FlashVSRNode` —— 1/17 个有
- `GIMMVFI_interpolate` —— 1/17 个有
- `ImageConcatenate_UTK` —— 1/17 个有
- `ImageMirror` —— 1/17 个有
- `MathExpression|pysssss` —— 1/17 个有
- `RTXVideoSuperResolution` —— 1/17 个有
- `WanAnimatePlus BlockSwap` —— 1/17 个有
- `easy int` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1.23834e+09 | 1.27484e+08 - 2.14652e+09 | 14 | 53% |
| Prompt 约束强度(CFG) | randomize | - | 14 | 100% |
| 采样算法 | 2 | 2 - 2 | 14 | 100% |
| 调度器 | 3.5 | 3.5 - 3.5 | 14 | 100% |
| 重绘幅度 | 11 | 11 - 11 | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 1.23834e+09，观测区间 1.27484e+08 - 2.14652e+09，14 个样本
- Prompt 约束强度(CFG) 最常用 randomize，14 个样本，一致性 100%
- 采样算法 中位数 2，观测区间 2 - 2，14 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，14 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 11 - 11，14 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 2.14652e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
