---
name: unknown_workflow_lora_sampler_clip_29
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.813111
common_nodes: [BasicScheduler, BerniniConditioning, CLIPLoader, CLIPTextEncode, CR Prompt Text, GetVideoComponents, ImageFromBatch, JWInteger, KSamplerSelect, LoadImage, LoadVideo, LoraLoaderModelOnly, PathchSageAttentionKJ, PreviewAny, RHLLMChatNode, SamplerCustom, SplitSigmas, StringReplace, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2063038125223538690.json, 视频生成/图生视频/2063144841558708225.json, 视频生成/图生视频/2065359403267739650.json, 视频生成/图生视频/2063267448056541186.json, 视频生成/图生视频/2062393408311873538.json, 视频生成/图生视频/2073466192983052289.json, 视频生成/图生视频/2061857100334194689.json, 视频生成/图生视频/2062007172694892545.json, 视频生成/图生视频/2062019836196249601.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_29

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/2063038125223538690.json、视频生成/图生视频/2063144841558708225.json、视频生成/图生视频/2065359403267739650.json、视频生成/图生视频/2063267448056541186.json、视频生成/图生视频/2062393408311873538.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 9 个 workflow 都包含：
- `BasicScheduler`
- `BerniniConditioning`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `GetVideoComponents`
- `ImageFromBatch`
- `JWInteger`
- `KSamplerSelect`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PreviewAny`
- `RHLLMChatNode`
- `SamplerCustom`
- `SplitSigmas`
- `StringReplace`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `BerniniPromptEnhancer` —— 8/9 个有
- `CreateVideo` —— 8/9 个有
- `ImageConcanate` —— 8/9 个有
- `SaveVideo` —— 8/9 个有
- `VHS_VideoCombine` —— 8/9 个有
- `Float` —— 7/9 个有
- `BatchImagesNode` —— 6/9 个有
- `MathExpression|pysssss` —— 5/9 个有
- `easy batchAnything` —— 5/9 个有
- `ImageScaleToTotalPixels` —— 1/9 个有
- `Label (rgthree)` —— 1/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/9 个有
- `SeedVR2LoadDiTModel` —— 1/9 个有
- `SeedVR2LoadVAEModel` —— 1/9 个有
- `SeedVR2VideoUpscaler` —— 1/9 个有
- `WanContextWindowsManual` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
