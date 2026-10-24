---
name: unknown_workflow_video_upscale_latent_upscale_112
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.546
common_nodes: [CFGGuider, CS-MultiImageLoader, ComfyMathExpression, ComfySwitchNode, DualCLIPLoader, GetICLoRAParameters, GetImage, GetNode, INTConstant, KSamplerSelect, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVCropGuides, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, RegexExtract, SamplerCustomAdvanced, SetNode, ShowText|pysssss, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, YUAN_TXTConvertAny, YUAN_TXTListNumber, YUAN_TXTParagraphSplitter, YuanCLIPTimeline, YuanTool, easy positive]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3全栈式短剧生成V19.3(易用版)_2069230316849553409.json, 视频生成/图生视频/LTX2.3全栈式短剧生成V23.1(易用版)_2079201412885602305.json, 视频生成/图生视频/全栈式短剧生成V20.0 (易用版)_2074058822251008001.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_112

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/LTX2.3全栈式短剧生成V19.3(易用版)_2069230316849553409.json、视频生成/图生视频/LTX2.3全栈式短剧生成V23.1(易用版)_2079201412885602305.json、视频生成/图生视频/全栈式短剧生成V20.0 (易用版)_2074058822251008001.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CS-MultiImageLoader`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `DualCLIPLoader`
- `GetICLoRAParameters`
- `GetImage`
- `GetNode`
- `INTConstant`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `RegexExtract`
- `SamplerCustomAdvanced`
- `SetNode`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `YUAN_TXTConvertAny`
- `YUAN_TXTListNumber`
- `YUAN_TXTParagraphSplitter`
- `YuanCLIPTimeline`
- `YuanTool`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 2/3 个有
- `LTXVConditioning` —— 2/3 个有
- `VAELoader` —— 2/3 个有
- `YuanClipGuide` —— 2/3 个有
- `BerniniConditioning` —— 1/3 个有
- `CLIPLoader` —— 1/3 个有
- `ComfyAndNode` —— 1/3 个有
- `ComfyNotNode` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `GetImageSize` —— 1/3 个有
- `ImageBatchMulti` —— 1/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `KSamplerAdvanced` —— 1/3 个有
- `LTXVAddGuide` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `ResizeImageMaskNode` —— 1/3 个有
- `StringConcatenate` —— 1/3 个有
- `StringLength` —— 1/3 个有
- `StringReplace` —— 1/3 个有
- `VAEDecode` —— 1/3 个有
- `VAEEncode` —— 1/3 个有
- `YUAN_TXTAppearanceOrder` —— 1/3 个有
- `YUAN_TXTReplace` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 1 | 100% |
| Prompt 约束强度(CFG) | 4 | - | 1 | 100% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | euler_ancestral | - | 1 | 100% |
| 重绘幅度 | simple | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
