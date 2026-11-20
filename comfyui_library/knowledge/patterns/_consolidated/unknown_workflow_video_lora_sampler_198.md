---
name: unknown_workflow_video_lora_sampler_198
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.4632
common_nodes: [BlockifyMask, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DrawMaskOnImage, DrawViTPose, GetNode, GrowMask, ImageBlend, KSampler, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, OnnxDetectionModelLoader, PathchSageAttentionKJ, PoseAndFaceDetection, PreviewImage, SetNode, TorchCompileModelWanVideoV2, TrimVideoLatent, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, WanAnimateToVideo, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/Wan-Animate全自动版_1978389452143923202.json, 视频生成/图生视频/AnimateV2遮罩升级版SeC人物替换_1977328876730896386.json, 视频生成/图生视频/Wan-Animatev2.2_1971886781874499586.json, 视频生成/图生视频/Wan-Animate全自动版_1976469755416715266.json, 视频生成/图生视频/WanAnimateV2SEC自动遮罩_1978107415881211906.json, 视频生成/图生视频/Work-Fisher_Wan-Animate全自动版_1969348581830389761.json, 视频生成/图生视频/YZ金鱼-Wan Animate_Mix_官方版_v2.2_1971377068741214210.json, 视频生成/图生视频/动作迁移+角色替换二合一官方工作流（小显存、速度快、质量好）_2077716276075651074.json, 视频生成/图生视频/官方 SEC遮罩WAN Animate 长视频动作迁移_替换_1977331034679332865.json, 视频生成/图生视频/更换视频人物【动作】【五官】【一致】+手动遮罩_2008366086382690306.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_198

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/反推提示词/Wan-Animate全自动版_1978389452143923202.json、视频生成/图生视频/AnimateV2遮罩升级版SeC人物替换_1977328876730896386.json、视频生成/图生视频/Wan-Animatev2.2_1971886781874499586.json、视频生成/图生视频/Wan-Animate全自动版_1976469755416715266.json、视频生成/图生视频/WanAnimateV2SEC自动遮罩_1978107415881211906.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：46%

## 共有节点

全部 10 个 workflow 都包含：
- `BlockifyMask`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetNode`
- `GrowMask`
- `ImageBlend`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `OnnxDetectionModelLoader`
- `PathchSageAttentionKJ`
- `PoseAndFaceDetection`
- `PreviewImage`
- `SetNode`
- `TorchCompileModelWanVideoV2`
- `TrimVideoLatent`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanAnimateToVideo`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 9/10 个有
- `INTConstant` —— 9/10 个有
- `ImageResizeKJv2` —— 9/10 个有
- `PrimitiveFloat` —— 9/10 个有
- `easy showAnything` —— 9/10 个有
- `PlaySound|pysssss` —— 8/10 个有
- `DownloadAndLoadGIMMVFIModel` —— 6/10 个有
- `EmptyImage` —— 6/10 个有
- `GIMMVFI_interpolate` —— 6/10 个有
- `ImageRemoveBackground+` —— 6/10 个有
- `RemBGSession+` —— 6/10 个有
- `UnetLoaderGGUF` —— 6/10 个有
- `ImageConcatMulti` —— 5/10 个有
- `SeCModelLoader` —— 4/10 个有
- `SeCVideoSegmentation` —— 4/10 个有
- `easy cleanGpuUsed` —— 4/10 个有
- `GGUFLoaderKJ` —— 3/10 个有
- `ImageFromBatch` —— 3/10 个有
- `PointsEditor` —— 3/10 个有
- `RIFE VFI` —— 3/10 个有
- `UNETLoader` —— 2/10 个有
- `Bjornulf_ShowFloat` —— 1/10 个有
- `Bjornulf_ShowInt` —— 1/10 个有
- `ClothesSegment` —— 1/10 个有
- `Fast Groups Muter (rgthree)` —— 1/10 个有
- `Int` —— 1/10 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/10 个有
- `MathExpression_UTK` —— 1/10 个有
- `PrimitiveInt` —— 1/10 个有
- `SDVN Any Show` —— 1/10 个有
- `SaveImage` —— 1/10 个有
- `TT_img_enc_v2` —— 1/10 个有
- `UnloadAllModels` —— 1/10 个有
- `VHS_LoadVideoPath` —— 1/10 个有
- `VHS_VideoInfoLoaded` —— 1/10 个有
- `easy clearCacheAll` —— 1/10 个有
- `easy int` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | sa_solver | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
