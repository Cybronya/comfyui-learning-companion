---
name: unknown_workflow_lora_sampler_clip_42
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.856833
common_nodes: [BasicScheduler, BatchImagesNode, BerniniConditioning, CLIPLoader, CLIPTextEncode, CreateVideo, GetVideoComponents, KSamplerSelect, LoadImage, LoadVideo, LoraLoaderModelOnly, PathchSageAttentionKJ, SamplerCustom, SaveVideo, SplitSigmas, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2062112812658417666.json, 视频生成/图生视频/2062167785479950338.json, 视频生成/图生视频/2066715725934448641.json, 视频生成/图生视频/2061852006909825025.json, 视频生成/图生视频/2062526408332763137.json, 视频生成/图生视频/2062779488521506817.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_42

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2062112812658417666.json、视频生成/图生视频/2062167785479950338.json、视频生成/图生视频/2066715725934448641.json、视频生成/图生视频/2061852006909825025.json、视频生成/图生视频/2062526408332763137.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicScheduler`
- `BatchImagesNode`
- `BerniniConditioning`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `GetVideoComponents`
- `KSamplerSelect`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `SamplerCustom`
- `SaveVideo`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 4/6 个有
- `BerniniPromptEnhancer` —— 3/6 个有
- `ImageConcanate` —— 3/6 个有
- `ImageResizeKJv2` —— 3/6 个有
- `PreviewAny` —— 3/6 个有
- `RHLLMChatNode` —— 3/6 个有
- `CR Text` —— 2/6 个有
- `ImageFromBatch` —— 2/6 个有
- `ImageScaleBy` —— 2/6 个有
- `Int` —— 2/6 个有
- `RIFE VFI` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `ttN seed` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `PrimitiveInt` —— 1/6 个有
- `TextInput_` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
