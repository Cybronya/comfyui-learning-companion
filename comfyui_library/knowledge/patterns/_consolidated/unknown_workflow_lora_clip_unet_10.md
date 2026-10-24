---
name: unknown_workflow_lora_clip_unet_10
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7646
common_nodes: [BatchImagesNode, BerniniConditioning, BerniniPromptEnhancer, Bool, CLIPLoader, CLIPTextEncode, ComfySwitchNode, CreateVideo, Fast Groups Bypasser (rgthree), ImageResizeKJv2, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, PreviewAny, PrimitiveInt, RH_LLMAPI_NODE, SaveVideo, TTP_text_mix, TextInput_, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Bernini多图参考成片_2062857023867408385.json, 视频生成/图生视频/Bernini Prompt Relay多图参考时序控制视频_2067931552071376897.json, 视频生成/图生视频/Bernini+Prompt Relay视频编辑or多图参考_2068343750555955202.json, 视频生成/图生视频/Bernini多图参考视频_2067557998221946881.json, 视频生成/图生视频/bernini context视频编辑不限时长_2073236445627772930.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_clip_unet_10

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Bernini多图参考成片_2062857023867408385.json、视频生成/图生视频/Bernini Prompt Relay多图参考时序控制视频_2067931552071376897.json、视频生成/图生视频/Bernini+Prompt Relay视频编辑or多图参考_2068343750555955202.json、视频生成/图生视频/Bernini多图参考视频_2067557998221946881.json、视频生成/图生视频/bernini context视频编辑不限时长_2073236445627772930.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 5 个 workflow 都包含：
- `BatchImagesNode`
- `BerniniConditioning`
- `BerniniPromptEnhancer`
- `Bool`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfySwitchNode`
- `CreateVideo`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `PrimitiveInt`
- `RH_LLMAPI_NODE`
- `SaveVideo`
- `TTP_text_mix`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 4/5 个有
- `StringReplace` —— 4/5 个有
- `BasicScheduler` —— 3/5 个有
- `ConditioningZeroOut` —— 3/5 个有
- `EmptyHunyuanLatentVideo` —— 3/5 个有
- `KSamplerSelect` —— 3/5 个有
- `SplitSigmas` —— 3/5 个有
- `BerniniPromptResultParser` —— 2/5 个有
- `MaxNode` —— 2/5 个有
- `PromptRelayEncodeTimeline` —— 2/5 个有
- `VHS_LoadVideo` —— 2/5 个有
- `VRAM_Debug` —— 2/5 个有
- `easy convertAnything` —— 2/5 个有
- `PromptRelayEncode` —— 1/5 个有
- `SamplerCustom` —— 1/5 个有
- `SplitStringByDelimiter` —— 1/5 个有
- `VHS_VideoCombine` —— 1/5 个有
- `WanContextWindowsManual` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 100% |
| Prompt 约束强度(CFG) | 10 | 10 - 10 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 10，观测区间 10 - 10，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
