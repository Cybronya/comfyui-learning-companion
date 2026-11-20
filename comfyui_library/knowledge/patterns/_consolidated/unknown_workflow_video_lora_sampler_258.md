---
name: unknown_workflow_video_lora_sampler_258
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.5228
common_nodes: [CLIPLoader, CLIPTextEncode, GetImageRangeFromBatch, GetNode, INTConstant, ImageResizeKJv2, KSampler, ModelSamplingSD3, PathchSageAttentionKJ, Power Lora Loader (rgthree), PreviewImage, SetNode, TorchCompileModelWanVideo, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVaceToVideo, WanVideoVACEStartToEndFrame]
problems: []
missing: []
members: [平台全量/AI大模型把你变身为灵魂舞者_1955827163482263554.json, 平台全量/「AI定帧术」上传自拍照让你变身舞蹈达人_1954807827320627202.json, 平台全量/「延长术」独创完美复刻太极拳，一招一式力量感爆棚！轻松生成60秒武术长视频！_1949685874297589761.json, 平台全量/【肯优麦瑞蜜】创意贴画视频工作流_1948721106720043010.json, 视频生成/图生视频/【AI缩放术】上传照片→1：1复刻擒敌拳！ComfyUI动作模仿+人物替换教程_1951333020332666881.json, 视频生成/图生视频/【ComfyUI分身术】一键批量复刻猫爷走秀！Flux.1 Krea让AI模特毫无塑料感✨_1952994072745152513.json, 视频生成/图生视频/【定帧术2.0】一键把你变成太极拳大师，生成60秒武术长视频_1952340963568095234.json, 视频生成/图生视频/🔥 「定帧术」神还原太极拳！外国人秒变武林高手！_1949032732500926465.json, 视频生成/图生视频/🔥AI幻境术：一键替换视频背景+人物！🔥_1953347970265698305.json, 视频生成/图生视频/🔥【AI反转术】让你秒变功夫巨星！_1950622987424845825.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_258

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（平台全量/AI大模型把你变身为灵魂舞者_1955827163482263554.json、平台全量/「AI定帧术」上传自拍照让你变身舞蹈达人_1954807827320627202.json、平台全量/「延长术」独创完美复刻太极拳，一招一式力量感爆棚！轻松生成60秒武术长视频！_1949685874297589761.json、平台全量/【肯优麦瑞蜜】创意贴画视频工作流_1948721106720043010.json、视频生成/图生视频/【AI缩放术】上传照片→1：1复刻擒敌拳！ComfyUI动作模仿+人物替换教程_1951333020332666881.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：52%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetImageRangeFromBatch`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSampler`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `Power Lora Loader (rgthree)`
- `PreviewImage`
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
- `Bjornulf_ShowInt` —— 9/10 个有
- `Bookmark (rgthree)` —— 9/10 个有
- `DWPreprocessor` —— 9/10 个有
- `GroundingDinoModelLoader (segment anything)` —— 9/10 个有
- `GroundingDinoSAMSegment (segment anything)` —— 9/10 个有
- `GrowMaskWithBlur` —— 9/10 个有
- `ImageBatchMulti` —— 9/10 个有
- `Label (rgthree)` —— 9/10 个有
- `LoadImage` —— 9/10 个有
- `MaskToImage` —— 9/10 个有
- `MathExpression|pysssss` —— 9/10 个有
- `Mix Color By Mask` —— 9/10 个有
- `RMBG` —— 9/10 个有
- `SAMModelLoader (segment anything)` —— 9/10 个有
- `RepeatImageBatch` —— 7/10 个有
- `easy forLoopEnd` —— 7/10 个有
- `easy forLoopStart` —— 7/10 个有
- `Fast Groups Bypasser (rgthree)` —— 6/10 个有
- `VHS_DuplicateMasks` —— 6/10 个有
- `DepthAnything_V2` —— 5/10 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 5/10 个有
- `HfImageToRGB` —— 4/10 个有
- `SaveImage` —— 4/10 个有
- `VHS_GetImageCount` —— 4/10 个有
- `ConditioningZeroOut` —— 3/10 个有
- `DualCLIPLoader` —— 3/10 个有
- `EmptySD3LatentImage` —— 3/10 个有
- `ImagePadKJ` —— 3/10 个有
- `Int` —— 3/10 个有
- `ImageConcatMulti` —— 1/10 个有
- `ImagePadForOutpaint` —— 1/10 个有
- `ImageScale` —— 1/10 个有
- `InvertMask` —— 1/10 个有
- `LayerUtility: PurgeVRAM` —— 1/10 个有
- `ModelSamplingAuraFlow` —— 1/10 个有
- `preview_mask` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 20 | 10 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | uni_pc | - | 10 | 80% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 20，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，10 个样本，一致性 80%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
