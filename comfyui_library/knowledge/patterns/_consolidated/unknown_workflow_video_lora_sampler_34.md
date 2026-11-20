---
name: unknown_workflow_video_lora_sampler_34
type: Unknown Workflow
frequency: 26
level: strong
coverage: 0.602923
common_nodes: [CLIPVisionLoader, DrawViTPose, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/WanAnimate 最强动作迁移，解决强制绑定参考视频骨骼的问题_2003700640893288450.json, 视频生成/图生视频/WanAnimate动作迁移-修复版_2049893204031488002.json, 视频生成/图生视频/animate版后裔摇_2070049005316435969.json, 视频生成/图生视频/animate舞蹈迁移摇一摇_2061344115643736066.json, 视频生成/图生视频/animate舞蹈迁移摇一摇_2099776395709861890.json, 视频生成/图生视频/animate舞蹈迁移摇一摇_2100036331069075458.json, 视频生成/图生视频/人物舞蹈动作模仿_2079228691137257473.json, 视频生成/图生视频/全能人物模仿_2081019730562998274.json, 视频生成/图生视频/刀马刀马_2055133948241563650.json, 视频生成/图生视频/动作模仿舞蹈迁移_2072605420753084417.json, 视频生成/图生视频/女生舞蹈复刻_2098325811605622786.json, 视频生成/图生视频/我最红#南音#_2055152024093765633.json, 视频生成/图生视频/本地开源免费， tiktok dancing_2054138634953084930.json, 视频生成/图生视频/本地开源免费，4 minutes_2054476614616010753.json, 视频生成/图生视频/本地开源免费，bubblepop_2054151947208413186.json, 视频生成/图生视频/本地开源免费，kpop jennie进行曲_2054190698328535041.json, 视频生成/图生视频/本地开源免费，tiktok dancing_2053700198567817217.json, 视频生成/图生视频/本地开源免费，tiktok dancing_2053885364179357697.json, 视频生成/图生视频/本地开源免费，tiktok dancing_2054085546393260034.json, 视频生成/图生视频/本地开源免费，tiktok dancing_2054098992224579585.json, 视频生成/图生视频/本地开源免费，刀马舞真人版_2055285137239232514.json, 视频生成/图生视频/本地开源免费，动作迁移_2053895835615809538.json, 视频生成/图生视频/本地开源免费，我最红真人版_2055202834680950786.json, 视频生成/图生视频/本地开源免费，杀青梗_2054219479617425409.json, 视频生成/图生视频/本地开源免费，越南鼓捣蒜舞_2055312593698467841.json, 视频生成/图生视频/本地开源免费，香菜摇5_2054476626561388545.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_34

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（视频生成/图生视频/WanAnimate 最强动作迁移，解决强制绑定参考视频骨骼的问题_2003700640893288450.json、视频生成/图生视频/WanAnimate动作迁移-修复版_2049893204031488002.json、视频生成/图生视频/animate版后裔摇_2070049005316435969.json、视频生成/图生视频/animate舞蹈迁移摇一摇_2061344115643736066.json、视频生成/图生视频/animate舞蹈迁移摇一摇_2099776395709861890.json…）

- **类型**：Unknown Workflow
- **样本数**：26
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 26 个 workflow 都包含：
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
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 25/26 个有
- `SetNode` —— 25/26 个有
- `WanVideoLoraSelectMulti` —— 25/26 个有
- `WanVideoTorchCompileSettings` —— 25/26 个有
- `CR Prompt Text` —— 24/26 个有
- `JWInteger` —— 24/26 个有
- `easy showAnything` —— 24/26 个有
- `VHS_VideoInfoSource` —— 23/26 个有
- `WanVideoBlockSwap` —— 22/26 个有
- `LayerUtility: PurgeVRAM V2` —— 20/26 个有
- `FlashVSR_SM_KSampler` —— 16/26 个有
- `FlashVSR_SM_Model` —— 16/26 个有
- `GetImageRangeFromBatch` —— 16/26 个有
- `GetImageSize` —— 16/26 个有
- `easy indexAnything` —— 7/26 个有
- `ImageConcatenate_UTK` —— 4/26 个有
- `easy mathInt` —— 4/26 个有
- `GetImageSizeAndCount` —— 2/26 个有
- `INTConstant` —— 2/26 个有
- `ImageConcatMulti` —— 2/26 个有
- `Bjornulf_ShowInt` —— 1/26 个有
- `ImageFromBatch+` —— 1/26 个有
- `ImageMirror` —— 1/26 个有
- `ImagePadKJ` —— 1/26 个有
- `RHHiddenNodes` —— 1/26 个有
- `VHS_GetImageCount` —— 1/26 个有
- `VHS_SelectImages` —— 1/26 个有
- `WanVideoContextOptions` —— 1/26 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1.35013e+09 | 1.27484e+08 - 2.14652e+09 | 16 | 54% |
| Prompt 约束强度(CFG) | randomize | - | 16 | 100% |
| 采样算法 | 2 | 2 - 2 | 16 | 100% |
| 调度器 | 3.5 | 3.5 - 3.5 | 16 | 100% |
| 重绘幅度 | 11 | 11 - 11 | 16 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 1.35013e+09，观测区间 1.27484e+08 - 2.14652e+09，16 个样本
- Prompt 约束强度(CFG) 最常用 randomize，16 个样本，一致性 100%
- 采样算法 中位数 2，观测区间 2 - 2，16 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，16 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 11 - 11，16 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 2.14652e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
