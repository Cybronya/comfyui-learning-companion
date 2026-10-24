---
name: unknown_workflow_video_lora_sampler_252
type: Unknown Workflow
frequency: 8
level: weak
coverage: 0.752
common_nodes: [CFGGuider, CLIPTextEncode, CreateVideo, Dapao_LlamaCaption, Dapao_LlamaCaptionOptions, EmptyLTXVLatentVideo, GetVideoComponents, KSamplerSelect, LTXAVTextEncoderLoader, LTXAddVideoICLoRAGuide, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LiconMSR, LoadImage, ManualSigmas, RandomNoise, RegexReplace, SamplerCustomAdvanced, VAEDecode, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Ltx2.3 Licon-MSR  慢镜头用（可惜只能人类写实）_2069279414692704257.json, 视频生成/图生视频/Ltx2.3 Licon-MSR-全能参考生视频_2068903513152909314.json, 视频生成/图生视频/Ltx2.3 Licon-MSR-全能参考生视频_2069328807546417154.json, 视频生成/图生视频/Ltx2.3 Licon-MSR-全能参考生视频正式版V1-自动提示词版-高帧率-高动态-去字幕_2064345849135722497.json, 视频生成/图生视频/Ltx2.3 Licon-MSR-全能参考生视频正式版V1-自动提示词版-高帧率-高动态-去字幕_2064359460616884226.json, 视频生成/图生视频/Ltx2.3 Licon-MSR-全能参考生视频正式版V1-自动提示词版-高帧率-高动态_2064002512151212034.json, 视频生成/图生视频/Ltx2.3+Licon-MSR-全能参考生视频_2069219281786720258.json, 视频生成/图生视频/Ltx2.3+Licon-MSR-全能参考生视频_2069991614805798913.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_252

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/Ltx2.3 Licon-MSR  慢镜头用（可惜只能人类写实）_2069279414692704257.json、视频生成/图生视频/Ltx2.3 Licon-MSR-全能参考生视频_2068903513152909314.json、视频生成/图生视频/Ltx2.3 Licon-MSR-全能参考生视频_2069328807546417154.json、视频生成/图生视频/Ltx2.3 Licon-MSR-全能参考生视频正式版V1-自动提示词版-高帧率-高动态-去字幕_2064345849135722497.json、视频生成/图生视频/Ltx2.3 Licon-MSR-全能参考生视频正式版V1-自动提示词版-高帧率-高动态-去字幕_2064359460616884226.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CreateVideo`
- `Dapao_LlamaCaption`
- `Dapao_LlamaCaptionOptions`
- `EmptyLTXVLatentVideo`
- `GetVideoComponents`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXAddVideoICLoRAGuide`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LiconMSR`
- `LoadImage`
- `ManualSigmas`
- `RandomNoise`
- `RegexReplace`
- `SamplerCustomAdvanced`
- `VAEDecode`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 7/8 个有
- `VAELoaderKJ` —— 7/8 个有
- `CheckpointLoaderSimple` —— 5/8 个有
- `GuHaiAutoImageSplit` —— 5/8 个有
- `MathExpression|pysssss` —— 5/8 个有
- `PrimitiveInt` —— 5/8 个有
- `PrimitiveStringMultiline` —— 5/8 个有
- `SaveImage` —— 5/8 个有
- `StringConcatenate` —— 5/8 个有
- `CR Prompt Text` —— 3/8 个有
- `Float` —— 3/8 个有
- `GetNode` —— 3/8 个有
- `Int` —— 3/8 个有
- `LTXICLoRALoaderModelOnly` —— 3/8 个有
- `LowVRAMCheckpointLoader` —— 3/8 个有
- `MultiTextConcatenate` —— 3/8 个有
- `RH_LLMAPI_Pro_Node` —— 3/8 个有
- `SetNode` —— 3/8 个有
- `SimpleMath+` —— 3/8 个有
- `孤海注释` —— 3/8 个有
- `DualCLIPLoader` —— 2/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 241 | 8 | 54% |
| 高度 | 25 | 25 - 50 | 8 | 65% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 241，8 个样本
- 高度 中位数 25，观测区间 25 - 50，8 个样本
