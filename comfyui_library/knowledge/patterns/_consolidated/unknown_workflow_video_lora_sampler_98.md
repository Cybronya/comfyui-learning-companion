---
name: unknown_workflow_video_lora_sampler_98
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.789067
common_nodes: [BasicScheduler, ConditioningZeroOut, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTX2SamplingPreviewOverride, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVSeparateAVLatent, LoraLoaderModelOnly, PathchSageAttentionKJ, SamplerCustom, VAEDecode, VAELoaderKJ, VHS_VideoCombine, VisualizeSigmasKJ]
problems: []
missing: []
members: [视频生成/图生视频/2046802828332634114.json, 视频生成/图生视频/2057262111021158401.json, 视频生成/图生视频/+图生长视频Ltx2.3+细化多镜头长时间+KJ版+图生视频时间分段剪辑++逻辑控制PromptRe_2089602214410149889.json, 视频生成/图生视频/2059827902316900354.json, 视频生成/图生视频/2063798363463704577.json, 视频生成/图生视频/2047485702841049089.json, 视频生成/图生视频/2050810161220071425.json, 视频生成/图生视频/2054823248579317761.json, 视频生成/图生视频/2050993375851106306.json, 视频生成/图生视频/2052745658586677250.json, 视频生成/图生视频/2050032331129405442.json, 视频生成/图生视频/2046957180640829441.json, 视频生成/图生视频/2050043137099350017.json, 视频生成/图生视频/2047122187932409857.json, 视频生成/文生视频/LTX2.3图生视频 -时间线分镜-PromptRelay-服装模特带货短视频_2055106849938132994.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_98

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/2046802828332634114.json、视频生成/图生视频/2057262111021158401.json、视频生成/图生视频/+图生长视频Ltx2.3+细化多镜头长时间+KJ版+图生视频时间分段剪辑++逻辑控制PromptRe_2089602214410149889.json、视频生成/图生视频/2059827902316900354.json、视频生成/图生视频/2063798363463704577.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 15 个 workflow 都包含：
- `BasicScheduler`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplaceKJ`
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `SamplerCustom`
- `VAEDecode`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 14/15 个有
- `LTXVPreprocess` —— 14/15 个有
- `LoadImage` —— 14/15 个有
- `SetNode` —— 14/15 个有
- `UNETLoader` —— 14/15 个有
- `JWInteger` —— 13/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 12/15 个有
- `PromptRelayEncode` —— 10/15 个有
- `PreviewAny` —— 9/15 个有
- `RH_LLMAPI_Pro_Node` —— 9/15 个有
- `RegexExtract` —— 9/15 个有
- `CM_IntToFloat` —— 8/15 个有
- `SimpleMath+` —— 8/15 个有
- `Text` —— 8/15 个有
- `PreviewImage` —— 7/15 个有
- `CR Prompt Text` —— 5/15 个有
- `PromptRelayEncodeTimeline` —— 5/15 个有
- `AudioCrop` —— 1/15 个有
- `INTConstant` —— 1/15 个有
- `Int` —— 1/15 个有
- `LTXVAudioVAEEncode` —— 1/15 个有
- `LoadAudio` —— 1/15 个有
- `SetLatentNoiseMask` —— 1/15 个有
- `SolidMask` —— 1/15 个有
- `UnetLoaderGGUF` —— 1/15 个有
- `easy cleanGpuUsed` —— 1/15 个有
- `easy ifElse` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 489 | 409 - 489 | 15 | 96% |
| 高度 | 25 | 25 - 25 | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 489，观测区间 409 - 489，15 个样本，取值集中（一致性 96%）
- 高度 中位数 25，观测区间 25 - 25，15 个样本，取值集中（一致性 100%）
