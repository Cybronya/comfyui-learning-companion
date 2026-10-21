---
name: unknown_workflow_lora_sampler_clip_92
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.767
common_nodes: [BatchImagesNode, BerniniConditioning, BerniniPromptEnhancer, Bool, CLIPLoader, CLIPTextEncode, ComfySwitchNode, CreateVideo, Fast Groups Bypasser (rgthree), ImageResizeKJv2, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, PreviewAny, PrimitiveInt, RH_LLMAPI_NODE, SaveVideo, StringReplace, TTP_text_mix, TextInput_, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2067931552071376897.json, 视频生成/图生视频/2068343750555955202.json, 视频生成/图生视频/2067557998221946881.json, 视频生成/图生视频/2073236445627772930.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_92

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2067931552071376897.json、视频生成/图生视频/2068343750555955202.json、视频生成/图生视频/2067557998221946881.json、视频生成/图生视频/2073236445627772930.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 4 个 workflow 都包含：
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
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `PrimitiveInt`
- `RH_LLMAPI_NODE`
- `SaveVideo`
- `StringReplace`
- `TTP_text_mix`
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `EmptyHunyuanLatentVideo` —— 3/4 个有
- `BasicScheduler` —— 2/4 个有
- `KSamplerSelect` —— 2/4 个有
- `MaxNode` —— 2/4 个有
- `PromptRelayEncodeTimeline` —— 2/4 个有
- `SplitSigmas` —— 2/4 个有
- `VHS_LoadVideo` —— 2/4 个有
- `VRAM_Debug` —— 2/4 个有
- `easy convertAnything` —— 2/4 个有
- `BerniniPromptResultParser` —— 1/4 个有
- `PromptRelayEncode` —— 1/4 个有
- `WanContextWindowsManual` —— 1/4 个有

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
