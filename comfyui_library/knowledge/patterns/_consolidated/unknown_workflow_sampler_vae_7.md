---
name: unknown_workflow_sampler_vae_7
type: Unknown Workflow
frequency: 28
level: strong
coverage: 0.7775
common_nodes: [BasicScheduler, ConditioningZeroOut, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTX2SamplingPreviewOverride, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVEmptyLatentAudio, LTXVImgToVideoInplaceKJ, LTXVSeparateAVLatent, LoadImage, SamplerCustom, VAEDecode, VAELoaderKJ, VisualizeSigmasKJ]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3-PromptRelay-图生视频_2084829161968984065.json, 视频生成/图生视频/LTX2.3_PromptRelay图生视频模型和工作流_2111402430121472002.json, 视频生成/图生视频/2047152091981942785.json, 视频生成/图生视频/2070818205395931138.json, 视频生成/图生视频/LTX2.3多镜头时间+逻辑控制PromptRelay+VBVR（KJ版）图文生视频_2082777967612223489.json, 视频生成/图生视频/LTX2.3多镜头时间+逻辑控制PromptRelay+VBVR（KJ版）图文生视频_2082793220383264770.json, 视频生成/图生视频/LTX2.3音频图片视频工作流_2084178470162223105.json, 视频生成/图生视频/2051822918727938049.json, 视频生成/图生视频/2046850819689029634.json, 视频生成/图生视频/2046813603185037314.json, 视频生成/图生视频/2046869684942802945.json, 视频生成/图生视频/2047251956011372546.json, 视频生成/图生视频/2047251992128528386.json, 视频生成/图生视频/2046812792329609218.json, 视频生成/图生视频/Ltx2.3细化多镜头长时间+KJ版+时间分段剪辑+逻辑控制PromptRe图生视频_2056233662454222849.json, 视频生成/图生视频/2056368359754780674.json, 视频生成/图生视频/2056620885733363713.json, 视频生成/图生视频/2057015136241668097.json, 视频生成/图生视频/2057105862644297729.json, 视频生成/图生视频/2058724424081305602.json, 视频生成/图生视频/2067168001845194753.json, 视频生成/图生视频/Ltx2.3细化多镜头长时间+KJ版+时间分段剪辑+逻辑控制PromptRe图生视频_2098717431224168449.json, 视频生成/图生视频/Ltx2.3细化多镜头长时间+KJ版+时间分段剪辑+逻辑控制PromptRe图生视频_2098745841820459009.json, 视频生成/图生视频/2079524853648019458.json, 视频生成/图生视频/2056004828781916162.json, 视频生成/图生视频/2071039400221433858.json, 视频生成/图生视频/最新LTX2.3+Gemma4本地自动化运行_2052786138674409473.json, 视频生成/图生视频/2053359877090758657.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_7

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（视频生成/图生视频/LTX2.3-PromptRelay-图生视频_2084829161968984065.json、视频生成/图生视频/LTX2.3_PromptRelay图生视频模型和工作流_2111402430121472002.json、视频生成/图生视频/2047152091981942785.json、视频生成/图生视频/2070818205395931138.json、视频生成/图生视频/LTX2.3多镜头时间+逻辑控制PromptRelay+VBVR（KJ版）图文生视频_2082777967612223489.json…）

- **类型**：Unknown Workflow
- **样本数**：28
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 28 个 workflow 都包含：
- `BasicScheduler`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplaceKJ`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `SamplerCustom`
- `VAEDecode`
- `VAELoaderKJ`
- `VisualizeSigmasKJ`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 27/28 个有
- `LTXVConditioning` —— 27/28 个有
- `LTXVPreprocess` —— 27/28 个有
- `LoraLoaderModelOnly` —— 27/28 个有
- `PathchSageAttentionKJ` —— 27/28 个有
- `PreviewImage` —— 27/28 个有
- `SetNode` —— 27/28 个有
- `UNETLoader` —— 27/28 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 26/28 个有
- `VHS_VideoCombine` —— 26/28 个有
- `JWInteger` —— 25/28 个有
- `PromptRelayEncode` —— 23/28 个有
- `CR Prompt Text` —— 22/28 个有
- `PreviewAny` —— 8/28 个有
- `RegexExtract` —— 7/28 个有
- `RH_LLMAPI_Pro_Node` —— 4/28 个有
- `easy mathInt` —— 4/28 个有
- `ComfyNumberConvert` —— 3/28 个有
- `PromptRelayEncodeTimeline` —— 3/28 个有
- `SaveImage` —— 3/28 个有
- `StringReplace` —— 3/28 个有
- `Text` —— 3/28 个有
- `FlashVSR_SM_KSampler` —— 2/28 个有
- `FlashVSR_SM_Model` —— 2/28 个有
- `GetImageRangeFromBatch` —— 2/28 个有
- `GetImageSize` —— 2/28 个有
- `INTConstant` —— 2/28 个有
- `LayerUtility: PurgeVRAM V2` —— 2/28 个有
- `PromptRelaySmartEncode` —— 2/28 个有
- `RH_Captioner` —— 2/28 个有
- `TSVideoCombineNoMetadata` —— 2/28 个有
- `CheckpointLoaderSimple` —— 1/28 个有
- `LTX2MemoryEfficientSageAttentionPatch` —— 1/28 个有
- `LTXVAddGuide` —— 1/28 个有
- `TextConcatenate_UTK` —— 1/28 个有
- `easy int` —— 1/28 个有
- `easy showAnything` —— 1/28 个有
- `llama_cpp_instruct_adv` —— 1/28 个有
- `llama_cpp_model_loader` —— 1/28 个有
- `llama_cpp_parameters` —— 1/28 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 489 | 97 - 489 | 28 | 78% |
| 高度 | 25 | 25 - 25 | 28 | 100% |
| 采样步数 | 1.34123e+09 | - | 2 | 47% |
| Prompt 约束强度(CFG) | randomize | - | 2 | 100% |
| 采样算法 | 2 | - | 2 | 100% |
| 调度器 | 3.5 | - | 2 | 100% |
| 重绘幅度 | 11 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 489，观测区间 97 - 489，28 个样本
- 高度 中位数 25，观测区间 25 - 25，28 个样本，取值集中（一致性 100%）
- 采样步数 中位数 1.34123e+09，样本不足，未给区间，2 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 最常用 randomize，2 个样本，一致性 100%
- 采样算法 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 2.05601e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
