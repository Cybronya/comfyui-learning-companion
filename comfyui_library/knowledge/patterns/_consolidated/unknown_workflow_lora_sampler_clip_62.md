---
name: unknown_workflow_lora_sampler_clip_62
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.858111
common_nodes: [CFGGuider, CLIPTextEncode, CreateVideo, EmptyLTXVLatentVideo, INTConstant, KSamplerSelect, LTXAddVideoICLoRAGuide, LTXICLoRALoaderModelOnly, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LiconMSR, LoadImage, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecode]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.3_小seedance2全能参考节点_2065439100508921858.json, 视频生成/图生视频/LTX2.3多图参考（小）Seedance 2.0_2067207518782316546.json, 视频生成/图生视频/Licon-MSR生成视频参考工作流_2061975400108093442.json, 视频生成/图生视频/Ltx2.3 MSR全能参考生视频V1_2067141677512482818.json, 视频生成/图生视频/Ltx2.3多参生视频（seedance2青春版MSR自动提示词版）_2063973958436876290.json, 视频生成/图生视频/aidir-LTX2.3多图参考（小）Seedance 2.0_2069617886041305089.json, 视频生成/图生视频/（高帧率-高动态）Ltx2.3 Licon-MSR自动提示词版全能参考生视频正式版V1_2063485331059601410.json, 视频生成/图生视频/（高帧率）Ltx2.3 Licon-MSR自动提示词版全能参考生视频正式版V1_2063464652104884226.json, 视频生成/文生视频/（高帧率图生视频）Ltx2.3 Licon-MSR自动提示词版全能参考视频_2064880215909814273.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_62

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/LTX-2.3_小seedance2全能参考节点_2065439100508921858.json、视频生成/图生视频/LTX2.3多图参考（小）Seedance 2.0_2067207518782316546.json、视频生成/图生视频/Licon-MSR生成视频参考工作流_2061975400108093442.json、视频生成/图生视频/Ltx2.3 MSR全能参考生视频V1_2067141677512482818.json、视频生成/图生视频/Ltx2.3多参生视频（seedance2青春版MSR自动提示词版）_2063973958436876290.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `KSamplerSelect`
- `LTXAddVideoICLoRAGuide`
- `LTXICLoRALoaderModelOnly`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LiconMSR`
- `LoadImage`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LTXAVTextEncoderLoader` —— 6/9 个有
- `LTXVAudioVAELoader` —— 6/9 个有
- `LowVRAMCheckpointLoader` —— 6/9 个有
- `CR Prompt Text` —— 5/9 个有
- `RH_LLMAPI_Pro_Node` —— 5/9 个有
- `ShowText|pysssss` —— 5/9 个有
- `DualCLIPLoader` —— 3/9 个有
- `GetNode` —— 3/9 个有
- `SetNode` —— 3/9 个有
- `UNETLoader` —— 3/9 个有
- `VAELoader` —— 3/9 个有
- `MuyeTextEditOutput` —— 2/9 个有
- `AtSignCLIPTextEncode` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `LTXVAddGuideMulti` —— 1/9 个有
- `LoadVideo` —— 1/9 个有
- `MultiIntFormula` —— 1/9 个有
- `Qwen3VL_Chat` —— 1/9 个有
- `SaveImage` —— 1/9 个有
- `TT_img_enc` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 241 | 97 - 241 | 9 | 76% |
| 高度 | 50 | 24 - 50 | 9 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 241，观测区间 97 - 241，9 个样本
- 高度 中位数 50，观测区间 24 - 50，9 个样本
