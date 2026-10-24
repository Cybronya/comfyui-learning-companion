---
name: unknown_workflow_video_lora_sampler_78
type: Unknown Workflow
frequency: 17
level: strong
coverage: 0.797353
common_nodes: [BasicScheduler, ConditioningZeroOut, DualCLIPLoader, EmptyLTXVLatentVideo, JWInteger, KSamplerSelect, LTX2SamplingPreviewOverride, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVSeparateAVLatent, LoraLoaderModelOnly, PathchSageAttentionKJ, SamplerCustom, UNETLoader, VAEDecode, VAELoaderKJ, VHS_VideoCombine, VisualizeSigmasKJ]
problems: []
missing: []
members: [图片生成/图生图/Ltx2.3细化多镜头长时间+KJ版+时间分段剪辑+逻辑控制PromptRe图生视频_2057109101624258561.json, 图片生成/图生图/图生长视频Ltx2.3+细化多镜头长时间+KJ版+图生视频时间分段剪辑++逻辑控制+自动计算帧数_2069651466062745602.json, 视频生成/图生视频/(文生视频)Ltx2.3多镜头精准时间控制PromptRelay（KJ版）_2046802828332634114.json, 视频生成/图生视频/+图生长视频Ltx2.3+细化多镜头长时间+KJ版+图生视频时间分段剪辑++逻辑控制PromptRe_2057262111021158401.json, 视频生成/图生视频/+图生长视频Ltx2.3+细化多镜头长时间+KJ版+图生视频时间分段剪辑++逻辑控制PromptRe_2089602214410149889.json, 视频生成/图生视频/+图生长视频Ltx2.3+细化多镜头长时间+KJ版1)_2059827902316900354.json, 视频生成/图生视频/KJ版+图生视频时间分段剪辑++逻辑控制PromptRe (1)_2063798363463704577.json, 视频生成/图生视频/LTX2.3-时间线分镜-PromptRelay-图生视频_2054823248579317761.json, 视频生成/图生视频/LTX2.3图生视频PromptRelay Timeline_2050993375851106306.json, 视频生成/图生视频/Ltx2.3_2052745658586677250.json, 视频生成/图生视频/图生视频 分镜控制 Ltx2.3 -PromptRelay Timeline 可视化控制V2_2050032331129405442.json, 视频生成/图生视频/图生视频 分镜控制 Ltx2.3 -PromptRelay_2046957180640829441.json, 视频生成/图生视频/图生视频 多镜头分镜时间控制 Ltx2.3  PromptRelay_2046944174850711553.json, 视频生成/图生视频/图生视频 节奏控制 Ltx2.3 -PromptRelay Timeline可视化控制 V2_2050043137099350017.json, 视频生成/图生视频/图生视频Ltx2.3+-PromptRelay_2047122187932409857.json, 视频生成/图生视频/最新LTX2.3+Gemma4本地自动化运行_2052786138674409473.json, 视频生成/图生视频/最新ltx2.3V1_2053359877090758657.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_78

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/Ltx2.3细化多镜头长时间+KJ版+时间分段剪辑+逻辑控制PromptRe图生视频_2057109101624258561.json、图片生成/图生图/图生长视频Ltx2.3+细化多镜头长时间+KJ版+图生视频时间分段剪辑++逻辑控制+自动计算帧数_2069651466062745602.json、视频生成/图生视频/(文生视频)Ltx2.3多镜头精准时间控制PromptRelay（KJ版）_2046802828332634114.json、视频生成/图生视频/+图生长视频Ltx2.3+细化多镜头长时间+KJ版+图生视频时间分段剪辑++逻辑控制PromptRe_2057262111021158401.json、视频生成/图生视频/+图生长视频Ltx2.3+细化多镜头长时间+KJ版+图生视频时间分段剪辑++逻辑控制PromptRe_2089602214410149889.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicScheduler`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `JWInteger`
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
- `UNETLoader`
- `VAEDecode`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `VisualizeSigmasKJ`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 16/17 个有
- `LTXVPreprocess` —— 16/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 16/17 个有
- `LoadImage` —— 16/17 个有
- `SetNode` —— 16/17 个有
- `PromptRelayEncode` —— 13/17 个有
- `PreviewAny` —— 10/17 个有
- `RegexExtract` —— 10/17 个有
- `PreviewImage` —— 9/17 个有
- `Text` —— 9/17 个有
- `CM_IntToFloat` —— 8/17 个有
- `CR Prompt Text` —— 8/17 个有
- `RH_LLMAPI_Pro_Node` —— 8/17 个有
- `SimpleMath+` —— 8/17 个有
- `PromptRelayEncodeTimeline` —— 4/17 个有
- `FlashVSR_SM_KSampler` —— 2/17 个有
- `FlashVSR_SM_Model` —— 2/17 个有
- `GetImageRangeFromBatch` —— 2/17 个有
- `GetImageSize` —— 2/17 个有
- `LayerUtility: PurgeVRAM V2` —— 2/17 个有
- `StringReplace` —— 2/17 个有
- `easy mathInt` —— 2/17 个有
- `llama_cpp_instruct_adv` —— 2/17 个有
- `llama_cpp_model_loader` —— 2/17 个有
- `llama_cpp_parameters` —— 2/17 个有
- `CM_IntBinaryOperation` —— 1/17 个有
- `JWStringConcat` —— 1/17 个有
- `JWStringSplit` —— 1/17 个有
- `LTX2MemoryEfficientSageAttentionPatch` —— 1/17 个有
- `RH_Captioner` —— 1/17 个有
- `SaveImage` —— 1/17 个有
- `ShowText|pysssss` —— 1/17 个有
- `SomethingToString` —— 1/17 个有
- `TextConcatenate_UTK` —— 1/17 个有
- `easy cleanGpuUsed` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 489 | 489 - 489 | 17 | 100% |
| 高度 | 25 | 25 - 25 | 17 | 100% |
| 采样步数 | 1.34123e+09 | - | 2 | 47% |
| Prompt 约束强度(CFG) | randomize | - | 2 | 100% |
| 采样算法 | 2 | - | 2 | 100% |
| 调度器 | 3.5 | - | 2 | 100% |
| 重绘幅度 | 11 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 489，观测区间 489 - 489，17 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，17 个样本，取值集中（一致性 100%）
- 采样步数 中位数 1.34123e+09，样本不足，未给区间，2 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 最常用 randomize，2 个样本，一致性 100%
- 采样算法 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 2.05601e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
