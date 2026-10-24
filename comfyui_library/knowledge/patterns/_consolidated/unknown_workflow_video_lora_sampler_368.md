---
name: unknown_workflow_video_lora_sampler_368
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.523833
common_nodes: [Bjornulf_ShowInt, CLIPLoader, CLIPTextEncode, DWPreprocessor, GetImageRangeFromBatch, GetNode, INTConstant, ImageResizeKJv2, KSampler, Label (rgthree), ModelSamplingSD3, PathchSageAttentionKJ, Power Lora Loader (rgthree), PreviewImage, RMBG, SetNode, TorchCompileModelWanVideo, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVaceToVideo, WanVideoVACEStartToEndFrame]
problems: []
missing: []
members: [视频生成/图生视频/【AI缩放术】上传照片→1：1复刻擒敌拳！ComfyUI动作模仿+人物替换教程_1951333020332666881.json, 视频生成/图生视频/【ComfyUI分身术】一键批量复刻猫爷走秀！Flux.1 Krea让AI模特毫无塑料感✨_1952994072745152513.json, 视频生成/图生视频/【定帧术2.0】一键把你变成太极拳大师，生成60秒武术长视频_1952340963568095234.json, 视频生成/图生视频/🔥 「定帧术」神还原太极拳！外国人秒变武林高手！_1949032732500926465.json, 视频生成/图生视频/🔥AI幻境术：一键替换视频背景+人物！🔥_1953347970265698305.json, 视频生成/图生视频/🔥【AI反转术】让你秒变功夫巨星！_1950622987424845825.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_368

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/【AI缩放术】上传照片→1：1复刻擒敌拳！ComfyUI动作模仿+人物替换教程_1951333020332666881.json、视频生成/图生视频/【ComfyUI分身术】一键批量复刻猫爷走秀！Flux.1 Krea让AI模特毫无塑料感✨_1952994072745152513.json、视频生成/图生视频/【定帧术2.0】一键把你变成太极拳大师，生成60秒武术长视频_1952340963568095234.json、视频生成/图生视频/🔥 「定帧术」神还原太极拳！外国人秒变武林高手！_1949032732500926465.json、视频生成/图生视频/🔥AI幻境术：一键替换视频背景+人物！🔥_1953347970265698305.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：52%

## 共有节点

全部 6 个 workflow 都包含：
- `Bjornulf_ShowInt`
- `CLIPLoader`
- `CLIPTextEncode`
- `DWPreprocessor`
- `GetImageRangeFromBatch`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSampler`
- `Label (rgthree)`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `Power Lora Loader (rgthree)`
- `PreviewImage`
- `RMBG`
- `SetNode`
- `TorchCompileModelWanVideo`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVaceToVideo`
- `WanVideoVACEStartToEndFrame`

**可变部分**（部分 workflow 才有）：
- `Bookmark (rgthree)` —— 5/6 个有
- `Fast Groups Bypasser (rgthree)` —— 5/6 个有
- `GroundingDinoModelLoader (segment anything)` —— 5/6 个有
- `GroundingDinoSAMSegment (segment anything)` —— 5/6 个有
- `GrowMaskWithBlur` —— 5/6 个有
- `ImageBatchMulti` —— 5/6 个有
- `LoadImage` —— 5/6 个有
- `MaskToImage` —— 5/6 个有
- `MathExpression|pysssss` —— 5/6 个有
- `Mix Color By Mask` —— 5/6 个有
- `RepeatImageBatch` —— 5/6 个有
- `SAMModelLoader (segment anything)` —— 5/6 个有
- `VHS_DuplicateMasks` —— 4/6 个有
- `easy forLoopEnd` —— 4/6 个有
- `easy forLoopStart` —— 4/6 个有
- `DepthAnything_V2` —— 3/6 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 3/6 个有
- `ConditioningZeroOut` —— 2/6 个有
- `DualCLIPLoader` —— 2/6 个有
- `EmptySD3LatentImage` —— 2/6 个有
- `HfImageToRGB` —— 2/6 个有
- `ImagePadKJ` —— 2/6 个有
- `Int` —— 2/6 个有
- `SaveImage` —— 2/6 个有
- `VHS_GetImageCount` —— 2/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `ImagePadForOutpaint` —— 1/6 个有
- `ImageScale` —— 1/6 个有
- `InvertMask` —— 1/6 个有
- `ModelSamplingAuraFlow` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 20 | 6 | 68% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | uni_pc | - | 6 | 83% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
