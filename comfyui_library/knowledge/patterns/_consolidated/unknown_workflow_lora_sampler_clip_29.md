---
name: unknown_workflow_lora_sampler_clip_29
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.810538
common_nodes: [BasicScheduler, BerniniConditioning, CLIPLoader, CLIPTextEncode, CR Prompt Text, GetVideoComponents, ImageFromBatch, JWInteger, KSamplerSelect, LoadImage, LoadVideo, LoraLoaderModelOnly, PathchSageAttentionKJ, PreviewAny, SamplerCustom, SplitSigmas, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [平台全量/Bernini 视频高质量编辑（10S）_2063069115425837057.json, 平台全量/Bernini--视频换人物_2062336313944268801.json, 平台全量/Bernini--长视频换人物_2062338907647340546.json, 平台全量/Bernini自用_2062408532850462721.json, 视频生成/图生视频/Bernini视频换人+视频换装_2063038125223538690.json, 视频生成/图生视频/Bernini视频换人+视频换装_2063144841558708225.json, 视频生成/图生视频/Bernini视频编辑（角色替换）优化加速版_2065359403267739650.json, 视频生成/图生视频/Bernini视频高质量编辑wan2.2图生视频动作迁移SeedVR2-二次高清放大视频1080p_2063267448056541186.json, 视频生成/图生视频/最新加速bernini人物替换10S版_2062393408311873538.json, 视频生成/图生视频/（4步极速版-sd2.0平替）Bernini 视频编辑高质量加速优化版V4_2073466192983052289.json, 视频生成/图生视频/（sd2.0平替）Bernini 视频编辑高质量加速优化版V3_2061857100334194689.json, 视频生成/图生视频/（长时稳定版方案1）Bernini 视频编辑高质量加速优化版V4_2062007172694892545.json, 视频生成/图生视频/（长时稳定版方案2）Bernini 视频编辑高质量加速优化版Beta版V4_2062019836196249601.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_29

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（平台全量/Bernini 视频高质量编辑（10S）_2063069115425837057.json、平台全量/Bernini--视频换人物_2062336313944268801.json、平台全量/Bernini--长视频换人物_2062338907647340546.json、平台全量/Bernini自用_2062408532850462721.json、视频生成/图生视频/Bernini视频换人+视频换装_2063038125223538690.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 13 个 workflow 都包含：
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
- `SamplerCustom`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 12/13 个有
- `RHLLMChatNode` —— 12/13 个有
- `StringReplace` —— 12/13 个有
- `VHS_VideoCombine` —— 12/13 个有
- `BerniniPromptEnhancer` —— 11/13 个有
- `CreateVideo` —— 11/13 个有
- `Float` —— 11/13 个有
- `SaveVideo` —— 11/13 个有
- `BatchImagesNode` —— 10/13 个有
- `MathExpression|pysssss` —— 7/13 个有
- `easy batchAnything` —— 7/13 个有
- `ImageScaleToTotalPixels` —— 2/13 个有
- `SeedVR2LoadDiTModel` —— 2/13 个有
- `SeedVR2LoadVAEModel` —— 2/13 个有
- `SeedVR2VideoUpscaler` —— 2/13 个有
- `Label (rgthree)` —— 1/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/13 个有
- `WanContextWindowsManual` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
